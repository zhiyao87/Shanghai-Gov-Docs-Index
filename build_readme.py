# -*- coding: utf-8 -*-
"""生成 README.md 与 index/ 分类索引。

用法：python build_readme.py
"""

import collections
import csv
import os
import sys
import urllib.parse

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from build_docs_index import CAT_ORDER, CORE_TYPES, OUT_CSV  # noqa: E402
from channels import DISTRICTS, MUNICIPAL  # noqa: E402

HERE = os.path.dirname(os.path.abspath(__file__))
INDEX_DIR = os.path.join(HERE, "index")
CAT_NO = ["一", "二", "三", "四", "五", "六", "七", "八", "九", "十"]


def q(url):
    return urllib.parse.quote(url or "", safe=":/?#[]@!$&'*+,;=%~.-_")


def link(url, label="官方"):
    return "[%s](%s)" % (label, q(url)) if url else "-"


def rows_of(path):
    return list(csv.DictReader(open(path, encoding="utf-8-sig")))


def table(rows, with_body=True):
    if with_body:
        head = ("| 标题 | 类型 | 层级 | 文号 | 发布机关 | 发布日期 | 状态 | 正文 |\n"
                "|---|---|---|---|---|---|---|---|\n")
    else:
        head = ("| 标题 | 类型 | 层级 | 文号 | 发布机关 | 发布日期 | 状态 |\n"
                "|---|---|---|---|---|---|---|\n")
    out = [head]
    for r in rows:
        title = "[%s](%s)" % ((r["标题"] or "").replace("|", "｜"), q(r["官方链接"]))
        cells = [title, r["类型"], r["层级"], r["文号"] or "-",
                 (r["发布单位"] or "-").replace("|", "｜"), r["发布日期"] or "-", r["状态"] or "-"]
        if with_body:
            body = r.get("正文") or ""
            cells.append(link(body, "全文") if body else "-")
        out.append("| " + " | ".join(cells) + " |\n")
    return "".join(out)


# ------------------------------------------------------------------ 索引文件

def write_category_indexes(rows):
    os.makedirs(INDEX_DIR, exist_ok=True)
    cat_files = {}
    for i, cat in enumerate(CAT_ORDER, 1):
        sub = [r for r in rows if r["分类"] == cat]
        if not sub:
            continue
        sub.sort(key=lambda r: (r["层级"] != "市级", r["类型"] not in CORE_TYPES,
                                -int(r["发布日期"][:4] or 0)))
        fn = "index/%02d-%s.md" % (i, cat)
        cat_files[cat] = fn
        L = ["# %s\n" % cat,
             "\n共 **%d** 条（市级 %d ／ 区级 %d ／ 其他 %d）\n"
             % (len(sub),
                sum(1 for r in sub if r["层级"] == "市级"),
                sum(1 for r in sub if r["层级"] == "区级"),
                sum(1 for r in sub if r["层级"] not in ("市级", "区级"))),
             "\n[← 返回总目录](../README.md)\n",
             "\n## 市级\n\n"]
        L.append(table([r for r in sub if r["层级"] == "市级"]))
        qu = [r for r in sub if r["层级"] != "市级"]
        if qu:
            L.append("\n## 区级 / 街镇级\n\n")
            L.append(table(qu))
        open(os.path.join(HERE, fn), "w", encoding="utf-8").write("".join(L))
    return cat_files


# ------------------------------------------------------------------ README

def build_readme(rows, cat_files):
    total = len(rows)
    core = [r for r in rows if r["类型"] in CORE_TYPES]
    lv = collections.Counter(r["层级"] for r in rows)
    src = collections.Counter(r["来源"] for r in rows)
    typ = collections.Counter(r["类型"] for r in rows)
    with_body = sum(1 for r in rows if r.get("正文"))
    districts = collections.Counter()
    for r in rows:
        for d, _ in DISTRICTS:
            if d in (r["发布单位"] or ""):
                districts[d] += 1
                break

    L = []
    A = L.append
    A("# 上海建设工程政府发文索引\n\n")
    A("上海市 **建筑、规划、工程建设** 领域的政府规章与行政规范性文件索引。\n"
      "只收录**元数据 + 官方链接**，并为有实质约束力的文件附上**官方正文全文**（可全文收录，见文末法律说明）。\n\n")
    A("> 配套仓库：[Arch-Standards-Index](https://github.com/zhiyao87/Arch-Standards-Index)"
      " —— 上海及全国**工程建设标准**（DGJ08 / GB / JGJ）索引。\n"
      "> 本库管「政府发文」，标准库管「技术标准」，两者互补。\n\n")

    A("## 数据概览\n\n")
    A("| 指标 | 数量 |\n|---|---|\n")
    A("| 收录文件总数 | **%d** |\n" % total)
    A("| 其中的核心文件（条例/规章/办法/规定/细则/导则/审查许可规则） | **%d** |\n" % len(core))
    A("| 已附官方正文全文 | **%d** |\n" % with_body)
    A("| 市级 ／ 区级 ／ 街镇级 ／ 未标注 | %d ／ %d ／ %d ／ %d |\n"
      % (lv["市级"], lv["区级"], lv["街镇级"], len(rows) - lv["市级"] - lv["区级"] - lv["街镇级"]))
    _yrs = sorted(r["发布日期"][:4] for r in rows if r["发布日期"][:4].isdigit())
    A("| 时间跨度 | %s – %s |\n" % (_yrs[0], _yrs[-1]) if _yrs else "| 时间跨度 | - |\n")
    A("| 覆盖区 | %d / 16 个区有收录 |\n" % sum(1 for d, _ in DISTRICTS if districts.get(d)))
    A("| 数据抓取日 | 2026-09-11 |\n")
    A("\n**按来源**\n\n| 来源 | 条数 |\n|---|---|\n")
    for k, v in src.most_common():
        A("| %s | %d |\n" % (k, v))
    A("\n**按文件类型**\n\n| 类型 | 条数 | 是否附全文 |\n|---|---|---|\n")
    for k, v in typ.most_common():
        A("| %s | %d | %s |\n" % (k, v, "✓" if k in CORE_TYPES else "—"))
    A("\n**按分类**\n\n| # | 分类 | 条数 | 索引 |\n|---|---|---|---|\n")
    for i, cat in enumerate(CAT_ORDER, 1):
        n = sum(1 for r in rows if r["分类"] == cat)
        if not n:
            continue
        A("| %s | %s | %d | [查看](%s) |\n" % (CAT_NO[i - 1] if i <= 10 else i, cat, n, cat_files.get(cat, "")))

    # ---------------- 渠道地图
    A("\n## 官方发布渠道地图\n\n")
    A("找上海的建设类政府文件，认准下面这几个口子就够。**全部为官方发布源**。\n\n")
    A("### 市级\n\n| 渠道 | 官方入口 | 覆盖 | 备注 |\n|---|---|---|---|\n")
    for name, url, scope, note in MUNICIPAL:
        A("| %s | [打开](%s) | %s | %s |\n" % (name, q(url), scope, note))
    A("\n### 区级（16 区）\n\n")
    A("区级文件不在市级栏目里，需到各区政府门户的「政务公开 → 规范性文件／政策文件」取。\n"
      "下表入口取自上海市人民政府《政府信息公开指南》页，**均经核实**。\n\n")
    A("| 区 | 政府信息公开入口 | 本库收录 |\n|---|---|---|\n")
    for d, url in DISTRICTS:
        A("| %s | [打开](%s) | %d 条 |\n" % (d, q(url), districts.get(d, 0)))
    A("\n> **提示**：区级文件的检索体验普遍弱于市级，各区栏目结构不统一、分页方式各异。\n"
      "想一次覆盖全，用 [上海市统一政策发布平台](https://www.shanghai.gov.cn/zhengce/list)"
      "——它纵向贯通市/区/镇三级、横向覆盖各部门，本库的区级数据即来源于此。\n")

    # ---------------- 重点速查
    A("\n## 设计报建高频文件速查\n\n")
    A("按实务环节整理的常用依据（全部来自本库，含正文）：\n\n")
    hotspots = [
        ("规划条件与方案报建",
         ["规划管理技术规定", "城市规划管理技术规定", "方案规划公示", "日照分析",
          "建设工程设计方案", "规划报批入库"]),
        ("施工图审查",
         ["施工图", "多图联审", "设计文件审查"]),
        ("抗震与人防",
         ["抗震设防", "人民防空", "民防工程"]),
        ("施工许可与验收",
         ["施工许可", "竣工验收", "工程总承包"]),
        ("绿色建筑与节能",
         ["绿色建筑", "建筑节能", "超低能耗", "装配式", "海绵城市"]),
        ("既有建筑与城市更新",
         ["城市更新", "既有建筑", "历史建筑", "优秀历史建筑", "加装电梯", "装饰装修"]),
        ("房屋与住宅",
         ["住宅设计", "物业管理", "住宅小区", "住宅专项维修"]),
    ]
    for label, kws in hotspots:
        hits = [r for r in rows
                if any(k in r["标题"] for k in kws) and r["类型"] in CORE_TYPES]
        hits.sort(key=lambda r: -int(r["发布日期"][:4] or 0))
        hits = hits[:8]
        if not hits:
            continue
        A("\n### %s\n\n" % label)
        A("| 标题 | 文号 | 发布机关 | 日期 | 正文 |\n|---|---|---|---|---|\n")
        for r in hits:
            A("| [%s](%s) | %s | %s | %s | %s |\n"
              % ((r["标题"] or "").replace("|", "｜"), q(r["官方链接"]),
                 r["文号"] or "-", (r["发布单位"] or "-").replace("|", "｜"),
                 r["发布日期"] or "-", link(r.get("正文") or "", "全文")))
        A("\n[→ 查看该主题全部条目](%s)\n" % cat_files.get(
            "建筑设计与报建" if "报建" in label or "图" in label else
            "城市更新与历史保护" if "更新" in label else
            "绿色低碳与节能" if "绿色" in label else
            "房屋与住房" if "房屋" in label else
            "消防与人防" if "人防" in label else
            "工程建设管理", "README.md"))

    # ---------------- 怎么用
    A("\n## 目录结构\n\n```\n")
    A("Shanghai-Gov-Docs-Index/\n")
    A("├── README.md                 本文件（概览 + 渠道地图 + 速查）\n")
    A("├── index/                    按分类的完整索引（每条含官方链接）\n")
    A("├── docs/                     核心文件官方正文全文（Markdown，按分类分目录）\n")
    A("├── data/\n")
    A("│   ├── gov_docs.csv          全量清单（本库唯一数据源）\n")
    A("│   ├── raw_gz_rules.tsv      市政府规章库原始抓取\n")
    A("│   ├── raw_zjw_gfxwj.tsv     市住建委规范性文件原始抓取\n")
    A("│   └── raw_policy_all.json   统一政策平台原始抓取（10,518 条，未入库）\n")
    A("├── channels.py               官方渠道地图常量（16 区入口）\n")
    A("├── classify.py               主题分类与相关性判定规则\n")
    A("├── common.py                 抓取工具（零第三方依赖）\n")
    A("├── scrape_policy.py          抓统一政策发布平台全量\n")
    A("├── build_docs_index.py       三源合并 → data/gov_docs.csv\n")
    A("├── fetch_fulltext.py         抓核心文件官方正文 → docs/\n")
    A("├── build_readme.py           生成 README.md 与 index/\n")
    A("└── check_links.py            链接批量巡检\n```\n")

    A("\n## 怎么用 / 怎么维护\n\n")
    A("**查文件**：先看上面的分类索引，或直接搜 `data/gov_docs.csv`。\n\n")
    A("**要全文**：`docs/` 下按分类存放，文件名即标题。只覆盖核心类型"
      "（条例/规章/办法/规定/细则/导则/审查规则），通知公告类只给官方链接。\n\n")
    A("**重建流程**（需要联网）：\n\n```bash\n")
    A("python scrape_policy.py        # 1. 抓统一政策平台全量（约 3 分钟）\n")
    A("python build_docs_index.py     # 2. 三源合并去重 → data/gov_docs.csv\n")
    A("python fetch_fulltext.py       # 3. 抓核心文件正文 → docs/（约 8 分钟）\n")
    A("python build_readme.py         # 4. 生成 README 与索引\n")
    A("python check_links.py          # 5. 巡检链接\n```\n")
    A("\n**加新文件**：不要直接改 README —— 改 `data/gov_docs.csv` 后重跑 `build_readme.py`，"
      "否则下次生成会被冲掉。若某文件未被自动筛出，在 `classify.py` 的关键词表里补词。\n")

    A("\n## 数据来源与法律说明\n\n")
    A("**数据来源**（均为上海市官方发布渠道）：\n\n")
    for name, url, _, _ in MUNICIPAL:
        A("- %s：%s\n" % (name, url))
    A("\n**法律说明**\n\n")
    A("本库收录的文件属于**具有立法、行政、司法性质的文件**。依《中华人民共和国著作权法》"
      "**第五条第一项**，该类文件不适用著作权法，故本库**可全文收录**正文。\n\n")
    A("这与技术标准的情形不同：《工程建设标准》（GB / JGJ / DGJ08）属**受著作权保护的推荐性技术文件**，"
      "在 [Arch-Standards-Index](https://github.com/zhiyao87/Arch-Standards-Index) 中"
      "**只收录元数据与官方链接、不收录正文**。两个库的版权处理差异源于此。\n\n")
    A("正文由脚本自官方公开页面自动提取，可能因页面改版而与发布版本有差异，"
      "**请以每份文件中的官方链接为准**。\n")
    return "".join(L)


def main():
    rows = rows_of(OUT_CSV)
    cat_files = write_category_indexes(rows)
    md = build_readme(rows, cat_files)
    open(os.path.join(HERE, "README.md"), "w", encoding="utf-8").write(md)
    print("✓ README.md（%.1f KB）" % (os.path.getsize(os.path.join(HERE, "README.md")) / 1024))
    print("✓ index/ 共 %d 个分类文件" % len(cat_files))


if __name__ == "__main__":
    main()
