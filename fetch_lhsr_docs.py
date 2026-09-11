# -*- coding: utf-8 -*-
"""抓取上海市绿化和市容管理局官网文件正文，写 docs/ 并入库 CSV。

配合 scrape_lhsr.py 产出的 data/raw_lhsr.json 使用。

用法
----
    python fetch_lhsr_docs.py            # 抓取 SELECT 规则筛出的条目
    python fetch_lhsr_docs.py --dry      # 只列清单不落盘
    python fetch_lhsr_docs.py --all      # 忽略筛选，抓全部未收录条目

筛选口径（A 档）
--------------
1. 规范性文件栏：全收
2. 政策法规栏：主题词（绿化/绿地/公园/景观/户外/招牌/广告/照明/屋顶/行道树/绿道/湿地/园林…）
   + 体裁词（技术规范/标准/导则/规程/指标/办法/规定/细则/意见…）
3. 其它文件栏：只收含「景观照明/户外设施/招牌/广告/建设工程」的
四项黑名单（表扬、通报、批复、职称…）一律排除。
"""

import csv
import io
import json
import os
import re
import sys
import time
from html.parser import HTMLParser

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import common  # noqa: E402
import classify  # noqa: E402

HERE = os.path.dirname(os.path.abspath(__file__))
RAW = os.path.join(HERE, "data", "raw_lhsr.json")
CSV = os.path.join(HERE, "data", "gov_docs.csv")
DOCS = os.path.join(HERE, "docs")

COLS = ["分类", "类型", "层级", "标题", "文号", "发布单位", "发布日期", "状态",
        "来源", "官方链接", "红头PDF", "红头封面", "附件", "正文",
        "原始发布年", "施行日期", "有效期止", "时效复核", "链接形态"]

SOURCE = "市绿化市容局官网"

# ---------- 筛选口径 ----------
DROP = ["表扬", "通报", "名单", "批复", "议案", "年鉴", "要点", "竞赛", "志愿",
        "普法", "党建", "党组", "工会", "职称", "任免", "资格", "资金", "补贴",
        "扶持", "评选", "公示", "领导小组", "安全稳定", "防汛", "防台", "节日",
        "春节", "国庆", "中秋", "进博会", "疫情", "文明实践", "国有资产", "编纂",
        "信息员", "政务", "微信", "微博", "年鉴", "热线", "考核", "投诉", "信访",
        "舆情", "保密", "档案", "统计", "审计", "预算", "决算", "采购", "中标",
        "招标", "合同", "培训", "会议", "论坛", "宣传周", "科普", "展览", "疗休养",
        "体检", "慰问", "退休", "招聘", "录用", "纪检", "廉政", "巡视", "中期",
        "总结", "落实情况", "领导", "分工", "通知公告", "动员", "倡议", "致全市"]

SUBJ_STRONG = ["绿化", "绿地", "公园", "景观", "户外", "招牌", "广告", "照明",
               "屋顶", "立体绿化", "行道树", "绿道", "湿地", "园林", "树木",
               "古树", "市容", "环卫", "公厕", "垃圾", "渣土", "土方"]
SUBJ_WEAK = ["林业", "林地", "森林", "野生动物", "自然保护"]
FORM = ["技术规范", "技术标准", "规范", "标准", "导则", "规程", "技术规定",
        "技术要求", "指标", "指南", "办法", "规定", "细则", "意见", "规则", "程序"]
OTHER_KEEP = ["景观照明", "户外设施", "户外广告", "户外招牌", "建设工程"]


def want(d):
    t = d["title"]
    if any(w in t for w in DROP):
        return False
    sec = d["section"]
    if sec == "规范性文件":
        return True
    if sec == "政策法规":
        if not any(w in t for w in SUBJ_STRONG):
            return False
        return any(w in t for w in FORM)
    if sec == "其它文件":
        return any(w in t for w in OTHER_KEEP)
    return False


# ---------- HTML → 文本 ----------
class ZwParser(HTMLParser):
    """提取 class 含 zw_content 的容器内的文本，按块分段。"""

    def __init__(self):
        super().__init__()
        self.depth = 0
        self.capture = False
        self.buf = []
        self.out = []

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        cls = a.get("class", "")
        if not self.capture and "zw_content" in cls:
            self.capture = True
            self.depth = 1
            return
        if self.capture:
            if tag in ("p", "div", "tr", "br", "li"):
                self.flush()
            self.depth += 1

    def handle_endtag(self, tag):
        if not self.capture:
            return
        self.flush()
        self.depth -= 1
        if self.depth <= 0:
            self.capture = False

    def handle_data(self, data):
        if self.capture:
            s = data.strip()
            if s:
                self.buf.append(s)

    def flush(self):
        if self.buf:
            self.out.append("".join(self.buf))
            self.buf = []

    def result(self):
        self.flush()
        return [x for x in (s.strip() for s in self.out) if x]


def meta_of(html):
    """从政府信息公开元数据表里抓字段。"""
    flat = re.sub(r"<[^>]+>", "\u0001", html)
    flat = re.sub(r"[\s\u3000]+", "", flat)
    out = {}
    for key in ["信息名称", "文件编号", "发布机构", "发布日期", "公开类别"]:
        m = re.search(key + r"\u0001+([^\u0001]{1,120})", flat)
        if m:
            out[key] = m.group(1).strip()
    return out


def body_of(html):
    p = ZwParser()
    try:
        p.feed(html)
    except Exception:
        pass
    txt = p.result()
    if len(txt) >= 2:
        return txt
    # 退化方案：去掉脚本样式后取正文最长文本块
    t = re.sub(r"(?is)<script.*?</script>", "", html)
    t = re.sub(r"(?is)<style.*?</style>", "", t)
    t = re.sub(r"(?i)</(p|div|tr|li)>", "\n", t)
    t = re.sub(r"<[^>]+>", "", t)
    lines = [re.sub(r"[\s\u3000]+", " ", x).strip() for x in t.split("\n")]
    return [x for x in lines if len(x) > 8]


def safe_name(s, limit=80):
    s = re.sub(r'[\\/:*?"<>|\r\n\t]', "", s).strip()
    s = re.sub(r"\s+", " ", s)
    return s[:limit]


def guess_type(title):
    for k, v in [("技术规范", "技术规定与导则"), ("标准", "技术规定与导则"),
                 ("导则", "技术规定与导则"), ("规程", "技术规定与导则"),
                 ("技术规定", "技术规定与导则"), ("实施细则", "实施细则"),
                 ("若干规定", "规定"), ("指导意见", "实施意见"),
                 ("实施意见", "实施意见"), ("实施办法", "办法"),
                 ("管理办法", "办法"), ("暂行办法", "办法"),
                 ("办法", "办法"), ("规定", "规定"), ("细则", "实施细则")]:
        if k in title:
            return v
    return "通知公告"


def main():
    dry = "--dry" in sys.argv
    take_all = "--all" in sys.argv

    data = json.load(open(RAW, encoding="utf-8"))
    rows = list(csv.DictReader(io.open(CSV, encoding="utf-8-sig")))

    def norm(s):
        return re.sub(r"[《》〈〉（）()\s、，,。:：;；\"'`\-—_]", "", s or "")

    have = {norm(r["标题"]) for r in rows}
    todo = [d for d in data if norm(d["title"]) not in have]
    if not take_all:
        todo = [d for d in todo if want(d)]
    min_year = 2010
    for a in sys.argv:
        if a.startswith("--min-year="):
            min_year = int(a.split("=")[1])
    todo = [d for d in todo if int(d["date"][:4]) >= min_year]
    # 去重（列表页可能有重复条目）
    seen, uniq = set(), []
    for d in todo:
        k = (norm(d["title"]), d["url"])
        if k in seen:
            continue
        seen.add(k)
        uniq.append(d)
    todo = uniq
    print("待抓 %d 条" % len(todo))
    if dry:
        for d in todo:
            print("  [%s]%s %s" % (d["section"][:2], d["date"], d["title"][:70]))
        return 0
    if not todo:
        return 0

    os.makedirs(DOCS, exist_ok=True)
    added, failed = [], []
    for i, d in enumerate(todo, 1):
        st, b = common.fetch(d["url"], timeout=35, retries=2)
        if st != 200 or not b:
            failed.append((d["title"], "HTTP %s" % st))
            continue
        html = b.decode("utf-8", "ignore")
        meta = meta_of(html)
        body = body_of(html)
        title = meta.get("信息名称") or d["title"]
        title = re.sub(r"\s+", " ", title).strip()
        if len(body) < 2:
            failed.append((title, "正文提取为空"))
            continue

        try:
            cat = classify.classify(title)[0] or "市容绿化与景观"
        except Exception:
            cat = "市容绿化与景观"
        docno = meta.get("文件编号", "")
        if docno in ("无", "-", "/", ""):
            docno = ""
        pub = meta.get("发布日期") or d["date"]
        pub = re.sub(r"[年月]", "-", pub).replace("日", "").strip("-")
        if not re.match(r"^\d{4}-\d{2}-\d{2}$", pub):
            raw = d["date"]
            pub = "%s-%s-%s" % (raw[:4], raw[4:6], raw[6:8])

        rel = os.path.join(cat, safe_name(title) + ".md")
        path = os.path.join(DOCS, rel)
        os.makedirs(os.path.dirname(path), exist_ok=True)
        lines = ["---",
                 "标题: %s" % title,
                 "文号: %s" % docno,
                 "发布单位: %s" % (meta.get("发布机构") or "上海市绿化和市容管理局"),
                 "发布日期: %s" % pub,
                 "层级: 市级",
                 "类型: %s" % guess_type(title),
                 "分类: %s" % cat,
                 "状态: 有效",
                 "官方链接: %s" % d["url"],
                 "---", "",
                 "> 本文正文由脚本自上海市绿化和市容管理局官网页面提取，仅供检索查阅；"
                 "以[官方链接](%s)发布版本为准。" % d["url"],
                 "> 依《中华人民共和国著作权法》第五条第一项，具有立法、行政、司法性质的文件不适用著作权法。",
                 "", "# %s" % title, ""]
        lines += [x for x in body] + [""]
        with io.open(path, "w", encoding="utf-8") as f:
            f.write("\n".join(lines))

        added.append({
            "分类": cat, "类型": guess_type(title), "层级": "市级",
            "标题": title, "文号": docno,
            "发布单位": meta.get("发布机构") or "上海市绿化和市容管理局",
            "发布日期": pub, "状态": "有效", "来源": SOURCE,
            "官方链接": d["url"], "红头PDF": "", "红头封面": "", "附件": "",
            "正文": "docs/" + rel.replace("\\", "/"),
            "原始发布年": pub[:4], "施行日期": "", "有效期止": "",
            "时效复核": "现行有效（未标有效期）", "链接形态": "other",
        })
        if i % 10 == 0:
            print("  %d/%d …" % (i, len(todo)))
        time.sleep(0.25)

    print("抓到 %d 条，失败 %d 条" % (len(added), len(failed)))
    for t, why in failed[:20]:
        print("  ✗ %s（%s）" % (t[:50], why))

    if added:
        rows.extend(added)
        rows.sort(key=lambda r: (r.get("发布日期") or ""), reverse=True)
        with io.open(CSV, "w", encoding="utf-8-sig", newline="") as f:
            w = csv.DictWriter(f, fieldnames=COLS, extrasaction="ignore")
            w.writeheader()
            w.writerows(rows)
        print("CSV 现有 %d 条" % len(rows))
    return 0


if __name__ == "__main__":
    sys.exit(main())
