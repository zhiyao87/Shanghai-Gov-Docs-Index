# -*- coding: utf-8 -*-
"""抓取上海市绿化和市容管理局官网（lhsr.sh.gov.cn）三个文件栏目。

背景
----
统一政策发布平台（POST /gwk/policy/page）只收录「现行有效政策文件」，
绿化市容局大量规范性文件只挂在自家官网上，平台库里没有 businessId，
导致《上海市绿化行政许可（协助）审核若干规定》（沪绿容规〔2023〕6号）这类
文件整类缺失。本脚本补齐这一盲区。

栏目
----
    gfxwj  规范性文件   https://lhsr.sh.gov.cn/gfxwj/
    zcfg   政策法规     https://lhsr.sh.gov.cn/zcfgl/
    yjgl   其它文件     https://lhsr.sh.gov.cn/yjgl/

分页：index.html 为第 1 页，其后 index_2.html / index_3.html …（无 index_1.html）

产出：data/raw_lhsr.json
"""

import json
import os
import re
import sys
import time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import common  # noqa: E402

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "data", "raw_lhsr.json")

BASE = "https://lhsr.sh.gov.cn"
SECTIONS = [
    ("规范性文件", "/gfxwj/"),
    ("政策法规", "/zcfgl/"),
    ("其它文件", "/yjgl/"),
]
ITEM_RE = re.compile(r'href="([^"]*?/20\d{6}/[^"]+\.html)"[^>]*>\s*([^<]{4,200})')
MAX_PAGE = 40


def one_page(section, page):
    name = "index.html" if page == 1 else "index_%d.html" % page
    url = BASE + section + name
    st, b = common.fetch(url, timeout=30, retries=2)
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
            "url": href if href.startswith("http") else BASE + href,
            "date": (re.search(r"/(20\d{6})/", href).group(1)
                     if re.search(r"/(20\d{6})/", href) else ""),
        })
    return out


def main():
    result = []
    seen = set()
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
            print("  %s 第%d页：%d 条（新增 %d）" % (label, p, len(items), fresh))
            if fresh == 0:
                break
            time.sleep(0.3)
        print("[%s] 小计 %d 条" % (label, n))

    with open(OUT, "w", encoding="utf-8") as f:
        json.dump(result, f, ensure_ascii=False, indent=1)
    print("合计 %d 条 → %s" % (len(result), OUT))
    return 0


if __name__ == "__main__":
    sys.exit(main())
