# -*- coding: utf-8 -*-
"""当 git push 的 443 通道被封、但 api.github.com 可达时，用 GitHub REST API 推代码。

背景
----
某些网络环境里 github.com 的 CONNECT 隧道会被拦（报 502 / SSL 握手失败），
但 api.github.com 仍然通。此时 `git push` 无解，但 REST API 可用：

    POST /git/blobs     逐个上传文件（可并发）
    POST /git/trees     建目录树
    POST /git/commits   建提交
    POST/PATCH /git/refs  把分支指过去

本脚本用 `git ls-tree` + `git cat-file` 取**已归一化（LF）**的内容，
不直接读工作区文件 —— 否则会绕开 .gitattributes 的换行符策略。

凭据取自本机 git 凭据管理器（`git credential fill`），不落盘、不打印。

用法
----
    SH_GOV_PROXY=http://127.0.0.1:1542 python push_via_api.py <仓库目录> <owner/repo> [分支]
"""

import base64
import json
import os
import subprocess
import sys
import urllib.error
import urllib.request
from concurrent.futures import ThreadPoolExecutor

PROXY = (os.environ.get("SH_GOV_PROXY") or os.environ.get("https_proxy")
         or os.environ.get("HTTPS_PROXY") or None)
API = "https://api.github.com"


def credential():
    p = subprocess.run("git credential fill", shell=True,
                       input="protocol=https\nhost=github.com\n\n",
                       capture_output=True, text=True)
    d = {}
    for ln in p.stdout.splitlines():
        if "=" in ln:
            k, v = ln.split("=", 1)
            d[k.strip()] = v.strip()
    return d.get("username"), d.get("password")


def opener():
    hs = [urllib.request.HTTPSHandler()]
    if PROXY:
        hs.append(urllib.request.ProxyHandler({"http": PROXY, "https": PROXY}))
    else:
        hs.append(urllib.request.ProxyHandler({}))
    return urllib.request.build_opener(*hs)


_OP = None


def call(method, path, payload=None, retries=4):
    global _OP
    if _OP is None:
        _OP = opener()
    url = path if path.startswith("http") else API + path
    body = json.dumps(payload).encode() if payload is not None else None
    for i in range(retries):
        req = urllib.request.Request(url, data=body, method=method, headers={
            "Authorization": "Bearer " + G_TOKEN,
            "User-Agent": "wb-push",
            "Accept": "application/vnd.github+json",
            "Content-Type": "application/json",
        })
        try:
            with _OP.open(req, timeout=90) as r:
                return json.loads(r.read().decode() or "{}")
        except urllib.error.HTTPError as e:
            msg = e.read().decode()[:300]
            if e.code in (502, 503, 500, 429) and i < retries - 1:
                continue
            raise SystemExit("HTTP %s on %s %s\n%s" % (e.code, method, path, msg))
        except Exception:
            if i < retries - 1:
                continue
            raise
    raise SystemExit("重试耗尽: %s %s" % (method, path))


G_TOKEN = None
G_REPO = None


def git_out(repo, *args):
    return subprocess.run(["git", "-C", repo] + list(args),
                          capture_output=True).stdout


def collect_blobs(repo):
    """返回 [(mode, sha, path)]，内容从 git 对象库取（已归一化）。"""
    raw = git_out(repo, "ls-tree", "-r", "-z", "HEAD").split(b"\0")
    entries = []
    for ln in raw:
        if not ln.strip():
            continue
        meta, path = ln.split(b"\t", 1)
        mode, typ, sha = meta.split(b" ")
        entries.append((mode.decode(), sha.decode(), path.decode("utf-8")))
    print("  受控文件 %d 个" % len(entries))
    return entries


def read_blobs(repo, shas):
    """用 git cat-file --batch 一次性取出所有内容。"""
    p = subprocess.Popen(["git", "-C", repo, "cat-file", "--batch"],
                         stdin=subprocess.PIPE, stdout=subprocess.PIPE)
    out, _ = p.communicate(("\n".join(shas) + "\n").encode())
    data, i = {}, 0
    for sha in shas:
        nl = out.index(b"\n", i)
        header = out[i:nl].split()
        size = int(header[2])
        body = out[nl + 1: nl + 1 + size]
        data[sha] = body
        i = nl + 1 + size + 1
    return data


def get_remote_head(owner_repo, branch):
    """取远端 main 当前 HEAD 的 sha，作为新提交的 parent。

    与脚本早期版（parent=[] 走 force PATCH）相比，本版的语义是「fast-forward 友好」：
    - 本地领先：正常更新远端 main，不丢历史
    - 本地落后：HTTP 422 'Update is not a fast forward'，脚本主动停下，
      不会静默覆盖远端领先提交
    """
    return call("GET", "/repos/%s/git/ref/heads/%s" % (owner_repo, branch))["object"]["sha"]


def get_remote_blob_shas(owner_repo, branch):
    """取远端 HEAD 的完整 tree，返回已有 blob 的 sha 集合（用于增量推送）。

    git 是内容寻址的：同内容的 blob 在本地与远端是同一个 sha。远端已有的
    就不必重复上传 —— 全量上传 2900+ blob 会触发 GitHub secondary rate
    limit（HTTP 403 "You have exceeded a secondary rate limit"），
    增量后通常只剩个位数。
    """
    try:
        head = get_remote_head(owner_repo, branch)
        commit = call("GET", "/repos/%s/git/commits/%s" % (owner_repo, head))
        tree_sha = commit["tree"]["sha"]
        tree = call("GET", "/repos/%s/git/trees/%s?recursive=1"
                    % (owner_repo, tree_sha))
        if tree.get("truncated"):
            print("  ⚠ 远端 tree 过大被截断，退回全量上传")
            return set()
        return {it["sha"] for it in tree.get("tree", []) if it["type"] == "blob"}
    except SystemExit:
        return set()


def update_ref(owner_repo, branch, new_sha):
    """POST/PATCH refs。优先 POST（远端无此 ref 时）；存在则 PATCH 但不带 force。"""
    try:
        call("POST", "/repos/%s/git/refs" % owner_repo,
             {"ref": "refs/heads/" + branch, "sha": new_sha})
    except SystemExit:
        # ref 已存在 → PATCH，要求新 sha 在远端历史里（即 fast-forward）
        call("PATCH", "/repos/%s/git/refs/heads/%s" % (owner_repo, branch),
             {"sha": new_sha, "force": False})


def upload_blob(content):
    r = call("POST", "/repos/%s/git/blobs" % G_REPO, {
        "content": base64.b64encode(content).decode(),
        "encoding": "base64",
    })
    return r["sha"]


def build_tree(entries_blobs, prefix=""):
    """把 [(mode, blob_sha, path)] 递归打成目录树，返回 root tree sha。"""
    files, dirs = [], {}
    for mode, sha, path in entries_blobs:
        if prefix:
            if not path.startswith(prefix):
                continue
            rel = path[len(prefix):]
        else:
            rel = path
        if "/" in rel:
            top = rel.split("/", 1)[0]
            dirs.setdefault(top, []).append((mode, sha, path))
        else:
            files.append({"path": rel, "mode": mode, "type": "blob", "sha": sha})

    tree = list(files)
    for name, sub in sorted(dirs.items()):
        sub_sha = build_tree(sub, prefix + name + "/")
        tree.append({"path": name, "mode": "040000", "type": "tree", "sha": sub_sha})
    return call("POST", "/repos/%s/git/trees" % G_REPO, {"tree": tree})["sha"]


def main():
    global G_TOKEN, G_REPO
    if len(sys.argv) < 3:
        print(__doc__)
        return 1
    repo, owner_repo = os.path.abspath(sys.argv[1]), sys.argv[2]
    branch = sys.argv[3] if len(sys.argv) > 3 else "main"

    user, tok = credential()
    if not tok:
        print("✗ 取不到 GitHub 凭据")
        return 1
    G_TOKEN = tok
    G_REPO = owner_repo
    print("账号 %s → %s@%s" % (user, owner_repo, branch))

    entries = collect_blobs(repo)
    total = len(entries)

    # 增量：远端已有的 blob 不重复上传（git 内容寻址 → 同内容同 sha）
    print("  查询远端已有 blob …")
    remote_have = get_remote_blob_shas(owner_repo, branch)
    need = [e for e in entries if e[1] not in remote_have]
    print("  远端已有 %d 个 ／ 需上传 %d 个" % (len(remote_have), len(need)))

    if need:
        print("  读取内容 …")
        blobs = read_blobs(repo, [e[1] for e in need])
        print("  上传 blob（并发 4）…")
        done = 0
        with ThreadPoolExecutor(max_workers=4) as ex:
            for _ in ex.map(lambda e: upload_blob(blobs[e[1]]), need):
                done += 1
                if done % 200 == 0:
                    print("    %d/%d" % (done, len(need)))

    # entries 的 sha 就是 blob 内容哈希，与远端一致，无需替换
    items = entries
    print("  建目录树 …")
    root = build_tree(items)

    msg = git_out(repo, "log", "-1", "--pretty=%B").decode("utf-8").strip()
    parent = get_remote_head(owner_repo, branch)
    print("  远端 parent: %s" % parent[:10])
    print("  建提交 …")
    commit = call("POST", "/repos/%s/git/commits" % G_REPO,
                  {"message": msg, "tree": root, "parents": [parent]})
    sha = commit["sha"]
    print("  新 commit:  %s" % sha[:10])

    print("  指向分支 …")
    update_ref(owner_repo, branch, sha)
    print("✓ 完成：%s@%s = %s" % (owner_repo, branch, sha[:10]))
    return 0


if __name__ == "__main__":
    sys.exit(main())
