#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""最终合并器：把「国家法律法规数据库·上海市地方性法规」追加进 gov_docs.csv。

适用场景
--------
fetch_assets.py 写回 csv 时只更新已有行的列、不动行数；它会把 csv 列结构扩成
原列 + 红头PDF / 红头封面 / 附件 三列。本脚本在它之后跑，读最新 csv + 读人大
TSV，把人大法规作为新行追加，并把对应的官方正文路径写进 docs/<分类>/。

来源
----
- data/gov_docs.csv               已有 2,578 条（市/区/街镇三级）
- data/raw_flk_sh_laws.tsv        上海市地方性法规 530 条
- data/flk_fulltext/<bbbs>.txt    已抓官方正文（71 篇建设相关）

字段差异
-------
原 csv 字段: 分类/类型/层级/标题/文号/发布单位/发布日期/状态/来源/官方链接/正文/...
新增列待 fetch_assets 完成后补全: 红头PDF / 红头封面 / 附件
人大行用以下规则填:
    分类    -> 主题分类（用 is_relevant）
    类型    -> 「地方性法规」
    层级    -> 「市级」
    标题    -> 原文
    文号    -> 留空（地方性法规无文号）
    发布单位 -> 「上海市人民代表大会常务委员会」
    发布日期 -> 公布日期
    状态    -> 时效性（"有效"/"已修改"等）
    来源    -> 「国家法律法规数据库（flk.npc.gov.cn）」
    官方链接 -> https://flk.npc.gov.cn/detail?id=<bbbs>&title=<urlencoded>
    正文    -> docs/<分类>/<净化标题>.md（若 flk_fulltext/ 有正文）

去重
----
如某条标题在原 csv 中已存在（如「上海市住宅物业管理规定」可能被规章库抓过），
本脚本**跳过**——保留 csv 已有行（优先级更高）。
"""
import csv
import io
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from classify import is_relevant  # noqa: E402

CSV_PATH = os.path.join(HERE, "data", "gov_docs.csv")
TSV = os.path.join(HERE, "data", "raw_flk_sh_laws.tsv")
FLK_DIR = os.path.join(HERE, "data", "flk_fulltext")
DOCS_DIR = os.path.join(HERE, "docs")


def norm_title(t):
    t = re.sub(r"\s+", "", t or "")
    t = t.replace("《", "").replace("》", "").replace("〈", "").replace("〉", "")
    return t.lower()


def safe_filename(t, max_len=48):
    s = re.sub(r"[\\/:*?\"<>|\n\r\t]", "", t or "未命名")
    return s[:max_len]


def main():
    if not os.path.exists(CSV_PATH):
        print("✗ 缺 %s" % CSV_PATH)
        return
    if not os.path.exists(TSV):
        print("✗ 缺 %s" % TSV)
        return

    rows = list(csv.DictReader(open(CSV_PATH, encoding="utf-8-sig")))
    have_titles = set(norm_title(r["标题"]) for r in rows)
    fields = list(rows[0].keys()) if rows else [
        "分类", "类型", "层级", "标题", "文号", "发布单位",
        "发布日期", "状态", "来源", "官方链接", "正文",
    ]
    # 兜底补字段
    for c in ("分类", "类型", "层级", "文号", "正文"):
        if c not in fields:
            fields.append(c)
    print("现有 csv %d 行 / 字段 %d" % (len(rows), len(fields)))

    flk_rows = [l.rstrip("\n").split("\t") for l in io.open(TSV, encoding="utf-8")][1:]
    print("人大源 %d 条" % len(flk_rows))

    agency = "上海市人民代表大会常务委员会"
    added = []
    patched = []
    skipped = []
    for r in flk_rows:
        title, pub_date, eff_date, status, org, bbbs = (r + [""] * 6)[:6]
        if not title or not bbbs:
            continue
        nt = norm_title(title)
        if nt in have_titles:
            # 标题已存在 —— 但可能缺正文。flk 抓到全文的，补挂到已有行上。
            src_txt = os.path.join(FLK_DIR, bbbs + ".txt")
            if os.path.exists(src_txt):
                for r0 in rows:
                    if norm_title(r0["标题"]) == nt:
                        if not (r0.get("正文") or "").strip():
                            cat0 = r0["分类"]
                            cat_dir = os.path.join(DOCS_DIR, cat0)
                            os.makedirs(cat_dir, exist_ok=True)
                            fname = safe_filename(title) + ".md"
                            dst = os.path.join(cat_dir, fname)
                            if not os.path.exists(dst):
                                body = open(src_txt, encoding="utf-8").read()
                                md = (
                                    "# %s\n\n"
                                    "- **公布日期**：%s\n"
                                    "- **施行日期**：%s\n"
                                    "- **时效性**：%s\n"
                                    "- **制定机关**：%s\n"
                                    "- **国家法规库**：https://flk.npc.gov.cn/detail?id=%s\n"
                                    "- **来源**：国家法律法规数据库（flk.npc.gov.cn）\n\n"
                                    "---\n\n%s\n"
                                ) % (title, pub_date, eff_date, status, org, bbbs, body)
                                open(dst, "w", encoding="utf-8").write(md)
                            r0["正文"] = "docs/" + cat0 + "/" + fname
                            patched.append(title)
                        # 类型未标成地方性法规的，纠正一下
                        if r0.get("类型") not in ("地方性法规",):
                            r0["类型"] = "地方性法规"
                        break
            skipped.append(title)
            continue
        cat = is_relevant(title, agency)
        if not cat:
            continue
        cat_name, _ = cat

        # 正文路径（落盘到 docs/<分类>/）
        rel_path = ""
        src_txt = os.path.join(FLK_DIR, bbbs + ".txt")
        if os.path.exists(src_txt):
            cat_dir = os.path.join(DOCS_DIR, cat_name)
            os.makedirs(cat_dir, exist_ok=True)
            fname = safe_filename(title) + ".md"
            dst = os.path.join(cat_dir, fname)
            if not os.path.exists(dst):
                # 包装成 markdown：标题 + 时效 + 正文
                body = open(src_txt, encoding="utf-8").read()
                md = (
                    "# %s\n\n"
                    "- **公布日期**：%s\n"
                    "- **施行日期**：%s\n"
                    "- **时效性**：%s\n"
                    "- **制定机关**：%s\n"
                    "- **国家法规库**：https://flk.npc.gov.cn/detail?id=%s\n"
                    "- **来源**：国家法律法规数据库（flk.npc.gov.cn）\n\n"
                    "---\n\n%s\n"
                ) % (title, pub_date, eff_date, status, org, bbbs, body)
                open(dst, "w", encoding="utf-8").write(md)
            rel_path = "docs/" + cat_name + "/" + fname

        detail = "https://flk.npc.gov.cn/detail?id=%s" % bbbs
        new_row = {f: "" for f in fields}
        new_row.update({
            "分类": cat_name,
            "类型": "地方性法规",
            "层级": "市级",
            "标题": title,
            "文号": "",
            "发布单位": org or agency,
            "发布日期": pub_date or "",
            "状态": status or "",
            "来源": "国家法律法规数据库（flk.npc.gov.cn）",
            "官方链接": detail,
            "正文": rel_path,
        })
        rows.append(new_row)
        have_titles.add(nt)
        added.append(title)

    print("\n新增 %d 条（建设相关地方性法规）" % len(added))
    for t in added:
        print("  + %s" % t[:50])
    if patched:
        print("\n★ 为已存在条目补挂官方正文 %d 条：" % len(patched))
        for t in patched:
            print("  ✓ %s" % t[:50])
    if skipped:
        print("\n跳过 %d 条（标题已存在）：" % len(skipped))
        for t in skipped[:10]:
            print("  - %s" % t[:50])
        if len(skipped) > 10:
            print("  … 共 %d 条" % len(skipped))

    with open(CSV_PATH, "w", encoding="utf-8-sig", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields, extrasaction="ignore")
        w.writeheader()
        w.writerows(rows)
    print("\n✓ 写回 %s（%d 行）" % (CSV_PATH, len(rows)))


if __name__ == "__main__":
    main()