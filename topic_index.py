#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""主题速查 —— 从 docs/ 下的 markdown 文件 grep 关键词，映射回 gov_docs.csv 的行。

戴工常问的几个高频主题（屋顶绿化 / 屋顶光伏 / 太阳能 / 绿色建筑 / 海绵 / 既有建筑改造），
标题不一定含主题词但正文一定涉及。用本脚本按主题词扫全文，给一份"主题—相关条目—正文摘录"表。

输出：index/12-主题速查.md
"""
import csv
import os
import re
import sys
from collections import defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
CSV = os.path.join(HERE, "data", "gov_docs.csv")
DOCS = os.path.join(HERE, "docs")
INDEX = os.path.join(HERE, "index", "12-主题速查.md")

# (主题标签, 命中关键词(空格分隔, 命中任一即算), 主题简介, 摘要抓取关键词)
TOPICS = [
    ("屋顶绿化 / 立体绿化",
     "屋顶绿化 屋顶花园 立体绿化 垂直绿化 棚架绿化 架空绿化 沿口绿化 屋顶折算 立体折算 屋顶植被 第五立面",
     "屋顶绿化 / 立体绿化 / 第五立面",
     "建设设计阶段要做的屋顶绿化专项；旧改中常见",
     "屋顶绿化 立体绿化 折算 第五立面"),
    ("屋顶分布式光伏 / 光伏建筑一体化",
     "屋顶分布式光伏 屋顶光伏 光伏建筑一体化 BIPV 光伏一体化 整县(市、区)推进分布式光伏 整街道屋顶光伏 光伏入楼 光伏幕墙 屋顶光伏开发",
     "屋顶光伏 / BIPV / 整县(市、区)推进",
     "光伏建筑一体化是建设审批与电力接入的交叉点",
     "屋顶光伏 BIPV 光伏建筑一体化"),
    ("建筑光伏 / 太阳能应用",
     "太阳能热水系统 太阳能光伏 光伏发电 分布式光伏 光伏电站 海上光伏 陆上风电 新能源专项 太阳能建筑 可再生能源建筑应用 太阳能供热",
     "光伏 / 太阳能热水 / 新能源建筑",
     "建筑光伏与可再生能源应用",
     "光伏 太阳能 可再生能源 新能源"),
    ("绿色建筑 / 节能",
     "绿色建筑 绿建 建筑节能 节能改造 节能审查 超低能耗 近零能耗 零能耗 能耗监测 能耗定额 碳排放 碳达峰 碳中和 双碳",
     "绿色建筑 / 建筑节能 / 双碳",
     "绿色建筑评价、节能审查与碳排放",
     "绿色建筑 建筑节能 双碳 节能审查"),
    ("海绵城市",
     "海绵城市 海绵 雨水控制 雨水回用 透水铺装 雨水花园 下凹式绿地 雨水调蓄 雨水排放 雨水管渠",
     "海绵城市规划建设管理",
     "海绵城市规划、设计、施工、验收全流程",
     "海绵 雨水"),
    ("既有建筑改造",
     "既有建筑改造 既有建筑装饰装修 既有建筑幕墙 幕墙检查 幕墙鉴定 幕墙安全 历史建筑修缮 优秀历史建筑 风貌保护 城市更新 旧区改造 城中村",
     "既有建筑 / 历史建筑 / 城市更新",
     "既有建筑改造与历史风貌保护",
     "既有建筑 城市更新 优秀历史 幕墙"),
    # —— 2026-09-11 新增：住建委规范补录后，设计类标准散落在「工程建设管理」等册，
    #    单独开专题，避免戴工按设计口径找文件时被分类误导。
    ("上海市工程建设规范（设计类）",
     "设计标准 设计规范 设计规程 标准设计 设计导则 图集",
     "工程建设规范中的设计类 / 标准设计 / 图集",
     "住建委批准为上海市工程建设规范的设计类标准，跨建筑、市政、轨交；"
     "含标准设计与图集（如道路照明设施标准图集、人防警报设施专用房图集）",
     "设计标准 设计规范 标准设计 图集"),
    ("施工图审查 / 设计文件审查",
     "施工图 审查要点 多图联审 设计文件审查 设计文件编制深度 联合审图 智能辅助审查",
     "施工图审查 / 审查要点 / 多图联审",
     "施工图审查要点（建筑篇/岩土勘察篇/无障碍篇）、编制深度规定、BIM 智能辅助审查",
     "施工图 审查要点 编制深度"),
    ("既有多层住宅加装电梯",
     "加装电梯 既有多层住宅 电梯加装 表决比例",
     "加装电梯政策与审批",
     "加装电梯的审批管理、质量安全管理、业主表决比例",
     "加装电梯 表决 审批"),
    ("建筑幕墙安全",
     "幕墙 玻璃幕墙 幕墙安全 幕墙排查 幕墙高坠",
     "幕墙安全排查 / 既有幕墙改造",
     "幕墙安全排查整治、既有建筑幕墙隐患排查",
     "幕墙 排查 高坠"),
]


def load():
    rows = list(csv.DictReader(open(CSV, encoding="utf-8-sig")))
    body_by_title = {}  # title -> md body
    csv_by_title = {}
    for r in rows:
        csv_by_title[r["标题"]] = r
        body = r.get("正文") or ""
        if body and os.path.exists(body):
            try:
                body_by_title[r["标题"]] = open(body, encoding="utf-8").read()
            except Exception:
                pass
    print("CSV %d 条，已加载 %d 篇正文" % (len(rows), len(body_by_title)))
    return rows, csv_by_title, body_by_title


def hit_title(r, kws):
    s = r["标题"] + "|" + (r.get("文号") or "")
    for k in kws:
        if k in s:
            return True
    return False


def hit_body(body, kws):
    for k in kws:
        if k in body:
            return True
    return False


def snippet(body, summary_kws, limit=140):
    for kw in summary_kws:
        i = body.find(kw)
        if i >= 0:
            s = max(0, i - 30)
            e = min(len(body), i + limit)
            txt = body[s:e].replace("\n", " ").replace("\r", " ")
            if s > 0:
                txt = "…" + txt
            if e < len(body):
                txt = txt + "…"
            return txt
    return ""


def main():
    rows, csv_by_title, body_by_title = load()

    rows.sort(key=lambda r: -(int((r["发布日期"] or "0")[:4] or 0) * 10000 +
                              int((r["发布日期"] or "0-0-0")[5:7] or 0) * 100 +
                              int((r["发布日期"] or "0-0-0")[8:10] or 0)))

    L = []
    L.append("# 主题速查\n\n")
    L.append("戴工常问的几个高频主题（屋顶绿化 / 屋顶光伏 / 太阳能 / 绿色建筑 / 海绵 / 既有建筑改造）。"
             "这里把库内**标题或正文含主题词**的全部条目按主题归并。\n\n")
    L.append("> 命中策略：先按标题匹配（精准），未命中再扫正文（兜底）。")
    L.append("匹配范围：2,578 条全量。\n\n")

    summary_lines = []
    for label, kw_str, sub, hint, summary_kws in TOPICS:
        kws = kw_str.split()
        sm_kws = summary_kws.split()
        title_hits = [r for r in rows if hit_title(r, kws)]
        body_hits = []
        seen_titles = set(r["标题"] for r in title_hits)
        for title, body in body_by_title.items():
            if title in seen_titles:
                continue
            if hit_body(body, kws):
                body_hits.append(csv_by_title[title])
        all_hits = title_hits + body_hits
        summary_lines.append((label, len(title_hits), len(body_hits)))

        L.append("## %s\n\n" % label)
        L.append("> %s —— %s\n\n" % (sub, hint))
        if not all_hits:
            L.append("⚠ 库内**无命中** —— 建议去 `www.shanghai.gov.cn` 站内检索补充。\n\n")
            continue
        L.append("共 **%d 条**（标题命中 %d / 正文命中 %d；按发布日期倒序）：\n\n"
                 % (len(all_hits), len(title_hits), len(body_hits)))
        L.append("| 日期 | 层级 | 标题 | 文号 | 主题摘录 | 原文 |\n")
        L.append("|---|---|---|---|---|---|\n")
        for r in all_hits[:40]:
            title = "[%s](%s)" % ((r["标题"] or "").replace("|", "｜"), r["官方链接"])
            body_path = r.get("正文") or ""
            body = body_by_title.get(r["标题"], "")
            snip = snippet(body, sm_kws) if body else ""
            L.append("| %s | %s | %s | %s | %s | %s |\n"
                     % (r["发布日期"][:10] or "-",
                        r["层级"],
                        title,
                        r["文号"] or "-",
                        (snip[:80].replace("|", "｜") + "…") if len(snip) > 80 else snip.replace("|", "｜"),
                        ("[全文](%s)" % body_path) if body_path else "-"))
        if len(all_hits) > 40:
            L.append("\n_（仅显示前 40 条，库内共 %d 条）_\n" % len(all_hits))
        L.append("\n")

    L.append("## 主题速查小结\n\n")
    L.append("| 主题 | 标题命中 | 正文命中 | 合计 |\n|---|---|---|---|\n")
    for label, t, b in summary_lines:
        L.append("| %s | %d | %d | **%d** |\n" % (label, t, b, t + b))
    L.append("\n_生成时间：本脚本运行时刻；版本随 `data/gov_docs.csv` 与 `docs/` 自动更新。_\n")

    os.makedirs(os.path.dirname(INDEX), exist_ok=True)
    open(INDEX, "w", encoding="utf-8").write("".join(L))
    print("✓ %s (%.1f KB)" % (INDEX, os.path.getsize(INDEX) / 1024))
    for label, t, b in summary_lines:
        print("  %-22s 标题 %2d + 正文 %2d = %d" % (label, t, b, t + b))


if __name__ == "__main__":
    main()