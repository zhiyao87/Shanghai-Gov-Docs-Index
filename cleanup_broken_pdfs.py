# -*- coding: utf-8 -*-
"""按链接巡检结果清空失效的「红头PDF」字段。

用法
----
    python cleanup_broken_pdfs.py --report link-check-2026-09-12.json   # 演练
    python cleanup_broken_pdfs.py --report link-check-2026-09-12.json --apply

背景
----
巡检脚本 (check_links.py) 输出 JSON 报告；本脚本读 JSON，从
data/gov_docs.csv 里把「红头PDF」字段是 JSON 报告里 bad 的 URL
**逐项清空**。

只清「红头PDF」一列。「官方链接」「附件」「正文」三列不动 —— 失效
PDF 都是 shanghai.gov.cn/cmsres/... 旧路径，官方详情页还活着，
用户仍能从页面里找到替代资源或正文。

执行前自动备份到 _backup/gov_docs.BEFORE-link-cleanup-YYYY-MM-DD.csv。
"""

import argparse
import csv
import datetime
import json
import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
CSV = os.path.join(HERE, "data", "gov_docs.csv")
BACKUP = os.path.join(HERE, "_backup")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--report", required=True,
                    help="check_links.py 输出的 JSON 报告路径")
    ap.add_argument("--apply", action="store_true",
                    help="真正写盘（默认 dry-run）")
    args = ap.parse_args()

    rep = json.load(open(args.report, encoding="utf-8"))
    bads = {r["链接"] for r in rep["结果"] if r["等级"] == "bad"}
    print("报告里 bad %d 个 URL" % len(bads))

    rows = list(csv.DictReader(open(CSV, encoding="utf-8-sig")))
    cols = list(rows[0].keys())

    n_pdf = 0
    n_attach = 0  # 暂留作未来扩展：附件里若含失效 URL 也清空
    sample = []
    for r in rows:
        if r["红头PDF"] and r["红头PDF"] in bads:
            n_pdf += 1
            sample.append((r["标题"][:50], r["红头PDF"][:80]))
            if not args.apply:
                continue
            r["红头PDF"] = ""
    print("命中「红头PDF」字段：%d 行" % n_pdf)
    for t, u in sample[:8]:
        print("  - %s\n    %s" % (t, u))
    if len(sample) > 8:
        print("  …还有 %d 行" % (len(sample) - 8))

    if not args.apply:
        print("\n（dry-run，加 --apply 才写盘）")
        return

    if n_pdf == 0:
        print("\n没有命中，CSV 无需修改。")
        return

    # 备份
    os.makedirs(BACKUP, exist_ok=True)
    ts = datetime.date.today().isoformat()
    bk = os.path.join(BACKUP, "gov_docs.BEFORE-link-cleanup-%s.csv" % ts)
    shutil.copy2(CSV, bk)
    print("\n备份: %s" % bk)

    # 写盘
    with open(CSV, "w", encoding="utf-8-sig", newline="") as f:
        w = csv.DictWriter(f, fieldnames=cols, extrasaction="ignore")
        w.writeheader()
        w.writerows(rows)
    print("已写盘：%d 条「红头PDF」清空" % n_pdf)


if __name__ == "__main__":
    sys.exit(main() or 0)