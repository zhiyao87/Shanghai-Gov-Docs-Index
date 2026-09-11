# -*- coding: utf-8 -*-
"""手工补录：收录政策平台之外（jzts 集中公示 / 委办局官网）漏掉的文件。

用法
----
    python add_missing.py            # 补录 ADD 列表里尚未入库的条目
    python add_missing.py --dry      # 只看会补什么，不落盘

说明
----
统一政策发布平台（POST /gwk/policy/page）只覆盖「现行有效政策文件」库，
部分规范性文件只挂在 www.shanghai.gov.cn 的集中公示栏目（/jzts/…）或
委办局自有网站，平台库里没有 businessId，故无法自动抓取，只能手工补。
"""

import csv
import io
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
CSV = os.path.join(HERE, "data", "gov_docs.csv")

COLS = ["分类", "类型", "层级", "标题", "文号", "发布单位", "发布日期", "状态",
        "来源", "官方链接", "红头PDF", "红头封面", "附件", "正文",
        "原始发布年", "施行日期", "有效期止", "时效复核", "链接形态"]

# 补录清单：字段见 CSV 表头；正文文件需已放在 docs/<分类>/ 下
ADD = [
    {
        "分类": "市容绿化与景观",
        "类型": "审查与许可规则",
        "层级": "市级",
        "标题": "关于印发《上海市绿化行政许可（协助）审核若干规定》的通知",
        "文号": "沪绿容规〔2023〕6号",
        "发布单位": "上海市绿化和市容管理局",
        "发布日期": "2023-10-30",
        "状态": "有效",
        "来源": "市政府门户网站（集中公示）",
        "官方链接": "https://www.shanghai.gov.cn/jzts/20231109/4449b61681d149b2ba801f74979ea897.html",
        "红头PDF": "",
        "红头封面": "",
        "附件": "",
        "正文": "docs/市容绿化与景观/关于印发《上海市绿化行政许可（协助）审核若干规定》的通知.md",
        "原始发布年": "2023",
        "施行日期": "2023-12-01",
        "有效期止": "",
        "时效复核": "现行有效（未标有效期）",
        "链接形态": "other",
    },
]


def main():
    dry = "--dry" in sys.argv
    rows = list(csv.DictReader(io.open(CSV, encoding="utf-8-sig")))
    exist = {(r.get("标题"), r.get("文号")) for r in rows}

    todo = [a for a in ADD if (a["标题"], a["文号"]) not in exist]
    print("现有 %d 条；待补 %d 条" % (len(rows), len(todo)))
    for a in todo:
        p = os.path.join(HERE, a["正文"])
        flag = "正文已就位" if os.path.exists(p) else "!! 缺正文文件"
        print("  + %s（%s）  %s" % (a["标题"], a["文号"], flag))
    if not todo or dry:
        return 0

    rows.extend(todo)
    rows.sort(key=lambda r: (r.get("发布日期") or ""), reverse=True)
    with io.open(CSV, "w", encoding="utf-8-sig", newline="") as f:
        w = csv.DictWriter(f, fieldnames=COLS, extrasaction="ignore")
        w.writeheader()
        w.writerows(rows)
    print("已写入 %d 条 → %s" % (len(rows), CSV))
    return 0


if __name__ == "__main__":
    sys.exit(main())
