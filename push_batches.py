# -*- coding: utf-8 -*-
"""分批 git add/commit/push —— 代理对大包不稳，拆成小批逐个推。

用法：
    python push_batches.py <仓库目录> [每批最大文件数]
"""
import os
import subprocess
import sys
import time

REPO = os.path.abspath(sys.argv[1]) if len(sys.argv) > 1 else "."
BATCH = int(sys.argv[2]) if len(sys.argv) > 2 else 200
MAX_RETRY = 5


def run(cmd, cwd=REPO, check=False):
    p = subprocess.run(cmd, shell=True, cwd=cwd, capture_output=True, text=True,
                       encoding="utf-8", errors="replace")
    if check and p.returncode != 0:
        raise RuntimeError("%s\n%s" % (cmd, p.stderr[:400]))
    return p.returncode, (p.stdout or "") + (p.stderr or "")


def pending():
    """返回未跟踪/已修改的文件列表（相对路径）。"""
    rc, out = run("git status --porcelain -z", check=True)
    items = [x[3:] for x in out.split("\0") if x.strip()]
    # -z 输出格式：XY<space>path，去掉引号
    res = []
    for it in items:
        it = it.strip()
        if it.startswith('"') and it.endswith('"'):
            it = it[1:-1]
        if it:
            res.append(it)
    return res


def main():
    files = pending()
    print("待处理 %d 个文件，每批 %d" % (len(files), BATCH))
    if not files:
        print("无可推内容")
        return

    # 按目录分组，保证同目录文件在同一批（提交信息更好看）
    groups = {}
    for f in files:
        d = os.path.dirname(f) or "(根目录)"
        groups.setdefault(d, []).append(f)

    # 小目录在前，大目录在后；大目录再按 BATCH 切分
    order = sorted(groups.items(), key=lambda kv: len(kv[1]))
    batches = []
    for d, fs in order:
        if len(fs) <= BATCH:
            batches.append((d, fs))
        else:
            for i in range(0, len(fs), BATCH):
                batches.append(("%s (%d-%d)" % (d, i + 1, min(i + BATCH, len(fs))),
                                fs[i:i + BATCH]))

    print("分为 %d 批" % len(batches))
    ok = 0
    for idx, (label, fs) in enumerate(batches, 1):
        # add
        quoted = " ".join('"%s"' % f for f in fs)
        rc, out = run("git add %s" % quoted)
        rc2, staged = run("git diff --cached --name-only")
        n_staged = len([x for x in staged.splitlines() if x.strip()])
        if n_staged == 0:
            print("[%d/%d] %s：无变更，跳过" % (idx, len(batches), label))
            continue
        # commit
        msg = "docs: %s（%d 个文件）" % (label, n_staged)
        rc, out = run('git commit -q -m "%s"' % msg.replace('"', "'"))
        if rc != 0:
            print("[%d/%d] %s：commit 失败 %s" % (idx, len(batches), label, out[:200]))
            continue
        # push with retry
        for attempt in range(1, MAX_RETRY + 1):
            rc, out = run("git push origin HEAD", )
            if rc == 0:
                print("[%d/%d] ✓ %s（%d 文件）" % (idx, len(batches), label, n_staged))
                ok += 1
                break
            if attempt == MAX_RETRY:
                print("[%d/%d] ✗ %s 推送失败（%d 次重试）：%s"
                      % (idx, len(batches), label, MAX_RETRY, out.strip().splitlines()[-1][:120]))
            else:
                time.sleep(3)
    print("\n完成：%d/%d 批推送成功" % (ok, len(batches)))


if __name__ == "__main__":
    main()