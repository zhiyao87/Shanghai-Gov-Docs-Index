# -*- coding: utf-8 -*-
"""住建委未收录条目分类筛查 —— 用于确定 A 档补录口径。用法: python zjw_screen.py"""
import csv, io, json, re, sys
from collections import Counter

rows = list(csv.DictReader(io.open("data/gov_docs.csv", encoding="utf-8-sig")))
PUNC = re.compile(r"[《》〈〉（）()\s、，,。:：;；\"'\-—_`]")


def norm(s):
    return PUNC.sub("", s or "")


have = {norm(r["标题"]) for r in rows}
d = json.load(open("data/raw_agency_zjw.json", encoding="utf-8"))
miss = [x for x in d if norm(x["title"]) not in have]
print("住建委抓到 %d 条，未收录 %d 条" % (len(d), len(miss)))

# ---- 硬噪音：一律不收 ----
NOISE = re.compile(
    "通报|公告|公示|名单|撤销|注销|撤回|失信|拖欠|资质|期刊|复函|"
    "四不两直|检查情况|巡查|安全生产|防汛|防台|高温|专项整治|考评|征集|"
    "报送|编报|公布|下达|质量月|应急预案|复审|终止|宣贯|培训计划|"
    "工作要点|编制计划|活动|竞赛|会议|任免|表彰|试点工作|总结")

# ---- A 档：批准类（真正的规范/标准设计） ----
APPROVE = re.compile(r"批准.{0,80}?(工程建设规范|标准设计|建筑标准设计)")

# ---- B 档：发布/印发 导则·技术标准·技术规定 ----
ISSUE = re.compile(
    r"(导则|技术标准|技术规程|技术规定|技术要求|技术指引|设计标准|"
    r"设计文件编制深度|审查要点|技术导则)")

# ---- C 档：设计质量管理类（有实质规则，非通报） ----
RULE = re.compile(
    "幕墙|加装电梯|施工图|设计文件|绿色建筑|装配式|海绵城市|既有建筑|"
    "改造|城市更新|节能|装配|建筑信息模型|BIM|造价|租赁住房|保障性住房|"
    "住宅设计|修缮|历史建筑")


# C 档内部的行政噪音：年度报告 / 任务分解 / 继续教育 / 机构认定
C_NOISE = re.compile("发展报告|任务分解|继续教育|认定工作|危旧房改造")


def grade(x):
    t = x["title"]
    if NOISE.search(t) or C_NOISE.search(t):
        return None
    if APPROVE.search(t):
        return "A"
    if ISSUE.search(t) and re.search(r"发布|印发|出台|施行", t):
        return "B"
    if RULE.search(t):
        return "C"
    return None


sel = [x for x in miss if grade(x)]
c = Counter(grade(x) for x in miss if grade(x))
print("A 档 %d ／ B 档 %d ／ C 档 %d  合计 %d 条" % (c["A"], c["B"], c["C"], len(sel)))
print("剔除噪音 %d 条" % (len(miss) - len(sel)))

for tag, name in [("A", "A 批准为工程建设规范/标准设计"),
                  ("B", "B 发布导则/技术标准/技术规定"),
                  ("C", "C 设计质量管理类")]:
    sub = [x for x in sel if grade(x) == tag]
    print()
    print("=== %s（%d 条）===" % (name, len(sub)))
    for x in sorted(sub, key=lambda y: y["date"], reverse=True):
        print("   ", x["date"], x["title"][:70])

# 与库中已有标题再比对一次，去掉重复
sel = [x for x in sel if norm(x["title"]) not in have]
with io.open("data/raw_agency_zjw_prescreened.json", "w", encoding="utf-8") as f:
    json.dump(sel, f, ensure_ascii=False, indent=1)
print()
print("去重后 %d 条 → data/raw_agency_zjw_prescreened.json" % len(sel))
