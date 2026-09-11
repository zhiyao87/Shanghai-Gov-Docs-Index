# -*- coding: utf-8 -*-
"""官方链接与正文文件巡检。

做三件事
--------
1. 本地一致性：data/gov_docs.csv 里「正文」列指向的文件是否真的存在
2. 链接格式：官方链接是否为合法 URL（不做网络请求）
3. 联网抽检/全检：同时巡检「官方链接」与「红头PDF」两条，
   判定 200 / 受限 / 失效 / SPA 详情页 / 内容未命中

用法
----
    python check_links.py              # 本地一致性 + 格式检查（秒级）
    python check_links.py --net        # 全部联网巡检（约 12–15 分钟）
    python check_links.py --net --core # 只巡检核心文件
    python check_links.py --net -n 40  # 随机抽检 40 条
    python check_links.py --net --col official    # 只巡检「官方链接」

要点（与 Arch-Standards-Index 的 check_links.py 对齐）
----------------------------------------------------
- HTTP 200 不等于「通过」：纯前端渲染的详情页（政策平台
  shanghai.gov.cn/zhengce/detail?businessId=…）原始 HTML 只有几 KB
  空壳 + 满屏 <script>，正文由 JS 异步注入，urllib 抓不到一个字。
  这种不归「失效」，归「需浏览器确认」。
- 真正的「内容命中」判定：200 页面里去 <script>/<style> 后的可见文本，
  应能命中该行的「标题」前 14 字或「文号」。命中不了才报 warn。
- 政府站偶发抖动（HTTPS 1 次，HTTP 0 是沙箱代理超时），所有失败重试
  2 次；最终 HTTP 0 的会进 bad，需手工 curl 复验。
"""

import argparse
import csv
import json
import os
import random
import re
import sys
import time
import urllib.parse

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import common  # noqa: E402
from build_docs_index import CORE_TYPES, OUT_CSV  # noqa: E402

HERE = os.path.dirname(os.path.abspath(__file__))


def _flat(html):
    """去 script/style/标签，剩纯文本。"""
    if not html:
        return ""
    return common.html_to_text(html)


def _is_spa(html):
    """政策平台详情页是纯 JS 渲染，<script> 满屏但可见文本几乎是空。

    判据：去标签后可见文本 < 300 字符 且 <script> 标签 ≥ 5 个。
    """
    if not html:
        return False
    script_n = html.count("<script")
    visible = _flat(html).strip()
    return script_n >= 5 and len(visible) < 300


def _title(html):
    """从 HTML 里抠 <title>。失败返回空串。"""
    if not html:
        return ""
    m = re.search(r"<title[^>]*>(.*?)</title>", html, re.S | re.I)
    if not m:
        return ""
    t = re.sub(r"\s+", " ", m.group(1)).strip()
    return t[:80]


def judge(code, ctype="", body=b"", row=None):
    """返回 (等级, 说明)。

    等级：ok / warn / bad / limited

    limited 又分两种：站点反爬（403/429/503）与 SPA 详情页（前端渲染），
    都不是失效，但需要单独看。
    """
    if code == 200:
        if "pdf" in (ctype or "").lower():
            return "ok", "PDF 可下载"
        # HTML/JSON 类页面：先看是不是 SPA 详情页
        try:
            html = body.decode("utf-8", "replace")
        except Exception:
            html = ""
        if _is_spa(html):
            return "limited-spa", "前端渲染页（需浏览器加载）"
        # 真的能取到内容 → 做命中判定
        text = _flat(html)
        title = _title(html)
        if row:
            kw1 = (row.get("标题") or "").strip()[:14]
            kw2 = (row.get("文号") or "").strip()
            if kw1 and (kw1 in text or kw1 in title):
                return "ok", "命中标题｜%s" % title[:40]
            if kw2 and (kw2 in text or kw2 in title):
                return "ok", "命中文号｜%s" % title[:40]
        # 既不是 PDF、又没有正文命中，但有内容（多半是栏目首页）
        return "warn", "200 但内容未命中（页面：%s）" % title[:40]
    if code in (403, 429, 503):
        return "limited", "反爬限制（非失效）"
    if code == 404:
        return "bad", "404"
    if code == 0:
        return "bad", "网络不可达"
    return "warn", "HTTP %d" % code


def fetch_one(url):
    """走 common.fetch：返回 (status, bytes, content_type)。"""
    code, body = common.fetch(url, timeout=30, retries=2)
    return code, body, ""  # urllib 不直接给 content-type，按 body 嗅探


def sniff_type(body, url):
    """从 body 前 1024 字节嗅探：PDF / HTML / JSON / 其他。"""
    head = body[:1024] if body else b""
    if head.startswith(b"%PDF"):
        return "pdf"
    if head.lstrip().startswith(b"<!DOCTYPE") or head.lstrip().startswith(b"<html"):
        return "html"
    if head.lstrip().startswith(b"{") or head.lstrip().startswith(b"["):
        return "json"
    # URL 路径里带 .pdf 也算
    if ".pdf" in (url or "").lower():
        return "pdf"
    return ""


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--net", action="store_true")
    ap.add_argument("--core", action="store_true")
    ap.add_argument("-n", "--limit", type=int, default=0)
    ap.add_argument("--sleep", type=float, default=0.3)
    ap.add_argument("--col", choices=["all", "official", "pdf"],
                    default="all", help="巡检列：all=官方链接+红头PDF / official / pdf")
    ap.add_argument("--json", help="把结果写入 JSON 文件")
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

    # 2) 联网巡检
    todo = rows
    if args.core:
        todo = [r for r in rows if r.get("类型") in CORE_TYPES]

    # 展开成 (row, col, url) 三元组
    jobs = []
    for r in todo:
        if args.col in ("all", "official"):
            u = (r.get("官方链接") or "").strip()
            if u:
                jobs.append((r, "official", u))
        if args.col in ("all", "pdf"):
            u = (r.get("红头PDF") or "").strip()
            if u:
                jobs.append((r, "pdf", u))
    if args.limit:
        jobs = random.sample(jobs, min(args.limit, len(jobs)))
    print("\n[联网] 巡检 %d 个链接（%d 条记录）…" % (len(jobs), len(todo)))

    stat = {"ok": 0, "limited": 0, "limited-spa": 0,
            "warn": 0, "bad": 0}
    bads = []
    results = []
    for i, (r, col, url) in enumerate(jobs, 1):
        code, body, ctype = fetch_one(url)
        ctype = sniff_type(body, url) or ctype
        st, note = judge(code, ctype, body, r)
        stat[st] += 1
        results.append({
            "标题": r.get("标题") or "",
            "列": col,
            "链接": url,
            "状态": code,
            "等级": st,
            "说明": note,
        })
        if st in ("bad", "warn"):
            bads.append((col, code, note, r.get("标题") or "", url))
        if i % 100 == 0:
            print("   %d/%d  ok=%d spa=%d limited=%d warn=%d bad=%d"
                  % (i, len(jobs), stat["ok"], stat["limited-spa"],
                     stat["limited"], stat["warn"], stat["bad"]))
        time.sleep(args.sleep)

    print("\n=== 结果 ===")
    print("正常 %d ｜ SPA %d ｜ 受限 %d ｜ 警告 %d ｜ 失效 %d" %
          (stat["ok"], stat["limited-spa"], stat["limited"],
           stat["warn"], stat["bad"]))
    if bads:
        print("\n失效/警告前 30：")
        for col, code, note, title, u in bads[:30]:
            print("  [%s %s] [%s] %s\n      %s"
                  % (code, note, col, title[:50], u))
    else:
        print("\n全部链接 OK。")

    if args.json:
        with open(args.json, "w", encoding="utf-8") as f:
            json.dump({
                "总数": len(rows),
                "抽样": len(jobs),
                "列": args.col,
                "core_only": args.core,
                "统计": stat,
                "结果": results,
            }, f, ensure_ascii=False, indent=1)
        print("\n结果已写入 %s" % args.json)


if __name__ == "__main__":
    main()