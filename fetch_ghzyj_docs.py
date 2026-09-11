# -*- coding: utf-8 -*-
"""抓取上海市规划和自然资源局（ghzyj.sh.gov.cn）文件正文 + 附件直链。

与 lhsr.sh.gov.cn 的差异
------------------------
1. 正文容器是 `id="ivs_content" class="Article_content"`，不是 `zw_content`
2. 页面**没有**政府信息公开元数据表（信息名称/文件编号…），只能取列表标题 + URL 日期
3. 大量文件（尤其技术标准、规划文本）页面正文只有一句「详情见附件」，
   **全文在 /cmsres/… 的 PDF 里** → 必须把附件直链一并登记，否则等于没补

产出
----
- docs/<分类>/<标题>.md —— frontmatter 含「附件:」字段（多个用 | 分隔）
- data/gov_docs.csv —— 「附件」列填官方直链，「来源」列 = 市规划资源局官网

用法
----
    python fetch_ghzyj_docs.py            # 抓 SELECT 筛出的条目
    python fetch_ghzyj_docs.py --dry      # 只列清单
    python fetch_ghzyj_docs.py --all      # 忽略筛选
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
RAW = os.path.join(HERE, "data", "raw_ghzyj.json")
CSV = os.path.join(HERE, "data", "gov_docs.csv")
DOCS = os.path.join(HERE, "docs")

COLS = ["分类", "类型", "层级", "标题", "文号", "发布单位", "发布日期", "状态",
        "来源", "官方链接", "红头PDF", "红头封面", "附件", "正文",
        "原始发布年", "施行日期", "有效期止", "时效复核", "链接形态"]

SOURCE = "市规划资源局官网"
BASE = "https://ghzyj.sh.gov.cn"

# ---------- 筛选口径 ----------
DROP = ["职称", "任职资格", "名单", "复函", "考评", "法治政府", "工作要点",
        "责任分工", "检查", "宣传周", "宣传日", "年报", "申报", "评审", "表彰",
        "通报", "公示", "领导小组", "总结", "计划", "通知公告", "竞赛", "活动",
        "培训", "会议", "经费", "预算", "审计", "统计", "任免", "党建", "廉政",
        "信访", "舆情", "年鉴", "征集", "问卷", "调研", "关于报送", "关于编报",
        "关于同意", "关于公布", "关于下达", "领导干部应知应会", "测绘资质"]
KEEP = ["规划", "城市更新", "风貌", "历史", "建筑", "市政", "交通工程",
        "社区生活圈", "产业用地", "低效", "土地", "出让", "征收", "宅基地",
        "不动产", "测绘", "多测合一", "建设工程", "设计", "标准", "规范",
        "技术规定", "导则", "规程", "指标", "管理办法", "若干意见", "实施细则",
        "规定", "办法", "细则", "意见", "指南", "工具箱", "行动方案"]


def want(d):
    t = d["title"]
    if any(w in t for w in DROP):
        return False
    return any(w in t for w in KEEP)


# ---------- 提取 ----------
CONTAINERS = ("ivs_content", "Article_content", "zw_content", "TRS_Editor")
ATTACH_RE = re.compile(r'href="(/cmsres/[^"]+\.(?:pdf|doc|docx|xls|xlsx|zip))"', re.I)


class BodyParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.depth = 0
        self.capture = False
        self.buf = []
        self.out = []

    def handle_starttag(self, tag, attrs):
        if self.capture:
            if tag in ("p", "div", "tr", "br", "li"):
                self.flush()
            self.depth += 1
            return
        a = dict(attrs)
        blob = " ".join([a.get("id", ""), a.get("class", "")])
        if any(c in blob for c in CONTAINERS):
            self.capture = True
            self.depth = 1

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


def body_of(html):
    p = BodyParser()
    try:
        p.feed(html)
    except Exception:
        pass
    txt = p.result()
    if txt:
        return txt
    t = re.sub(r"(?is)<script.*?</script>", "", html)
    t = re.sub(r"(?is)<style.*?</style>", "", t)
    t = re.sub(r"(?i)</(p|div|tr|li)>", "\n", t)
    t = re.sub(r"<[^>]+>", "", t)
    return [x for x in (re.sub(r"[\s\u3000]+", " ", l).strip() for l in t.split("\n")) if len(x) > 8]


def attaches_of(html):
    out = []
    for m in ATTACH_RE.findall(html):
        u = BASE + m if m.startswith("/") else m
        if u not in out:
            out.append(u)
    return out


def safe_name(s, limit=80):
    s = re.sub(r'[\\/:*?"<>|\r\n\t]', "", s).strip()
    return re.sub(r"\s+", " ", s)[:limit]


def guess_type(title):
    for k, v in [("技术规范", "技术规定与导则"), ("标准", "技术规定与导则"),
                 ("导则", "技术规定与导则"), ("规程", "技术规定与导则"),
                 ("技术规定", "技术规定与导则"), ("实施细则", "实施细则"),
                 ("若干规定", "规定"), ("指导意见", "实施意见"),
                 ("实施意见", "实施意见"), ("若干意见", "实施意见"),
                 ("实施办法", "办法"), ("管理办法", "办法"),
                 ("暂行办法", "办法"), ("办法", "办法"),
                 ("规定", "规定"), ("细则", "实施细则"), ("指南", "技术规定与导则")]:
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

    added, failed, with_att = [], [], 0
    for i, d in enumerate(todo, 1):
        st, b = common.fetch(d["url"], timeout=35, retries=2)
        if st != 200 or not b:
            failed.append((d["title"], "HTTP %s" % st))
            continue
        html = b.decode("utf-8", "ignore")
        body = body_of(html)
        atts = attaches_of(html)
        title = re.sub(r"\s+", " ", d["title"]).strip()
        if not body:
            failed.append((title, "正文为空"))
            continue

        try:
            cat = classify.classify(title)[0] or "规划与土地"
        except Exception:
            cat = "规划与土地"

        pub = "%s-%s-%s" % (d["date"][:4], d["date"][4:6], d["date"][6:8])
        rel = os.path.join(cat, safe_name(title) + ".md")
        path = os.path.join(DOCS, rel)
        os.makedirs(os.path.dirname(path), exist_ok=True)

        note = ""
        if len(body) <= 3 and atts:
            note = "> ⚠️ 官方页面仅发布通知正文，全文见下方附件直链。\n\n"
        lines = ["---",
                 "标题: %s" % title,
                 "文号: ",
                 "发布单位: 上海市规划和自然资源局",
                 "发布日期: %s" % pub,
                 "层级: 市级",
                 "类型: %s" % guess_type(title),
                 "分类: %s" % cat,
                 "状态: 有效",
                 "官方链接: %s" % d["url"],
                 "附件: %s" % " | ".join(atts),
                 "---", "",
                 "> 本文正文由脚本自上海市规划和自然资源局官网页面提取，仅供检索查阅；"
                 "以[官方链接](%s)发布版本为准。" % d["url"],
                 "> 依《中华人民共和国著作权法》第五条第一项，具有立法、行政、司法性质的文件不适用著作权法。",
                 "", note, "# %s" % title, ""]
        lines += [x for x in body if "政策性文件留言咨询" not in x
                  and "只接收对该政策性文件的相关咨询" not in x]
        if atts:
            lines += ["", "## 附件（官方直链）", ""]
            lines += ["- [%s](%s)" % (a.rsplit("/", 1)[-1], a) for a in atts]
        lines.append("")
        with io.open(path, "w", encoding="utf-8") as f:
            f.write("\n".join(lines))
        if atts:
            with_att += 1

        added.append({
            "分类": cat, "类型": guess_type(title), "层级": "市级",
            "标题": title, "文号": "",
            "发布单位": "上海市规划和自然资源局",
            "发布日期": pub, "状态": "有效", "来源": SOURCE,
            "官方链接": d["url"], "红头PDF": "", "红头封面": "",
            "附件": " | ".join(atts),
            "正文": "docs/" + rel.replace("\\", "/"),
            "原始发布年": pub[:4], "施行日期": "", "有效期止": "",
            "时效复核": "现行有效（未标有效期）", "链接形态": "other",
        })
        if i % 15 == 0:
            print("  %d/%d …" % (i, len(todo)))
        time.sleep(0.2)

    print("抓到 %d 条（其中 %d 条带附件直链），失败 %d 条" % (len(added), with_att, len(failed)))
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
