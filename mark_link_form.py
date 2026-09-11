#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""给「统一政策发布平台」链接标注形态，识别可能在前端渲染失败的短数字 ID。

背景
----
戴工实测 `https://www.shanghai.gov.cn/zhengce/detail/0084::00844352` 打开后
不是文件内容。排查结论：

- 平台详情页是 Vue SPA，服务端只返回 4,475 字节的壳页，正文由 JS 调
  `/gwk/policy/detail` 渲染 —— 所以**服务端无法验证渲染成败**；
- 数据本身没问题：用 API 查 `siteId=0084&businessId=00844352` 正文 85,069 字符；
- 差异只在 ID 形态：主流 businessId 是 32 位 hash（如 `39b001a3f37d48cbbdd5dd1eb2ccc5e6`），
  而部分区级老数据是 **8–11 位纯数字**（如 `00844352`）；
- 前端路由/解析对短数字 ID 处理异常（去掉前导 0 后 API 返回空，已实测 `844352` → 空），
  因此这类链接**有渲染失败风险**；
- 库内正文不受影响（docs/ 已有全文），只有"点击原网页"这一路径受影响。

本脚本给 data/gov_docs.csv 加「链接形态」列：
    hash    标准 32 位 hash，正常
    short   8–11 位纯数字，前端可能渲染失败 → 优先看库内正文
    其他/空 非平台链接
"""
import csv
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
CSV = os.path.join(HERE, "data", "gov_docs.csv")
COL = "链接形态"

PAT = re.compile(r"/zhengce/detail/([0-9a-zA-Z]+)::(.+)$")


def form_of(url):
    m = PAT.search(url or "")
    if not m:
        return ""
    bid = m.group(2)
    if re.fullmatch(r"\d{8,11}", bid):
        return "short"
    if len(bid) >= 16:
        return "hash"
    return "other"


def main():
    rows = list(csv.DictReader(open(CSV, encoding="utf-8-sig")))
    fields = list(rows[0].keys())
    if COL not in fields:
        fields.append(COL)

    from collections import Counter
    c = Counter()
    for r in rows:
        f = form_of(r.get("官方链接"))
        r[COL] = f
        if f:
            c[f] += 1

    with open(CSV, "w", encoding="utf-8-sig", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=fields, extrasaction="ignore")
        w.writeheader()
        w.writerows(rows)

    total = len(rows)
    print("标注 %d 条" % total)
    for k, v in c.most_common():
        print("  %-6s %5d" % (k, v))
    print("  非平台链接 %d" % (total - sum(c.values())))
    print("✓ 回写 %s" % CSV)


if __name__ == "__main__":
    main()