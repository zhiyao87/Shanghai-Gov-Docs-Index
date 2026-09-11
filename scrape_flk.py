# -*- coding: utf-8 -*-
"""抓「国家法律法规数据库」里的**上海市地方性法规**（含正文）。

为什么用这一源
--------------
上海市政府那三个源都不含地方性法规；上海人大官网的「法规公布」栏目又只是**近期公布流**
（2020 年以后的新规），《上海市住宅物业管理规定》《上海市城乡规划条例》《上海市建筑市场
管理条例》这类**早年的现行法规根本不在里面**。

国家法律法规数据库（全国人大常委会办公厅维护）收录**全部现行有效地方性法规**，
并且提供官方 DOCX / PDF 正文 —— 这是把「地方性法规」这一档补齐的唯一可靠来源。

接口（2026-09-11 逆向前端得到，前端为 Vue3 + vite 打包）
----------------------------------------------------
检索   POST /law-search/search/list
       body: {searchContent, searchType:1, searchRange:2, zdjgCodeId:[250], flfgCodeId:[],
              gbrqYear:[], orderByParam:null, scoreDto:{}, pageNum, pageSize}
       ⚠ searchRange 不能为 0（返回 500）；zdjgCodeId=250 即「地方人大及其常委会 → 上海」
详情   GET  /law-search/search/flfgDetails?bbbs=<bbbs>      → ossFile 内的 word/pdf 路径
下载   GET  /law-search/download/pc?format=docx&bbbs=<id>&fileId=
       → data.url（公网直链，可下到官方 DOCX/PDF 原件）
枚举   GET  /law-search/search/enumData                     → flfgfl / zdjgfl / flcaStatus
前台详情页  https://flk.npc.gov.cn/detail?id=<bbbs>&title=<标题>

产出
----
data/raw_flk_sh_laws.tsv   上海地方性法规全量清单（含时效性 sxx）
data/flk_fulltext/<bbbs>.txt  建设相关法规的官方正文（纯文本）

用法
----
    python scrape_flk.py            # 抓清单 + 建设相关正文
    python scrape_flk.py --list     # 只抓清单
"""
import argparse
import io
import json
import os
import re
import sys
import time
import zipfile

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import fetch, post_json  # noqa: E402

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(HERE, "data")
OUT_TSV = os.path.join(DATA, "raw_flk_sh_laws.tsv")
FULLTEXT_DIR = os.path.join(DATA, "flk_fulltext")

API = "https://flk.npc.gov.cn"
LIST_URL = API + "/law-search/search/list"
DL_URL = API + "/law-search/download/pc"
DETAIL_URL = API + "/detail?id=%s&title=%s"

HDRS = {"Referer": API + "/", "Origin": API}

ZDJG_SHANGHAI = 250          # 制定机关：地方人大及其常委会 → 上海
PER_PAGE = 100

# sxx（时效性）取值 → 文案。取值由全量数据分布推断，仅作提示。
SXX = {1: "尚未生效", 2: "已修改", 3: "有效", 4: "已废止", 5: "已失效"}


def post(url, payload, timeout=40):
    return post_json(url, payload, headers=HDRS, timeout=timeout)


def list_page(page, size=PER_PAGE, extra=None):
    body = {
        "searchContent": "", "searchType": 1, "searchRange": 2,
        "zdjgCodeId": [ZDJG_SHANGHAI], "flfgCodeId": [],
        "gbrqYear": [], "orderByParam": None, "scoreDto": {},
        "pageNum": page, "pageSize": size,
    }
    if extra:
        body.update(extra)
    return post(LIST_URL, body)


def strip_hl(s):
    return re.sub(r"<[^>]+>", "", s or "")


def scrape_list():
    first = list_page(1)
    if not first:
        raise RuntimeError("检索失败")
    total = first.get("total") or 0
    pages = (total + PER_PAGE - 1) // PER_PAGE
    print("上海地方性法规 共 %d 条 / %d 页" % (total, pages))
    rows, seen = [], set()
    for p in range(1, pages + 1):
        d = first if p == 1 else list_page(p)
        for r in (d or {}).get("rows", []):
            b = r.get("bbbs")
            if not b or b in seen:
                continue
            seen.add(b)
            rows.append({
                "标题": strip_hl(r.get("title")),
                "公布日期": r.get("gbrq") or "",
                "施行日期": r.get("sxrq") or "",
                "时效性": SXX.get(r.get("sxx"), str(r.get("sxx") or "")),
                "制定机关": r.get("zdjgName") or "",
                "bbbs": b,
            })
        print("  第 %2d/%d 页，累计 %d" % (p, pages, len(rows)))
        time.sleep(0.2)
    return rows


def docx_to_text(blob):
    """DOCX（zip + word/document.xml）→ 纯文本，零第三方依赖。"""
    with zipfile.ZipFile(io.BytesIO(blob)) as z:
        try:
            xml = z.read("word/document.xml").decode("utf-8", "replace")
        except KeyError:
            return ""
    # 段落/换行 → 换行；tab → 制表符；其余标签剔除
    xml = re.sub(r"</w:p>", "\n", xml)
    xml = re.sub(r"<w:tab[^>]*/>", "\t", xml)
    xml = re.sub(r"<w:br[^>]*/>", "\n", xml)
    txt = re.sub(r"<[^>]+>", "", xml)
    import html as _html
    txt = _html.unescape(txt)
    lines = [ln.strip() for ln in txt.split("\n")]
    out, blank = [], 0
    for ln in lines:
        if not ln:
            blank += 1
            if blank > 1:
                continue
        else:
            blank = 0
        out.append(ln)
    return "\n".join(out).strip()


def fetch_fulltext(bbbs, want="docx"):
    """下载官方正文并转纯文本；失败返回空串。"""
    code, raw = fetch("%s?format=%s&bbbs=%s&fileId=" % (DL_URL, want, bbbs),
                      headers=HDRS, timeout=60)
    if code != 200:
        return ""
    try:
        payload = json.loads(raw.decode("utf-8"))
        url = (payload.get("data") or {}).get("url") or ""
    except Exception:
        return ""
    if not url:
        return ""
    code, blob = fetch(url, timeout=90)
    if code != 200:
        return ""
    if blob[:4] == b"PK\x03\x04":
        return docx_to_text(blob)
    if blob[:4] == b"%PDF":
        return ""          # 不引第三方 PDF 解析；正文以 DOCX 为准
    return blob.decode("utf-8", "replace")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--list", action="store_true", help="只抓清单，不抓正文")
    args = ap.parse_args()

    os.makedirs(DATA, exist_ok=True)
    rows = scrape_list()

    with open(OUT_TSV, "w", encoding="utf-8", newline="") as f:
        f.write("标题\t公布日期\t施行日期\t时效性\t制定机关\tbbbs\n")
        for r in rows:
            f.write("\t".join(r[k].replace("\t", " ")
                              for k in ("标题", "公布日期", "施行日期", "时效性", "制定机关", "bbbs"))
                    + "\n")
    print("✓ %s（%d 条）" % (OUT_TSV, len(rows)))

    if args.list:
        return

    # 只为「建设相关」的抓正文，避免无谓下载
    sys.path.insert(0, HERE)
    from classify import is_relevant
    os.makedirs(FULLTEXT_DIR, exist_ok=True)
    todo = [r for r in rows if is_relevant(r["标题"], r["制定机关"])]
    print("其中建设相关 %d 条，开始抓官方正文…" % len(todo))
    ok = 0
    for i, r in enumerate(todo, 1):
        path = os.path.join(FULLTEXT_DIR, r["bbbs"] + ".txt")
        if os.path.exists(path) and os.path.getsize(path) > 200:
            ok += 1
            continue
        txt = fetch_fulltext(r["bbbs"])
        if len(txt) > 200:
            with open(path, "w", encoding="utf-8") as f:
                f.write(txt)
            ok += 1
        else:
            print("    ✗ %s" % r["标题"][:40])
        if i % 10 == 0:
            print("   %d/%d，成功 %d" % (i, len(todo), ok))
        time.sleep(0.25)
    print("✓ 正文 %d/%d → %s" % (ok, len(todo), FULLTEXT_DIR))


if __name__ == "__main__":
    main()
