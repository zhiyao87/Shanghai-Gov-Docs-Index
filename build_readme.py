# -*- coding: utf-8 -*-
"""生成 README.md 与 index/ 分类索引。

用法：python build_readme.py
"""

import collections
import csv
import os
import re
import sys
import urllib.parse

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from build_docs_index import CAT_ORDER, CORE_TYPES, OUT_CSV  # noqa: E402
from channels import DEAD, DISTRICTS, MUNICIPAL  # noqa: E402

HERE = os.path.dirname(os.path.abspath(__file__))
INDEX_DIR = os.path.join(HERE, "index")
CAT_NO = ["一", "二", "三", "四", "五", "六", "七", "八", "九", "十"]


def q(url):
    return urllib.parse.quote(url or "", safe=":/?#[]@!$&'*+,;=%~.-_")


def link(url, label="官方"):
    return "[%s](%s)" % (label, q(url)) if url else "-"


def rows_of(path):
    return list(csv.DictReader(open(path, encoding="utf-8-sig")))


# 街镇机关名常见形态：上海市XX区YY镇人民政府 / XX区YY街道办事处 / YY街道办事处
_RE_TOWN = [
    re.compile(r"上海市[\u4e00-\u9fa5]{2,4}区([\u4e00-\u9fa5]{1,8}?(?:镇|街道办事处))"),
    re.compile(r"[\u4e00-\u9fa5]{2,4}区([\u4e00-\u9fa5]{1,8}?(?:镇|街道办事处))"),
    re.compile(r"([\u4e00-\u9fa5]{1,8}?(?:镇|街道办事处))"),
]


def town_unit(agency):
    """从发布机关里剥出街镇名。

    机关名的常见形态五花八门：
        上海市浦东新区人民政府洋泾街道办事处
        上海市奉贤区人民政府永丰街道办事处
        上海市青浦区朱家角镇人民政府
        海市浦东新区万祥镇人民政府          ← 源数据缺「上」字
        上海市吴泾镇人民政府
    统一做法：先砍掉「(中共)?上海市」，再砍到第一个「区」为止，再删「人民政府」。
    """
    ag = re.sub(r"\s+", "", (agency or "").strip())
    ag = re.sub(r"^(中共)?上海市", "", ag)
    if "区" in ag:
        ag = re.sub(r"^.*?区", "", ag, count=1)
    ag = ag.replace("人民政府", "").replace("管理委员会", "").replace("管委会", "")
    m = re.match(r"^([\u4e00-\u9fa5]{1,8}?(?:镇|街道办事处|街道))", ag)
    if m:
        return m.group(1)
    return ag[:14] or "其他"


def town_district(agency):
    ag = agency or ""
    for d in ("浦东新区", "黄浦区", "徐汇区", "长宁区", "静安区", "普陀区", "虹口区",
              "杨浦区", "宝山区", "闵行区", "嘉定区", "金山区", "松江区", "青浦区",
              "奉贤区", "崇明区"):
        if d in ag:
            return d
    return "其他"


def validity_mark(v):
    """把「时效复核」列压成一个字符，方便在宽表里一眼扫。"""
    v = (v or "").strip()
    if v.startswith("现行有效"):
        return "✓"
    if v.startswith("⚠"):
        return "⚠"
    if v.startswith("已废止"):
        return "✗"
    return "?"


def assets_cell(r):
    """正文列：把「正文 / 红头文件 / 附表附图」三种取用方式并成一格，避免表格过宽。"""
    bits = []
    body = r.get("正文") or ""
    if body:
        bits.append(link(body, "正文"))
    pdf = (r.get("红头PDF") or "").strip()
    if pdf:
        bits.append(link(pdf, "红头PDF"))
    raw = (r.get("附件") or "").strip()
    if raw:
        atts = []
        for part in raw.split(" ｜ "):
            name, _, url = part.partition("|")
            if url:
                atts.append((name.strip() or "附件", url.strip()))
        if len(atts) == 1:
            bits.append(link(atts[0][1], "附表附图"))
        elif atts:
            bits.append("%s（%d 个）" % (link(atts[0][1], "附表附图"), len(atts)))
    return " · ".join(bits) if bits else "-"


def table(rows, with_body=True):
    if with_body:
        head = ("| 标题 | 类型 | 层级 | 文号 | 发布机关 | 发布日期 | 状态 | 时效 | 正文 / 原件 |\n"
                "|---|---|---|---|---|---|---|---|---|\n")
    else:
        head = ("| 标题 | 类型 | 层级 | 文号 | 发布机关 | 发布日期 | 状态 | 时效 |\n"
                "|---|---|---|---|---|---|---|---|\n")
    out = [head]
    for r in rows:
        title = "[%s](%s)" % ((r["标题"] or "").replace("|", "｜"), q(r["官方链接"]))
        cells = [title, r["类型"], r["层级"], r["文号"] or "-",
                 (r["发布单位"] or "-").replace("|", "｜"), r["发布日期"] or "-",
                 r["状态"] or "-", validity_mark(r.get("时效复核"))]
        if with_body:
            cells.append(assets_cell(r))
        out.append("| " + " | ".join(cells) + " |\n")
    return "".join(out)


# ------------------------------------------------------------------ 索引文件

def write_category_indexes(rows):
    os.makedirs(INDEX_DIR, exist_ok=True)
    cat_files = {}
    for i, cat in enumerate(CAT_ORDER, 1):
        sub = [r for r in rows if r["分类"] == cat]
        if not sub:
            continue
        sub.sort(key=lambda r: (r["层级"] != "市级", r["类型"] not in CORE_TYPES,
                                -int(r["发布日期"][:4] or 0)))
        fn = "index/%02d-%s.md" % (i, cat)
        cat_files[cat] = fn
        L = ["# %s\n" % cat,
             "\n共 **%d** 条（市级 %d ／ 区级 %d ／ 其他 %d）\n"
             % (len(sub),
                sum(1 for r in sub if r["层级"] == "市级"),
                sum(1 for r in sub if r["层级"] == "区级"),
                sum(1 for r in sub if r["层级"] not in ("市级", "区级"))),
             "\n[← 返回总目录](../README.md)\n",
             "\n## 市级\n\n"]
        L.append(table([r for r in sub if r["层级"] == "市级"]))
        qu = [r for r in sub if r["层级"] != "市级"]
        if qu:
            L.append("\n## 区级 / 街镇级\n\n")
            L.append(table(qu))
        open(os.path.join(HERE, fn), "w", encoding="utf-8").write("".join(L))
    return cat_files


def write_town_index(rows):
    """街镇级发文单独成册 —— **2026-09-11 戴工指示：街镇级不再收录，本册停用**。

    原设计理由（留档）：街镇是「限额以下小型建设工程」的实际管理主体，
    限额以下小项目（装修、加建、小型改造）报建时真正卡人的是街镇自己出的办法，
    而它在市、区两级栏目里检索不到。
    现按戴工指示整层移除：街镇级条目已从 CSV 删除，正文与索引册一并下架。
    函数保留但直接返回空，避免调用方改动。
    """
    return None, []


def _write_town_index_disabled(rows):
    town = [r for r in rows if r["层级"] == "街镇级"]
    fn = "index/11-街镇级发文.md"
    L = ["# 街镇级发文\n",
         "\n**共 %d 条**，出自 %d 个街镇/街道。\n"
         % (len(town), len({town_unit(r["发布单位"]) for r in town})),
         "\n> 为什么单列：街镇是**限额以下小型建设工程**的实际管理主体。\n"
         "> 这类项目（装修、加建、小型改造）报建时真正卡你的是街镇自己出的办法，\n"
         "> 而它在市、区两级的栏目里**检索不到**。\n",
         "\n[← 返回总目录](../README.md)\n",
         "\n## 专题：限额以下小型建设工程\n\n"]
    small = [r for r in town if re.search(r"(限额以下|小型建设|小额建设|村级集体投资|政府投资小型)", r["标题"])]
    small.sort(key=lambda r: -int(r["发布日期"][:4] or 0))
    if small:
        L.append("同一主题在不同街镇各有一套办法，**用前务必确认项目所属街镇**：\n\n")
        L.append(table(small))
    else:
        L.append("（本库暂无）")

    L.append("\n## 全部街镇级发文（按街镇）\n")
    g = collections.defaultdict(list)
    for r in town:
        g[town_unit(r["发布单位"])].append(r)
    for unit in sorted(g, key=lambda u: (-len(g[u]), u)):
        L.append("\n### %s（%d 条）\n\n" % (unit, len(g[unit])))
        L.append(table(sorted(g[unit], key=lambda x: -int(x["发布日期"][:4] or 0))))
    open(os.path.join(HERE, fn), "w", encoding="utf-8").write("".join(L))
    return fn, town


# ------------------------------------------------------------------ README

def build_readme(rows, cat_files, town_fn="", town=None):
    town = town or []
    total = len(rows)
    core = [r for r in rows if r["类型"] in CORE_TYPES]
    lv = collections.Counter(r["层级"] for r in rows)
    src = collections.Counter(r["来源"] for r in rows)
    typ = collections.Counter(r["类型"] for r in rows)
    with_body = sum(1 for r in rows if r.get("正文"))
    districts = collections.Counter()
    for r in rows:
        for d, _ in DISTRICTS:
            if d in (r["发布单位"] or ""):
                districts[d] += 1
                break

    L = []
    A = L.append
    A("# 上海建设工程政府发文索引\n\n")
    A("上海市 **建筑、规划、工程建设** 领域的**地方性法规**、政府规章与行政规范性文件索引。\n"
      "只收录**元数据 + 官方链接**，并为有实质约束力的文件附上**官方正文全文**与**红头文件 PDF / 附表附图**直链"
      "（可全文收录，见文末法律说明）。\n\n")
    A("> 配套仓库：[Arch-Standards-Index](https://github.com/zhiyao87/Arch-Standards-Index)"
      " —— 上海及全国**工程建设标准**（DGJ08 / GB / JGJ）索引。\n"
      "> 本库管「政府发文」，标准库管「技术标准」，两者互补。\n\n")

    A("## 数据概览\n\n")
    A("| 指标 | 数量 |\n|---|---|\n")
    A("| 收录文件总数 | **%d** |\n" % total)
    A("| 其中的核心文件（地方性法规/规章/办法/规定/细则/导则/审查许可规则） | **%d** |\n" % len(core))
    A("| 已附官方正文全文 | **%d** |\n" % with_body)
    A("| 已登记红头 PDF / 附表附图 | **%d** / **%d** |\n"
      % (sum(1 for r in rows if (r.get("红头PDF") or "").strip()),
         sum(1 for r in rows if (r.get("附件") or "").strip())))
    A("| 地方性法规（市人大制定，效力最高） | **%d** |\n"
      % sum(1 for r in rows if r["类型"] == "地方性法规"))
    # 2026-09-11 起层级只剩三类：市级 ／ 区级 ／ 市级（临港）。
    # 街镇级已整层下架；原「其他」里的临港新片区管委会 41 条改标为「市级（临港）」
    # （管委会是市政府派出机构，其发文属市级），其余并入市级。
    A("| 市级 ／ 区级 ／ 市级（临港） | %d ／ %d ／ %d |\n"
      % (lv["市级"], lv["区级"], lv["市级（临港）"]))
    _yrs = sorted(r["发布日期"][:4] for r in rows if r["发布日期"][:4].isdigit())
    A("| 时间跨度 | %s – %s |\n" % (_yrs[0], _yrs[-1]) if _yrs else "| 时间跨度 | - |\n")
    A("| 覆盖区 | %d / 16 个区有收录 |\n" % sum(1 for d, _ in DISTRICTS if districts.get(d)))
    A("| 数据抓取日 | 2026-09-11 |\n")
    A("\n**按来源**\n\n| 来源 | 条数 |\n|---|---|\n")
    for k, v in src.most_common():
        A("| %s | %d |\n" % (k, v))
    A("\n**按文件类型**\n\n| 类型 | 条数 | 已附全文 | 说明 |\n|---|---|---|---|\n")
    for k, v in typ.most_common():
        got = sum(1 for r in rows if r["类型"] == k and r.get("正文"))
        A("| %s | %d | %d | %s |\n"
          % (k, v, got, "★ 有实质约束力" if k in CORE_TYPES else ""))
    A("\n**按分类**\n\n| # | 分类 | 条数 | 索引 |\n|---|---|---|---|\n")
    for i, cat in enumerate(CAT_ORDER, 1):
        n = sum(1 for r in rows if r["分类"] == cat)
        if not n:
            continue
        A("| %s | %s | %d | [查看](%s) |\n" % (CAT_NO[i - 1] if i <= 10 else i, cat, n, cat_files.get(cat, "")))
    # 街镇级册已于 2026-09-11 按戴工指示停用（条目、正文、索引册全部下架），
    # 此处不再输出该行 —— 否则会留下指向已删文件的死链。
    A("| 12 | **主题速查**（屋顶绿化/光伏/绿建/海绵/既有建筑改造） | - | "
      "[查看](index/12-主题速查.md) |\n")

    # ---------------- 三种原件
    n_pdf = sum(1 for r in rows if (r.get("红头PDF") or "").strip())
    n_att = sum(1 for r in rows if (r.get("附件") or "").strip())
    n_cov = sum(1 for r in rows if (r.get("红头封面") or "").strip())
    A("\n## 每条文件都挂三种取用方式\n\n")
    A("政府发文详情页上其实有**三样**东西，只抓网页正文会丢掉最有用的那部分：\n\n")
    A("| 取用方式 | 说明 | 已收录 |\n|---|---|---|\n")
    A("| **正文** | 网页正文，转为 Markdown 便于检索与全文搜 | %d 条 |\n" % with_body)
    A("| **红头PDF** | 盖章红头文件原件，认文号、对版式、报建送审都用它 | %d 条 |\n" % n_pdf)
    A("| **附表附图** | 技术规范真正的操作部分（参数表、取值表、图示）——只在附件里 | %d 条 |\n" % n_att)
    A("\n**为什么专门标出附表附图**：以《上海市日照分析技术规范》（沪规划资源建〔2021〕437 号）为例，"
      "日照计算参数、窗台高度取值、图示全在随文的「附表、附图、附件.pdf」里，"
      "**网页正文一个字都没有**。只存正文，等于把这份规范最有用的部分丢了。\n\n")
    A("各类索引表的「正文 / 原件」列即按 **正文 · 红头PDF · 附表附图** 三种链接并排给出。\n\n")
    A("> 二进制原件（PDF/PNG）默认**只登记官方直链、不镜像进本仓库**，以免把公开索引撑成 GB 级。"
      "需要离线留存就跑 `python fetch_assets.py --download`，原件会落到本地 `attachments/`，"
      "并生成 `attachment_manifest.csv` 清单。\n")

    # ---------------- 街镇级单列
    if town:
        units = collections.defaultdict(list)
        for r in town:
            units[town_unit(r["发布单位"])].append(r)
        small = [r for r in town
                 if re.search(r"(限额以下|小型建设|小额建设|村级集体投资|政府投资小型)", r["标题"])]
        A("\n### 单独一册：街镇级发文（%d 条 / %d 个街镇）\n\n" % (len(town), len(units)))
        A("**为什么要把街镇级单独拎出来**：限额以下的小型建设工程，依据往往既不是国标、"
          "也不是市里的文件，而是**项目所在街镇自己出的办法**。这类文件在市、区两级栏目里"
          "**根本检索不到**，但报建时最能卡人。\n\n")
        keys = sorted(units, key=lambda u: (-len(units[u]), u))
        A("| 街镇 / 街道 | 条数 | ｜ | 街镇 / 街道 | 条数 |\n|---|---|---|---|---|\n")
        half = (len(keys) + 1) // 2
        for a, b in zip(keys[:half], keys[half:]):
            A("| %s | %d | ｜ | %s | %d |\n" % (a, len(units[a]), b, len(units[b])))
        if len(keys) % 2:
            last = keys[-1]
            A("| %s | %d | ｜ | | |\n" % (last, len(units[last])))
        A("\n[→ 查看街镇级全部条目](%s)\n" % town_fn)
        if small:
            A("\n其中「限额以下 / 小型建设工程」专题共 **%d 份**，各街镇一套，"
              "**用前先确认项目所属街镇**：\n\n" % len(small))
            A("| 街镇 | 标题 | 发布日期 | 正文 / 原件 |\n|---|---|---|---|\n")
            for r in sorted(small, key=lambda x: -int(x["发布日期"][:4] or 0))[:20]:
                A("| %s | [%s](%s) | %s | %s |\n"
                  % (town_unit(r["发布单位"]),
                     (r["标题"] or "").replace("|", "｜"), q(r["官方链接"]),
                     r["发布日期"] or "-", assets_cell(r)))

    # ---------------- 时效复核
    val = collections.Counter((r.get("时效复核") or "").split("（")[0].strip() or "未复核" for r in rows)
    expired = [r for r in rows if (r.get("时效复核") or "").startswith("⚠ 有效期已届满")]
    if any(r.get("时效复核") for r in rows):
        A("\n## 时效复核：这几条现在还算数吗\n\n")
        A("上海的建设类规范性文件普遍带**有效期**（多为 5 年），到期若不续期就自动失效。"
          "所以「一条还灵不灵」**不能只看发布日期** —— 本库从官方正文里挖出**有效期止**，逐条判定：\n\n")
        A("| 判定 | 条数 | 含义 |\n|---|---|---|\n")
        meaning = {
            "现行有效": "有效期止在今天之后，或未标有效期但平台状态为「有效」",
            "⚠ 有效期已届满": "有效期止已过，**须核对是否已发续期通知**",
            "⚠ 正文含废止表述": "正文出现「本X…废止/失效」，可能只是**废止他文**，须人工确认",
            "已废止/失效": "平台明确标注废止或失效，**不要再引用**",
            "未标注": "无正文且平台无状态",
        }
        for k in ["现行有效", "⚠ 有效期已届满", "⚠ 正文含废止表述", "已废止/失效", "未标注"]:
            if val.get(k):
                A("| %s | %d | %s |\n" % (k, val[k], meaning.get(k, "")))
        A("\n索引各表的「**时效**」列就是这张表的缩略：**✓** 现行有效 ／ **⚠** 需人工确认 ／ **✗** 已废止 ／ **?** 未标注。\n")
        if expired:
            byy = collections.Counter((r["有效期止"] or "")[:4] for r in expired)
            A("\n**⚠ 有效期已届满的 %d 条，按届满年份**（越靠后越可能是「刚过期、续期还没上网」）：\n\n" % len(expired))
            A("| 届满年份 | 条数 |\n|---|---|\n")
            for y in sorted(byy):
                A("| %s | %d |\n" % (y or "-", byy[y]))
            A("\n最近到期的 12 条：\n\n")
            A("| 有效期止 | 标题 | 发布机关 |\n|---|---|---|\n")
            for r in sorted(expired, key=lambda x: x["有效期止"], reverse=True)[:12]:
                A("| %s | [%s](%s) | %s |\n"
                  % (r["有效期止"], (r["标题"] or "").replace("|", "｜"), q(r["官方链接"]),
                     (r["发布单位"] or "-").replace("|", "｜")))
        A("\n> **怎么用**：查到年代久远的文件，先看「时效」列。是 ⚠ 就去官方链接核对有没有续期通知；"
          "是 ✗ 就别再引用了。⚠ **不等于**失效 —— 相当一部分只是刚到期、续期文件还没公布。\n")

    # ---------------- 渠道地图
    A("\n## 官方发布渠道地图\n\n")
    A("找上海的建设类政府文件，认准下面这几个口子就够。**全部为官方发布源**。\n\n")
    A("### 市级\n\n| 渠道 | 官方入口 | 覆盖 | 备注 |\n|---|---|---|---|\n")
    for name, url, scope, note in MUNICIPAL:
        A("| %s | [打开](%s) | %s | %s |\n" % (name, q(url), scope, note))
    if DEAD:
        A("\n**⚠ 已失效的旧入口（勿再使用）**\n\n")
        for name, url, note in DEAD:
            A("- ~~%s~~（`%s`）：%s\n" % (name, url, note))
    A("\n### 区级（16 区）\n\n")
    A("区级文件不在市级栏目里，需到各区政府门户的「政务公开 → 规范性文件／政策文件」取。\n"
      "下表入口取自上海市人民政府《政府信息公开指南》页，**均经核实**。\n\n")
    A("| 区 | 政府信息公开入口 | 本库收录 |\n|---|---|---|\n")
    for d, url in DISTRICTS:
        A("| %s | [打开](%s) | %d 条 |\n" % (d, q(url), districts.get(d, 0)))
    A("\n> **提示**：区级文件的检索体验普遍弱于市级，各区栏目结构不统一、分页方式各异。\n"
      "想一次覆盖全，用 [上海市统一政策发布平台](https://www.shanghai.gov.cn/zhengce/list)"
      "——它纵向贯通市/区/镇三级、横向覆盖各部门，本库的区级数据即来源于此。\n")

    # ---------------- 链接巡检快照（可选：data/link_check_summary.json 存在时渲染）
    link_summary = os.path.join(HERE, "data", "link_check_summary.json")
    if os.path.exists(link_summary):
        import json
        lc = json.load(open(link_summary, encoding="utf-8"))
        A("\n## 链接巡检：%s 个 URL 的状态快照（%s）\n\n" %
          ("{:,}".format(lc["总数"]), lc["日期"]))
        A("`check_links.py --net --json` 把 `gov_docs.csv` 里每个条目的"
          "**官方链接**与**红头PDF**两个字段都拉一遍。判定分四档：\n\n")
        A("| 判定 | 数量 | 占比 | 含义 |\n|---|---|---|---|\n")
        for level, count, desc in lc["档位"]:
            pct = "%.1f%%" % (100 * count / lc["总数"])
            A("| %s | %s | %s | %s |\n" %
              (level, "{:,}".format(count), pct, desc))
        if "失效处理" in lc:
            A("\n**%s**（备份在 `%s`）。\n" %
              (lc["失效处理"]["说明"].rstrip("。"), lc["失效处理"]["备份"]))
        A("\n> **怎么用这份快照**：四档中除 ✘ 已修，其它都无需处理。"
          "巡检脚本本身输出 JSON 报告（不入库，2.3 MB，跑一次 50 分钟），"
          "核心四档数字由 `data/link_check_summary.json` 提供，"
          "`build_readme.py` 读它渲染本节。\n")

    # ---------------- 已知检索盲区（诚实标注，避免误以为漏收）
    A("\n## 已知检索盲区（按标题检索找不到的）\n\n")
    A("有若干实务高频主题，**没有以它命名的独立文件**，条款散落在综合性文件里。"
      "按标题关键词检索会显示「0 条」，容易误判为漏收 —— 特此列明。\n")
    A("需要这些主题时请走「正文全文检索」或直接看下列的承载文件。\n\n")
    A("| 主题 | 标题命中 | 实际承载文件（正文含相关条款） |\n|---|---|---|\n")
    blind_spots = [
        ("容积率 / 建筑容量 / 技术经济指标",
         "《上海市建筑面积计算规划管理规定》（2021-09-30）、"
         "《上海市城市规划管理技术规定（土地使用 建筑管理）应用解释》"),
        ("屋顶绿化 / 立体绿化 / 垂直绿化",
         "《上海市居住区绿化调整实施办法》沪绿容规〔2023〕1 号（屋顶/棚架/垂直绿化折算 35%）、"
         "《\"智造空间\"工业项目配套绿化管理的工作指引》沪绿容〔2024〕154 号、"
         "《关于加强城市第五立面规划建设的指导意见》"),
        ("消防案例 / 火灾案例汇编",
         "库内无此体裁。消防类实际收录的是**规范 + 审查验收办法**："
         "《建设工程消防设计审查验收技术服务管理办法》《上海市智造空间防火设计导则》等 4 条"),
        ("既有建筑光伏 / 光伏建筑一体化（BIPV）专项办法",
         "库内无专门办法。实际覆盖见「建筑光伏 / 太阳能应用」主题（76 条，含专项资金、开发建设方案）"),
    ]
    for topic, carrier in blind_spots:
        A("| %s | 0 | %s |\n" % (topic, carrier))
    A("\n> 想按正文找这些主题，用 [`index/12-主题速查.md`](index/12-主题速查.md)"
      " —— 它按**全文**匹配，不受标题命名限制。\n")

    # ---------------- 链接形态说明（戴工实测 0084 打不开，特此说明）
    n_short = sum(1 for r in rows if (r.get("链接形态") or "") == "short")
    if n_short:
        A("\n## 官方链接的格式（曾踩过的坑，已修正）\n\n")
        A("统一政策发布平台的详情页是**单页应用**，前台 URL 必须写成**查询参数式**：\n\n")
        A("```\n")
        A("✓ 正确  /zhengce/detail?businessId=<businessId>&siteId=<siteId>\n")
        A("✗ 错误  /zhengce/detail/<siteId>::<businessId>        ← 打开后显示不出文件内容\n")
        A("```\n\n")
        A("本库早期版本用的是「路径式」，2026-09-11 由戴工实测发现打不开，"
          "已把 **2,436 条官方链接 + 2,431 篇正文里的链接**全部改为查询参数式。\n\n")
        A("另外，部分区级老数据的 businessId 是 **8–11 位纯数字**（多为浦东新区、普陀、"
          "奉贤、青浦、长宁），与主流 32 位 hash 不同。这类条目已在 CSV 的"
          "「链接形态」列标为 `short`（共 %d 条），若个别仍打不开，请：\n\n" % n_short)
        A("1. **看库内正文** —— `docs/` 已存官方全文，不受影响；\n")
        A("2. 到**对应区政府门户**站内检索标题；\n")
        A("3. 或在 [统一政策发布平台](https://www.shanghai.gov.cn/zhengce/list) 搜标题。\n")

    # ---------------- 重点速查
    A("\n## 设计报建高频文件速查\n\n")
    A("按实务环节整理的常用依据（全部来自本库，含正文）：\n\n")
    hotspots = [
        ("规划条件与方案报建",
         ["规划管理技术规定", "城市规划管理技术规定", "方案规划公示", "日照分析",
          "建设工程设计方案", "规划报批入库"]),
        ("面积计算与容积率",
         ["建筑面积计算", "建筑面积和容积率", "容积率", "面积计算", "计容",
          "建筑面积计算规则", "面积计算规则"]),
        ("第五立面与屋面",
         ["第五立面", "屋面", "屋顶", "建筑立面", "外立面", "坡屋面", "立面整治"]),
        ("施工图审查",
         ["施工图", "多图联审", "设计文件审查"]),
        ("抗震与人防",
         ["抗震设防", "人民防空", "民防工程"]),
        ("施工许可与验收",
         ["施工许可", "竣工验收", "工程总承包"]),
        ("绿色建筑与节能",
         ["绿色建筑", "建筑节能", "超低能耗", "装配式", "海绵城市"]),
        ("既有建筑与城市更新",
         ["城市更新", "既有建筑", "历史建筑", "优秀历史建筑", "加装电梯", "装饰装修"]),
        ("房屋与住宅",
         ["住宅设计", "物业管理", "住宅小区", "住宅专项维修"]),
    ]
    more_map = {
        "规划条件与方案报建": "建筑设计与报建",
        "面积计算与容积率": "规划与土地",
        "第五立面与屋面": "城市更新与历史保护",
        "施工图审查": "建筑设计与报建",
        "抗震与人防": "消防与人防",
        "施工许可与验收": "工程建设管理",
        "绿色建筑与节能": "绿色低碳与节能",
        "既有建筑与城市更新": "城市更新与历史保护",
        "房屋与住宅": "房屋与住房",
    }
    for label, kws in hotspots:
        hits = [r for r in rows if any(k in r["标题"] for k in kws)]
        hits.sort(key=lambda r: (not r.get("正文"), -int(r["发布日期"][:4] or 0)))
        hits = hits[:8]
        if not hits:
            continue
        A("\n### %s\n\n" % label)
        A("| 标题 | 文号 | 发布机关 | 日期 | 时效 | 正文 / 原件 |\n|---|---|---|---|---|---|\n")
        for r in hits:
            A("| [%s](%s) | %s | %s | %s | %s | %s |\n"
              % ((r["标题"] or "").replace("|", "｜"), q(r["官方链接"]),
                 r["文号"] or "-", (r["发布单位"] or "-").replace("|", "｜"),
                 r["发布日期"] or "-", validity_mark(r.get("时效复核")),
                 assets_cell(r)))
        A("\n[→ 查看该主题全部条目](%s)\n" % cat_files.get(more_map.get(label, ""), "README.md"))

    # ---------------- 怎么用
    A("\n## 目录结构\n\n```\n")
    A("Shanghai-Gov-Docs-Index/\n")
    A("├── README.md                 本文件（概览 + 渠道地图 + 速查）\n")
    A("├── index/                    按分类的完整索引（每条含官方链接）\n")
    A("├── docs/                     核心文件官方正文全文（Markdown，按分类分目录）\n")
    A("├── data/\n")
    A("│   ├── gov_docs.csv          全量清单（本库唯一数据源）\n")
    A("│   ├── raw_flk_sh_laws.tsv   上海地方性法规原始抓取（国家法律法规数据库）\n")
    A("│   ├── flk_fulltext/         地方性法规官方正文（纯文本，按 bbbs 命名）\n")
    A("│   ├── raw_gz_rules.tsv      市政府规章库原始抓取\n")
    A("│   ├── raw_zjw_gfxwj.tsv     市住建委规范性文件原始抓取\n")
    A("│   ├── raw_shrd_laws.tsv     上海人大「法规公布」原始抓取\n")
    A("│   └── raw_policy_all.json   统一政策平台原始抓取（10,518 条，未入库）\n")
    A("├── attachments/              原件（PDF/PNG），默认不提交；fetch_assets.py --download 生成\n")
    A("├── channels.py               官方渠道地图常量（16 区入口 + 已失效入口）\n")
    A("├── classify.py               主题分类与相关性判定规则\n")
    A("├── common.py                 抓取工具（零第三方依赖）\n")
    A("├── scrape_policy.py          抓统一政策发布平台全量\n")
    A("├── scrape_flk.py             抓上海地方性法规 + 官方正文（国家法律法规数据库）\n")
    A("├── scrape_shrd.py            抓上海人大「法规公布」栏目\n")
    A("├── build_docs_index.py       五源合并 → data/gov_docs.csv\n")
    A("├── fetch_fulltext.py         抓核心文件官方正文 → docs/\n")
    A("├── fetch_assets.py           抓红头 PDF / 附表附图 / 封面 直链（--download 可落盘）\n")
    A("├── build_readme.py           生成 README.md 与 index/\n")
    A("├── audit_validity.py         时效复核：从正文判现行有效/已届满/已废止\n")
    A("├── check_links.py            链接批量巡检\n")
    A("└── push_via_api.py           走 GitHub REST API 推送（git 443 不通时用）\n```\n")

    A("\n## 怎么用 / 怎么维护\n\n")
    A("**查文件**：先看上面的分类索引，或直接搜 `data/gov_docs.csv`。\n\n")
    A("**要全文**：`docs/` 下按分类存放，文件名即标题。全量回采政府公开正文"
      "（极少数页面已下架或无正文的来源仅给官方链接）。\n\n")
    A("**重建流程**（需要联网）：\n\n```bash\n")
    A("python scrape_policy.py        # 1. 抓统一政策平台全量（约 3 分钟）\n")
    A("python build_docs_index.py     # 2. 三源合并去重 → data/gov_docs.csv\n")
    A("python fetch_fulltext.py       # 3. 抓核心文件正文 → docs/（约 8 分钟）\n")
    A("python build_readme.py         # 4. 生成 README 与索引\n")
    A("python check_links.py          # 5. 巡检链接\n```\n")
    A("\n**加新文件**：不要直接改 README —— 改 `data/gov_docs.csv` 后重跑 `build_readme.py`，"
      "否则下次生成会被冲掉。若某文件未被自动筛出，在 `classify.py` 的关键词表里补词。\n")

    A("\n## 数据来源与法律说明\n\n")
    A("**数据来源**（均为上海市官方发布渠道）：\n\n")
    for name, url, _, _ in MUNICIPAL:
        A("- %s：%s\n" % (name, url))
    A("\n**法律说明**\n\n")
    A("本库收录的文件属于**具有立法、行政、司法性质的文件**。依《中华人民共和国著作权法》"
      "**第五条第一项**，该类文件不适用著作权法，故本库**可全文收录**正文。\n\n")
    A("这与技术标准的情形不同：《工程建设标准》（GB / JGJ / DGJ08）属**受著作权保护的推荐性技术文件**，"
      "在 [Arch-Standards-Index](https://github.com/zhiyao87/Arch-Standards-Index) 中"
      "**只收录元数据与官方链接、不收录正文**。两个库的版权处理差异源于此。\n\n")
    A("正文由脚本自官方公开页面自动提取，可能因页面改版而与发布版本有差异，"
      "**请以每份文件中的官方链接为准**。\n")
    return "".join(L)


def main():
    rows = rows_of(OUT_CSV)
    cat_files = write_category_indexes(rows)
    town_fn, town = write_town_index(rows)
    md = build_readme(rows, cat_files, town_fn, town)
    open(os.path.join(HERE, "README.md"), "w", encoding="utf-8").write(md)
    print("✓ README.md（%.1f KB）" % (os.path.getsize(os.path.join(HERE, "README.md")) / 1024))
    print("✓ index/ 共 %d 个分类文件" % len(cat_files))
    print("  （街镇级册已按 2026-09-11 指示停用）")


if __name__ == "__main__":
    main()
