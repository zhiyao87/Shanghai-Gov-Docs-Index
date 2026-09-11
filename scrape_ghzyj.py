# -*- coding: utf-8 -*-
"""抓取上海市规划和自然资源局官网「政策文件」栏目（ghzyj.sh.gov.cn/zcwj/）。

子栏目：cxgh 城乡规划 / tdgl 土地管理 / bdcgl 不动产登记 / chgl 测绘管理 /
       dzkc 地质矿产 / cjdagl 城建档案 / dmgl 地名管理 / zhl 综合 / gfxwj 规范性文件

分页：index.html 为第 1 页，其后 index_2.html …

用法
----
    python scrape_ghzyj.py            # 抓全量 → data/raw_ghzyj.json
    python scrape_ghzyj.py --diff     # 抓完顺带与 CSV 比对，列出未收录条目
"""

import json
import os
import re
import sys
import time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import common  # noqa: E402

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "data", "raw_ghzyj.json")
CSV = os.path.join(HERE, "data", "gov_docs.csv")

BASE = "https://ghzyj.sh.gov.cn"
SECTIONS = [
    ("城乡规划", "/zcwj/cxgh/"),
    ("土地管理", "/zcwj/tdgl/"),
    ("不动产登记", "/zcwj/bdcgl/"),
    ("测绘管理", "/zcwj/chgl/"),
    ("地质矿产", "/zcwj/dzkc/"),
    ("城建档案", "/zcwj/cjdagl/"),
    ("地名管理", "/zcwj/dmgl/"),
    ("综合", "/zcwj/zhl/"),
    ("规范性文件", "/zcwj/gfxwj/"),
]
ITEM_RE = re.compile(r'href="([^"]*?/20\d{6}/[^"]+\.html)"[^>]*>\s*([^<]{4,200})')
MAX_PAGE = 60


def one_page(sec, page):
    name = "index.html" if page == 1 else "index_%d.html" % page
    st, b = common.fetch(BASE + sec + name, timeout=30, retries=2)
    if st != 200 or not b:
        return []
    t = b.decode("utf-8", "ignore")
    out = []
    for href, title in ITEM_RE.findall(t):
        title = title.strip()
        if not title:
            continue
        out.append({
            "title": title,
            "url": BASE + href if href.startswith("/") else href,
            "date": (re.search(r"/(20\d{6})/", href).group(1)
                     if re.search(r"/(20\d{6})/", href) else ""),
        })
    return out


def main():
    result, seen = [], set()
    for label, sec in SECTIONS:
        n = 0
        for p in range(1, MAX_PAGE + 1):
            items = one_page(sec, p)
            if not items:
                break
            fresh = 0
            for it in items:
                if it["url"] in seen:
                    continue
                seen.add(it["url"])
                it["section"] = label
                result.append(it)
                fresh += 1
                n += 1
            if fresh == 0:
                break
            time.sleep(0.2)
        print("[%s] %d 条" % (label, n))

    with open(OUT, "w", encoding="utf-8") as f:
        json.dump(result, f, ensure_ascii=False, indent=1)
    print("合计 %d 条 → %s" % (len(result), OUT))

    if "--diff" in sys.argv:
        import csv
        import io
        rows = list(csv.DictReader(io.open(CSV, encoding="utf-8-sig")))

        def norm(s):
            return re.sub(r"[《》〈〉（）()\s、，,。:：;；\"'`\-—_]", "", s or "")

        have = {norm(r["标题"]) for r in rows}
        miss = [d for d in result if norm(d["title"]) not in have]
        print("\n未收录 %d 条：" % len(miss))
        for d in sorted(miss, key=lambda x: x["date"], reverse=True)[:60]:
            print("  [%s]%s %s" % (d["section"][:2], d["date"], d["title"][:70]))
    return 0


if __name__ == "__main__":
    sys.exit(main())
