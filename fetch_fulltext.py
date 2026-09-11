# -*- coding: utf-8 -*-
"""抓取核心文件的官方正文，落盘为 Markdown。

正文来源（按 row['来源'] 分流）
-------------------------------
- 统一政策发布平台 → POST https://www.shanghai.gov.cn/gwk/policy/detail
                     {siteId, businessId} → data.txt（HTML 片段）
- 市政府规章库 / 市住建委规范性文件 → 抓 HTML 页面，取 <div id="ivs_content"> 区块

产出
----
docs/<分类>/<slug>.md      每份文件一个 Markdown（含 YAML front-matter）
data/gov_docs.csv          回填「正文」列（相对路径）

用法
----
    python fetch_fulltext.py               # 只抓核心类型
    python fetch_fulltext.py --all         # 全部 2500+ 条（慢）
    python fetch_fulltext.py --limit 20    # 调试
    python fetch_fulltext.py --redo        # 重抓已存在的
"""

import argparse
import csv
import json
import os
import re
import sys
import time
import urllib.parse

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import common  # noqa: E402
from build_docs_index import CORE_TYPES, FIELDS, OUT_CSV  # noqa: E402

HERE = os.path.dirname(os.path.abspath(__file__))
DOCS = os.path.join(HERE, "docs")
DETAIL_API = "https://www.shanghai.gov.cn/gwk/policy/detail"
REFERER = {"Referer": "https://www.shanghai.gov.cn/zhengce/list"}
BAD_CHARS = re.compile(r'[\\/:*?"<>|\r\n\t]+')


def slug(text, maxlen=50):
    s = BAD_CHARS.sub("_", (text or "").strip())
    s = re.sub(r"\s+", " ", s).strip(" ._")
    return s[:maxlen] or "untitled"


# ------------------------------------------------------------ HTML 片段提取

def extract_div(html, marker):
    """从 marker（形如 'id="ivs_content"'）开始，按 div 嵌套深度取整个区块。"""
    i = html.find(marker)
    if i < 0:
        return ""
    start = html.find(">", i)
    if start < 0:
        return ""
    body_start = start + 1
    depth, j = 1, body_start
    tag = re.compile(r"<(/?)div\b[^>]*?(/?)>", re.I)
    while depth > 0:
        m = tag.search(html, j)
        if not m:
            return html[body_start:]
        if m.group(2) == "/":          # <div ... />
            pass
        elif m.group(1) == "/":
            depth -= 1
        else:
            depth += 1
        j = m.end()
    return html[body_start:j - len(m.group(0))]


def page_body(html):
    """从政府站详情页 HTML 中取正文。"""
    if not html:
        return ""
    seg = extract_div(html, 'id="ivs_content"')
    if not seg:
        seg = extract_div(html, 'class="Article_content"')
    if not seg:
        return ""
    seg = re.sub(r"<div[^>]*id=\"ivs_(title|date|player)\"[^>]*>.*?</div>", " ",
                 seg, flags=re.S | re.I)
    return common.html_to_text(seg)


# ------------------------------------------------------------ 单条抓取

def get_text(row):
    src = row.get("来源", "")
    if src == "统一政策发布平台":
        sid, bid = row.get("_siteId"), row.get("_businessId")
        if not sid or not bid:
            # businessId 可能含连字符、下划线、非十六进制字符（如
            # 9d8fad8f-b20b-44b9-..., 5_181167, test_..., xxfbdf...），
            # 所以不能限定字符集，必须一路取到末尾。
            m = re.search(r"detail/([^:]+)::(.+?)/?$", row.get("官方链接", ""))
            if m:
                sid, bid = m.group(1), m.group(2)
        if not sid or not bid:
            return ""
        d = common.post_json(DETAIL_API, {"siteId": sid, "businessId": bid},
                             headers=REFERER, timeout=45, retries=3)
        if not d or d.get("code") != 0 or not d.get("data"):
            return ""
        html = d["data"].get("txt") or ""
        if not html:
            html = d["data"].get("txt1") or ""
        return common.html_to_text(html)
    # 规章库 / 住建委：抓页面
    html = common.fetch_text(row.get("官方链接", ""), timeout=45, retries=3)
    return page_body(html)


def write_md(row, body):
    cat = slug(row.get("分类") or "其他", 20)
    d = os.path.join(DOCS, cat)
    os.makedirs(d, exist_ok=True)
    name = slug(row.get("标题"), 50)
    path = os.path.join(d, name + ".md")
    k = 2
    while os.path.exists(path):
        # 同名不同文件，追加序号
        existing = open(path, encoding="utf-8").read(400)
        if row.get("官方链接") and row["官方链接"] in existing:
            break
        path = os.path.join(d, "%s_%d.md" % (name, k))
        k += 1
    fm = [
        "---",
        "标题: %s" % (row.get("标题") or "").replace("\n", " "),
        "文号: %s" % (row.get("文号") or "-"),
        "发布单位: %s" % (row.get("发布单位") or "-"),
        "发布日期: %s" % (row.get("发布日期") or "-"),
        "层级: %s" % (row.get("层级") or "-"),
        "类型: %s" % (row.get("类型") or "-"),
        "分类: %s" % (row.get("分类") or "-"),
        "状态: %s" % (row.get("状态") or "-"),
        "官方链接: %s" % (row.get("官方链接") or ""),
        "---",
        "",
        "> 本文正文由脚本自上海市官方公开页面提取，仅供检索查阅；"
        "以[官方链接](%s)发布版本为准。" % (row.get("官方链接") or ""),
        "> 依《中华人民共和国著作权法》第五条第一项，"
        "具有立法、行政、司法性质的文件不适用著作权法。",
        "",
        "# %s" % (row.get("标题") or ""),
        "",
        body.strip(),
        "",
    ]
    with open(path, "w", encoding="utf-8") as f:
        f.write("\n".join(fm))
    return os.path.relpath(path, HERE).replace("\\", "/")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--all", action="store_true")
    ap.add_argument("--limit", type=int, default=0)
    ap.add_argument("--redo", action="store_true")
    ap.add_argument("--sleep", type=float, default=0.35)
    args = ap.parse_args()

    rows = list(csv.DictReader(open(OUT_CSV, encoding="utf-8-sig")))
    todo = rows if args.all else [r for r in rows if r.get("类型") in CORE_TYPES]
    if args.limit:
        todo = todo[:args.limit]
    print("待抓 %d 条（总 %d）" % (len(todo), len(rows)))

    ok = empty = 0
    for n, row in enumerate(todo, 1):
        if not args.redo and row.get("正文") and os.path.exists(os.path.join(HERE, row["正文"])):
            ok += 1
            continue
        body = get_text(row)
        if len(body) < 60:
            empty += 1
            if n % 50 == 0 or empty <= 5:
                print("   ✗[%d/%d] 正文缺 %s" % (n, len(todo), row["标题"][:36]))
        else:
            row["正文"] = write_md(row, body)
            ok += 1
        if n % 25 == 0:
            print("   %d/%d  成功 %d ｜ 缺正文 %d" % (n, len(todo), ok, empty))
        time.sleep(args.sleep)

    with open(OUT_CSV, "w", encoding="utf-8-sig", newline="") as f:
        w = csv.DictWriter(f, fieldnames=FIELDS, extrasaction="ignore")
        w.writeheader()
        w.writerows(rows)
    print("\n完成：成功 %d ｜ 缺正文 %d ｜ 总计 %d" % (ok, empty, len(todo)))
    print("✓ 回写 %s" % OUT_CSV)


if __name__ == "__main__":
    main()
