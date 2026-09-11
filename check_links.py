# -*- coding: utf-8 -*-
"""官方链接与正文文件巡检。

做三件事
--------
1. 本地一致性：data/gov_docs.csv 里「正文」列指向的文件是否真的存在
2. 链接格式：官方链接是否为合法 URL（不做网络请求）
3. 联网抽检/全检：逐个 GET，判定 200 / 受限 / 失效

用法
----
    python check_links.py              # 本地一致性 + 格式检查（秒级）
    python check_links.py --net        # 全部联网巡检（2500+ 条，约 20 分钟）
    python check_links.py --net --core # 只巡检核心文件（约 1000 条）
    python check_links.py --net -n 40  # 随机抽检 40 条
"""

import argparse
import csv
import os
import random
import sys
import time
import urllib.parse

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import common  # noqa: E402
from build_docs_index import CORE_TYPES, OUT_CSV  # noqa: E402

HERE = os.path.dirname(os.path.abspath(__file__))


def judge(code, ctype="", body=b""):
    if code == 200:
        if "pdf" in (ctype or "").lower():
            return "ok", "PDF 可下载"
        if "html" in (ctype or "").lower() and len(body) > 500:
            return "ok", "页面正常"
        return "ok", "200"
    if code in (403, 429, 503):
        return "limited", "反爬限制（非失效）"
    if code == 404:
        return "bad", "404"
    if code == 0:
        return "bad", "网络不可达"
    return "warn", "HTTP %d" % code


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--net", action="store_true")
    ap.add_argument("--core", action="store_true")
    ap.add_argument("-n", "--limit", type=int, default=0)
    ap.add_argument("--sleep", type=float, default=0.3)
    args = ap.parse_args()

    rows = list(csv.DictReader(open(OUT_CSV, encoding="utf-8-sig")))
    print("清单 %d 条" % len(rows))

    # 1) 本地一致性
    miss, badfmt, noch = [], [], 0
    for r in rows:
        u = r.get("官方链接") or ""
        p = urllib.parse.urlparse(u)
        if p.scheme not in ("http", "https") or not p.netloc:
            badfmt.append(u or "(空)")
        body = r.get("正文") or ""
        if body:
            if not os.path.exists(os.path.join(HERE, body)):
                miss.append(body)
        else:
            noch += 1
    print("\n[本地] 正文文件缺失：%d" % len(miss))
    for m in miss[:10]:
        print("        %s" % m)
    print("[本地] 链接格式异常：%d" % len(badfmt))
    for m in badfmt[:10]:
        print("        %s" % m)
    print("[本地] 无正文（仅链接）：%d" % noch)

    if not args.net:
        print("\n（加 --net 做联网巡检）")
        return

    todo = rows
    if args.core:
        todo = [r for r in rows if r.get("类型") in CORE_TYPES]
    if args.limit:
        todo = random.sample(todo, min(args.limit, len(todo)))
    print("\n[联网] 巡检 %d 条 …" % len(todo))

    stat = {"ok": 0, "limited": 0, "warn": 0, "bad": 0}
    bads = []
    for i, r in enumerate(todo, 1):
        code, body = common.fetch(r["官方链接"], timeout=30, retries=2)
        ctype = ""
        st, note = judge(code, ctype, body)
        stat[st] += 1
        if st in ("bad", "warn"):
            bads.append((code, note, r["标题"], r["官方链接"]))
        if i % 100 == 0:
            print("   %d/%d  ok=%d limited=%d warn=%d bad=%d"
                  % (i, len(todo), stat["ok"], stat["limited"], stat["warn"], stat["bad"]))
        time.sleep(args.sleep)

    print("\n=== 结果 ===")
    print("正常 %d ｜ 受限 %d ｜ 警告 %d ｜ 失效 %d" %
          (stat["ok"], stat["limited"], stat["warn"], stat["bad"]))
    for code, note, title, u in bads[:30]:
        print("  [%s %s] %s\n      %s" % (code, note, title[:50], u))


if __name__ == "__main__":
    main()
