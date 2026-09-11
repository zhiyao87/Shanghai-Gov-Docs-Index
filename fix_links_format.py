#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""把 data/gov_docs.csv 里「路径式」的平台详情链接批量改为「查询参数式」。

背景
----
戴工 2026-09-11 实测：
    /zhengce/detail/0010::6e3f54d554174dfd8f366c2f8bd32d93   → 打不开文件内容
    /zhengce/detail?businessId=6e3f54d554174dfd8f366c2f8bd32d93&siteId=0010  → 正常

本库此前统一用路径式拼接，影响全部平台条目（约 2,400 条）。
本脚本把 CSV 里形如
    https://www.shanghai.gov.cn/zhengce/detail/<siteId>::<businessId>
改写为
    https://www.shanghai.gov.cn/zhengce/detail?businessId=<businessId>&siteId=<siteId>

幂等：已是查询参数式的跳过。
"""
import csv
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
CSV = os.path.join(HERE, "data", "gov_docs.csv")
SH = "https://www.shanghai.gov.cn"

# 路径式：.../zhengce/detail/<siteId>::<businessId>
PAT_PATH = re.compile(r"(?P<base>https?://[^\s|]*?/zhengce/detail)/(?P<site>[0-9A-Za-z]+)::(?P<bid>[^\s|?#]+)")
# 查询参数式（已正确的）
PAT_QUERY = re.compile(r"/zhengce/detail\?businessId=")


def fix(url):
    if not url:
        return url, False
    if PAT_QUERY.search(url):
        return url, False
    m = PAT_PATH.search(url)
    if not m:
        return url, False
    new = "%s/zhengce/detail?businessId=%s&siteId=%s" % (SH, m.group("bid"), m.group("site"))
    return new, True


def main():
    rows = list(csv.DictReader(open(CSV, encoding="utf-8-sig")))
    fields = list(rows[0].keys())

    n = 0
    samples = []
    for r in rows:
        old = r.get("官方链接") or ""
        new, changed = fix(old)
        if changed:
            r["官方链接"] = new
            n += 1
            if len(samples) < 5:
                samples.append((old, new))

    # 正文 md 里若含旧链接，也一并替换
    n_md = 0
    for r in rows:
        p = (r.get("正文") or "").strip()
        if not p:
            continue
        fp = os.path.join(HERE, p) if not os.path.isabs(p) else p
        if not os.path.exists(fp):
            continue
        try:
            s = open(fp, encoding="utf-8").read()
        except Exception:
            continue
        new_s, k = PAT_PATH.subn(
            lambda m: "%s/zhengce/detail?businessId=%s&siteId=%s" % (SH, m.group("bid"), m.group("site")),
            s)
        if k:
            open(fp, "w", encoding="utf-8").write(new_s)
            n_md += 1

    with open(CSV, "w", encoding="utf-8-sig", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields, extrasaction="ignore")
        w.writeheader()
        w.writerows(rows)

    print("修正官方链接 %d / %d 条" % (n, len(rows)))
    for old, new in samples:
        print("  - %s" % old)
        print("  + %s" % new)
    print("同步修正正文 md 中的链接：%d 个文件" % n_md)
    print("✓ 回写 %s" % CSV)


if __name__ == "__main__":
    main()