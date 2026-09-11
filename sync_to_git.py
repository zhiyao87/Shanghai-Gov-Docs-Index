# -*- coding: utf-8 -*-
"""把工作区（权威副本）同步回 F 盘 git 仓库。

背景
----
F 盘仓库的 data/gov_docs.csv 被 `--limit` 测试截成 12 条，而工作区那份是完好的。
同时 F 盘 docs/ 里还留着已软删除（从 CSV 移除）的停车/交通类正文 md。
本脚本一次性完成：备份 → 删除多余 md → 回灌 CSV → 同步新增文件与脚本。

安全设计
--------
1. 删除前先把待删文件按原目录结构复制到 _backup/docs-removed-<N>个/
2. 复制完逐个校验字节大小一致，校验不通过就不删
3. 只删 docs/ 下的 .md，绝不动其它目录

用法
----
    export SH_GOV_GIT=/path/to/Shanghai-Gov-Docs-Index   # 或每次用 --git 指定
    python sync_to_git.py            # 完整执行（含删除）
    python sync_to_git.py --dry      # 只报告会做什么
"""

import argparse
import csv
import io
import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
# 目标 git 仓库路径绝不硬编码（公开仓库不宜暴露本机目录组织），
# 从环境变量 SH_GOV_GIT 或 --git 参数取。
DEFAULT_GIT = os.environ.get("SH_GOV_GIT", "")

BACKUP = os.path.join(HERE, "_backup")
SYNC_SCRIPTS = ["add_missing.py", "scrape_lhsr.py", "fetch_lhsr_docs.py",
                "clean_lhsr.py", "scrape_ghzyj.py", "fetch_ghzyj_docs.py",
                "probe_agency.py",
                "sync_to_git.py", "classify.py",
                "build_docs_index.py", "build_readme.py",
                # 2026-09-11 追加：通用委办局抓取链 + 主题速查 + 街镇级下架脚本
                "scrape_agency.py", "fetch_agency_docs.py", "zjw_screen.py",
                "topic_index.py", "drop_town.py"]


def scan_md(root):
    out = set()
    for dp, _, fn in os.walk(root):
        for f in fn:
            if f.endswith(".md"):
                out.add(os.path.relpath(os.path.join(dp, f), root))
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--git", default=DEFAULT_GIT,
                    help="目标 git 仓库路径（或设环境变量 SH_GOV_GIT）")
    ap.add_argument("--dry", action="store_true")
    args = ap.parse_args()
    dry = args.dry
    GIT = args.git
    if not GIT or not os.path.isdir(GIT):
        print("✗ 找不到目标 git 仓库：%r" % GIT)
        print("  用法：python sync_to_git.py --git <仓库路径>")
        print("  或设环境变量：SH_GOV_GIT=<仓库路径>")
        return 1

    wdocs = os.path.join(HERE, "docs")
    fdocs = os.path.join(GIT, "docs")
    w = scan_md(wdocs)
    f = scan_md(fdocs)
    only_f = sorted(f - w)
    only_w = sorted(w - f)
    print("工作区 md %d / F 盘 md %d" % (len(w), len(f)))
    print("仅 F 盘有（待删）：%d" % len(only_f))
    print("仅工作区有（待同步）：%d" % len(only_w))

    # ---------- 1. 备份待删文件 ----------
    bdir = os.path.join(BACKUP, "docs-removed-%d个" % len(only_f))
    if only_f and not dry:
        os.makedirs(bdir, exist_ok=True)
        ok = 0
        for rel in only_f:
            src = os.path.join(fdocs, rel)
            dst = os.path.join(bdir, rel)
            os.makedirs(os.path.dirname(dst), exist_ok=True)
            shutil.copy2(src, dst)
            if os.path.getsize(src) == os.path.getsize(dst):
                ok += 1
        print("备份 %d/%d → %s" % (ok, len(only_f), bdir))
        if ok != len(only_f):
            print("✗ 备份不完整，放弃删除")
            return 1

    # ---------- 2. 删除 ----------
    if only_f and not dry:
        done = 0
        for rel in only_f:
            p = os.path.join(fdocs, rel)
            try:
                os.remove(p)
                done += 1
            except Exception as e:
                print("  ✗ 删除失败 %s : %s" % (rel[:50], e))
        print("已删除 %d/%d" % (done, len(only_f)))
        # 清掉空目录
        for dp, dn, fn in os.walk(fdocs, topdown=False):
            if dp == fdocs:
                continue
            if not os.listdir(dp):
                try:
                    os.rmdir(dp)
                except Exception:
                    pass

    # ---------- 3. 同步工作区新增/更新的 md ----------
    if not dry:
        n = 0
        for rel in sorted(w):
            src = os.path.join(wdocs, rel)
            dst = os.path.join(fdocs, rel)
            if os.path.exists(dst) and os.path.getsize(src) == os.path.getsize(dst):
                continue
            os.makedirs(os.path.dirname(dst), exist_ok=True)
            shutil.copy2(src, dst)
            n += 1
        print("同步 md %d 个（新增/有差异的）" % n)

    # ---------- 4. 回灌 CSV ----------
    src_csv = os.path.join(HERE, "data", "gov_docs.csv")
    rows = list(csv.DictReader(io.open(src_csv, encoding="utf-8-sig")))
    print("待回灌 CSV：%d 条" % len(rows))
    if not dry:
        dst_csv = os.path.join(GIT, "data", "gov_docs.csv")
        if os.path.exists(dst_csv):
            old = sum(1 for _ in io.open(dst_csv, encoding="utf-8-sig")) - 1
            shutil.copy2(dst_csv, os.path.join(BACKUP, "gov_docs.F盘损坏版-%d条.csv" % old))
            print("  已备份 F 盘旧 CSV（%d 条）" % old)
        shutil.copy2(src_csv, dst_csv)
        chk = len(list(csv.DictReader(io.open(dst_csv, encoding="utf-8-sig"))))
        print("  回灌完成，F 盘现有 %d 条" % chk)

    # ---------- 4.5 同步生成物：README.md 与 index/*.md ----------
    # （2026-09-11 踩坑：初版只同步了 docs/ 与 CSV，重建后的 README 和
    #   13 个索引册被漏在仓库外，导致线上 README 停在旧条数。）
    if not dry:
        n = 0
        src_readme = os.path.join(HERE, "README.md")
        if os.path.exists(src_readme):
            shutil.copy2(src_readme, os.path.join(GIT, "README.md"))
            n += 1
        w_index = os.path.join(HERE, "index")
        g_index = os.path.join(GIT, "index")
        if os.path.isdir(w_index):
            os.makedirs(g_index, exist_ok=True)
            for fn in sorted(os.listdir(w_index)):
                if fn.endswith(".md"):
                    shutil.copy2(os.path.join(w_index, fn), os.path.join(g_index, fn))
                    n += 1
        print("同步 README + index %d 个" % n)

    # ---------- 5. 同步脚本 ----------
    if not dry:
        for s in SYNC_SCRIPTS:
            p = os.path.join(HERE, s)
            if os.path.exists(p):
                shutil.copy2(p, os.path.join(GIT, s))
        print("同步脚本 %d 个" % len(SYNC_SCRIPTS))

    return 0


if __name__ == "__main__":
    sys.exit(main())
