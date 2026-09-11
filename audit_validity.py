# -*- coding: utf-8 -*-
"""时效复核：从官方正文里抽出「发布 / 施行 / 有效期止」，判定文件现在是否还在实施。

为什么必须做这件事
------------------
上海的建设类规范性文件普遍带**有效期**（多为 5 年），到期若不续期就自动失效。
市住建委「规范性文件」栏目会直接标有效期，但统一政策发布平台不标 ——
所以「这文件现在还算不算数」只能从**正文**里挖。

本脚本抽取四类信息
------------------
1. 原始发布日期 / 文号  —— 规章正文常写「（2003年10月18日上海市人民政府令第12号发布…）」
2. 施行日期            —— 「自2026年3月1日起施行」
3. 有效期止            —— 「有效期至2031年2月28日」（最常见、最有用）
4. 废止 / 失效信号      —— 「本规定自…废止」「有效期届满自动失效」

输出
----
给 data/gov_docs.csv 增加四列：
    原始发布年 / 施行日期 / 有效期止 / 时效复核
时效复核取值：
    现行有效            —— 有效期止 ≥ 今天，或未标有效期但平台状态为「有效」
    ⚠ 有效期已届满      —— 有效期止 < 今天，需人工确认是否已续期
    ⚠ 正文含废止表述    —— 正文出现「本X…废止/失效」，但可能是废止他文，须人工确认
    已废止/失效         —— 平台明确标注废止或失效（最权威）
    未标注              —— 无正文且平台无状态

用法
----
    python audit_validity.py            # 复核并回写 CSV
    python audit_validity.py --report   # 只打印统计与清单
"""

import argparse
import csv
import os
import re
import sys
from collections import Counter

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from build_docs_index import FIELDS, OUT_CSV  # noqa: E402

HERE = os.path.dirname(os.path.abspath(__file__))
TODAY = (2026, 9, 11)   # 数据抓取日；口径与 README 一致

NEW_COLS = ["原始发布年", "施行日期", "有效期止", "时效复核"]

# 有效期至 2031年2月28日 / 有效期至 2031年2月底 / 有效期至2031年2月
RE_DEADLINE = [
    re.compile(r"有效期(?:限)?至\s*(\d{4})\s*年\s*(\d{1,2})\s*月\s*(\d{1,2})\s*日"),
    re.compile(r"有效期(?:限)?至\s*(\d{4})\s*年\s*(\d{1,2})\s*月\s*底"),
    re.compile(r"有效期(?:限)?至\s*(\d{4})\s*年\s*(\d{1,2})\s*月(?![\d日])"),
    re.compile(r"有效(?:期|期限)\s*(\d+)\s*年"),          # 有效期为 5 年
]
RE_DEADLINE_ALT = re.compile(r"(\d{4})\s*年\s*(\d{1,2})\s*月\s*(\d{1,2})\s*日\s*止")
RE_IMPL = re.compile(r"自\s*(\d{4})\s*年\s*(\d{1,2})\s*月\s*(\d{1,2})\s*日\s*起?\s*(?:施行|执行|实施)")
RE_ORIG = re.compile(r"（?\s*(\d{4})\s*年\s*(\d{1,2})\s*月\s*(\d{1,2})\s*日[^）]{0,60}?"
                     r"(?:发布|公布|通过|批准)")
RE_ABOLISH = re.compile(r"(本(?:规定|办法|通知|意见|细则|规则|决定|条例))[^。；]{0,40}?"
                        r"(废止|失效|停止执行)")


def to_days(y, m, d):
    # 只做年月日比较，够用且不引入依赖
    return int(y) * 10000 + int(m) * 100 + int(d)


def read_body(row):
    p = row.get("正文") or ""
    if not p:
        return ""
    full = os.path.join(HERE, p)
    if not os.path.exists(full):
        return ""
    with open(full, encoding="utf-8") as f:
        return f.read()


def audit(row, body):
    deadline = ""
    impl = ""
    orig = ""
    note = ""

    if body:
        # 有效期止：取最靠后的一个匹配（续期通知里常出现多次）
        cands = []
        for pat in RE_DEADLINE[:3]:
            for m in pat.finditer(body):
                g = m.groups()
                y, mo = g[0], g[1]
                d = g[2] if len(g) > 2 and g[2] else "1"
                cands.append((to_days(y, mo, d), "%s-%02d-%02d" % (y, int(mo), int(d))))
        for m in RE_DEADLINE_ALT.finditer(body):
            y, mo, d = m.groups()
            cands.append((to_days(y, mo, d), "%s-%02d-%02d" % (y, int(mo), int(d))))
        if cands:
            cands.sort()
            deadline = cands[-1][1]

        m = RE_IMPL.search(body)
        if m:
            y, mo, d = m.groups()
            impl = "%s-%02d-%02d" % (y, int(mo), int(d))

        m = RE_ORIG.search(body)
        if m:
            orig = m.group(1)

    # 判定。优先级：平台明确废止 > 正文含废止表述 > 有效期是否届满。
    # 平台状态是官方标注，最权威；「正文含废止表述」常出现在**废止他文的通知**里，
    # 只能当提示，不能当结论，所以两者分开写、用不同措辞。
    st = (row.get("状态") or "").strip()
    flag = ""
    if st in ("废止", "失效", "已废止", "已失效"):
        flag = "已废止/失效"
        note = "平台标注：" + st
    elif RE_ABOLISH.search(body or ""):
        flag = "⚠ 正文含废止表述"
        note = "须人工确认是本文废止还是废止他文"
    elif deadline:
        if to_days(*deadline.split("-")) < to_days(*TODAY):
            flag = "⚠ 有效期已届满"
            note = "有效期止 " + deadline
        else:
            flag = "现行有效"
            note = "有效期至 " + deadline
    elif st == "有效":
        flag = "现行有效"
        note = "未标有效期，平台状态有效"
    else:
        flag = "未标注"
        note = "无正文且平台无状态"
    return orig, impl, deadline, flag + ("（" + note + "）" if note else "")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--report", action="store_true")
    args = ap.parse_args()

    rows = list(csv.DictReader(open(OUT_CSV, encoding="utf-8-sig")))
    for c in NEW_COLS:
        if c not in FIELDS:
            FIELDS.append(c)

    stat = Counter()
    for r in rows:
        body = read_body(r)
        orig, impl, dl, fl = audit(r, body)
        r["原始发布年"] = orig
        r["施行日期"] = impl
        r["有效期止"] = dl
        r["时效复核"] = fl
        stat[fl.split("（")[0]] += 1

    print("复核 %d 条" % len(rows))
    for k, v in stat.most_common():
        print("   %-16s %5d" % (k, v))

    expired = [r for r in rows if r["时效复核"].startswith("⚠")]
    print("\n⚠ 有效期已届满、需确认是否续期的 %d 条（按年份）：" % len(expired))
    for y, n in sorted(Counter(r["有效期止"][:4] for r in expired).items()):
        print("   %s 年届满：%d 条" % (y, n))
    print("\n最近到期的 25 条：")
    for r in sorted(expired, key=lambda x: x["有效期止"], reverse=True)[:25]:
        print("   [%s] %s ｜ %s" % (r["有效期止"], r["标题"][:52], r["发布单位"][:16]))

    if args.report:
        return
    with open(OUT_CSV, "w", encoding="utf-8-sig", newline="") as f:
        w = csv.DictWriter(f, fieldnames=FIELDS, extrasaction="ignore")
        w.writeheader()
        w.writerows(rows)
    print("\n✓ 回写 %s" % OUT_CSV)


if __name__ == "__main__":
    main()
