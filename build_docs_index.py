# -*- coding: utf-8 -*-
"""上海建设工程政府发文索引 —— 生成器。

三数据源合并
------------
1. 上海市人民政府「现行市政府规章」库       data/raw_gz_rules.tsv      （优先级 1）
2. 市住建委「规范性文件」栏目               data/raw_zjw_gfxwj.tsv     （优先级 2）
3. 上海市统一政策发布平台（市/区/街镇三级） data/raw_policy_all.json   （优先级 3）

产出
----
data/gov_docs.csv   合并去重后的核心清单
README.md           分类索引 + 渠道地图

法律说明
--------
本库收录的是具有立法、行政、司法性质的文件，依《中华人民共和国著作权法》
第五条第一项，该类文件不适用著作权法。故可全文收录；正文由 fetch_fulltext.py
从官方页面提取，每条均保留官方链接以便核对。
"""

import argparse
import csv
import json
import os
import re
import sys
from collections import Counter, defaultdict

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from classify import is_relevant  # noqa: E402

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(HERE, "data")
OUT_CSV = os.path.join(DATA, "gov_docs.csv")
OUT_MD = os.path.join(HERE, "README.md")

SH = "https://www.shanghai.gov.cn"
ZJW = "https://zjw.sh.gov.cn"
PLATFORM_DETAIL = SH + "/zhengce/detail/%s::%s"

DISTRICTS = ["浦东新区", "黄浦区", "徐汇区", "长宁区", "静安区", "普陀区", "虹口区",
             "杨浦区", "宝山区", "闵行区", "嘉定区", "金山区", "松江区", "青浦区",
             "奉贤区", "崇明区"]

CAT_ORDER = ["规划与土地", "建筑设计与报建", "工程建设管理", "消防与人防", "房屋与住房",
             "城市更新与历史保护", "绿色低碳与节能", "市政与基础设施", "市容绿化与景观",
             "建筑垃圾与材料"]

# 文件类型判定：(类型名, 判定规则)——顺序即优先级
TYPE_RULES = [
    ("地方性法规", r"条例"),
    ("政府规章", r"^上海市.{0,12}(办法|规定|细则)$"),
    ("办法", r"办法"),
    ("规定", r"规定"),
    ("实施细则", r"(实施细则|细则)"),
    ("技术规定与导则", r"(技术规定|技术规范|导则|技术标准|技术规程|设计标准|应用标准|计算标准)"),
    ("审查与许可规则", r"(审查|许可|审批|报建|备案|验收)"),
    ("规划与计划", r"(规划|计划|纲要)"),
    ("实施意见", r"(实施意见|指导意见|若干意见|若干措施|实施方案|工作方案|行动计划)"),
    ("通知公告", r"(通知|公告|通报|批复|函)"),
    ("公示公告", r"(名单|公示|命名|表彰|评选|招标|中标|结果)"),
]

# 有实质约束力、值得抓正文的类型
CORE_TYPES = {"地方性法规", "政府规章", "办法", "规定", "实施细则",
              "技术规定与导则", "审查与许可规则"}


# ------------------------------------------------------------------ 工具函数

def norm_title(t):
    """标题归一化，用于跨源去重。"""
    t = t or ""
    t = re.sub(r"[《》〈〉“”\"'（）()\[\]【】\s、，,。．\.：:；;—\-_/\\]", "", t)
    t = re.sub(r"^(上海市|关于|印发|转发|批转|公布|发布)+", "", t)
    return t[:24]


def doc_no_of(rec):
    dt, dy, dn = rec.get("docType"), rec.get("docYear"), rec.get("docNo")
    if dt and dy:
        return "%s〔%s〕%s号" % (dt, dy, dn or "")
    if dt:
        return str(dt)
    a = rec.get("attrs") or {}
    return str(a.get("documentAgency") or "")


def agency_of(rec):
    a = rec.get("attrs") or {}
    return re.sub(r"\s+", " ", (a.get("agency") or a.get("draftUnit") or "")).strip()


def level_of(agency, platform_level=""):
    """按发布机关名判定层级（平台自带的 policyLevel 常把区级标成市级）。

    判定顺序很关键：街镇机关名里通常**同时**含区名（如「上海市闵行区莘庄镇
    人民政府」），所以必须先判街镇，再判区，否则街镇级会被区级吃掉。
    """
    ag = agency or ""
    if re.search(r"(镇人民政府|镇政府|街道办事处)", ag):
        return "街镇级"
    for d in DISTRICTS:
        if d in ag:
            return "区级"
    if ag.startswith("上海市") or ag.startswith("中共上海市委"):
        return "市级"
    if platform_level in ("市级", "区级", "街镇级"):
        return platform_level
    return "其他"


def type_of(title, source):
    if source == "gz_rules":
        return "政府规章"
    t = title or ""
    for name, pat in TYPE_RULES:
        if re.search(pat, t):
            return name
    return "其他"


# ------------------------------------------------------------------ 装载各源

def load_gz_rules():
    path = os.path.join(DATA, "raw_gz_rules.tsv")
    if not os.path.exists(path):
        return []
    out = []
    with open(path, encoding="utf-8") as f:
        for line in f:
            parts = line.rstrip("\n").split("\t")
            if len(parts) < 2:
                continue
            path_, title = parts[0], parts[1]
            out.append({
                "标题": title.strip(),
                "发布单位": "上海市人民政府",
                "文号": "",
                "发布日期": "",
                "层级": "市级",
                "状态": "有效",
                "来源": "市政府规章库",
                "官方链接": SH + path_,
                "优先级": 1,
                "_siteId": "", "_businessId": "",
            })
    return out


def load_zjw():
    path = os.path.join(DATA, "raw_zjw_gfxwj.tsv")
    if not os.path.exists(path):
        return []
    out = []
    with open(path, encoding="utf-8") as f:
        for line in f:
            parts = line.rstrip("\n").split("\t")
            if len(parts) < 2:
                continue
            path_, title = parts[0], parts[1]
            out.append({
                "标题": title.strip(),
                "发布单位": "上海市住房和城乡建设管理委员会",
                "文号": "",
                "发布日期": path_.split("/")[2][:4] + "-" + path_.split("/")[2][4:6],
                "层级": "市级",
                "状态": "有效",
                "来源": "市住建委规范性文件",
                "官方链接": ZJW + path_,
                "优先级": 2,
                "_siteId": "", "_businessId": "",
            })
    return out


def load_platform():
    path = os.path.join(DATA, "raw_policy_all.json")
    if not os.path.exists(path):
        return []
    raw = json.load(open(path, encoding="utf-8"))
    out = []
    for r in raw.get("records", []):
        title = (r.get("title") or "").strip()
        if not title:
            continue
        ag = agency_of(r)
        sid, bid = r.get("siteId"), r.get("businessId")
        out.append({
            "标题": title,
            "发布单位": ag,
            "文号": doc_no_of(r),
            "发布日期": (r.get("publishDate") or "")[:10],
            "层级": level_of(ag, r.get("policyLevel") or ""),
            "状态": r.get("effectiveFlag") or (r.get("attrs") or {}).get("policyStatus") or "",
            "来源": "统一政策发布平台",
            "官方链接": PLATFORM_DETAIL % (sid, bid),
            "优先级": 3,
            "_siteId": sid or "", "_businessId": bid or "",
        })
    return out


# ------------------------------------------------------------------ 合并

def build_rows():
    merged = {}
    stats = Counter()
    for loader in (load_gz_rules(), load_zjw(), load_platform()):
        for row in loader:
            title = row["标题"]
            res = is_relevant(title, row["发布单位"])
            if not res:
                continue
            cat, hits = res
            # 同一文件多源命中时保留优先级更高（数值更小）的那条
            key = norm_title(title)
            if key in merged and merged[key]["优先级"] <= row["优先级"]:
                continue
            row = dict(row)
            row["分类"] = cat
            row["标签"] = "、".join(hits)
            row["类型"] = type_of(title, "gz_rules" if row["来源"] == "市政府规章库" else "other")
            row["正文"] = ""
            merged[key] = row
            stats[row["来源"]] += 1

    rows = list(merged.values())
    rows.sort(key=lambda r: (CAT_ORDER.index(r["分类"]) if r["分类"] in CAT_ORDER else 99,
                             -int(r["发布日期"][:4] or 0)))
    return rows


FIELDS = ["分类", "类型", "层级", "标题", "文号", "发布单位", "发布日期", "状态", "来源", "官方链接", "正文"]


def carry_over_fulltext(rows, path=OUT_CSV):
    """把上一次抓好的正文路径沿用下来 —— 重跑本脚本不应丢掉 fetch_fulltext 的成果。"""
    if not os.path.exists(path):
        return rows
    old = {}
    with open(path, encoding="utf-8-sig") as f:
        for r in csv.DictReader(f):
            if r.get("正文"):
                old[norm_title(r.get("标题"))] = r["正文"]
    if not old:
        return rows
    n = 0
    for r in rows:
        p = old.get(norm_title(r["标题"]))
        if p:
            r["正文"] = p
            n += 1
    print("   沿用已有正文 %d 条" % n)
    return rows


def write_csv(rows, path=OUT_CSV):
    with open(path, "w", encoding="utf-8-sig", newline="") as f:
        w = csv.DictWriter(f, fieldnames=FIELDS, extrasaction="ignore")
        w.writeheader()
        w.writerows(rows)
    return len(rows)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--stats", action="store_true", help="只统计，不写文件")
    args = ap.parse_args()

    rows = build_rows()

    print("合并去重后 %d 条" % len(rows))
    print("\n按分类：")
    for c in CAT_ORDER:
        n = sum(1 for r in rows if r["分类"] == c)
        if n:
            print("   %-12s %4d" % (c, n))
    print("\n按类型：")
    for t, n in Counter(r["类型"] for r in rows).most_common():
        print("   %-14s %4d%s" % (t, n, "   ★核心" if t in CORE_TYPES else ""))
    print("\n按层级：", dict(Counter(r["层级"] for r in rows)))
    print("按来源：", dict(Counter(r["来源"] for r in rows)))
    core = [r for r in rows if r["类型"] in CORE_TYPES]
    print("\n核心（有实质约束力）共 %d 条" % len(core))

    if args.stats:
        return
    carry_over_fulltext(rows)
    n = write_csv(rows)
    print("\n✓ %s（%d 条）" % (OUT_CSV, n))


if __name__ == "__main__":
    main()
