# -*- coding: utf-8 -*-
"""清洗 fetch_lhsr_docs.py 产出的 md：剔除正文里的政府信息公开元数据表。

页面结构问题：lhsr.sh.gov.cn 的元数据表（信息名称/索取号/发布机构/文件编号/
公开类别/发布日期）位于 class="zw_content" 容器内部，会被一起抽进正文。
本脚本按「键行 + 值行」成对剥离，并修掉占位文号（如「发文字号 (2015) 330号」）。

用法
----
    python clean_lhsr.py            # 清洗来源=市绿化市容局官网的条目，并回写 CSV
    python clean_lhsr.py --dry      # 只报告会改什么
"""

import csv
import io
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
CSV = os.path.join(HERE, "data", "gov_docs.csv")
SOURCE = "市绿化市容局官网"

META_KEYS = {"信息名称", "索取号", "发布机构", "文件编号", "公开类别", "发布日期",
             "内容概述", "主题词", "载体类型", "记录形式", "发文日期", "索引号",
             "生成日期", "附注", "废止日期", "有效性"}

# 只删键行、保留后续内容（这些键后面跟的是正文正文，不是元数据值）
KEY_ONLY = {"信息内容", "附件", "相关附件"}

# 页脚噪音
TAIL_NOISE = ["政策性文件留言咨询", "只接收对该政策性文件的相关咨询",
              "留言时请注明政策性文件名称"]

# 真实文号（正文里通常写在抬头下方）
DOCNO_RE = re.compile(r"[\u4e00-\u9fa5]{0,8}[〔\[]\s*(\d{4})\s*[〕\]]\s*(\d+)\s*号")


def pick_docno(body_lines, old):
    """优先从正文抬头上提取真实文号，取不到再沿用旧值。"""
    for ln in body_lines[:25]:
        m = DOCNO_RE.search(ln)
        if m and len(ln) < 60:
            return ln.strip()
    return fix_docno(old)


def clean_body(lines):
    """按 (键, 值) 成对剥离元数据行。"""
    out, i = [], 0
    while i < len(lines):
        s = lines[i].strip()
        if s in KEY_ONLY:
            i += 1
            continue
        if s in META_KEYS:
            i += 1
            # 跳过紧随的「值」行（短且不像正文段落）
            if i < len(lines) and len(lines[i].strip()) < 120:
                i += 1
            continue
        out.append(lines[i])
        i += 1
    return out


def fix_docno(s):
    s = (s or "").strip()
    if not s:
        return ""
    if "发文字号" in s or s in ("无", "-", "/", "—"):
        return ""
    s = re.sub(r"\s+", "", s)
    return s


def main():
    dry = "--dry" in sys.argv
    rows = list(csv.DictReader(io.open(CSV, encoding="utf-8-sig")))
    tgt = [r for r in rows if r["来源"] == SOURCE]
    print("待清洗 %d 条" % len(tgt))

    changed_body = changed_no = 0
    for r in tgt:
        p = os.path.join(HERE, r["正文"])
        if not os.path.exists(p):
            continue
        txt = io.open(p, encoding="utf-8").read()
        # 正文从「# 标题」之后开始
        m = re.search(r"(?m)^# .*$", txt)
        if not m:
            continue
        head, body = txt[:m.end()], txt[m.end():]
        lines = body.split("\n")
        new_lines = clean_body(lines)
        # 去掉页脚留言咨询噪音
        new_lines = [x for x in new_lines if not any(n in x for n in TAIL_NOISE)]
        if new_lines != lines:
            changed_body += 1

        new_no = pick_docno(new_lines, r["文号"])
        if new_no != (r["文号"] or ""):
            changed_no += 1
            r["文号"] = new_no
        if not dry:
            head = re.sub(r"(?m)^文号:.*$", "文号: %s" % new_no, head)
            io.open(p, "w", encoding="utf-8").write(head + "\n" + "\n".join(new_lines))

    print("正文清洗 %d 篇；文号修正 %d 条" % (changed_body, changed_no))
    if not dry:
        with io.open(CSV, "w", encoding="utf-8-sig", newline="") as f:
            w = csv.DictWriter(f, fieldnames=list(rows[0].keys()), extrasaction="ignore")
            w.writeheader()
            w.writerows(rows)
        print("CSV 已回写")
    return 0


if __name__ == "__main__":
    sys.exit(main())
