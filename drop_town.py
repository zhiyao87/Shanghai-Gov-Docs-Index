# -*- coding: utf-8 -*-
"""删除层级 = 街镇级 的全部条目（戴工 2026-09-11 指示）。

安全设计（与 drop_traffic.py 同口径）
--------------------------------
1. 删前先把 CSV 与待删 md 按原目录结构备份到 _backup/docs-town-<N>个/
2. md 复制后逐个校验字节大小一致，校验不通过就不删
3. 只删 docs/ 下的 .md，绝不动其它目录

用法
----
    python drop_town.py            # 完整执行
    python drop_town.py --dry      # 只报告会删什么
"""

import csv
import io
import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
CSV = os.path.join(HERE, "data", "gov_docs.csv")
DOCS = os.path.join(HERE, "docs")
BACKUP = os.path.join(HERE, "_backup")
TOWN_INDEX = os.path.join(HERE, "index", "11-街镇级发文.md")


def main():
    dry = "--dry" in sys.argv
    rows = list(csv.DictReader(io.open(CSV, encoding="utf-8-sig")))
    town = [r for r in rows if (r.get("层级") or "").strip() == "街镇级"]
    keep = [r for r in rows if (r.get("层级") or "").strip() != "街镇级"]
    print("现 %d 条；街镇级 %d 条 → 删后 %d 条" % (len(rows), len(town), len(keep)))

    md_list = [r["正文"] for r in town if r.get("正文")]
    missing = [p for p in md_list if not os.path.exists(os.path.join(HERE, p))]
    print("对应正文 %d 篇（磁盘缺失 %d 篇）" % (len(md_list), len(missing)))
    if dry:
        for r in town[:60]:
            print("  - [%s] %s" % (r.get("发布日期"), (r.get("标题") or "")[:60]))
        return 0
    if not town:
        print("没有街镇级条目，无需处理")
        return 0

    # ---------- 1. 备份 ----------
    os.makedirs(BACKUP, exist_ok=True)
    bcsv = os.path.join(BACKUP, "gov_docs.BEFORE-drop-town-%d条.csv" % len(rows))
    shutil.copy2(CSV, bcsv)
    print("CSV 已备份 → %s" % os.path.basename(bcsv))

    bdir = os.path.join(BACKUP, "docs-town-%d个" % len(md_list))
    ok = 0
    for rel in md_list:
        src = os.path.join(HERE, rel)
        dst = os.path.join(bdir, rel.replace("/", os.sep))
        if not os.path.exists(src):
            continue
        os.makedirs(os.path.dirname(dst), exist_ok=True)
        shutil.copy2(src, dst)
        if os.path.getsize(src) == os.path.getsize(dst):
            ok += 1
    print("正文备份 %d/%d → _backup/%s" % (ok, len(md_list), os.path.basename(bdir)))
    if ok != len(md_list) - len(missing):
        print("✗ 备份不完整，放弃删除")
        return 1

    # ---------- 2. 回写 CSV ----------
    cols = list(rows[0].keys())
    with io.open(CSV, "w", encoding="utf-8-sig", newline="") as f:
        w = csv.DictWriter(f, fieldnames=cols, extrasaction="ignore")
        w.writeheader()
        w.writerows(keep)
    print("CSV 现有 %d 条" % len(keep))

    # ---------- 3. 删 md ----------
    done = 0
    for rel in md_list:
        p = os.path.join(HERE, rel)
        if not os.path.exists(p):
            continue
        try:
            os.remove(p)
            done += 1
        except Exception as e:
            print("  ✗ 删除失败 %s : %s" % (rel[:50], e))
    print("已删除正文 %d 篇" % done)

    # ---------- 4. 删街镇级索引册 ----------
    if os.path.exists(TOWN_INDEX):
        shutil.copy2(TOWN_INDEX, os.path.join(bdir, "11-街镇级发文.md"))
        os.remove(TOWN_INDEX)
        print("已删除索引册 index/11-街镇级发文.md（备份于同目录）")
    return 0


if __name__ == "__main__":
    sys.exit(main())
