# -*- coding: utf-8 -*-
"""探测上海市各委办局官网的「政策文件 / 规范性文件」栏目，评估政策平台未覆盖的缺口。

用法
----
    python probe_agency.py              # 探测内置站点清单
    python probe_agency.py --deep       # 连子栏目一起数条目

产出：只打印报告，不改数据。
"""

import os
import re
import sys
import time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import common  # noqa: E402

SITES = [
    ("规划和自然资源局", "https://ghzyj.sh.gov.cn/"),
    ("住房和城乡建设管理委员会", "https://zjw.sh.gov.cn/"),
    ("交通委员会", "https://jtys.sh.gov.cn/"),
    ("房屋管理局", "https://fgj.sh.gov.cn/"),
    ("水务局", "https://swj.sh.gov.cn/"),
    ("生态环境局", "https://sthj.sh.gov.cn/"),
    ("应急管理局", "https://yjglj.sh.gov.cn/"),
    ("市场监督管理局", "https://scjgj.sh.gov.cn/"),
]

# 栏目关键词
COL_HINT = ["gfxwj", "zcwj", "zcfg", "xxgk", "zdgk", "zcjd", "zfwj", "gkxx"]
# 列表页条目链接形如 /xxx/20260101/<hash>.html
ITEM_RE = re.compile(r'href="([^"]*?/20\d{6}/[^"]+\.html)"[^>]*>\s*([^<]{4,160})')


def fetch(u):
    st, b = common.fetch(u, timeout=25, retries=1)
    return st, (b.decode("utf-8", "ignore") if b else "")


def main():
    deep = "--deep" in sys.argv
    for name, home in SITES:
        st, t = fetch(home)
        if st != 200:
            print("== %-14s 首页不可达（%s）" % (name, st))
            continue
        # 找栏目候选
        cols = set()
        for m in re.finditer(r'href="([^"]+)"', t):
            u = m.group(1)
            if any(h in u for h in COL_HINT):
                cols.add(u)
        # 归一化成绝对地址
        abs_cols = set()
        for c in cols:
            if c.startswith("http"):
                abs_cols.add(c)
            elif c.startswith("/"):
                abs_cols.add(re.match(r"https?://[^/]+", home).group(0) + c)
        print("== %-14s 首页 %d 字节，候选栏目 %d 个" % (name, len(t), len(abs_cols)))
        for c in sorted(abs_cols)[:30]:
            note = ""
            if deep and re.search(r"/(index\.html)?$", c):
                st2, t2 = fetch(c if c.endswith("/") else c + "/")
                items = ITEM_RE.findall(t2)
                note = "  → 首页 %d 条" % len(items)
                time.sleep(0.2)
            print("     %s%s" % (c, note))
        print()


if __name__ == "__main__":
    sys.exit(main())
