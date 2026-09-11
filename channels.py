# -*- coding: utf-8 -*-
"""官方发布渠道地图。

所有地址均由脚本从官方页面提取/验证（2026-09-11），不手写猜测。
区级入口取自上海市人民政府「政府信息公开指南」页的「各区政府信息公开平台」栏目：
    https://www.shanghai.gov.cn/nw49252/index.html
"""

# 市级渠道：(名称, 入口, 覆盖范围, 备注)
MUNICIPAL = [
    ("上海市人民政府 · 现行市政府规章库",
     "https://www.shanghai.gov.cn/xxzfgzwj/",
     "现行有效市政府规章 235 部",
     "每条提供网页正文 + 文字版(.doc) + 图片版(.pdf)"),
    ("上海市统一政策发布平台",
     "https://www.shanghai.gov.cn/zhengce/list",
     "市 / 区 / 街镇三级政策文件 10,518 条",
     "2026-06 上线试运行；本库的主数据源，含区级、街镇级文件"),
    ("上海市住房和城乡建设管理委员会 · 规范性文件",
     "https://zjw.sh.gov.cn/gfxwj/index.html",
     "约 160 份（本库取 100 份）",
     "列表直接标注施行日期与有效期，判断现行/废止最方便"),
    ("上海市规划和自然资源局",
     "https://ghzyj.sh.gov.cn/",
     "规划、土地、测绘类文件",
     "报建口径的规划管理文件主要出自此部门"),
    ("上海市房屋管理局",
     "https://fgj.sh.gov.cn/",
     "房屋管理、住房保障、旧住房改造",
     "既有建筑、住宅类项目的高频依据来源"),
    ("上海市法规规章规范性文件数据库",
     "https://www.spcsc.sh.cn/",
     "地方性法规 258 + 规章及规范性文件 3,157 件",
     "2024-01 上线，覆盖市/区/镇三级 + 人大/政府/监委/法院/检察五系统"),
    ("上海市人民政府 · 政府信息公开指南",
     "https://www.shanghai.gov.cn/nw49252/index.html",
     "全部区级、部门级公开平台入口",
     "找不到入口时的总入口"),
]

# 区级渠道：(区名, 政府信息公开入口)
DISTRICTS = [
    ("浦东新区", "https://www.pudong.gov.cn/xxgk_gkzn/index.html"),
    ("黄浦区", "https://www.shhuangpu.gov.cn/zw/govopen/goverGuide.html"),
    ("静安区", "https://www.jingan.gov.cn/dynamic/infoOpenFile.html"),
    ("徐汇区", "https://www.xuhui.gov.cn/zfxxgk/wj/index.html"),
    ("长宁区", "https://zwgk.shcn.gov.cn/xxgk/zcwj-zfxxgk/index.html"),
    ("普陀区", "https://www.shpt.gov.cn/zhengwu/zfxxgkzn-zfxxgk/index.html"),
    ("虹口区", "https://www.shhk.gov.cn/hkxxgk/zdgknr/policydoc.html"),
    ("杨浦区", "https://www.shyp.gov.cn/shypq/xxgkzn/"),
    ("宝山区", "http://xxgk.shbsq.gov.cn/zfxxgk/pubguide.html"),
    ("闵行区", "https://zwgk.shmh.gov.cn/mh-xxgk-cms/website/mh_xxgk/zfxxgk_index/List/index.htm?tab=divzcwj"),
    ("嘉定区", "http://www.jiading.gov.cn/publicity/zfxxgk/zfxxgkzn2"),
    ("金山区", "https://www.jinshan.gov.cn/zhengwu/zwgk-zfxxgkzn/index.html"),
    ("松江区", "https://www.songjiang.gov.cn/Template/dynamic/zfxxgk/zfxxgk.html"),
    ("青浦区", "https://www.shqp.gov.cn/shqp/zwgk/zwgkzt/zf/index.html"),
    ("奉贤区", "https://www.fengxian.gov.cn/zwgk/xxgk/zn/index.html"),
    ("崇明区", "http://www.shcm.gov.cn/goverDetail.html?deptcode=004&categorynum=004"),
]
