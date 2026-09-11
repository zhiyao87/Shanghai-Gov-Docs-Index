# -*- coding: utf-8 -*-
"""通用委办局栏目抓取器 —— 抓列表 → 与 CSV 比对 → 列出未收录条目。

与 scrape_ghzyj.py 的区别：本脚本不写死单个站点，栏目用配置表描述，
适合快速评估「某个局还有多少东西在政策平台之外」。

用法
----
    python scrape_agency.py                # 抓 SITES 里全部栏目
    python scrape_agency.py --only zjw     # 只抓指定 key
    python scrape_agency.py --diff         # 顺带与 CSV 比对

产出：data/raw_agency_<key>.json
"""

import json
import os
import re
import sys
import time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import common  # noqa: E402

HERE = os.path.dirname(os.path.abspath(__file__))
CSV = os.path.join(HERE, "data", "gov_docs.csv")

# key -> (名称, 基址, [栏目路径…])
SITES = {
    "zjw": ("住房和城乡建设管理委员会", "https://zjw.sh.gov.cn", ["/zdgk/"]),
    "fgj": ("房屋管理局", "https://fgj.sh.gov.cn", ["/gfxwj/"]),
}

ITEM_RE = re.compile(r'href="([^"]*?/20\d{6}/[^"]+\.html)"[^>]*>\s*([^<]{4,200})')
MAX_PAGE = 80


def one_page(base, sec, page):
    name = "index.html" if page == 1 else "index_%d.html" % page
    st, b = common.fetch(base + sec + name, timeout=30, retries=2)
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
            "url": base + href if href.startswith("/") else href,
            "date": (re.search(r"/(20\d{6})/", href).group(1)
                     if re.search(r"/(20\d{6})/", href) else ""),
        })
    return out


def main():
    only = None
    for a in sys.argv:
        if a.startswith("--only="):
            only = a.split("=")[1]
    do_diff = "--diff" in sys.argv

    for key, (name, base, secs) in SITES.items():
        if only and key != only:
            continue
        result, seen = [], set()
        for sec in secs:
            n = 0
            for p in range(1, MAX_PAGE + 1):
                items = one_page(base, sec, p)
                if not items:
                    break
                fresh = 0
                for it in items:
                    if it["url"] in seen:
                        continue
                    seen.add(it["url"])
                    it["section"] = sec.strip("/")
                    result.append(it)
                    fresh += 1
                    n += 1
                if fresh == 0:
                    break
                time.sleep(0.2)
            print("[%s %s%s] %d 条" % (key, name, sec, n))
        out = os.path.join(HERE, "data", "raw_agency_%s.json" % key)
        with open(out, "w", encoding="utf-8") as f:
            json.dump(result, f, ensure_ascii=False, indent=1)
        print("  → %s（%d 条）" % (out, len(result)))

        if do_diff:
            import csv
            import io
            rows = list(csv.DictReader(io.open(CSV, encoding="utf-8-sig")))

            def norm(s):
                return re.sub(r"[《》〈〉（）()\s、，,。:：;；\"'`\-—_]", "", s or "")

            have = {norm(r["标题"]) for r in rows}
            miss = [d for d in result if norm(d["title"]) not in have]
            print("  未收录 %d / %d 条" % (len(miss), len(result)))
            for d in sorted(miss, key=lambda x: x["date"], reverse=True)[:40]:
                print("    %s %s" % (d["date"], d["title"][:70]))
    return 0


if __name__ == "__main__":
    sys.exit(main())
