# -*- coding: utf-8 -*-
"""抓每条文件的**权威原件**：红头文件 PDF / 红头封面图 / 附表附图附件。

为什么需要它
------------
统一政策发布平台的详情接口除了正文（``data.txt``）之外，还挂着三类**正文抓不到**的东西：

    data.attrs.zwPDFUrl           红头文件 PDF（盖章原件的扫描/排版稿）
    data.attrs.zwPDFCoverImgUrl   红头文件首页图（PNG，一眼认文号）
    data.attaches[]               附表、附图、附件（技术规范真正的操作部分）

以《上海市日照分析技术规范》（沪规划资源建〔2021〕437号）为例：
带参数的日照计算表格、窗台高度取值、图示全在“附表、附图、附件.pdf”里，
只抓正文等于把最有用的部分丢了。

市府规章库页面：「下载文字版」(.docx) / 「下载图片版」(.pdf)
市住建委页面：正文页面内嵌 ``/cmsres/...`` 下的 PDF（常名为「定稿正文.pdf」）
两类页面统一按“扫全部文件链接”处理。

产出
----
data/gov_docs.csv      新增三列：红头PDF / 红头封面 / 附件（均为绝对 URL；附件多条用 ｜ 分隔）
attachments/           （仅 --download 时）原件落盘，结构 attachments/<分类>/<标题>/，
                       并在 attachment_manifest.csv 留下清单。该目录默认 .gitignore，
                       避免公开仓库被二进制撑爆。
用法
----
    python fetch_assets.py                # 只抓链接，回写 CSV
    python fetch_assets.py --download     # 同时把原件下到 attachments/
    python fetch_assets.py --limit 30
    python fetch_assets.py --redo
"""
import argparse
import csv
import os
import re
import sys
import time
import urllib.parse

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import common  # noqa: E402
from build_docs_index import OUT_CSV  # noqa: E402

HERE = os.path.dirname(os.path.abspath(__file__))
SH = "https://www.shanghai.gov.cn"
DETAIL_API = SH + "/gwk/policy/detail"
REFERER = {"Referer": SH + "/zhengce/list"}
ATTACH_DIR = os.path.join(HERE, "attachments")
MANIFEST = os.path.join(HERE, "attachment_manifest.csv")

NEW_COLS = ["红头PDF", "红头封面", "附件"]
BAD = re.compile(r'[\\/:*?"<>|\r\n\t]+')

# 页面里出现的文件链接（含 /cmsres/ 与 resource/file 两种形态）
RE_FILE = re.compile(
    r'(?:href|src)\s*=\s*["\']([^"\']+?\.(?:pdf|docx?|xlsx?|ofd|wps|zip))(?:\?[^"\']*)?["\']'
    r'|["\']([^"\']*?/gwk/resource/file\?[^"\']+)["\']',
    re.I)


def slug(t, n=48):
    s = BAD.sub("_", (t or "").strip())
    return re.sub(r"\s+", " ", s).strip(" ._")[:n] or "untitled"


def absu(href):
    href = (href or "").strip()
    if not href:
        return ""
    if href.startswith("http"):
        return href
    if href.startswith("//"):
        return "https:" + href
    return SH + (href if href.startswith("/") else "/" + href)


def from_platform(row):
    """平台条目：走详情接口拿三类原件。"""
    sid = bid = None
    url = row.get("官方链接", "")
    # 新格式（2026-09-11 起）：/zhengce/detail?businessId=<bid>&siteId=<sid>
    m = re.search(r"[?&]businessId=([^&#]+)", url)
    if m:
        bid = m.group(1)
        m2 = re.search(r"[?&]siteId=([^&#]+)", url)
        sid = m2.group(1) if m2 else None
    else:
        # 旧格式（路径式）：/zhengce/detail/<sid>::<bid>，仅作兼容
        m = re.search(r"detail/([^:]+)::(.+?)/?$", url)
        if m:
            sid, bid = m.group(1), m.group(2)
    if not (sid and bid):
        return "", "", []
    d = common.post_json(DETAIL_API, {"siteId": sid, "businessId": bid},
                         headers=REFERER, timeout=45, retries=3)
    if not d or not d.get("data"):
        return "", "", []
    data = d["data"]
    attrs = data.get("attrs") or {}
    pdf = absu(attrs.get("zwPDFUrl") or "")
    cover = absu(attrs.get("zwPDFCoverImgUrl") or "")
    atts = [(a.get("name") or "附件", absu(a.get("path") or ""))
            for a in (data.get("attaches") or []) if a.get("path")]
    return pdf, cover, atts


def from_page(row):
    """规章库 / 住建委条目：扫页面里的文件链接。

    规章库把「下载文字版(.docx)」和「下载图片版(.pdf)」并排给出，
    其中 .pdf 才是盖章原件，作为「红头PDF」；其余作为附件。
    """
    html = common.fetch_text(row.get("官方链接", ""), timeout=45, retries=3)
    if not html:
        return "", "", []
    files = []
    for m in RE_FILE.finditer(html):
        href = m.group(1) or m.group(2) or ""
        if not href:
            continue
        # 取锚文本作名字
        tail = html[m.end():m.end() + 120]
        nm = re.search(r">([^<]{1,40})<", tail)
        name = (nm.group(1).strip() if nm else "") or os.path.basename(
            urllib.parse.urlparse(href).path) or "附件"
        files.append((name, absu(href)))
    # 去重（同 URL 只留一条）
    seen, uniq = set(), []
    for name, url in files:
        if url in seen:
            continue
        seen.add(url)
        uniq.append((name, url))
    pdf = ""
    atts = []
    for name, url in uniq:
        if not pdf and url.lower().endswith(".pdf"):
            pdf = url
        else:
            atts.append((name, url))
    return pdf, "", atts


def download(row, want):
    """把原件下到 attachments/<分类>/<标题>/ 下，返回落盘清单。"""
    out = []
    d = os.path.join(ATTACH_DIR, slug(row.get("分类"), 20), slug(row.get("标题"), 48))
    for name, url in want:
        ext = os.path.splitext(urllib.parse.urlparse(url).path)[1] or ".bin"
        fn = slug(name, 40)
        if not fn.lower().endswith(ext.lower()):
            fn += ext
        code, blob = common.fetch(url, timeout=120)
        if code != 200 or len(blob) < 200:
            continue
        os.makedirs(d, exist_ok=True)
        path = os.path.join(d, fn)
        with open(path, "wb") as f:
            f.write(blob)
        out.append((os.path.relpath(path, HERE).replace("\\", "/"), len(blob), row.get("标题")))
        time.sleep(0.15)
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--download", action="store_true", help="同时下载原件到 attachments/")
    ap.add_argument("--limit", type=int, default=0)
    ap.add_argument("--redo", action="store_true", help="已有结果的也重抓")
    ap.add_argument("--sleep", type=float, default=0.3)
    args = ap.parse_args()

    rows = list(csv.DictReader(open(OUT_CSV, encoding="utf-8-sig")))
    if args.limit:
        rows = rows[:args.limit]
    todo = rows if args.redo else [r for r in rows if not r.get("红头PDF")
                                  and not r.get("附件") and not r.get("红头封面")]
    print("待处理 %d 条（总 %d）｜下载原件：%s" % (len(todo), len(rows), args.download))

    cols = list(rows[0].keys())
    for c in NEW_COLS:
        if c not in cols:
            cols.append(c)

    manifest, n_pdf, n_att = [], 0, 0
    for i, row in enumerate(todo, 1):
        try:
            if row.get("来源") == "统一政策发布平台":
                pdf, cover, atts = from_platform(row)
            else:
                pdf, cover, atts = from_page(row)
        except Exception as e:  # noqa: BLE001
            print("   ✗ %s：%s" % (row.get("标题", "")[:32], type(e).__name__))
            continue
        row["红头PDF"] = pdf or row.get("红头PDF", "")
        row["红头封面"] = cover or row.get("红头封面", "")
        row["附件"] = " ｜ ".join("%s|%s" % (n, u) for n, u in atts)
        if pdf:
            n_pdf += 1
        if atts:
            n_att += 1
        if args.download:
            want = [("红头文件", pdf)] if pdf else []
            want += atts
            want += [("封面", cover)] if cover else []
            manifest += download(row, [w for w in want if w[1]])
        if i % 25 == 0:
            print("   %d/%d ｜ 有红头PDF %d ｜ 有附件 %d" % (i, len(todo), n_pdf, n_att))
        time.sleep(args.sleep)

    with open(OUT_CSV, "w", encoding="utf-8-sig", newline="") as f:
        w = csv.DictWriter(f, fieldnames=cols, extrasaction="ignore")
        w.writeheader()
        w.writerows(rows)
    print("\n有红头PDF %d ｜ 有附件 %d ｜ 共 %d 条" % (n_pdf, n_att, len(todo)))
    print("✓ 回写 %s" % OUT_CSV)

    if args.download and manifest:
        with open(MANIFEST, "w", encoding="utf-8-sig", newline="") as f:
            w = csv.writer(f)
            w.writerow(["本地路径", "字节", "所属文件"])
            w.writerows(manifest)
        tot = sum(x[1] for x in manifest)
        print("✓ 原件 %d 个 / %.1f MB → %s" % (len(manifest), tot / 1048576, ATTACH_DIR))
        print("✓ 清单 %s" % MANIFEST)


if __name__ == "__main__":
    main()
