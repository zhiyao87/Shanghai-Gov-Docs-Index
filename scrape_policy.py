# -*- coding: utf-8 -*-
"""抓取「上海市统一政策发布平台」全量现行有效政策文件。

数据源：https://www.shanghai.gov.cn/zhengce/list
接口：  POST https://www.shanghai.gov.cn/gwk/policy/page
        {"pageNo":N,"pageSize":150}   （pageSize 上限 150）

返回体关键字段
--------------
title / publishDate / siteId / businessId / effectiveFlag / indexNo
attrs.agency         发布单位
attrs.zwPDFUrl       官方 PDF 直链（.pdf，可下载）
attrs.documentAgency 发文机关代字
attrs.policyLevel    市级 / 区级 / 街镇级
attrs.openType       主动公开 / 依申请公开

产出：data/raw_policy_all.json

用法
----
    python scrape_policy.py            # 全量抓取
    python scrape_policy.py --pages 3  # 只抓前 3 页（调试）
"""

import argparse
import json
import os
import sys
import time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import common  # noqa: E402

API = "https://www.shanghai.gov.cn/gwk/policy/page"
REFERER = {"Referer": "https://www.shanghai.gov.cn/zhengce/list"}
PAGE_SIZE = 150
HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "data", "raw_policy_all.json")


def one_page(page_no):
    payload = {"pageNo": page_no, "pageSize": PAGE_SIZE}
    return common.post_json(API, payload, headers=REFERER, timeout=50, retries=4)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--pages", type=int, default=0, help="只抓前 N 页（0=全部）")
    ap.add_argument("--sleep", type=float, default=0.4, help="每页间隔秒")
    args = ap.parse_args()

    print("[1/3] 取第一页确认总数 …")
    d = one_page(1)
    if not d or d.get("code") != 0:
        print("    ✗ 接口不可达：", d)
        return 1
    meta = d["data"]
    total = meta["totalCount"]
    total_pages = meta["totalPage"]
    limit = args.pages or total_pages
    print("    总数 %d 条 / %d 页（每页 %d）" % (total, total_pages, PAGE_SIZE))

    records = list(meta.get("records") or [])
    seen = {(r.get("siteId"), r.get("businessId")) for r in records}

    print("[2/3] 翻页抓取 …")
    for pn in range(2, limit + 1):
        d = one_page(pn)
        if not d or d.get("code") != 0 or not d.get("data"):
            print("    第 %d 页失败，跳过" % pn)
            time.sleep(2)
            continue
        n = 0
        for r in d["data"].get("records") or []:
            key = (r.get("siteId"), r.get("businessId"))
            if key in seen:
                continue
            seen.add(key)
            records.append(r)
            n += 1
        if pn % 10 == 0 or pn == limit:
            print("    第 %d/%d 页，累计 %d 条" % (pn, limit, len(records)))
        time.sleep(args.sleep)

    print("[3/3] 落盘 …")
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, "w", encoding="utf-8") as f:
        json.dump({"totalCount": total, "fetchedAt": time.strftime("%Y-%m-%d %H:%M:%S"),
                   "count": len(records), "records": records}, f,
                  ensure_ascii=False, indent=1)
    print("    ✓ %s（%d 条，%.1f KB）" % (OUT, len(records), os.path.getsize(OUT) / 1024))
    return 0


if __name__ == "__main__":
    sys.exit(main())
