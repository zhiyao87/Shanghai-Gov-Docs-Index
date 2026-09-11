# -*- coding: utf-8 -*-
"""抓「上海人大 · 法规公布」栏目的地方性法规清单。

为什么必须补这一源
------------------
市政府的三个源（规章库 / 住建委规范性文件 / 统一政策发布平台）**都不含地方性法规**。
地方性法规由**市人民代表大会及其常委会**制定，效力高于政府规章 ——
《上海市住宅物业管理规定》《上海市城市更新条例》《上海市历史文化风貌区和优秀历史建筑保护条例》
这类报建高频依据全在这里，缺了它库是残的。

栏目结构（2026-09-11 实测）
--------------------------
列表页     https://www.shrd.gov.cn/shrd/fggb/fggb.html
分页接口   /TrueCMS/messageController/getMessage.do
           ?startrecord=1&endrecord=20&perpage=20&columnId=82e1eed4-ef97-4ba8-b3da-2299d731060c
           （参数名 startrecord/endrecord/perpage 来自该站 jquery.jpage.js 的 getRemoteData()）
总数       279 条

⚠ 旧域名 www.spcsc.sh.cn（原「上海市法规规章规范性文件数据库」）已**被非官方站点占用**，
   2026-09-11 实测解析到博彩/直播站，**不可再用**。现用 www.shrd.gov.cn。

用法
----
    python scrape_shrd.py             # 抓全量 279 条 → data/raw_shrd_laws.tsv
"""
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import fetch, html_to_text, log  # noqa: E402

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "data", "raw_shrd_laws.tsv")

BASE = "https://www.shrd.gov.cn"
API = BASE + "/TrueCMS/messageController/getMessage.do"
LIST_PAGE = BASE + "/shrd/fggb/fggb.html"
COLUMN_ID = "82e1eed4-ef97-4ba8-b3da-2299d731060c"   # 「法规公布」栏目
PER_PAGE = 20

HEADERS = {
    "Referer": LIST_PAGE,
    "X-Requested-With": "XMLHttpRequest",
}


def fetch_page(start):
    """抓一页（startrecord 从 1 开始）。返回 (总记录数, [(标题, 绝对URL), ...])。"""
    url = ("%s?startrecord=%d&endrecord=%d&perpage=%d&columnId=%s"
           % (API, start, start + PER_PAGE - 1, PER_PAGE, COLUMN_ID))
    code, raw = fetch(url, headers=HEADERS, timeout=40)
    if code != 200:
        raise RuntimeError("HTTP %s @ startrecord=%d" % (code, start))
    txt = raw.decode("utf-8", "replace")
    try:
        payload = json.loads(txt)
        body = payload.get("result") or ""
    except Exception:
        body = txt

    m = re.search(r"<totalrecord>(\d+)</totalrecord>", body)
    total = int(m.group(1)) if m else 0

    items = []
    for href, title in re.findall(r'<a\s+href="([^"]+)"[^>]*>(.*?)</a>', body, re.S):
        title = html_to_text(title).strip()
        if not title:
            continue
        items.append((title, abs_url(href)))
    return total, items


def abs_url(href):
    href = html_to_text(href).strip()
    if href.startswith("http"):
        return href
    if href.startswith("/"):
        return BASE + href
    return BASE + "/shrd/fggb/" + href


def main():
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    rows, seen = [], set()
    start, total = 1, None
    while True:
        t, items = fetch_page(start)
        if total is None:
            total = t
            log("总记录数 %d，共 %d 页" % (total, (total + PER_PAGE - 1) // PER_PAGE))
        if not items:
            break
        for title, url in items:
            if url in seen:
                continue
            seen.add(url)
            rows.append((title, url))
        log("  startrecord=%-4d 累计 %d / %d" % (start, len(rows), total))
        start += PER_PAGE
        if start > total:
            break

    with open(OUT, "w", encoding="utf-8") as f:
        f.write("标题\t正文页URL\n")
        for title, url in rows:
            f.write("%s\t%s\n" % (title.replace("\t", " "), url))
    log("✓ %s（%d 条）" % (OUT, len(rows)))


if __name__ == "__main__":
    main()
