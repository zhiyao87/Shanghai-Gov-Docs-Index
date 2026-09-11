# -*- coding: utf-8 -*-
"""通用委办局正文抓取器 —— 配合 scrape_agency.py 的 raw_agency_<key>.json 使用。

与 fetch_ghzyj_docs.py 同逻辑，只是把「源 JSON / 来源名 / 发布单位」参数化，
一处改动就能接新局。

用法
----
    python fetch_agency_docs.py --src=agency_fgj \
        --agency=上海市房屋管理局 --source=市房管局官网
    python fetch_agency_docs.py --src=agency_zjw \
        --agency=上海市住房和城乡建设管理委员会 --source=市住建委官网 [--dry]
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
CSV = os.path.join(HERE, "data", "gov_docs.csv")
DOCS = os.path.join(HERE, "docs")

COLS = ["分类", "类型", "层级", "标题", "文号", "发布单位", "发布日期", "状态",
        "来源", "官方链接", "红头PDF", "红头封面", "附件", "正文",
        "原始发布年", "施行日期", "有效期止", "时效复核", "链接形态"]

# ---------- 筛选口径 ----------
DROP = ["职称", "任职资格", "名单", "复函", "考评", "法治政府", "工作要点",
        "责任分工", "通报", "公告", "公示", "领导小组", "总结", "计划", "竞赛",
        "活动", "培训", "会议", "经费", "预算", "审计", "统计", "任免", "党建",
        "廉政", "信访", "舆情", "年鉴", "征集", "问卷", "调研", "关于报送",
        "关于编报", "关于同意", "关于公布", "关于下达", "失信", "拖欠", "撤销",
        "撤回", "注销", "资质", "期刊", "四不两直", "检查情况", "专项整治",
        "安全生产", "防汛", "防台", "高温", "假期", "专项整治"]

# 对建筑/设计实务有直接价值的
KEEP = ["规范", "标准", "导则", "规程", "技术规定", "技术要求", "指标",
        "管理办法", "若干规定", "实施细则", "实施意见", "指导意见", "规定",
        "办法", "细则", "意见", "指南", "规则", "方案", "技术要求"]

# 房管局专属：与房屋面积/权属/修缮/历史建筑/拆除/征收评估直接相关的才收
KEEP_FGJ = ["面积", "测绘", "权属", "修缮", "历史建筑", "拆除", "房屋安全",
            "征收评估", "装修", "幕墙", "加装电梯", "住宅设计", "交付使用"]


def want(title, src):
    # 清单已在外部（zjw_screen.py）精筛过，跳过 DROP/KEEP 二次过滤
    if "prescreened" in src:
        return True
    if any(w in title for w in DROP):
        return False
    if "fgj" in src:
        return any(w in title for w in KEEP_FGJ)
    return any(w in title for w in KEEP)


# ---------- 提取 ----------
CONTAINERS = ("ivs_content", "Article_content", "zw_content", "TRS_Editor", "content")
ATTACH_RES = [re.compile(r'href="(/cmsres/[^"]+\.(?:pdf|doc|docx|xls|xlsx|zip))"', re.I),
              re.compile(r'href="([^"]+\.(?:pdf|doc|docx|xls|xlsx|zip))"', re.I)]


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


def attaches_of(html, base):
    out = []
    for rx in ATTACH_RES:
        for m in rx.findall(html):
            if m.startswith("/"):
                u = base + m
            elif m.startswith("http"):
                u = m
            else:
                continue
            if u.lower().endswith((".pdf", ".doc", ".docx", ".xls", ".xlsx", ".zip")) and u not in out:
                out.append(u)
    return out


DOCNO_RE = re.compile(r"[\u4e00-\u9fa5]{0,8}[〔\[]\s*(\d{4})\s*[〕\]]\s*(\d+)\s*号")


def pick_docno(lines):
    for ln in lines[:25]:
        m = DOCNO_RE.search(ln)
        if m and len(ln) < 60:
            return ln.strip()
    return ""


def safe_name(s, limit=80):
    s = re.sub(r'[\\/:*?"<>|\r\n\t]', "", s).strip()
    return re.sub(r"\s+", " ", s)[:limit]


def guess_type(title):
    for k, v in [("技术规范", "技术规定与导则"), ("技术导则", "技术规定与导则"),
                 ("标准", "技术规定与导则"), ("导则", "技术规定与导则"),
                 ("规程", "技术规定与导则"), ("技术规定", "技术规定与导则"),
                 ("实施细则", "实施细则"), ("若干规定", "规定"),
                 ("指导意见", "实施意见"), ("实施意见", "实施意见"),
                 ("若干意见", "实施意见"), ("实施办法", "办法"),
                 ("管理办法", "办法"), ("暂行办法", "办法"), ("办法", "办法"),
                 ("规定", "规定"), ("细则", "实施细则"), ("指南", "技术规定与导则")]:
        if k in title:
            return v
    return "通知公告"


def main():
    args = {}
    for a in sys.argv[1:]:
        if a.startswith("--"):
            k, _, v = a[2:].partition("=")
            args[k] = v or True
    src = args.get("src", "")
    agency = args.get("agency", "")
    source = args.get("source", "")
    dry = "dry" in args
    if not src:
        print("用法：python fetch_agency_docs.py --src=agency_fgj "
              "--agency=<发布单位> --source=<来源列取值>")
        return 1

    raw = os.path.join(HERE, "data", "raw_%s.json" % src)
    if not os.path.exists(raw):
        print("✗ 缺少 %s，先跑 scrape_agency.py" % raw)
        return 1
    data = json.load(open(raw, encoding="utf-8"))
    rows = list(csv.DictReader(io.open(CSV, encoding="utf-8-sig")))

    def norm(s):
        return re.sub(r"[《》〈〉（）()\s、，,。:：;；\"'`\-—_]", "", s or "")

    have = {norm(r["标题"]) for r in rows}
    base = re.match(r"https?://[^/]+", data[0]["url"]).group(0) if data else ""
    todo = [d for d in data if norm(d["title"]) not in have and want(d["title"], src)]
    seen, uniq = set(), []
    for d in todo:
        k = (norm(d["title"]), d["url"])
        if k in seen:
            continue
        seen.add(k)
        uniq.append(d)
    todo = uniq
    print("待抓 %d 条（%s）" % (len(todo), source or src))
    if dry:
        for d in todo:
            print("  %s %s" % (d["date"], d["title"][:70]))
        return 0
    if not todo:
        return 0

    added, failed, n_att = [], [], 0
    for i, d in enumerate(todo, 1):
        st, b = common.fetch(d["url"], timeout=35, retries=2)
        if st != 200 or not b:
            failed.append((d["title"], "HTTP %s" % st))
            continue
        html = b.decode("utf-8", "ignore")
        body = body_of(html)
        atts = attaches_of(html, base)
        title = re.sub(r"\s+", " ", d["title"]).strip()
        if not body:
            failed.append((title, "正文为空"))
            continue
        try:
            cat = classify.classify(title)[0] or "房屋与住房"
        except Exception:
            cat = "房屋与住房"
        pub = "%s-%s-%s" % (d["date"][:4], d["date"][4:6], d["date"][6:8])
        rel = os.path.join(cat, safe_name(title) + ".md")
        path = os.path.join(DOCS, rel)
        os.makedirs(os.path.dirname(path), exist_ok=True)
        docno = pick_docno(body)
        note = ""
        if len(body) <= 3 and atts:
            note = "> ⚠️ 官方页面仅发布通知正文，全文见下方附件直链。\n\n"
        L = ["---", "标题: %s" % title, "文号: %s" % docno,
             "发布单位: %s" % agency, "发布日期: %s" % pub, "层级: 市级",
             "类型: %s" % guess_type(title), "分类: %s" % cat, "状态: 有效",
             "官方链接: %s" % d["url"], "附件: %s" % " | ".join(atts), "---", "",
             "> 本文正文由脚本自官方公开页面提取，仅供检索查阅；"
             "以[官方链接](%s)发布版本为准。" % d["url"],
             "> 依《中华人民共和国著作权法》第五条第一项，具有立法、行政、司法性质的文件不适用著作权法。",
             "", note, "# %s" % title, ""]
        L += [x for x in body if "留言咨询" not in x and "只接收对该政策性" not in x]
        if atts:
            L += ["", "## 附件（官方直链）", ""] + \
                 ["- [%s](%s)" % (a.rsplit("/", 1)[-1], a) for a in atts]
        L.append("")
        io.open(path, "w", encoding="utf-8").write("\n".join(L))
        if atts:
            n_att += 1
        added.append({
            "分类": cat, "类型": guess_type(title), "层级": "市级", "标题": title,
            "文号": docno, "发布单位": agency, "发布日期": pub, "状态": "有效",
            "来源": source, "官方链接": d["url"], "红头PDF": "", "红头封面": "",
            "附件": " | ".join(atts), "正文": "docs/" + rel.replace("\\", "/"),
            "原始发布年": pub[:4], "施行日期": "", "有效期止": "",
            "时效复核": "现行有效（未标有效期）", "链接形态": "other",
        })
        if i % 20 == 0:
            print("  %d/%d …" % (i, len(todo)))
        time.sleep(0.2)

    print("抓到 %d 条（%d 条带附件），失败 %d 条" % (len(added), n_att, len(failed)))
    for t, why in failed[:10]:
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
