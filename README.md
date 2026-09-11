# 上海建设工程政府发文索引

上海市 **建筑、规划、工程建设** 领域的**地方性法规**、政府规章与行政规范性文件索引。
只收录**元数据 + 官方链接**，并为有实质约束力的文件附上**官方正文全文**与**红头文件 PDF / 附表附图**直链（可全文收录，见文末法律说明）。

> 配套仓库：[Arch-Standards-Index](https://github.com/zhiyao87/Arch-Standards-Index) —— 上海及全国**工程建设标准**（DGJ08 / GB / JGJ）索引。
> 本库管「政府发文」，标准库管「技术标准」，两者互补。

## 数据概览

| 指标 | 数量 |
|---|---|
| 收录文件总数 | **2590** |
| 其中的核心文件（地方性法规/规章/办法/规定/细则/导则/审查许可规则） | **1174** |
| 已附官方正文全文 | **2587** |
| 已登记红头 PDF / 附表附图 | **2025** / **946** |
| 地方性法规（市人大制定，效力最高） | **40** |
| 市级 ／ 区级 ／ 市级（临港） | 2074 ／ 475 ／ 41 |
| 时间跨度 | 2009 – 2026 |
| 覆盖区 | 16 / 16 个区有收录 |
| 数据抓取日 | 2026-09-11 |

**按来源**

| 来源 | 条数 |
|---|---|
| 统一政策发布平台 | 2022 |
| 市住建委官网 | 154 |
| 市绿化市容局官网 | 124 |
| 市住建委规范性文件 | 91 |
| 市规划资源局官网 | 86 |
| 市政府规章库 | 48 |
| 国家法律法规数据库（flk.npc.gov.cn） | 35 |
| 市房管局官网 | 29 |
| 市政府门户网站（集中公示） | 1 |

**按文件类型**

| 类型 | 条数 | 已附全文 | 说明 |
|---|---|---|---|
| 通知公告 | 928 | 927 |  |
| 办法 | 452 | 451 | ★ 有实质约束力 |
| 技术规定与导则 | 330 | 330 | ★ 有实质约束力 |
| 实施意见 | 322 | 321 |  |
| 规定 | 144 | 144 | ★ 有实质约束力 |
| 规划与计划 | 136 | 136 |  |
| 实施细则 | 91 | 91 | ★ 有实质约束力 |
| 审查与许可规则 | 66 | 66 | ★ 有实质约束力 |
| 政府规章 | 51 | 51 | ★ 有实质约束力 |
| 地方性法规 | 40 | 40 | ★ 有实质约束力 |
| 其他 | 30 | 30 |  |

**按分类**

| # | 分类 | 条数 | 索引 |
|---|---|---|---|
| 一 | 规划与土地 | 277 | [查看](index/01-规划与土地.md) |
| 二 | 建筑设计与报建 | 36 | [查看](index/02-建筑设计与报建.md) |
| 三 | 工程建设管理 | 902 | [查看](index/03-工程建设管理.md) |
| 四 | 消防与人防 | 88 | [查看](index/04-消防与人防.md) |
| 五 | 房屋与住房 | 567 | [查看](index/05-房屋与住房.md) |
| 六 | 城市更新与历史保护 | 46 | [查看](index/06-城市更新与历史保护.md) |
| 七 | 绿色低碳与节能 | 61 | [查看](index/07-绿色低碳与节能.md) |
| 八 | 市政与基础设施 | 289 | [查看](index/08-市政与基础设施.md) |
| 九 | 市容绿化与景观 | 278 | [查看](index/09-市容绿化与景观.md) |
| 十 | 建筑垃圾与材料 | 21 | [查看](index/10-建筑垃圾与材料.md) |
| 11 | 轨道交通 | 25 | [查看](index/11-轨道交通.md) |
| 12 | **主题速查**（屋顶绿化/光伏/绿建/海绵/既有建筑改造） | - | [查看](index/12-主题速查.md) |

## 每条文件都挂三种取用方式

政府发文详情页上其实有**三样**东西，只抓网页正文会丢掉最有用的那部分：

| 取用方式 | 说明 | 已收录 |
|---|---|---|
| **正文** | 网页正文，转为 Markdown 便于检索与全文搜 | 2587 条 |
| **红头PDF** | 盖章红头文件原件，认文号、对版式、报建送审都用它 | 2025 条 |
| **附表附图** | 技术规范真正的操作部分（参数表、取值表、图示）——只在附件里 | 946 条 |

**为什么专门标出附表附图**：以《上海市日照分析技术规范》（沪规划资源建〔2021〕437 号）为例，日照计算参数、窗台高度取值、图示全在随文的「附表、附图、附件.pdf」里，**网页正文一个字都没有**。只存正文，等于把这份规范最有用的部分丢了。

各类索引表的「正文 / 原件」列即按 **正文 · 红头PDF · 附表附图** 三种链接并排给出。

> 二进制原件（PDF/PNG）默认**只登记官方直链、不镜像进本仓库**，以免把公开索引撑成 GB 级。需要离线留存就跑 `python fetch_assets.py --download`，原件会落到本地 `attachments/`，并生成 `attachment_manifest.csv` 清单。

## 时效复核：这几条现在还算数吗

上海的建设类规范性文件普遍带**有效期**（多为 5 年），到期若不续期就自动失效。所以「一条还灵不灵」**不能只看发布日期** —— 本库从官方正文里挖出**有效期止**，逐条判定：

| 判定 | 条数 | 含义 |
|---|---|---|
| 现行有效 | 2484 | 有效期止在今天之后，或未标有效期但平台状态为「有效」 |
| ⚠ 有效期已届满 | 57 | 有效期止已过，**须核对是否已发续期通知** |
| ⚠ 正文含废止表述 | 14 | 正文出现「本X…废止/失效」，可能只是**废止他文**，须人工确认 |
| 已废止/失效 | 29 | 平台明确标注废止或失效，**不要再引用** |
| 未标注 | 6 | 无正文且平台无状态 |

索引各表的「**时效**」列就是这张表的缩略：**✓** 现行有效 ／ **⚠** 需人工确认 ／ **✗** 已废止 ／ **?** 未标注。

**⚠ 有效期已届满的 57 条，按届满年份**（越靠后越可能是「刚过期、续期还没上网」）：

| 届满年份 | 条数 |
|---|---|
| 2015 | 1 |
| 2017 | 1 |
| 2021 | 1 |
| 2022 | 1 |
| 2023 | 8 |
| 2024 | 18 |
| 2025 | 14 |
| 2026 | 13 |

最近到期的 12 条：

| 有效期止 | 标题 | 发布机关 |
|---|---|---|
| 2026-08-31 | [上海市住房和城乡建设管理委员会关于修订印发《上海市建设工程评标专家和评标专家库管理办法》的通知](https://zjw.sh.gov.cn/gfxwj/20210930/c0789a87c1664e139f9b913cbdea9ee9.html) | 上海市住房和城乡建设管理委员会 |
| 2026-08-31 | [上海市普陀区人民政府关于印发《上海市普陀区公共租赁住房实施办法》的通知](https://www.shanghai.gov.cn/zhengce/detail?businessId=007590789&siteId=0075) | 上海市普陀区人民政府 |
| 2026-08-31 | [关于修订《上海市共有产权保障住房价格管理办法》的通知](https://www.shanghai.gov.cn/zhengce/detail?businessId=8e1bd8818a7c408f9389551fda8c4f9f&siteId=0025) | 上海市发展和改革委员会 |
| 2026-08-31 | [关于印发《本市公安机关行使有关消防行政处罚权事项清单》的通知](https://www.shanghai.gov.cn/zhengce/detail?businessId=GKXX-20210907084806321--5667&siteId=0033) | 上海市公安局 |
| 2026-07-05 | [关于印发《上海市绿化和市容管理局科研项目管理办法》的通知](https://www.shanghai.gov.cn/zhengce/detail?businessId=f5c8adfe-e52a-4e91-89cd-b7274a7ed510&siteId=0039) | 上海市绿化和市容管理局 |
| 2026-06-30 | [关于印发《上海市共有产权保障住房供后管理实施细则》的通知](https://www.shanghai.gov.cn/zhengce/detail?businessId=484934a3ccdb4ed988e2c2e4d7004d83&siteId=0013) | 上海市房屋管理局 |
| 2026-06-30 | [关于本市城市基础设施配套费征收标准和使用范围等有关事项的通知](https://zjw.sh.gov.cn/gfxwj/20211109/c3bbd05093f24a398f673b3420618e3e.html) | 上海市住房和城乡建设管理委员会 |
| 2026-06-30 | [关于印发《上海市住宅物业管理区域机动车停放管理规定》的通知](https://www.shanghai.gov.cn/zhengce/detail?businessId=dba44d90510b4216b4be4cbe779dbf8d&siteId=0013) | 上海市房屋管理局 |
| 2026-06-30 | [关于印发《上海市共有产权保障住房销售差额资金管理办法》的通知](https://www.shanghai.gov.cn/zhengce/detail?businessId=6c8a3f8d6646459da2e971a2cce3b939&siteId=0013) | 上海市房屋管理局 |
| 2026-06-30 | [关于印发《关于进一步贯彻实施〈上海市住宅物业管理规定〉的若干意见》的通知](https://www.shanghai.gov.cn/zhengce/detail?businessId=c01bf90254bb4429826e5ee4771e580b&siteId=0013) | 上海市房屋管理局 |
| 2026-05-31 | [上海市住房和城乡建设管理委员会关于印发《上海市建设工程勘察设计单位项目主要负责人工程质量违法违规行为记分管理办法》的通知](https://zjw.sh.gov.cn/gfxwj/20210930/0ed5658e5dd24edba5ad53b479359436.html) | 上海市住房和城乡建设管理委员会 |
| 2026-04-30 | [关于印发《上海市政府购买服务管理办法》的通知](https://www.shanghai.gov.cn/zhengce/detail?businessId=xxfbdf0000017339&siteId=0017) | 上海市财政局 |

> **怎么用**：查到年代久远的文件，先看「时效」列。是 ⚠ 就去官方链接核对有没有续期通知；是 ✗ 就别再引用了。⚠ **不等于**失效 —— 相当一部分只是刚到期、续期文件还没公布。

## 官方发布渠道地图

找上海的建设类政府文件，认准下面这几个口子就够。**全部为官方发布源**。

### 市级

| 渠道 | 官方入口 | 覆盖 | 备注 |
|---|---|---|---|
| 上海市人民政府 · 现行市政府规章库 | [打开](https://www.shanghai.gov.cn/xxzfgzwj/) | 现行有效市政府规章 235 部 | 每条提供网页正文 + 文字版(.doc) + 图片版(.pdf) |
| 上海市统一政策发布平台 | [打开](https://www.shanghai.gov.cn/zhengce/list) | 市 / 区 / 街镇三级政策文件 10,518 条 | 2026-06 上线试运行；本库的主数据源，含区级、街镇级文件 |
| 上海市住房和城乡建设管理委员会 · 规范性文件 | [打开](https://zjw.sh.gov.cn/gfxwj/index.html) | 约 160 份（本库取 100 份） | 列表直接标注施行日期与有效期，判断现行/废止最方便 |
| 上海市规划和自然资源局 | [打开](https://ghzyj.sh.gov.cn/) | 规划、土地、测绘类文件 | 报建口径的规划管理文件主要出自此部门 |
| 上海市房屋管理局 | [打开](https://fgj.sh.gov.cn/) | 房屋管理、住房保障、旧住房改造 | 既有建筑、住宅类项目的高频依据来源 |
| 国家法律法规数据库 · 上海地方性法规 | [打开](https://flk.npc.gov.cn/) | 全部现行有效地方性法规（上海 530 件） | 全国人大常委会办公厅维护；可下官方 DOCX/PDF 原件。★ 唯一收录地方性法规的权威源 |
| 上海人大 · 法规公布 | [打开](https://www.shrd.gov.cn/shrd/fggb/fggb.html) | 近年新公布的地方性法规（约 180 件） | 市人大官网；只发「近期公布」流，早年法规需查国家法律法规数据库 |
| 上海市人民政府 · 政府信息公开指南 | [打开](https://www.shanghai.gov.cn/nw49252/index.html) | 全部区级、部门级公开平台入口 | 找不到入口时的总入口 |

**⚠ 已失效的旧入口（勿再使用）**

- ~~上海市法规规章规范性文件数据库~~（`https://www.spcsc.sh.cn/`）：2026-09-11 实测：该域名已被非官方站点占用（解析为博彩/直播站），不可再用；地方性法规请改查 www.shrd.gov.cn 或 flk.npc.gov.cn

### 区级（16 区）

区级文件不在市级栏目里，需到各区政府门户的「政务公开 → 规范性文件／政策文件」取。
下表入口取自上海市人民政府《政府信息公开指南》页，**均经核实**。

| 区 | 政府信息公开入口 | 本库收录 |
|---|---|---|
| 浦东新区 | [打开](https://www.pudong.gov.cn/xxgk_gkzn/index.html) | 38 条 |
| 黄浦区 | [打开](https://www.shhuangpu.gov.cn/zw/govopen/goverGuide.html) | 52 条 |
| 静安区 | [打开](https://www.jingan.gov.cn/dynamic/infoOpenFile.html) | 36 条 |
| 徐汇区 | [打开](https://www.xuhui.gov.cn/zfxxgk/wj/index.html) | 12 条 |
| 长宁区 | [打开](https://zwgk.shcn.gov.cn/xxgk/zcwj-zfxxgk/index.html) | 16 条 |
| 普陀区 | [打开](https://www.shpt.gov.cn/zhengwu/zfxxgkzn-zfxxgk/index.html) | 34 条 |
| 虹口区 | [打开](https://www.shhk.gov.cn/hkxxgk/zdgknr/policydoc.html) | 21 条 |
| 杨浦区 | [打开](https://www.shyp.gov.cn/shypq/xxgkzn/) | 17 条 |
| 宝山区 | [打开](http://xxgk.shbsq.gov.cn/zfxxgk/pubguide.html) | 41 条 |
| 闵行区 | [打开](https://zwgk.shmh.gov.cn/mh-xxgk-cms/website/mh_xxgk/zfxxgk_index/List/index.htm?tab=divzcwj) | 26 条 |
| 嘉定区 | [打开](http://www.jiading.gov.cn/publicity/zfxxgk/zfxxgkzn2) | 18 条 |
| 金山区 | [打开](https://www.jinshan.gov.cn/zhengwu/zwgk-zfxxgkzn/index.html) | 22 条 |
| 松江区 | [打开](https://www.songjiang.gov.cn/Template/dynamic/zfxxgk/zfxxgk.html) | 37 条 |
| 青浦区 | [打开](https://www.shqp.gov.cn/shqp/zwgk/zwgkzt/zf/index.html) | 18 条 |
| 奉贤区 | [打开](https://www.fengxian.gov.cn/zwgk/xxgk/zn/index.html) | 39 条 |
| 崇明区 | [打开](http://www.shcm.gov.cn/goverDetail.html?deptcode=004&categorynum=004) | 33 条 |

> **提示**：区级文件的检索体验普遍弱于市级，各区栏目结构不统一、分页方式各异。
想一次覆盖全，用 [上海市统一政策发布平台](https://www.shanghai.gov.cn/zhengce/list)——它纵向贯通市/区/镇三级、横向覆盖各部门，本库的区级数据即来源于此。

## 已知检索盲区（按标题检索找不到的）

有若干实务高频主题，**没有以它命名的独立文件**，条款散落在综合性文件里。按标题关键词检索会显示「0 条」，容易误判为漏收 —— 特此列明。
需要这些主题时请走「正文全文检索」或直接看下列的承载文件。

| 主题 | 标题命中 | 实际承载文件（正文含相关条款） |
|---|---|---|
| 容积率 / 建筑容量 / 技术经济指标 | 0 | 《上海市建筑面积计算规划管理规定》（2021-09-30）、《上海市城市规划管理技术规定（土地使用 建筑管理）应用解释》 |
| 屋顶绿化 / 立体绿化 / 垂直绿化 | 0 | 《上海市居住区绿化调整实施办法》沪绿容规〔2023〕1 号（屋顶/棚架/垂直绿化折算 35%）、《"智造空间"工业项目配套绿化管理的工作指引》沪绿容〔2024〕154 号、《关于加强城市第五立面规划建设的指导意见》 |
| 消防案例 / 火灾案例汇编 | 0 | 库内无此体裁。消防类实际收录的是**规范 + 审查验收办法**：《建设工程消防设计审查验收技术服务管理办法》《上海市智造空间防火设计导则》等 4 条 |
| 既有建筑光伏 / 光伏建筑一体化（BIPV）专项办法 | 0 | 库内无专门办法。实际覆盖见「建筑光伏 / 太阳能应用」主题（76 条，含专项资金、开发建设方案） |

> 想按正文找这些主题，用 [`index/12-主题速查.md`](index/12-主题速查.md) —— 它按**全文**匹配，不受标题命名限制。

## 官方链接的格式（曾踩过的坑，已修正）

统一政策发布平台的详情页是**单页应用**，前台 URL 必须写成**查询参数式**：

```
✓ 正确  /zhengce/detail?businessId=<businessId>&siteId=<siteId>
✗ 错误  /zhengce/detail/<siteId>::<businessId>        ← 打开后显示不出文件内容
```

本库早期版本用的是「路径式」，2026-09-11 由戴工实测发现打不开，已把 **2,436 条官方链接 + 2,431 篇正文里的链接**全部改为查询参数式。

另外，部分区级老数据的 businessId 是 **8–11 位纯数字**（多为浦东新区、普陀、奉贤、青浦、长宁），与主流 32 位 hash 不同。这类条目已在 CSV 的「链接形态」列标为 `short`（共 136 条），若个别仍打不开，请：

1. **看库内正文** —— `docs/` 已存官方全文，不受影响；
2. 到**对应区政府门户**站内检索标题；
3. 或在 [统一政策发布平台](https://www.shanghai.gov.cn/zhengce/list) 搜标题。

## 设计报建高频文件速查

按实务环节整理的常用依据（全部来自本库，含正文）：


### 规划条件与方案报建

| 标题 | 文号 | 发布机关 | 日期 | 时效 | 正文 / 原件 |
|---|---|---|---|---|---|
| [上海市城市规划管理技术规定（土地使用 建筑管理） 2010版](https://ghzyj.sh.gov.cn/zcwj/cxgh/20250618/144bc661e28e49e7aaba95d1b066c4df.html) | - | 上海市规划和自然资源局 | 2025-06-18 | ✓ | [正文](docs/%E8%A7%84%E5%88%92%E4%B8%8E%E5%9C%9F%E5%9C%B0/%E4%B8%8A%E6%B5%B7%E5%B8%82%E5%9F%8E%E5%B8%82%E8%A7%84%E5%88%92%E7%AE%A1%E7%90%86%E6%8A%80%E6%9C%AF%E8%A7%84%E5%AE%9A%EF%BC%88%E5%9C%9F%E5%9C%B0%E4%BD%BF%E7%94%A8%20%E5%BB%BA%E7%AD%91%E7%AE%A1%E7%90%86%EF%BC%89%202010%E7%89%88.md) |
| [关于《上海市城市规划管理技术规定（土地使用 建筑管理）应用解释》继续适用的通知](https://www.shanghai.gov.cn/zhengce/detail?businessId=72d2cd5662b54f14b2375a5e984867a3&siteId=0032) | 沪规划资源建〔2025〕131号 | 上海市规划和自然资源局 | 2025-04-16 | ✓ | [正文](docs/%E8%A7%84%E5%88%92%E4%B8%8E%E5%9C%9F%E5%9C%B0/%E5%85%B3%E4%BA%8E%E3%80%8A%E4%B8%8A%E6%B5%B7%E5%B8%82%E5%9F%8E%E5%B8%82%E8%A7%84%E5%88%92%E7%AE%A1%E7%90%86%E6%8A%80%E6%9C%AF%E8%A7%84%E5%AE%9A%EF%BC%88%E5%9C%9F%E5%9C%B0%E4%BD%BF%E7%94%A8%20%E5%BB%BA%E7%AD%91%E7%AE%A1%E7%90%86%EF%BC%89%E5%BA%94%E7%94%A8%E8%A7%A3%E9%87%8A%E3%80%8B%E7%BB%A7%E7%BB%AD%E9%80%82%E7%94%A8%E7%9A%84%E9%80%9A%E7%9F%A5.md) · [红头PDF](https://www.shanghai.gov.cn/gwk/resource/file?pathname=2/0032/12/1229d0b773fc41799730b85a4c0ad2c0/978eb69809f5eedf1a3f55ebb3d05daa.pdf&filename=%E5%85%B3%E4%BA%8E%E3%80%8A%E4%B8%8A%E6%B5%B7%E5%B8%82%E5%9F%8E%E5%B8%82%E8%A7%84%E5%88%92%E7%AE%A1%E7%90%86%E6%8A%80%E6%9C%AF%E8%A7%84%E5%AE%9A%EF%BC%88%E5%9C%9F%E5%9C%B0%E4%BD%BF%E7%94%A8+%E5%BB%BA%E7%AD%91%E7%AE%A1%E7%90%86%EF%BC%89%E5%BA%94%E7%94%A8%E8%A7%A3%E9%87%8A%E3%80%8B%E7%BB%A7%E7%BB%AD%E9%80%82%E7%94%A8%E7%9A%84%E9%80%9A%E7%9F%A5.pdf) |
| [关于印发《上海市建设工程设计方案批后调整和建设规划许可变更管理办法》的通知](https://www.shanghai.gov.cn/zhengce/detail?businessId=61b934dade3e4fbaab573e01f115db0e&siteId=0032) | 沪规划资源规〔2025〕1号 | 上海市规划和自然资源局 | 2025-01-26 | ✓ | [正文](docs/%E5%B7%A5%E7%A8%8B%E5%BB%BA%E8%AE%BE%E7%AE%A1%E7%90%86/%E5%85%B3%E4%BA%8E%E5%8D%B0%E5%8F%91%E3%80%8A%E4%B8%8A%E6%B5%B7%E5%B8%82%E5%BB%BA%E8%AE%BE%E5%B7%A5%E7%A8%8B%E8%AE%BE%E8%AE%A1%E6%96%B9%E6%A1%88%E6%89%B9%E5%90%8E%E8%B0%83%E6%95%B4%E5%92%8C%E5%BB%BA%E8%AE%BE%E8%A7%84%E5%88%92%E8%AE%B8%E5%8F%AF%E5%8F%98%E6%9B%B4%E7%AE%A1%E7%90%86%E5%8A%9E%E6%B3%95%E3%80%8B%E7%9A%84%E9%80%9A%E7%9F%A5.md) · [红头PDF](https://www.shanghai.gov.cn/gwk/resource/file?pathname=2/0032/8d/8d849de69eb04deab36eb43fd7a0e8d0/e5a99662596cf8df8e279720c894a6ec.pdf&filename=%E5%85%B3%E4%BA%8E%E5%8D%B0%E5%8F%91%E3%80%8A%E4%B8%8A%E6%B5%B7%E5%B8%82%E5%BB%BA%E8%AE%BE%E5%B7%A5%E7%A8%8B%E8%AE%BE%E8%AE%A1%E6%96%B9%E6%A1%88%E6%89%B9%E5%90%8E%E8%B0%83%E6%95%B4%E5%92%8C%E5%BB%BA%E8%AE%BE%E8%A7%84%E5%88%92%E8%AE%B8%E5%8F%AF%E5%8F%98%E6%9B%B4%E7%AE%A1%E7%90%86%E5%8A%9E%E6%B3%95%E3%80%8B%E7%9A%84%E9%80%9A%E7%9F%A5.pdf) |
| [关于发布《上海市城市规划管理技术规定（土地使用 建筑管理）应用解释》的通知](https://ghzyj.sh.gov.cn/zcwj/cxgh/20241023/e84deddfcf674440b2c8b10f2393334f.html) | - | 上海市规划和自然资源局 | 2024-10-23 | ✓ | [正文](docs/%E8%A7%84%E5%88%92%E4%B8%8E%E5%9C%9F%E5%9C%B0/%E5%85%B3%E4%BA%8E%E5%8F%91%E5%B8%83%E3%80%8A%E4%B8%8A%E6%B5%B7%E5%B8%82%E5%9F%8E%E5%B8%82%E8%A7%84%E5%88%92%E7%AE%A1%E7%90%86%E6%8A%80%E6%9C%AF%E8%A7%84%E5%AE%9A%EF%BC%88%E5%9C%9F%E5%9C%B0%E4%BD%BF%E7%94%A8%20%E5%BB%BA%E7%AD%91%E7%AE%A1%E7%90%86%EF%BC%89%E5%BA%94%E7%94%A8%E8%A7%A3%E9%87%8A%E3%80%8B%E7%9A%84%E9%80%9A%E7%9F%A5.md) |
| [杨浦区规划和自然资源局转发《上海市建设工程设计方案规划公示规定》的通知](https://www.shanghai.gov.cn/zhengce/detail?businessId=007705f58e9f300cdee2270da0a4138ea3a2&siteId=0077) | 杨规划资源〔2024〕1号 | 杨浦区规划和自然资源局 | 2024-06-25 | ✓ | [正文](docs/%E5%B7%A5%E7%A8%8B%E5%BB%BA%E8%AE%BE%E7%AE%A1%E7%90%86/%E6%9D%A8%E6%B5%A6%E5%8C%BA%E8%A7%84%E5%88%92%E5%92%8C%E8%87%AA%E7%84%B6%E8%B5%84%E6%BA%90%E5%B1%80%E8%BD%AC%E5%8F%91%E3%80%8A%E4%B8%8A%E6%B5%B7%E5%B8%82%E5%BB%BA%E8%AE%BE%E5%B7%A5%E7%A8%8B%E8%AE%BE%E8%AE%A1%E6%96%B9%E6%A1%88%E8%A7%84%E5%88%92%E5%85%AC%E7%A4%BA%E8%A7%84%E5%AE%9A%E3%80%8B%E7%9A%84%E9%80%9A%E7%9F%A5.md) · [红头PDF](https://www.shanghai.gov.cn/gwk/resource/file?pathname=2/0077/39/395bb9bf91594cca8bed767f30047858/6ccc34b1652db02ec541097d3d2ea0c2.pdf&filename=%E6%9D%A8%E6%B5%A6%E5%8C%BA%E8%A7%84%E5%88%92%E5%92%8C%E8%87%AA%E7%84%B6%E8%B5%84%E6%BA%90%E5%B1%80%E8%BD%AC%E5%8F%91%E3%80%8A%E4%B8%8A%E6%B5%B7%E5%B8%82%E5%BB%BA%E8%AE%BE%E5%B7%A5%E7%A8%8B%E8%AE%BE%E8%AE%A1%E6%96%B9%E6%A1%88%E8%A7%84%E5%88%92%E5%85%AC%E7%A4%BA%E8%A7%84%E5%AE%9A%E3%80%8B%E7%9A%84%E9%80%9A%E7%9F%A5.pdf) · [附表附图](https://www.shanghai.gov.cn/gwk/resource/file?pathname=2/0077/eb/eb1f60ec50d0471892255ba9206766da/6ccc34b1652db02ec541097d3d2ea0c2.pdf&filename=%E6%9D%A8%E6%B5%A6%E5%8C%BA%E8%A7%84%E5%88%92%E5%92%8C%E8%87%AA%E7%84%B6%E8%B5%84%E6%BA%90%E5%B1%80%E8%BD%AC%E5%8F%91%E3%80%8A%E4%B8%8A%E6%B5%B7%E5%B8%82%E5%BB%BA%E8%AE%BE%E5%B7%A5%E7%A8%8B%E8%AE%BE%E8%AE%A1%E6%96%B9%E6%A1%88%E8%A7%84%E5%88%92%E5%85%AC%E7%A4%BA%E8%A7%84%E5%AE%9A%E3%80%8B%E7%9A%84%E9%80%9A%E7%9F%A5.pdf) |
| [关于印发《上海市建设工程设计方案规划公示规定》的通知](https://www.shanghai.gov.cn/zhengce/detail?businessId=f0f8f01b2ac44cbea21900feab80c34e&siteId=0032) | 沪规划资源规〔2024〕2号 | 上海市规划和自然资源局 | 2024-03-26 | ✓ | [正文](docs/%E5%B7%A5%E7%A8%8B%E5%BB%BA%E8%AE%BE%E7%AE%A1%E7%90%86/%E5%85%B3%E4%BA%8E%E5%8D%B0%E5%8F%91%E3%80%8A%E4%B8%8A%E6%B5%B7%E5%B8%82%E5%BB%BA%E8%AE%BE%E5%B7%A5%E7%A8%8B%E8%AE%BE%E8%AE%A1%E6%96%B9%E6%A1%88%E8%A7%84%E5%88%92%E5%85%AC%E7%A4%BA%E8%A7%84%E5%AE%9A%E3%80%8B%E7%9A%84%E9%80%9A%E7%9F%A5.md) · [红头PDF](https://www.shanghai.gov.cn/gwk/resource/file?pathname=2/0032/39/396a65679a0f4b979ea87d9efc25966f/78a50ed56a608188e169834940a0feae.pdf&filename=%E5%85%B3%E4%BA%8E%E5%8D%B0%E5%8F%91%E3%80%8A%E4%B8%8A%E6%B5%B7%E5%B8%82%E5%BB%BA%E8%AE%BE%E5%B7%A5%E7%A8%8B%E8%AE%BE%E8%AE%A1%E6%96%B9%E6%A1%88%E8%A7%84%E5%88%92%E5%85%AC%E7%A4%BA%E8%A7%84%E5%AE%9A%E3%80%8B%E7%9A%84%E9%80%9A%E7%9F%A5.pdf) |
| [关于印发《上海市日照分析技术规范》的通知](https://www.shanghai.gov.cn/zhengce/detail?businessId=6802a03eb7184253bb5c9b39f9181443&siteId=0032) | 沪规划资源建〔2021〕437号 | 上海市规划和自然资源局 | 2021-11-26 | ✓ | [正文](docs/%E8%A7%84%E5%88%92%E4%B8%8E%E5%9C%9F%E5%9C%B0/%E5%85%B3%E4%BA%8E%E5%8D%B0%E5%8F%91%E3%80%8A%E4%B8%8A%E6%B5%B7%E5%B8%82%E6%97%A5%E7%85%A7%E5%88%86%E6%9E%90%E6%8A%80%E6%9C%AF%E8%A7%84%E8%8C%83%E3%80%8B%E7%9A%84%E9%80%9A%E7%9F%A5.md) · [红头PDF](https://www.shanghai.gov.cn/gwk/resource/file?pathname=2/0032/33/3344d748b3a84c92ac526ec5221b7443/dbfa2d859a8d81d63791795a07fa73bd.pdf&filename=%E5%85%B3%E4%BA%8E%E5%8D%B0%E5%8F%91%E3%80%8A%E4%B8%8A%E6%B5%B7%E5%B8%82%E6%97%A5%E7%85%A7%E5%88%86%E6%9E%90%E6%8A%80%E6%9C%AF%E8%A7%84%E8%8C%83%E3%80%8B%E7%9A%84%E9%80%9A%E7%9F%A5.pdf) · [附表附图](https://www.shanghai.gov.cn/gwk/resource/file?pathname=2/0032/1e/1e8e76a897dd474e8211e53033d9e7b0/31a9b8359d02e9b984cd9c1485ffbadc.pdf&filename=%E9%99%84%E8%A1%A8%E3%80%81%E9%99%84%E5%9B%BE%E3%80%81%E9%99%84%E4%BB%B6.pdf) |
| [上海市城市规划管理技术规定（土地使用建筑管理）](https://www.shanghai.gov.cn/xxzfgzwj/20210608/7c162f6f13f64d9ba26f21db7a11503b.html) | - | 上海市人民政府 | - | ✓ | [正文](docs/%E8%A7%84%E5%88%92%E4%B8%8E%E5%9C%9F%E5%9C%B0/%E4%B8%8A%E6%B5%B7%E5%B8%82%E5%9F%8E%E5%B8%82%E8%A7%84%E5%88%92%E7%AE%A1%E7%90%86%E6%8A%80%E6%9C%AF%E8%A7%84%E5%AE%9A%EF%BC%88%E5%9C%9F%E5%9C%B0%E4%BD%BF%E7%94%A8%E5%BB%BA%E7%AD%91%E7%AE%A1%E7%90%86%EF%BC%89.md) · [红头PDF](https://www.shanghai.gov.cn/cmsres/86/86b1c89fade347b3b2349e077bfe8a99/0e5e011bfdea700a47c78f3c9c55d3af.pdf) · [附表附图](https://www.shanghai.gov.cn/cmsres/3a/3aac761fe5924802a5f9d33bb8c7e9be/0e5e011bfdea700a47c78f3c9c55d3af.doc) |

[→ 查看该主题全部条目](index/02-建筑设计与报建.md)

### 面积计算与容积率

| 标题 | 文号 | 发布机关 | 日期 | 时效 | 正文 / 原件 |
|---|---|---|---|---|---|
| [上海市绿化和市容管理局关于优化我市住宅品质提升项目配套绿化面积计算规则的通知](https://www.shanghai.gov.cn/zhengce/detail?businessId=f056628b-4183-497c-b41c-59b4977266c1&siteId=0039) | 沪绿容〔2026〕21号 | 上海市绿化和市容管理局 | 2026-02-27 | ✓ | [正文](docs/%E6%88%BF%E5%B1%8B%E4%B8%8E%E4%BD%8F%E6%88%BF/%E4%B8%8A%E6%B5%B7%E5%B8%82%E7%BB%BF%E5%8C%96%E5%92%8C%E5%B8%82%E5%AE%B9%E7%AE%A1%E7%90%86%E5%B1%80%E5%85%B3%E4%BA%8E%E4%BC%98%E5%8C%96%E6%88%91%E5%B8%82%E4%BD%8F%E5%AE%85%E5%93%81%E8%B4%A8%E6%8F%90%E5%8D%87%E9%A1%B9%E7%9B%AE%E9%85%8D%E5%A5%97%E7%BB%BF%E5%8C%96%E9%9D%A2%E7%A7%AF%E8%AE%A1%E7%AE%97%E8%A7%84%E5%88%99%E7%9A%84%E9%80%9A%E7%9F%A5.md) · [红头PDF](https://www.shanghai.gov.cn/gwk/resource/file?pathname=2/0039/44/449510f74d204709b302d8af8fb3cd27/a9cfe4290b7be6a832e8ae7da97e7acd.pdf&filename=%E4%B8%8A%E6%B5%B7%E5%B8%82%E7%BB%BF%E5%8C%96%E5%92%8C%E5%B8%82%E5%AE%B9%E7%AE%A1%E7%90%86%E5%B1%80%E5%85%B3%E4%BA%8E%E4%BC%98%E5%8C%96%E6%88%91%E5%B8%82%E4%BD%8F%E5%AE%85%E5%93%81%E8%B4%A8%E6%8F%90%E5%8D%87%E9%A1%B9%E7%9B%AE%E9%85%8D%E5%A5%97%E7%BB%BF%E5%8C%96%E9%9D%A2%E7%A7%AF%E8%AE%A1%E7%AE%97%E8%A7%84%E5%88%99%E7%9A%84%E9%80%9A%E7%9F%A5.pdf) |
| [关于印发《上海市建筑面积计算规划管理规定》的通知](https://www.shanghai.gov.cn/zhengce/detail?businessId=146691b797364f4288d7945446adc057&siteId=0032) | 沪规划资源建〔2021〕363号 | 上海市规划和自然资源局 | 2021-09-30 | ✓ | [正文](docs/%E8%A7%84%E5%88%92%E4%B8%8E%E5%9C%9F%E5%9C%B0/%E5%85%B3%E4%BA%8E%E5%8D%B0%E5%8F%91%E3%80%8A%E4%B8%8A%E6%B5%B7%E5%B8%82%E5%BB%BA%E7%AD%91%E9%9D%A2%E7%A7%AF%E8%AE%A1%E7%AE%97%E8%A7%84%E5%88%92%E7%AE%A1%E7%90%86%E8%A7%84%E5%AE%9A%E3%80%8B%E7%9A%84%E9%80%9A%E7%9F%A5.md) · [红头PDF](https://www.shanghai.gov.cn/gwk/resource/file?pathname=2/0032/e0/e05ffcc233874f4b923ab68cf09ee003/976db0eecb694b7696643a6f1884d26a.pdf&filename=%E5%85%B3%E4%BA%8E%E5%8D%B0%E5%8F%91%E3%80%8A%E4%B8%8A%E6%B5%B7%E5%B8%82%E5%BB%BA%E7%AD%91%E9%9D%A2%E7%A7%AF%E8%AE%A1%E7%AE%97%E8%A7%84%E5%88%92%E7%AE%A1%E7%90%86%E8%A7%84%E5%AE%9A%E3%80%8B%E7%9A%84%E9%80%9A%E7%9F%A5.pdf) · [附表附图](https://www.shanghai.gov.cn/cmsres/policy_resources/146691b797364f4288d7945446adc057/13804c46bb4b4554ae3d5d3afb5f9746/%E9%99%84%E8%A1%A81-2.doc) |

[→ 查看该主题全部条目](index/01-规划与土地.md)

### 第五立面与屋面

| 标题 | 文号 | 发布机关 | 日期 | 时效 | 正文 / 原件 |
|---|---|---|---|---|---|
| [关于印发《关于加强城市第五立面规划建设的指导意见》的通知](https://www.shanghai.gov.cn/zhengce/detail?businessId=39b001a3f37d48cbbdd5dd1eb2ccc5e6&siteId=0032) | 沪规划资源建〔2023〕361号 | 上海市规划和自然资源局 | 2023-09-22 | ✓ | [正文](docs/%E8%A7%84%E5%88%92%E4%B8%8E%E5%9C%9F%E5%9C%B0/%E5%85%B3%E4%BA%8E%E5%8D%B0%E5%8F%91%E3%80%8A%E5%85%B3%E4%BA%8E%E5%8A%A0%E5%BC%BA%E5%9F%8E%E5%B8%82%E7%AC%AC%E4%BA%94%E7%AB%8B%E9%9D%A2%E8%A7%84%E5%88%92%E5%BB%BA%E8%AE%BE%E7%9A%84%E6%8C%87%E5%AF%BC%E6%84%8F%E8%A7%81%E3%80%8B%E7%9A%84%E9%80%9A%E7%9F%A5.md) · [红头PDF](https://www.shanghai.gov.cn/gwk/resource/file?pathname=2/0032/8a/8a9c22b8590844b5925bfc2a8caf9075/1fbac518d6054ee0ef0fe8fbf324acb3.pdf&filename=%E5%85%B3%E4%BA%8E%E5%8D%B0%E5%8F%91%E3%80%8A%E5%85%B3%E4%BA%8E%E5%8A%A0%E5%BC%BA%E5%9F%8E%E5%B8%82%E7%AC%AC%E4%BA%94%E7%AB%8B%E9%9D%A2%E8%A7%84%E5%88%92%E5%BB%BA%E8%AE%BE%E7%9A%84%E6%8C%87%E5%AF%BC%E6%84%8F%E8%A7%81%E3%80%8B%E7%9A%84%E9%80%9A%E7%9F%A5.pdf) |
| [上海市住房和城乡建设管理委员会关于批准《多层住宅平屋面改坡屋面工程技术标准》为上海市工程建设规范的通知](https://www.shanghai.gov.cn/zhengce/detail?businessId=559a2baba51742b5bdf097b76014cf7d&siteId=0011) | 沪建标定〔2022〕78号 | 上海市住房和城乡建设管理委员会 | 2022-01-28 | ✓ | [正文](docs/%E5%B7%A5%E7%A8%8B%E5%BB%BA%E8%AE%BE%E7%AE%A1%E7%90%86/%E4%B8%8A%E6%B5%B7%E5%B8%82%E4%BD%8F%E6%88%BF%E5%92%8C%E5%9F%8E%E4%B9%A1%E5%BB%BA%E8%AE%BE%E7%AE%A1%E7%90%86%E5%A7%94%E5%91%98%E4%BC%9A%E5%85%B3%E4%BA%8E%E6%89%B9%E5%87%86%E3%80%8A%E5%A4%9A%E5%B1%82%E4%BD%8F%E5%AE%85%E5%B9%B3%E5%B1%8B%E9%9D%A2%E6%94%B9%E5%9D%A1%E5%B1%8B%E9%9D%A2%E5%B7%A5%E7%A8%8B%E6%8A%80%E6%9C%AF%E6%A0%87%E5%87%86%E3%80%8B%E4%B8%BA%E4%B8%8A%E6%B5%B7%E5%B8%82%E5%B7%A5%E7%A8%8B%E5%BB%BA%E8%AE%BE%E8%A7%84%E8%8C%83%E7%9A%84%E9%80%9A.md) · [红头PDF](https://www.shanghai.gov.cn/gwk/resource/file?pathname=2/0011/3a/3a420dbcb32c4044808dd6a17f017abb/40c123644c8ce5784b15eb4a537ef4be.pdf&filename=%E4%B8%8A%E6%B5%B7%E5%B8%82%E4%BD%8F%E6%88%BF%E5%92%8C%E5%9F%8E%E4%B9%A1%E5%BB%BA%E8%AE%BE%E7%AE%A1%E7%90%86%E5%A7%94%E5%91%98%E4%BC%9A%E5%85%B3%E4%BA%8E%E6%89%B9%E5%87%86%E3%80%8A%E5%A4%9A%E5%B1%82%E4%BD%8F%E5%AE%85%E5%B9%B3%E5%B1%8B%E9%9D%A2%E6%94%B9%E5%9D%A1%E5%B1%8B%E9%9D%A2%E5%B7%A5%E7%A8%8B%E6%8A%80%E6%9C%AF%E6%A0%87%E5%87%86%E3%80%8B%E4%B8%BA%E4%B8%8A%E6%B5%B7%E5%B8%82%E5%B7%A5%E7%A8%8B%E5%BB%BA%E8%AE%BE%E8%A7%84%E8%8C%83%E7%9A%84%E9%80%9A%E7%9F%A5.pdf) |
| [关于印发《苏州河沿岸街区建筑立面整治设计要求》的通知](https://www.shanghai.gov.cn/zhengce/detail?businessId=6d3f04a598c6488a9157a852597fc6b9&siteId=0013) | 沪房更新〔2021〕175号 | 上海市房屋管理局 | 2021-10-22 | ✓ | [正文](docs/%E6%88%BF%E5%B1%8B%E4%B8%8E%E4%BD%8F%E6%88%BF/%E5%85%B3%E4%BA%8E%E5%8D%B0%E5%8F%91%E3%80%8A%E8%8B%8F%E5%B7%9E%E6%B2%B3%E6%B2%BF%E5%B2%B8%E8%A1%97%E5%8C%BA%E5%BB%BA%E7%AD%91%E7%AB%8B%E9%9D%A2%E6%95%B4%E6%B2%BB%E8%AE%BE%E8%AE%A1%E8%A6%81%E6%B1%82%E3%80%8B%E7%9A%84%E9%80%9A%E7%9F%A5.md) · [红头PDF](https://www.shanghai.gov.cn/gwk/resource/file?pathname=2/0013/b7/b775dac728924a598156bdd3675693c4/aa525da6aacd6e1a5073563c035e24b8.pdf&filename=%E5%85%B3%E4%BA%8E%E5%8D%B0%E5%8F%91%E3%80%8A%E8%8B%8F%E5%B7%9E%E6%B2%B3%E6%B2%BF%E5%B2%B8%E8%A1%97%E5%8C%BA%E5%BB%BA%E7%AD%91%E7%AB%8B%E9%9D%A2%E6%95%B4%E6%B2%BB%E8%AE%BE%E8%AE%A1%E8%A6%81%E6%B1%82%E3%80%8B%E7%9A%84%E9%80%9A%E7%9F%A5.pdf) |
| [关于印发2021年上海市整街道（镇、乡）屋顶分布式光伏开发试点名单的通知](https://www.shanghai.gov.cn/zhengce/detail?businessId=f186a4d372c14ba88304457fab6d3b52&siteId=0025) | 沪发改能源〔2021〕210号 | 上海市发展和改革委员会 | 2021-10-11 | ✓ | [正文](docs/%E7%BB%BF%E8%89%B2%E4%BD%8E%E7%A2%B3%E4%B8%8E%E8%8A%82%E8%83%BD/%E5%85%B3%E4%BA%8E%E5%8D%B0%E5%8F%912021%E5%B9%B4%E4%B8%8A%E6%B5%B7%E5%B8%82%E6%95%B4%E8%A1%97%E9%81%93%EF%BC%88%E9%95%87%E3%80%81%E4%B9%A1%EF%BC%89%E5%B1%8B%E9%A1%B6%E5%88%86%E5%B8%83%E5%BC%8F%E5%85%89%E4%BC%8F%E5%BC%80%E5%8F%91%E8%AF%95%E7%82%B9%E5%90%8D%E5%8D%95%E7%9A%84%E9%80%9A%E7%9F%A5.md) · [红头PDF](https://www.shanghai.gov.cn/gwk/resource/file?pathname=2/0025/23/23f783fc772045e185817e91f5b8202e/13afe6a71f9749d16a8dffb80caf30b7.pdf&filename=%E5%85%B3%E4%BA%8E%E5%8D%B0%E5%8F%912021%E5%B9%B4%E4%B8%8A%E6%B5%B7%E5%B8%82%E6%95%B4%E8%A1%97%E9%81%93%EF%BC%88%E9%95%87%E3%80%81%E4%B9%A1%EF%BC%89%E5%B1%8B%E9%A1%B6%E5%88%86%E5%B8%83%E5%BC%8F%E5%85%89%E4%BC%8F%E5%BC%80%E5%8F%91%E8%AF%95%E7%82%B9%E5%90%8D%E5%8D%95%E7%9A%84%E9%80%9A%E7%9F%A5.pdf) |
| [上海市住房和城乡建设管理委员会关于批准《既有建筑外立面整治设计标准》为上海市工程建设规范的通知](https://www.shanghai.gov.cn/zhengce/detail?businessId=3d979b039e6a4782820a47c16cc22e43&siteId=0011) | 沪建标定〔2021〕335号 | 上海市住房和城乡建设管理委员会 | 2021-05-31 | ✓ | [正文](docs/%E5%B7%A5%E7%A8%8B%E5%BB%BA%E8%AE%BE%E7%AE%A1%E7%90%86/%E4%B8%8A%E6%B5%B7%E5%B8%82%E4%BD%8F%E6%88%BF%E5%92%8C%E5%9F%8E%E4%B9%A1%E5%BB%BA%E8%AE%BE%E7%AE%A1%E7%90%86%E5%A7%94%E5%91%98%E4%BC%9A%E5%85%B3%E4%BA%8E%E6%89%B9%E5%87%86%E3%80%8A%E6%97%A2%E6%9C%89%E5%BB%BA%E7%AD%91%E5%A4%96%E7%AB%8B%E9%9D%A2%E6%95%B4%E6%B2%BB%E8%AE%BE%E8%AE%A1%E6%A0%87%E5%87%86%E3%80%8B%E4%B8%BA%E4%B8%8A%E6%B5%B7%E5%B8%82%E5%B7%A5%E7%A8%8B%E5%BB%BA%E8%AE%BE%E8%A7%84%E8%8C%83%E7%9A%84%E9%80%9A%E7%9F%A5.md) · [红头PDF](https://www.shanghai.gov.cn/gwk/resource/file?pathname=2/0011/6e/6e46f6cd10a8466faf06203ff0714313/18705cdcdbed85d8b82032f99afb59f5.pdf&filename=%E4%B8%8A%E6%B5%B7%E5%B8%82%E4%BD%8F%E6%88%BF%E5%92%8C%E5%9F%8E%E4%B9%A1%E5%BB%BA%E8%AE%BE%E7%AE%A1%E7%90%86%E5%A7%94%E5%91%98%E4%BC%9A%E5%85%B3%E4%BA%8E%E6%89%B9%E5%87%86%E3%80%8A%E6%97%A2%E6%9C%89%E5%BB%BA%E7%AD%91%E5%A4%96%E7%AB%8B%E9%9D%A2%E6%95%B4%E6%B2%BB%E8%AE%BE%E8%AE%A1%E6%A0%87%E5%87%86%E3%80%8B%E4%B8%BA%E4%B8%8A%E6%B5%B7%E5%B8%82%E5%B7%A5%E7%A8%8B%E5%BB%BA%E8%AE%BE%E8%A7%84%E8%8C%83%E7%9A%84%E9%80%9A%E7%9F%A5.pdf) |
| [上海市绿化和市容管理局关于印发《屋顶绿化技术规范》的通知](https://lhsr.sh.gov.cn/zcfg/20200727/1ac2c2da2fbd459b8a29732326b02207.html) | 沪绿容〔2015〕330号 | 上海市绿化和市容管理局 | 2015-11-04 | ✓ | [正文](docs/%E5%B8%82%E5%AE%B9%E7%BB%BF%E5%8C%96%E4%B8%8E%E6%99%AF%E8%A7%82/%E4%B8%8A%E6%B5%B7%E5%B8%82%E7%BB%BF%E5%8C%96%E5%92%8C%E5%B8%82%E5%AE%B9%E7%AE%A1%E7%90%86%E5%B1%80%E5%85%B3%E4%BA%8E%E5%8D%B0%E5%8F%91%E3%80%8A%E5%B1%8B%E9%A1%B6%E7%BB%BF%E5%8C%96%E6%8A%80%E6%9C%AF%E8%A7%84%E8%8C%83%E3%80%8B%E7%9A%84%E9%80%9A%E7%9F%A5.md) · [附表附图](http://sh.lhsr.cn/Plugins/ueditor1_2_5_1-utf8-net/net/upload/2017-02-22/e3865c19-02f5-405c-9951-ce528d45a494.doc) |
| [关于印发《本市新建屋顶绿化折算抵算配套绿地实施意见（试行）》的通知](https://lhsr.sh.gov.cn/zcfg/20140319/0039-6F4F15C1-0186-4803-8706-896764D4CCF2.html) | 沪绿容(2014)74号 | 上海市绿化和市容管理局 | 2014-03-19 | ✓ | [正文](docs/%E5%B8%82%E5%AE%B9%E7%BB%BF%E5%8C%96%E4%B8%8E%E6%99%AF%E8%A7%82/%E5%85%B3%E4%BA%8E%E5%8D%B0%E5%8F%91%E3%80%8A%E6%9C%AC%E5%B8%82%E6%96%B0%E5%BB%BA%E5%B1%8B%E9%A1%B6%E7%BB%BF%E5%8C%96%E6%8A%98%E7%AE%97%E6%8A%B5%E7%AE%97%E9%85%8D%E5%A5%97%E7%BB%BF%E5%9C%B0%E5%AE%9E%E6%96%BD%E6%84%8F%E8%A7%81%EF%BC%88%E8%AF%95%E8%A1%8C%EF%BC%89%E3%80%8B%E7%9A%84%E9%80%9A%E7%9F%A5.md) · [附表附图](https://www.shanghai.gov.cn/resource/37/3777024455804d928aac035b0bf58c1a/6844525296b32591e1848261330814c1.doc) |

[→ 查看该主题全部条目](index/06-城市更新与历史保护.md)

### 施工图审查

| 标题 | 文号 | 发布机关 | 日期 | 时效 | 正文 / 原件 |
|---|---|---|---|---|---|
| [关于印发《上海市建设工程施工图设计文件“多图联审”管理办法》的通知](https://zjw.sh.gov.cn/gfxwj/20260807/00978e58c73143b9989ddbfa3308525b.html) | - | 上海市住房和城乡建设管理委员会 | 2026-08 | ✓ | [正文](docs/%E5%BB%BA%E7%AD%91%E8%AE%BE%E8%AE%A1%E4%B8%8E%E6%8A%A5%E5%BB%BA/%E5%85%B3%E4%BA%8E%E5%8D%B0%E5%8F%91%E3%80%8A%E4%B8%8A%E6%B5%B7%E5%B8%82%E5%BB%BA%E8%AE%BE%E5%B7%A5%E7%A8%8B%E6%96%BD%E5%B7%A5%E5%9B%BE%E8%AE%BE%E8%AE%A1%E6%96%87%E4%BB%B6%E2%80%9C%E5%A4%9A%E5%9B%BE%E8%81%94%E5%AE%A1%E2%80%9D%E7%AE%A1%E7%90%86%E5%8A%9E%E6%B3%95%E3%80%8B%E7%9A%84%E9%80%9A%E7%9F%A5.md) · [红头PDF](https://www.shanghai.gov.cn/cmsres/be/bebad28cd7e64dddb8574010acc2a76b/b80791aa8c389e36eb5f8dc5f0058ce6.pdf) |
| [关于印发《上海市绿色建筑工程设计文件编制深度规定》《上海市住宅建筑绿色设计施工图设计文件审查要点》《上海市公共建筑绿色设计施工图设计文件审查要点》的通知](https://zjw.sh.gov.cn/jsgl/20250627/e9d93793550e41acb320a7d9a52cabf4.html) | 沪建建材〔2025〕315 号 | 上海市住房和城乡建设管理委员会 | 2025-06-27 | ✓ | [正文](docs/%E5%BB%BA%E7%AD%91%E8%AE%BE%E8%AE%A1%E4%B8%8E%E6%8A%A5%E5%BB%BA/%E5%85%B3%E4%BA%8E%E5%8D%B0%E5%8F%91%E3%80%8A%E4%B8%8A%E6%B5%B7%E5%B8%82%E7%BB%BF%E8%89%B2%E5%BB%BA%E7%AD%91%E5%B7%A5%E7%A8%8B%E8%AE%BE%E8%AE%A1%E6%96%87%E4%BB%B6%E7%BC%96%E5%88%B6%E6%B7%B1%E5%BA%A6%E8%A7%84%E5%AE%9A%E3%80%8B%E3%80%8A%E4%B8%8A%E6%B5%B7%E5%B8%82%E4%BD%8F%E5%AE%85%E5%BB%BA%E7%AD%91%E7%BB%BF%E8%89%B2%E8%AE%BE%E8%AE%A1%E6%96%BD%E5%B7%A5%E5%9B%BE%E8%AE%BE%E8%AE%A1%E6%96%87%E4%BB%B6%E5%AE%A1%E6%9F%A5%E8%A6%81%E7%82%B9%E3%80%8B%E3%80%8A%E4%B8%8A%E6%B5%B7%E5%B8%82%E5%85%AC%E5%85%B1%E5%BB%BA%E7%AD%91%E7%BB%BF%E8%89%B2%E8%AE%BE%E8%AE%A1%E6%96%BD%E5%B7%A5%E5%9B%BE%E8%AE%BE%E8%AE%A1%E6%96%87%E4%BB%B6%E5%AE%A1%E6%9F%A5%E8%A6%81%E7%82%B9%E3%80%8B%E7%9A%84%E9%80%9A%E7%9F%A5.md) · [附表附图](https://zjw.sh.gov.cn/cmsres/34/34cff2cecfaf4d28a4a3d6e5da66ca77/e76ead1b03360af59f322dacb13c229e.pdf%20%7C%20https://zjw.sh.gov.cn/cmsres/28/28c3b779c6cc45f784d995c8f0ff78db/cad9dd4ef7ef5730c1733af16d57f8b0.pdf%20%7C%20https://zjw.sh.gov.cn/cmsres/1c/1c868175b9d04473b63c4fab52b93738/b80791aa8c389e36eb5f8dc5f0058ce6.pdf) |
| [上海市住房和城乡建设管理委员会关于开展2026—2027年度上海市建设工程施工图设计文件审查机构认定工作的通知](https://www.shanghai.gov.cn/zhengce/detail?businessId=f1e10105d8854d51abb48613a8d7345f&siteId=0011) | 沪建建管〔2025〕318号 | 上海市住房和城乡建设管理委员会 | 2025-06-16 | ✓ | [正文](docs/%E5%BB%BA%E7%AD%91%E8%AE%BE%E8%AE%A1%E4%B8%8E%E6%8A%A5%E5%BB%BA/%E4%B8%8A%E6%B5%B7%E5%B8%82%E4%BD%8F%E6%88%BF%E5%92%8C%E5%9F%8E%E4%B9%A1%E5%BB%BA%E8%AE%BE%E7%AE%A1%E7%90%86%E5%A7%94%E5%91%98%E4%BC%9A%E5%85%B3%E4%BA%8E%E5%BC%80%E5%B1%952026%E2%80%942027%E5%B9%B4%E5%BA%A6%E4%B8%8A%E6%B5%B7%E5%B8%82%E5%BB%BA%E8%AE%BE%E5%B7%A5%E7%A8%8B%E6%96%BD%E5%B7%A5%E5%9B%BE%E8%AE%BE%E8%AE%A1%E6%96%87%E4%BB%B6%E5%AE%A1%E6%9F%A5%E6%9C%BA%E6%9E%84%E8%AE%A4%E5%AE%9A.md) · [红头PDF](https://www.shanghai.gov.cn/gwk/resource/file?pathname=2/0011/af/afb43a3fc2914211ba8b4214e6e61572/b80791aa8c389e36eb5f8dc5f0058ce6.pdf&filename=%E4%B8%8A%E6%B5%B7%E5%B8%82%E4%BD%8F%E6%88%BF%E5%92%8C%E5%9F%8E%E4%B9%A1%E5%BB%BA%E8%AE%BE%E7%AE%A1%E7%90%86%E5%A7%94%E5%91%98%E4%BC%9A%E5%85%B3%E4%BA%8E%E5%BC%80%E5%B1%952026%E2%80%942027%E5%B9%B4%E5%BA%A6%E4%B8%8A%E6%B5%B7%E5%B8%82%E5%BB%BA%E8%AE%BE%E5%B7%A5%E7%A8%8B%E6%96%BD%E5%B7%A5%E5%9B%BE%E8%AE%BE%E8%AE%A1%E6%96%87%E4%BB%B6%E5%AE%A1%E6%9F%A5%E6%9C%BA%E6%9E%84%E8%AE%A4%E5%AE%9A%E5%B7%A5%E4%BD%9C%E7%9A%84%E9%80%9A%E7%9F%A5.pdf) · [附表附图](https://www.shanghai.gov.cn/cmsres/policy_resources/f1e10105d8854d51abb48613a8d7345f/6bd1a3e73ed744ea91a864ef6a506ff2/2026%E2%80%942027%E5%B9%B4%E5%BA%A6%E4%B8%8A%E6%B5%B7%E5%B8%82%E5%BB%BA%E8%AE%BE%E5%B7%A5%E7%A8%8B%E6%96%BD%E5%B7%A5%E5%9B%BE%E8%AE%BE%E8%AE%A1%E6%96%87%E4%BB%B6%E5%AE%A1%E6%9F%A5%E6%9C%BA%E6%9E%84%E8%AE%A4%E5%AE%9A%E6%A0%87%E5%87%86.doc) |
| [上海市住房和城乡建设管理委员会关于印发《上海市房屋建筑施工图信息模型（BIM）交付要求》的通知](https://www.shanghai.gov.cn/zhengce/detail?businessId=d7c39dbb0d3d4d5e87f6f2dc5b1da7cb&siteId=0011) | 沪建建管〔2025〕290号 | 上海市住房和城乡建设管理委员会 | 2025-05-30 | ✓ | [正文](docs/%E5%BB%BA%E7%AD%91%E8%AE%BE%E8%AE%A1%E4%B8%8E%E6%8A%A5%E5%BB%BA/%E4%B8%8A%E6%B5%B7%E5%B8%82%E4%BD%8F%E6%88%BF%E5%92%8C%E5%9F%8E%E4%B9%A1%E5%BB%BA%E8%AE%BE%E7%AE%A1%E7%90%86%E5%A7%94%E5%91%98%E4%BC%9A%E5%85%B3%E4%BA%8E%E5%8D%B0%E5%8F%91%E3%80%8A%E4%B8%8A%E6%B5%B7%E5%B8%82%E6%88%BF%E5%B1%8B%E5%BB%BA%E7%AD%91%E6%96%BD%E5%B7%A5%E5%9B%BE%E4%BF%A1%E6%81%AF%E6%A8%A1%E5%9E%8B%EF%BC%88BIM%EF%BC%89%E4%BA%A4%E4%BB%98%E8%A6%81%E6%B1%82%E3%80%8B%E7%9A%84%E9%80%9A%E7%9F%A5.md) · [红头PDF](https://www.shanghai.gov.cn/gwk/resource/file?pathname=2/0011/f7/f7ef9113fd5c4a45b4aebe5fcec2ef21/b80791aa8c389e36eb5f8dc5f0058ce6.pdf&filename=%E4%B8%8A%E6%B5%B7%E5%B8%82%E4%BD%8F%E6%88%BF%E5%92%8C%E5%9F%8E%E4%B9%A1%E5%BB%BA%E8%AE%BE%E7%AE%A1%E7%90%86%E5%A7%94%E5%91%98%E4%BC%9A%E5%85%B3%E4%BA%8E%E5%8D%B0%E5%8F%91%E3%80%8A%E4%B8%8A%E6%B5%B7%E5%B8%82%E6%88%BF%E5%B1%8B%E5%BB%BA%E7%AD%91%E6%96%BD%E5%B7%A5%E5%9B%BE%E4%BF%A1%E6%81%AF%E6%A8%A1%E5%9E%8B%EF%BC%88BIM%EF%BC%89%E4%BA%A4%E4%BB%98%E8%A6%81%E6%B1%82%E3%80%8B%E7%9A%84%E9%80%9A%E7%9F%A5.pdf) · [附表附图](https://www.shanghai.gov.cn/cmsres/policy_resources/d7c39dbb0d3d4d5e87f6f2dc5b1da7cb/c8261c374c8f4233bbb8d07ceeef6830/%E4%B8%8A%E6%B5%B7%E5%B8%82%E6%88%BF%E5%B1%8B%E5%BB%BA%E7%AD%91%E6%96%BD%E5%B7%A5%E5%9B%BE%E4%BF%A1%E6%81%AF%E6%A8%A1%E5%9E%8B%28BIM%29%E4%BA%A4%E4%BB%98%E8%A6%81%E6%B1%82.docx) |
| [上海市住房和城乡建设管理委员会关于进一步明确本市工程建设项目施工图设计文件审查改革有关要求的通知](https://www.shanghai.gov.cn/zhengce/detail?businessId=f100d1e962294a0da699397877684ea6&siteId=0011) | 沪建建管〔2025〕55号 | 上海市住房和城乡建设管理委员会 | 2025-01-26 | ✓ | [正文](docs/%E5%BB%BA%E7%AD%91%E8%AE%BE%E8%AE%A1%E4%B8%8E%E6%8A%A5%E5%BB%BA/%E4%B8%8A%E6%B5%B7%E5%B8%82%E4%BD%8F%E6%88%BF%E5%92%8C%E5%9F%8E%E4%B9%A1%E5%BB%BA%E8%AE%BE%E7%AE%A1%E7%90%86%E5%A7%94%E5%91%98%E4%BC%9A%E5%85%B3%E4%BA%8E%E8%BF%9B%E4%B8%80%E6%AD%A5%E6%98%8E%E7%A1%AE%E6%9C%AC%E5%B8%82%E5%B7%A5%E7%A8%8B%E5%BB%BA%E8%AE%BE%E9%A1%B9%E7%9B%AE%E6%96%BD%E5%B7%A5%E5%9B%BE%E8%AE%BE%E8%AE%A1%E6%96%87%E4%BB%B6%E5%AE%A1%E6%9F%A5%E6%94%B9%E9%9D%A9%E6%9C%89%E5%85%B3%E8%A6%81%E6%B1%82%E7%9A%84%E9%80%9A%E7%9F%A5.md) · [红头PDF](https://www.shanghai.gov.cn/gwk/resource/file?pathname=2/0011/05/0517a19326f64699860e545651aa33cf/b80791aa8c389e36eb5f8dc5f0058ce6.pdf&filename=%E4%B8%8A%E6%B5%B7%E5%B8%82%E4%BD%8F%E6%88%BF%E5%92%8C%E5%9F%8E%E4%B9%A1%E5%BB%BA%E8%AE%BE%E7%AE%A1%E7%90%86%E5%A7%94%E5%91%98%E4%BC%9A%E5%85%B3%E4%BA%8E%E8%BF%9B%E4%B8%80%E6%AD%A5%E6%98%8E%E7%A1%AE%E6%9C%AC%E5%B8%82%E5%B7%A5%E7%A8%8B%E5%BB%BA%E8%AE%BE%E9%A1%B9%E7%9B%AE%E6%96%BD%E5%B7%A5%E5%9B%BE%E8%AE%BE%E8%AE%A1%E6%96%87%E4%BB%B6%E5%AE%A1%E6%9F%A5%E6%94%B9%E9%9D%A9%E6%9C%89%E5%85%B3%E8%A6%81%E6%B1%82%E7%9A%84%E9%80%9A%E7%9F%A5.pdf) · [附表附图](https://www.shanghai.gov.cn/cmsres/policy_resources/f100d1e962294a0da699397877684ea6/4b731e7b4db346189b3a6a0469abefa7/%E9%99%84%E4%BB%B61%EF%BC%9A%E4%B8%8A%E6%B5%B7%E5%B8%82%E5%BB%BA%E8%AE%BE%E5%B7%A5%E7%A8%8B%E6%96%BD%E5%B7%A5%E5%9B%BE%E8%AE%BE%E8%AE%A1%E6%96%87%E4%BB%B6%E5%85%8D%E4%BA%8E%E5%AE%A1%E6%9F%A5%E6%AD%A3%E9%9D%A2%E6%B8%85%E5%8D%95.docx)（2 个） |
| [关于印发《上海市房屋建筑工程施工图设计文件技术审查要点（岩土工程勘察篇）》（3.0版）和《上海市房屋建筑工程施工图设计文件技术审查要点（建筑设备篇）》（3.0版）的通知](https://zjw.sh.gov.cn/jsgl/20240129/75ce57f12921431798fb94a6745412e3.html) | 沪建质安〔2024〕38 号 | 上海市住房和城乡建设管理委员会 | 2024-01-29 | ✓ | [正文](docs/%E5%BB%BA%E7%AD%91%E8%AE%BE%E8%AE%A1%E4%B8%8E%E6%8A%A5%E5%BB%BA/%E5%85%B3%E4%BA%8E%E5%8D%B0%E5%8F%91%E3%80%8A%E4%B8%8A%E6%B5%B7%E5%B8%82%E6%88%BF%E5%B1%8B%E5%BB%BA%E7%AD%91%E5%B7%A5%E7%A8%8B%E6%96%BD%E5%B7%A5%E5%9B%BE%E8%AE%BE%E8%AE%A1%E6%96%87%E4%BB%B6%E6%8A%80%E6%9C%AF%E5%AE%A1%E6%9F%A5%E8%A6%81%E7%82%B9%EF%BC%88%E5%B2%A9%E5%9C%9F%E5%B7%A5%E7%A8%8B%E5%8B%98%E5%AF%9F%E7%AF%87%EF%BC%89%E3%80%8B%EF%BC%883.0%E7%89%88%EF%BC%89%E5%92%8C%E3%80%8A%E4%B8%8A%E6%B5%B7%E5%B8%82%E6%88%BF%E5%B1%8B%E5%BB%BA%E7%AD%91%E5%B7%A5%E7%A8%8B%E6%96%BD%E5%B7%A5%E5%9B%BE%E8%AE%BE%E8%AE%A1%E6%96%87%E4%BB%B6%E6%8A%80%E6%9C%AF%E5%AE%A1%E6%9F%A5%E8%A6%81%E7%82%B9%EF%BC%88%E5%BB%BA%E7%AD%91%E8%AE%BE%E5%A4%87%E7%AF%87%EF%BC%89%E3%80%8B%EF%BC%883.0%E7%89%88.md) · [附表附图](https://zjw.sh.gov.cn/cmsres/5e/5eb1f13f80e94ac49364bab84071e6f7/f6299208db95624f7d209d82fa513d4d.docx%20%7C%20https://zjw.sh.gov.cn/cmsres/91/91dbb73818cd414fb2173492c1995603/40b0fad310a07dfff8437affcb94c623.pdf) |
| [关于印发《上海市人防建设工程施工图设计和审查质量检查工作细则》的通知](https://www.shanghai.gov.cn/zhengce/detail?businessId=6d70099434a24148947652caab4ce5c4&siteId=0026) | 沪国动规〔2023〕3号 | 上海市国防动员办公室 | 2023-11-29 | ✓ | [正文](docs/%E5%BB%BA%E7%AD%91%E8%AE%BE%E8%AE%A1%E4%B8%8E%E6%8A%A5%E5%BB%BA/%E5%85%B3%E4%BA%8E%E5%8D%B0%E5%8F%91%E3%80%8A%E4%B8%8A%E6%B5%B7%E5%B8%82%E4%BA%BA%E9%98%B2%E5%BB%BA%E8%AE%BE%E5%B7%A5%E7%A8%8B%E6%96%BD%E5%B7%A5%E5%9B%BE%E8%AE%BE%E8%AE%A1%E5%92%8C%E5%AE%A1%E6%9F%A5%E8%B4%A8%E9%87%8F%E6%A3%80%E6%9F%A5%E5%B7%A5%E4%BD%9C%E7%BB%86%E5%88%99%E3%80%8B%E7%9A%84%E9%80%9A%E7%9F%A5.md) · [红头PDF](https://www.shanghai.gov.cn/gwk/resource/file?pathname=2/0026/3a/3a2d566c379d476ea724fcbf83e8f386/e06b41e3a5d7bb63a04358e12eea3f9d.pdf&filename=%E5%85%B3%E4%BA%8E%E5%8D%B0%E5%8F%91%E3%80%8A%E4%B8%8A%E6%B5%B7%E5%B8%82%E4%BA%BA%E9%98%B2%E5%BB%BA%E8%AE%BE%E5%B7%A5%E7%A8%8B%E6%96%BD%E5%B7%A5%E5%9B%BE%E8%AE%BE%E8%AE%A1%E5%92%8C%E5%AE%A1%E6%9F%A5%E8%B4%A8%E9%87%8F%E6%A3%80%E6%9F%A5%E5%B7%A5%E4%BD%9C%E7%BB%86%E5%88%99%E3%80%8B%E7%9A%84%E9%80%9A%E7%9F%A5.pdf) |
| [上海市住房和城乡建设管理委员会关于进一步加强本市建设工程海绵城市施工图设计审查和竣工验收管理的有关通知](https://zjw.sh.gov.cn/jsgl/20230926/94425200d6e446e1968a4514afc19c7f.html) | 沪建综规〔2023〕374 号 | 上海市住房和城乡建设管理委员会 | 2023-09-26 | ✓ | [正文](docs/%E5%BB%BA%E7%AD%91%E8%AE%BE%E8%AE%A1%E4%B8%8E%E6%8A%A5%E5%BB%BA/%E4%B8%8A%E6%B5%B7%E5%B8%82%E4%BD%8F%E6%88%BF%E5%92%8C%E5%9F%8E%E4%B9%A1%E5%BB%BA%E8%AE%BE%E7%AE%A1%E7%90%86%E5%A7%94%E5%91%98%E4%BC%9A%E5%85%B3%E4%BA%8E%E8%BF%9B%E4%B8%80%E6%AD%A5%E5%8A%A0%E5%BC%BA%E6%9C%AC%E5%B8%82%E5%BB%BA%E8%AE%BE%E5%B7%A5%E7%A8%8B%E6%B5%B7%E7%BB%B5%E5%9F%8E%E5%B8%82%E6%96%BD%E5%B7%A5%E5%9B%BE%E8%AE%BE%E8%AE%A1%E5%AE%A1%E6%9F%A5%E5%92%8C%E7%AB%A3%E5%B7%A5%E9%AA%8C%E6%94%B6%E7%AE%A1%E7%90%86%E7%9A%84%E6%9C%89%E5%85%B3%E9%80%9A%E7%9F%A5.md) · [附表附图](https://zjw.sh.gov.cn/cmsres/96/96e7d4826fef450785efcdb1265991ad/cd3cdb3834d55d3e6815faf0f0ba87c1.doc%20%7C%20https://zjw.sh.gov.cn/cmsres/d0/d0e92e78aeb4431fa4ff6d3aa71c08d6/b80791aa8c389e36eb5f8dc5f0058ce6.pdf) |

[→ 查看该主题全部条目](index/02-建筑设计与报建.md)

### 抗震与人防

| 标题 | 文号 | 发布机关 | 日期 | 时效 | 正文 / 原件 |
|---|---|---|---|---|---|
| [关于印发《上海市人民防空工程档案管理规定》的通知](https://www.shanghai.gov.cn/zhengce/detail?businessId=ad371e463ee241f48278e5a0a72daf47&siteId=0026) | 沪国动规〔2026〕2号 | 上海市国防动员办公室 | 2026-06-11 | ✓ | [正文](docs/%E6%B6%88%E9%98%B2%E4%B8%8E%E4%BA%BA%E9%98%B2/%E5%85%B3%E4%BA%8E%E5%8D%B0%E5%8F%91%E3%80%8A%E4%B8%8A%E6%B5%B7%E5%B8%82%E4%BA%BA%E6%B0%91%E9%98%B2%E7%A9%BA%E5%B7%A5%E7%A8%8B%E6%A1%A3%E6%A1%88%E7%AE%A1%E7%90%86%E8%A7%84%E5%AE%9A%E3%80%8B%E7%9A%84%E9%80%9A%E7%9F%A5.md) · [红头PDF](https://www.shanghai.gov.cn/gwk/resource/file?pathname=2/0026/d6/d6f73b2e800c46ccb7778d95c841468b/11f8a938459375763a916b8e58bc30ea.pdf&filename=%E5%85%B3%E4%BA%8E%E5%8D%B0%E5%8F%91%E3%80%8A%E4%B8%8A%E6%B5%B7%E5%B8%82%E4%BA%BA%E6%B0%91%E9%98%B2%E7%A9%BA%E5%B7%A5%E7%A8%8B%E6%A1%A3%E6%A1%88%E7%AE%A1%E7%90%86%E8%A7%84%E5%AE%9A%E3%80%8B%E7%9A%84%E9%80%9A%E7%9F%A5.pdf) |
| [关于印发《上海市人民防空工程防护设备检验检测管理办法》的通知](https://www.shanghai.gov.cn/zhengce/detail?businessId=2ece4cf42c6d44a9942cbe9cdff5a295&siteId=0026) | 沪国动规〔2025〕5号 | 上海市国防动员办公室 | 2025-12-30 | ✓ | [正文](docs/%E6%B6%88%E9%98%B2%E4%B8%8E%E4%BA%BA%E9%98%B2/%E5%85%B3%E4%BA%8E%E5%8D%B0%E5%8F%91%E3%80%8A%E4%B8%8A%E6%B5%B7%E5%B8%82%E4%BA%BA%E6%B0%91%E9%98%B2%E7%A9%BA%E5%B7%A5%E7%A8%8B%E9%98%B2%E6%8A%A4%E8%AE%BE%E5%A4%87%E6%A3%80%E9%AA%8C%E6%A3%80%E6%B5%8B%E7%AE%A1%E7%90%86%E5%8A%9E%E6%B3%95%E3%80%8B%E7%9A%84%E9%80%9A%E7%9F%A5.md) · [红头PDF](https://www.shanghai.gov.cn/gwk/resource/file?pathname=2/0026/7a/7af57c94b84f45bfa886c1e3c9e0b13c/792d125837214d2c7da57a33504776a4.pdf&filename=%E5%85%B3%E4%BA%8E%E5%8D%B0%E5%8F%91%E3%80%8A%E4%B8%8A%E6%B5%B7%E5%B8%82%E4%BA%BA%E6%B0%91%E9%98%B2%E7%A9%BA%E5%B7%A5%E7%A8%8B%E9%98%B2%E6%8A%A4%E8%AE%BE%E5%A4%87%E6%A3%80%E9%AA%8C%E6%A3%80%E6%B5%8B%E7%AE%A1%E7%90%86%E5%8A%9E%E6%B3%95%E3%80%8B%E7%9A%84%E9%80%9A%E7%9F%A5.pdf) |
| [关于印发《上海市人民防空领域行政处罚裁量基准实施办法（2025版）》的通知](https://www.shanghai.gov.cn/zhengce/detail?businessId=e4bb3d835cca4fe0867e34f824fd185b&siteId=0026) | 沪国动规〔2025〕3号 | 上海市国防动员办公室 | 2025-12-05 | ✓ | [正文](docs/%E6%B6%88%E9%98%B2%E4%B8%8E%E4%BA%BA%E9%98%B2/%E5%85%B3%E4%BA%8E%E5%8D%B0%E5%8F%91%E3%80%8A%E4%B8%8A%E6%B5%B7%E5%B8%82%E4%BA%BA%E6%B0%91%E9%98%B2%E7%A9%BA%E9%A2%86%E5%9F%9F%E8%A1%8C%E6%94%BF%E5%A4%84%E7%BD%9A%E8%A3%81%E9%87%8F%E5%9F%BA%E5%87%86%E5%AE%9E%E6%96%BD%E5%8A%9E%E6%B3%95%EF%BC%882025%E7%89%88%EF%BC%89%E3%80%8B%E7%9A%84%E9%80%9A%E7%9F%A5.md) · [红头PDF](https://www.shanghai.gov.cn/gwk/resource/file?pathname=2/0026/67/67a90e06774849858b1839c7bc7a9cf1/6b63f3e93fa5159ce1f32c7a59456d7e.pdf&filename=%E5%85%B3%E4%BA%8E%E5%8D%B0%E5%8F%91%E3%80%8A%E4%B8%8A%E6%B5%B7%E5%B8%82%E4%BA%BA%E6%B0%91%E9%98%B2%E7%A9%BA%E9%A2%86%E5%9F%9F%E8%A1%8C%E6%94%BF%E5%A4%84%E7%BD%9A%E8%A3%81%E9%87%8F%E5%9F%BA%E5%87%86%E5%AE%9E%E6%96%BD%E5%8A%9E%E6%B3%95%EF%BC%882025%E7%89%88%EF%BC%89%E3%80%8B%E7%9A%84%E9%80%9A%E7%9F%A5.pdf) · [附表附图](https://www.shanghai.gov.cn/cmsres/policy_resources/e4bb3d835cca4fe0867e34f824fd185b/972f5dc4fadd4c0fa65c458664bf80d6/%E4%B8%8A%E6%B5%B7%E5%B8%82%E4%BA%BA%E6%B0%91%E9%98%B2%E7%A9%BA%E9%A2%86%E5%9F%9F%E8%A1%8C%E6%94%BF%E5%A4%84%E7%BD%9A%E8%A3%81%E9%87%8F%E5%9F%BA%E5%87%86%E5%AE%9E%E6%96%BD%E5%8A%9E%E6%B3%95%EF%BC%882025%E7%89%88%EF%BC%89.wps)（2 个） |
| [关于印发《上海市人民防空防护设备管理实施办法》的通知](https://www.shanghai.gov.cn/zhengce/detail?businessId=440927b062ec48fd842de526e6fc53d1&siteId=0026) | 沪国动规〔2025〕2号 | 上海市国防动员办公室 | 2025-10-30 | ✓ | [正文](docs/%E6%B6%88%E9%98%B2%E4%B8%8E%E4%BA%BA%E9%98%B2/%E5%85%B3%E4%BA%8E%E5%8D%B0%E5%8F%91%E3%80%8A%E4%B8%8A%E6%B5%B7%E5%B8%82%E4%BA%BA%E6%B0%91%E9%98%B2%E7%A9%BA%E9%98%B2%E6%8A%A4%E8%AE%BE%E5%A4%87%E7%AE%A1%E7%90%86%E5%AE%9E%E6%96%BD%E5%8A%9E%E6%B3%95%E3%80%8B%E7%9A%84%E9%80%9A%E7%9F%A5.md) · [红头PDF](https://www.shanghai.gov.cn/gwk/resource/file?pathname=2/0026/fe/fe0f5ae7912748db92ab3a4d04d793bb/1c0fa28b80f41dfc1c85abd1c2d3b535.pdf&filename=%E5%85%B3%E4%BA%8E%E5%8D%B0%E5%8F%91%E3%80%8A%E4%B8%8A%E6%B5%B7%E5%B8%82%E4%BA%BA%E6%B0%91%E9%98%B2%E7%A9%BA%E9%98%B2%E6%8A%A4%E8%AE%BE%E5%A4%87%E7%AE%A1%E7%90%86%E5%AE%9E%E6%96%BD%E5%8A%9E%E6%B3%95%E3%80%8B%E7%9A%84%E9%80%9A%E7%9F%A5.pdf) |
| [关于印发《上海市人民防空领域轻微违法行为依法不予行政处罚清单》的通知](https://www.shanghai.gov.cn/zhengce/detail?businessId=6f2651e58ab649bf85e5d861425e4e9b&siteId=0026) | 沪国动规〔2025〕1号 | 上海市国防动员办公室 | 2025-07-30 | ✓ | [正文](docs/%E6%B6%88%E9%98%B2%E4%B8%8E%E4%BA%BA%E9%98%B2/%E5%85%B3%E4%BA%8E%E5%8D%B0%E5%8F%91%E3%80%8A%E4%B8%8A%E6%B5%B7%E5%B8%82%E4%BA%BA%E6%B0%91%E9%98%B2%E7%A9%BA%E9%A2%86%E5%9F%9F%E8%BD%BB%E5%BE%AE%E8%BF%9D%E6%B3%95%E8%A1%8C%E4%B8%BA%E4%BE%9D%E6%B3%95%E4%B8%8D%E4%BA%88%E8%A1%8C%E6%94%BF%E5%A4%84%E7%BD%9A%E6%B8%85%E5%8D%95%E3%80%8B%E7%9A%84%E9%80%9A%E7%9F%A5.md) · [红头PDF](https://www.shanghai.gov.cn/gwk/resource/file?pathname=2/0026/a0/a0ab8b2f425d48508050a612c97349af/fb94b3a3d7668d72ca329245e2aa3a7a.pdf&filename=%E5%85%B3%E4%BA%8E%E5%8D%B0%E5%8F%91%E3%80%8A%E4%B8%8A%E6%B5%B7%E5%B8%82%E4%BA%BA%E6%B0%91%E9%98%B2%E7%A9%BA%E9%A2%86%E5%9F%9F%E8%BD%BB%E5%BE%AE%E8%BF%9D%E6%B3%95%E8%A1%8C%E4%B8%BA%E4%BE%9D%E6%B3%95%E4%B8%8D%E4%BA%88%E8%A1%8C%E6%94%BF%E5%A4%84%E7%BD%9A%E6%B8%85%E5%8D%95%E3%80%8B%E7%9A%84%E9%80%9A%E7%9F%A5.pdf) · [附表附图](https://www.shanghai.gov.cn/cmsres/policy_resources/6f2651e58ab649bf85e5d861425e4e9b/ea3441443ee34719baaca34dab2117cc/%E9%99%84%E4%BB%B6%EF%BC%9A%E4%B8%8A%E6%B5%B7%E5%B8%82%E4%BA%BA%E6%B0%91%E9%98%B2%E7%A9%BA%E9%A2%86%E5%9F%9F%E8%BD%BB%E5%BE%AE%E8%BF%9D%E6%B3%95%E8%A1%8C%E4%B8%BA%E4%BE%9D%E6%B3%95%E4%B8%8D%E4%BA%88%E8%A1%8C%E6%94%BF%E5%A4%84%E7%BD%9A%E6%B8%85%E5%8D%95.wps) |
| [上海市住房和城乡建设管理委员会关于批准《人民防空工程安全风险评估技术标准》为上海市工程建设规范的通知](https://www.shanghai.gov.cn/zhengce/detail?businessId=44d1af2c147444e8bb3d6c4d1dcab86a&siteId=0011) | 沪建标定〔2025〕135号 | 上海市住房和城乡建设管理委员会 | 2025-03-05 | ✓ | [正文](docs/%E5%B7%A5%E7%A8%8B%E5%BB%BA%E8%AE%BE%E7%AE%A1%E7%90%86/%E4%B8%8A%E6%B5%B7%E5%B8%82%E4%BD%8F%E6%88%BF%E5%92%8C%E5%9F%8E%E4%B9%A1%E5%BB%BA%E8%AE%BE%E7%AE%A1%E7%90%86%E5%A7%94%E5%91%98%E4%BC%9A%E5%85%B3%E4%BA%8E%E6%89%B9%E5%87%86%E3%80%8A%E4%BA%BA%E6%B0%91%E9%98%B2%E7%A9%BA%E5%B7%A5%E7%A8%8B%E5%AE%89%E5%85%A8%E9%A3%8E%E9%99%A9%E8%AF%84%E4%BC%B0%E6%8A%80%E6%9C%AF%E6%A0%87%E5%87%86%E3%80%8B%E4%B8%BA%E4%B8%8A%E6%B5%B7%E5%B8%82%E5%B7%A5%E7%A8%8B%E5%BB%BA%E8%AE%BE%E8%A7%84%E8%8C%83%E7%9A%84%E9%80%9A%E7%9F%A5.md) · [红头PDF](https://www.shanghai.gov.cn/gwk/resource/file?pathname=2/0011/b6/b68934bdfc324caabaa594ce98c5291d/b80791aa8c389e36eb5f8dc5f0058ce6.pdf&filename=%E4%B8%8A%E6%B5%B7%E5%B8%82%E4%BD%8F%E6%88%BF%E5%92%8C%E5%9F%8E%E4%B9%A1%E5%BB%BA%E8%AE%BE%E7%AE%A1%E7%90%86%E5%A7%94%E5%91%98%E4%BC%9A%E5%85%B3%E4%BA%8E%E6%89%B9%E5%87%86%E3%80%8A%E4%BA%BA%E6%B0%91%E9%98%B2%E7%A9%BA%E5%B7%A5%E7%A8%8B%E5%AE%89%E5%85%A8%E9%A3%8E%E9%99%A9%E8%AF%84%E4%BC%B0%E6%8A%80%E6%9C%AF%E6%A0%87%E5%87%86%E3%80%8B%E4%B8%BA%E4%B8%8A%E6%B5%B7%E5%B8%82%E5%B7%A5%E7%A8%8B%E5%BB%BA%E8%AE%BE%E8%A7%84%E8%8C%83%E7%9A%84%E9%80%9A%E7%9F%A5.pdf) |
| [关于印发《上海市重点地区人民防空工程统筹建设管理规定》的通知](https://www.shanghai.gov.cn/zhengce/detail?businessId=2da5ce7e92df467089da954e28784c5a&siteId=0026) | 沪国动规〔2024〕1号 | 上海市国防动员办公室 | 2024-07-03 | ✓ | [正文](docs/%E6%B6%88%E9%98%B2%E4%B8%8E%E4%BA%BA%E9%98%B2/%E5%85%B3%E4%BA%8E%E5%8D%B0%E5%8F%91%E3%80%8A%E4%B8%8A%E6%B5%B7%E5%B8%82%E9%87%8D%E7%82%B9%E5%9C%B0%E5%8C%BA%E4%BA%BA%E6%B0%91%E9%98%B2%E7%A9%BA%E5%B7%A5%E7%A8%8B%E7%BB%9F%E7%AD%B9%E5%BB%BA%E8%AE%BE%E7%AE%A1%E7%90%86%E8%A7%84%E5%AE%9A%E3%80%8B%E7%9A%84%E9%80%9A%E7%9F%A5.md) · [红头PDF](https://www.shanghai.gov.cn/gwk/resource/file?pathname=2/0026/d2/d26123335dc74efdbc9dba4d6ee4688b/8726d7ccf32a1b424491d068638665b2.pdf&filename=%E5%85%B3%E4%BA%8E%E5%8D%B0%E5%8F%91%E3%80%8A%E4%B8%8A%E6%B5%B7%E5%B8%82%E9%87%8D%E7%82%B9%E5%9C%B0%E5%8C%BA%E4%BA%BA%E6%B0%91%E9%98%B2%E7%A9%BA%E5%B7%A5%E7%A8%8B%E7%BB%9F%E7%AD%B9%E5%BB%BA%E8%AE%BE%E7%AE%A1%E7%90%86%E8%A7%84%E5%AE%9A%E3%80%8B%E7%9A%84%E9%80%9A%E7%9F%A5.pdf) |
| [上海市住房和城乡建设管理委员会关于印发《上海市建筑工程设计文件抗震设防审查管理办法》的通知](https://zjw.sh.gov.cn/gfxwj/20240329/e73493bfaec14851bc904eac1d59e9d4.html) | - | 上海市住房和城乡建设管理委员会 | 2024-03 | ✓ | [正文](docs/%E5%BB%BA%E7%AD%91%E8%AE%BE%E8%AE%A1%E4%B8%8E%E6%8A%A5%E5%BB%BA/%E4%B8%8A%E6%B5%B7%E5%B8%82%E4%BD%8F%E6%88%BF%E5%92%8C%E5%9F%8E%E4%B9%A1%E5%BB%BA%E8%AE%BE%E7%AE%A1%E7%90%86%E5%A7%94%E5%91%98%E4%BC%9A%E5%85%B3%E4%BA%8E%E5%8D%B0%E5%8F%91%E3%80%8A%E4%B8%8A%E6%B5%B7%E5%B8%82%E5%BB%BA%E7%AD%91%E5%B7%A5%E7%A8%8B%E8%AE%BE%E8%AE%A1%E6%96%87%E4%BB%B6%E6%8A%97%E9%9C%87%E8%AE%BE%E9%98%B2%E5%AE%A1%E6%9F%A5%E7%AE%A1%E7%90%86%E5%8A%9E%E6%B3%95%E3%80%8B%E7%9A%84%E9%80%9A%E7%9F%A5.md) · [红头PDF](https://www.shanghai.gov.cn/cmsres/be/be11122906414c8399eecaffc6c16204/ff2b519f409aa04ab9f1b7672581d03c.pdf) · [附表附图](https://www.shanghai.gov.cn/cmsres/a2/a25060a72de44c8b9115cf1d0b2ad5a7/eaa07320161e8681a47bb9152da61ada.doc)（6 个） |

[→ 查看该主题全部条目](index/04-消防与人防.md)

### 施工许可与验收

| 标题 | 文号 | 发布机关 | 日期 | 时效 | 正文 / 原件 |
|---|---|---|---|---|---|
| [关于开展2026年度杨浦区工程总承包、全过程工程咨询政策申报的通知](https://www.shanghai.gov.cn/zhengce/detail?businessId=00773563&siteId=0077) | 杨科经〔2026〕13号 | 上海市杨浦区科技和经济委员会 | 2026-07-03 | ✓ | [正文](docs/%E5%B7%A5%E7%A8%8B%E5%BB%BA%E8%AE%BE%E7%AE%A1%E7%90%86/%E5%85%B3%E4%BA%8E%E5%BC%80%E5%B1%952026%E5%B9%B4%E5%BA%A6%E6%9D%A8%E6%B5%A6%E5%8C%BA%E5%B7%A5%E7%A8%8B%E6%80%BB%E6%89%BF%E5%8C%85%E3%80%81%E5%85%A8%E8%BF%87%E7%A8%8B%E5%B7%A5%E7%A8%8B%E5%92%A8%E8%AF%A2%E6%94%BF%E7%AD%96%E7%94%B3%E6%8A%A5%E7%9A%84%E9%80%9A%E7%9F%A5.md) · [红头PDF](https://www.shanghai.gov.cn/gwk/resource/file?pathname=2/0077/f7/f7536fa53709495d82919ec1af228642/f93bc444aed0188cbe0237e6c50f562d.pdf&filename=%E5%85%B3%E4%BA%8E%E5%BC%80%E5%B1%952026%E5%B9%B4%E5%BA%A6%E6%9D%A8%E6%B5%A6%E5%8C%BA%E5%B7%A5%E7%A8%8B%E6%80%BB%E6%89%BF%E5%8C%85%E3%80%81%E5%85%A8%E8%BF%87%E7%A8%8B%E5%B7%A5%E7%A8%8B%E5%92%A8%E8%AF%A2%E6%94%BF%E7%AD%96%E7%94%B3%E6%8A%A5%E7%9A%84%E9%80%9A%E7%9F%A5.pdf) · [附表附图](https://www.shanghai.gov.cn/gwk/resource/file?pathname=2/0077/39/39e0f8da7d2d408a9986043407c6e29e/452203c65d164544b621e7e17825c4eb.pdf&filename=%E9%99%84%E4%BB%B6%EF%BC%9A%E6%9D%A8%E6%B5%A6%E5%8C%BA%E5%B7%A5%E7%A8%8B%E6%80%BB%E6%89%BF%E5%8C%85%E3%80%81%E5%85%A8%E8%BF%87%E7%A8%8B%E5%B7%A5%E7%A8%8B%E5%92%A8%E8%AF%A2%E6%94%BF%E7%AD%96%E7%94%B3%E8%AF%B7%E6%8F%90%E7%BA%B2.pdf) |
| [上海市住房和城乡建设管理委员会关于开展BIM辅助综合竣工验收的通知](https://www.shanghai.gov.cn/zhengce/detail?businessId=ae9330e3f9a3428588a413d192f2a0f7&siteId=0011) | 沪建建管〔2026〕293号 | 上海市住房和城乡建设管理委员会 | 2026-07-01 | ✓ | [正文](docs/%E5%B7%A5%E7%A8%8B%E5%BB%BA%E8%AE%BE%E7%AE%A1%E7%90%86/%E4%B8%8A%E6%B5%B7%E5%B8%82%E4%BD%8F%E6%88%BF%E5%92%8C%E5%9F%8E%E4%B9%A1%E5%BB%BA%E8%AE%BE%E7%AE%A1%E7%90%86%E5%A7%94%E5%91%98%E4%BC%9A%E5%85%B3%E4%BA%8E%E5%BC%80%E5%B1%95BIM%E8%BE%85%E5%8A%A9%E7%BB%BC%E5%90%88%E7%AB%A3%E5%B7%A5%E9%AA%8C%E6%94%B6%E7%9A%84%E9%80%9A%E7%9F%A5.md) · [红头PDF](https://www.shanghai.gov.cn/gwk/resource/file?pathname=2/0011/99/99532170bf244e128a7bb3a95c4130df/b80791aa8c389e36eb5f8dc5f0058ce6.pdf&filename=%E4%B8%8A%E6%B5%B7%E5%B8%82%E4%BD%8F%E6%88%BF%E5%92%8C%E5%9F%8E%E4%B9%A1%E5%BB%BA%E8%AE%BE%E7%AE%A1%E7%90%86%E5%A7%94%E5%91%98%E4%BC%9A%E5%85%B3%E4%BA%8E%E5%BC%80%E5%B1%95BIM%E8%BE%85%E5%8A%A9%E7%BB%BC%E5%90%88%E7%AB%A3%E5%B7%A5%E9%AA%8C%E6%94%B6%E7%9A%84%E9%80%9A%E7%9F%A5.pdf) |
| [上海市住房和城乡建设管理委员会关于延长《上海市建设项目工程总承包管理办法》有效期的通知](https://www.shanghai.gov.cn/zhengce/detail?businessId=0e0118fce71542fcb6c3dafe41eee6d0&siteId=0011) | 沪建建管〔2026〕84号 | 上海市住房和城乡建设管理委员会 | 2026-03-10 | ✓ | [正文](docs/%E5%B7%A5%E7%A8%8B%E5%BB%BA%E8%AE%BE%E7%AE%A1%E7%90%86/%E4%B8%8A%E6%B5%B7%E5%B8%82%E4%BD%8F%E6%88%BF%E5%92%8C%E5%9F%8E%E4%B9%A1%E5%BB%BA%E8%AE%BE%E7%AE%A1%E7%90%86%E5%A7%94%E5%91%98%E4%BC%9A%E5%85%B3%E4%BA%8E%E5%BB%B6%E9%95%BF%E3%80%8A%E4%B8%8A%E6%B5%B7%E5%B8%82%E5%BB%BA%E8%AE%BE%E9%A1%B9%E7%9B%AE%E5%B7%A5%E7%A8%8B%E6%80%BB%E6%89%BF%E5%8C%85%E7%AE%A1%E7%90%86%E5%8A%9E%E6%B3%95%E3%80%8B%E6%9C%89%E6%95%88%E6%9C%9F%E7%9A%84%E9%80%9A%E7%9F%A5.md) · [红头PDF](https://www.shanghai.gov.cn/gwk/resource/file?pathname=2/0011/78/78507af3ca1e4dd19b6bd2537af2b9b2/b80791aa8c389e36eb5f8dc5f0058ce6.pdf&filename=%E4%B8%8A%E6%B5%B7%E5%B8%82%E4%BD%8F%E6%88%BF%E5%92%8C%E5%9F%8E%E4%B9%A1%E5%BB%BA%E8%AE%BE%E7%AE%A1%E7%90%86%E5%A7%94%E5%91%98%E4%BC%9A%E5%85%B3%E4%BA%8E%E5%BB%B6%E9%95%BF%E3%80%8A%E4%B8%8A%E6%B5%B7%E5%B8%82%E5%BB%BA%E8%AE%BE%E9%A1%B9%E7%9B%AE%E5%B7%A5%E7%A8%8B%E6%80%BB%E6%89%BF%E5%8C%85%E7%AE%A1%E7%90%86%E5%8A%9E%E6%B3%95%E3%80%8B%E6%9C%89%E6%95%88%E6%9C%9F%E7%9A%84%E9%80%9A%E7%9F%A5.pdf) |
| [关于印发《上海市建筑工程综合竣工验收管理办法》的通知](https://zjw.sh.gov.cn/gfxwj/20251112/f4594be5e90c4facacf5a548cb06717f.html) | - | 上海市住房和城乡建设管理委员会 | 2025-11 | ✓ | [正文](docs/%E5%B7%A5%E7%A8%8B%E5%BB%BA%E8%AE%BE%E7%AE%A1%E7%90%86/%E5%85%B3%E4%BA%8E%E5%8D%B0%E5%8F%91%E3%80%8A%E4%B8%8A%E6%B5%B7%E5%B8%82%E5%BB%BA%E7%AD%91%E5%B7%A5%E7%A8%8B%E7%BB%BC%E5%90%88%E7%AB%A3%E5%B7%A5%E9%AA%8C%E6%94%B6%E7%AE%A1%E7%90%86%E5%8A%9E%E6%B3%95%E3%80%8B%E7%9A%84%E9%80%9A%E7%9F%A5.md) · [红头PDF](https://www.shanghai.gov.cn/cmsres/cb/cb58224f183c4b898a228d42a62c7490/b80791aa8c389e36eb5f8dc5f0058ce6.pdf) |
| [上海市住房和城乡建设管理委员会关于进一步规范建设单位竣工验收消防查验工作的通知](https://www.shanghai.gov.cn/zhengce/detail?businessId=52453bd2c6a540b8a768847a6e225719&siteId=0011) | 沪建质安〔2025〕173号 | 上海市住房和城乡建设管理委员会 | 2025-03-24 | ✓ | [正文](docs/%E5%B7%A5%E7%A8%8B%E5%BB%BA%E8%AE%BE%E7%AE%A1%E7%90%86/%E4%B8%8A%E6%B5%B7%E5%B8%82%E4%BD%8F%E6%88%BF%E5%92%8C%E5%9F%8E%E4%B9%A1%E5%BB%BA%E8%AE%BE%E7%AE%A1%E7%90%86%E5%A7%94%E5%91%98%E4%BC%9A%E5%85%B3%E4%BA%8E%E8%BF%9B%E4%B8%80%E6%AD%A5%E8%A7%84%E8%8C%83%E5%BB%BA%E8%AE%BE%E5%8D%95%E4%BD%8D%E7%AB%A3%E5%B7%A5%E9%AA%8C%E6%94%B6%E6%B6%88%E9%98%B2%E6%9F%A5%E9%AA%8C%E5%B7%A5%E4%BD%9C%E7%9A%84%E9%80%9A%E7%9F%A5.md) · [红头PDF](https://www.shanghai.gov.cn/gwk/resource/file?pathname=2/0011/9d/9d4e23b4773243f9a132ba050bfe5b82/b80791aa8c389e36eb5f8dc5f0058ce6.pdf&filename=%E4%B8%8A%E6%B5%B7%E5%B8%82%E4%BD%8F%E6%88%BF%E5%92%8C%E5%9F%8E%E4%B9%A1%E5%BB%BA%E8%AE%BE%E7%AE%A1%E7%90%86%E5%A7%94%E5%91%98%E4%BC%9A%E5%85%B3%E4%BA%8E%E8%BF%9B%E4%B8%80%E6%AD%A5%E8%A7%84%E8%8C%83%E5%BB%BA%E8%AE%BE%E5%8D%95%E4%BD%8D%E7%AB%A3%E5%B7%A5%E9%AA%8C%E6%94%B6%E6%B6%88%E9%98%B2%E6%9F%A5%E9%AA%8C%E5%B7%A5%E4%BD%9C%E7%9A%84%E9%80%9A%E7%9F%A5.pdf) |
| [上海市住房和城乡建设管理委员会关于进一步规范和完善建筑工程施工许可审批管理工作的通知](https://www.shanghai.gov.cn/zhengce/detail?businessId=99e62fa9be3d461d8c6758c6df875073&siteId=0011) | 沪建建管〔2024〕484号 | 上海市住房和城乡建设管理委员会 | 2024-09-19 | ✓ | [正文](docs/%E5%BB%BA%E7%AD%91%E8%AE%BE%E8%AE%A1%E4%B8%8E%E6%8A%A5%E5%BB%BA/%E4%B8%8A%E6%B5%B7%E5%B8%82%E4%BD%8F%E6%88%BF%E5%92%8C%E5%9F%8E%E4%B9%A1%E5%BB%BA%E8%AE%BE%E7%AE%A1%E7%90%86%E5%A7%94%E5%91%98%E4%BC%9A%E5%85%B3%E4%BA%8E%E8%BF%9B%E4%B8%80%E6%AD%A5%E8%A7%84%E8%8C%83%E5%92%8C%E5%AE%8C%E5%96%84%E5%BB%BA%E7%AD%91%E5%B7%A5%E7%A8%8B%E6%96%BD%E5%B7%A5%E8%AE%B8%E5%8F%AF%E5%AE%A1%E6%89%B9%E7%AE%A1%E7%90%86%E5%B7%A5%E4%BD%9C%E7%9A%84%E9%80%9A%E7%9F%A5.md) · [红头PDF](https://www.shanghai.gov.cn/gwk/resource/file?pathname=2/0011/0e/0e461063cc7a47f4b41dd821832a64f4/b80791aa8c389e36eb5f8dc5f0058ce6.pdf&filename=%E4%B8%8A%E6%B5%B7%E5%B8%82%E4%BD%8F%E6%88%BF%E5%92%8C%E5%9F%8E%E4%B9%A1%E5%BB%BA%E8%AE%BE%E7%AE%A1%E7%90%86%E5%A7%94%E5%91%98%E4%BC%9A%E5%85%B3%E4%BA%8E%E8%BF%9B%E4%B8%80%E6%AD%A5%E8%A7%84%E8%8C%83%E5%92%8C%E5%AE%8C%E5%96%84%E5%BB%BA%E7%AD%91%E5%B7%A5%E7%A8%8B%E6%96%BD%E5%B7%A5%E8%AE%B8%E5%8F%AF%E5%AE%A1%E6%89%B9%E7%AE%A1%E7%90%86%E5%B7%A5%E4%BD%9C%E7%9A%84%E9%80%9A%E7%9F%A5.pdf) |
| [关于印发《上海市造林项目竣工验收办法》的通知](https://www.shanghai.gov.cn/zhengce/detail?businessId=0ca86a93-9fc0-4219-8807-8abd75951fbc&siteId=0039) | 沪绿容〔2024〕182号 | 上海市绿化和市容管理局 | 2024-05-06 | ✓ | [正文](docs/%E5%B7%A5%E7%A8%8B%E5%BB%BA%E8%AE%BE%E7%AE%A1%E7%90%86/%E5%85%B3%E4%BA%8E%E5%8D%B0%E5%8F%91%E3%80%8A%E4%B8%8A%E6%B5%B7%E5%B8%82%E9%80%A0%E6%9E%97%E9%A1%B9%E7%9B%AE%E7%AB%A3%E5%B7%A5%E9%AA%8C%E6%94%B6%E5%8A%9E%E6%B3%95%E3%80%8B%E7%9A%84%E9%80%9A%E7%9F%A5.md) · [红头PDF](https://www.shanghai.gov.cn/gwk/resource/file?pathname=2/0039/cf/cfcc2036c1e84e1ab1cc4e80a22d70f1/ccd2836c4239832843f320978b0f17e1.pdf&filename=%E5%85%B3%E4%BA%8E%E5%8D%B0%E5%8F%91%E3%80%8A%E4%B8%8A%E6%B5%B7%E5%B8%82%E9%80%A0%E6%9E%97%E9%A1%B9%E7%9B%AE%E7%AB%A3%E5%B7%A5%E9%AA%8C%E6%94%B6%E5%8A%9E%E6%B3%95%E3%80%8B%E7%9A%84%E9%80%9A%E7%9F%A5.pdf) · [附表附图](https://www.shanghai.gov.cn/gwk/resource/file?pathname=2/0039/ae/aeecbd4b74334dd9833d4efbccfebaf9/3da90db5ac8eb23685c7be613c33cc14.pdf&filename=%E9%99%84%E4%BB%B61%EF%BC%9A%E4%B8%8A%E6%B5%B7%E5%B8%82%E9%80%A0%E6%9E%97%E9%A1%B9%E7%9B%AE%E7%AB%A3%E5%B7%A5%E9%AA%8C%E6%94%B6%E5%8A%9E%E6%B3%95.pdf)（2 个） |
| [关于奉贤区庄行镇市级土地整治项目（二期）竣工验收和新增耕地确认的批复](https://ghzyj.sh.gov.cn/zcwj/tdgl/20240320/25f9b6f4c0c9435688a8271e190c76a2.html) | - | 上海市规划和自然资源局 | 2024-03-20 | ✓ | [正文](docs/%E8%A7%84%E5%88%92%E4%B8%8E%E5%9C%9F%E5%9C%B0/%E5%85%B3%E4%BA%8E%E5%A5%89%E8%B4%A4%E5%8C%BA%E5%BA%84%E8%A1%8C%E9%95%87%E5%B8%82%E7%BA%A7%E5%9C%9F%E5%9C%B0%E6%95%B4%E6%B2%BB%E9%A1%B9%E7%9B%AE%EF%BC%88%E4%BA%8C%E6%9C%9F%EF%BC%89%E7%AB%A3%E5%B7%A5%E9%AA%8C%E6%94%B6%E5%92%8C%E6%96%B0%E5%A2%9E%E8%80%95%E5%9C%B0%E7%A1%AE%E8%AE%A4%E7%9A%84%E6%89%B9%E5%A4%8D.md) |

[→ 查看该主题全部条目](index/03-工程建设管理.md)

### 绿色建筑与节能

| 标题 | 文号 | 发布机关 | 日期 | 时效 | 正文 / 原件 |
|---|---|---|---|---|---|
| [上海市住房和城乡建设管理委员会关于批准《装配式外挂墙板应用技术标准》为上海市工程建设规范的通知](https://www.shanghai.gov.cn/zhengce/detail?businessId=8d4bff46a30d4de280e319f8332cc898&siteId=0011) | 沪建标定〔2026〕294号 | 上海市住房和城乡建设管理委员会 | 2026-07-01 | ✓ | [正文](docs/%E5%B7%A5%E7%A8%8B%E5%BB%BA%E8%AE%BE%E7%AE%A1%E7%90%86/%E4%B8%8A%E6%B5%B7%E5%B8%82%E4%BD%8F%E6%88%BF%E5%92%8C%E5%9F%8E%E4%B9%A1%E5%BB%BA%E8%AE%BE%E7%AE%A1%E7%90%86%E5%A7%94%E5%91%98%E4%BC%9A%E5%85%B3%E4%BA%8E%E6%89%B9%E5%87%86%E3%80%8A%E8%A3%85%E9%85%8D%E5%BC%8F%E5%A4%96%E6%8C%82%E5%A2%99%E6%9D%BF%E5%BA%94%E7%94%A8%E6%8A%80%E6%9C%AF%E6%A0%87%E5%87%86%E3%80%8B%E4%B8%BA%E4%B8%8A%E6%B5%B7%E5%B8%82%E5%B7%A5%E7%A8%8B%E5%BB%BA%E8%AE%BE%E8%A7%84%E8%8C%83%E7%9A%84%E9%80%9A%E7%9F%A5.md) · [红头PDF](https://www.shanghai.gov.cn/gwk/resource/file?pathname=2/0011/f1/f1c5ff57b34645b69d99b319f0ce1c9e/b80791aa8c389e36eb5f8dc5f0058ce6.pdf&filename=%E4%B8%8A%E6%B5%B7%E5%B8%82%E4%BD%8F%E6%88%BF%E5%92%8C%E5%9F%8E%E4%B9%A1%E5%BB%BA%E8%AE%BE%E7%AE%A1%E7%90%86%E5%A7%94%E5%91%98%E4%BC%9A%E5%85%B3%E4%BA%8E%E6%89%B9%E5%87%86%E3%80%8A%E8%A3%85%E9%85%8D%E5%BC%8F%E5%A4%96%E6%8C%82%E5%A2%99%E6%9D%BF%E5%BA%94%E7%94%A8%E6%8A%80%E6%9C%AF%E6%A0%87%E5%87%86%E3%80%8B%E4%B8%BA%E4%B8%8A%E6%B5%B7%E5%B8%82%E5%B7%A5%E7%A8%8B%E5%BB%BA%E8%AE%BE%E8%A7%84%E8%8C%83%E7%9A%84%E9%80%9A%E7%9F%A5.pdf) |
| [上海市住房和城乡建设管理委员会关于印发上海市绿色建筑全过程管理相关格式文本的通知](https://www.shanghai.gov.cn/zhengce/detail?businessId=63d5b03228d34b55a08786cb4138645e&siteId=0011) | 沪建建材〔2026〕229号 | 上海市住房和城乡建设管理委员会 | 2026-05-26 | ✓ | [正文](docs/%E6%88%BF%E5%B1%8B%E4%B8%8E%E4%BD%8F%E6%88%BF/%E4%B8%8A%E6%B5%B7%E5%B8%82%E4%BD%8F%E6%88%BF%E5%92%8C%E5%9F%8E%E4%B9%A1%E5%BB%BA%E8%AE%BE%E7%AE%A1%E7%90%86%E5%A7%94%E5%91%98%E4%BC%9A%E5%85%B3%E4%BA%8E%E5%8D%B0%E5%8F%91%E4%B8%8A%E6%B5%B7%E5%B8%82%E7%BB%BF%E8%89%B2%E5%BB%BA%E7%AD%91%E5%85%A8%E8%BF%87%E7%A8%8B%E7%AE%A1%E7%90%86%E7%9B%B8%E5%85%B3%E6%A0%BC%E5%BC%8F%E6%96%87%E6%9C%AC%E7%9A%84%E9%80%9A%E7%9F%A5.md) · [红头PDF](https://www.shanghai.gov.cn/gwk/resource/file?pathname=2/0011/61/611b2a87f8c54a28b867ccb560f85bfd/b80791aa8c389e36eb5f8dc5f0058ce6.pdf&filename=%E4%B8%8A%E6%B5%B7%E5%B8%82%E4%BD%8F%E6%88%BF%E5%92%8C%E5%9F%8E%E4%B9%A1%E5%BB%BA%E8%AE%BE%E7%AE%A1%E7%90%86%E5%A7%94%E5%91%98%E4%BC%9A%E5%85%B3%E4%BA%8E%E5%8D%B0%E5%8F%91%E4%B8%8A%E6%B5%B7%E5%B8%82%E7%BB%BF%E8%89%B2%E5%BB%BA%E7%AD%91%E5%85%A8%E8%BF%87%E7%A8%8B%E7%AE%A1%E7%90%86%E7%9B%B8%E5%85%B3%E6%A0%BC%E5%BC%8F%E6%96%87%E6%9C%AC%E7%9A%84%E9%80%9A%E7%9F%A5.pdf) · [附表附图](https://www.shanghai.gov.cn/gwk/resource/file?pathname=2/0011/90/909e770c721942008e0e7f551977104d/eab48fe76c38b1b838ece6cfe0c5b55c.pdf&filename=%E4%B8%8A%E6%B5%B7%E5%B8%82%E7%BB%BF%E8%89%B2%E5%BB%BA%E7%AD%91%E5%85%A8%E8%BF%87%E7%A8%8B%E7%AE%A1%E7%90%86%E7%9B%B8%E5%85%B3%E6%A0%BC%E5%BC%8F%E6%96%87%E6%9C%AC%EF%BC%882026%E7%89%88%EF%BC%89%E5%A1%AB%E5%86%99%E8%AF%B4%E6%98%8E.pdf)（8 个） |
| [上海市住房和城乡建设管理委员会关于印发《上海市装配式混凝土建筑工程质量管理规定》的通知](https://zjw.sh.gov.cn/gfxwj/20260407/6ec441a8c774415da7b9076487ffdaa4.html) | - | 上海市住房和城乡建设管理委员会 | 2026-04 | ✓ | [正文](docs/%E5%B7%A5%E7%A8%8B%E5%BB%BA%E8%AE%BE%E7%AE%A1%E7%90%86/%E4%B8%8A%E6%B5%B7%E5%B8%82%E4%BD%8F%E6%88%BF%E5%92%8C%E5%9F%8E%E4%B9%A1%E5%BB%BA%E8%AE%BE%E7%AE%A1%E7%90%86%E5%A7%94%E5%91%98%E4%BC%9A%E5%85%B3%E4%BA%8E%E5%8D%B0%E5%8F%91%E3%80%8A%E4%B8%8A%E6%B5%B7%E5%B8%82%E8%A3%85%E9%85%8D%E5%BC%8F%E6%B7%B7%E5%87%9D%E5%9C%9F%E5%BB%BA%E7%AD%91%E5%B7%A5%E7%A8%8B%E8%B4%A8%E9%87%8F%E7%AE%A1%E7%90%86%E8%A7%84%E5%AE%9A%E3%80%8B%E7%9A%84%E9%80%9A%E7%9F%A5.md) · [红头PDF](https://www.shanghai.gov.cn/cmsres/cf/cf19244fbe824ed3b2ce231f86ff9a38/b80791aa8c389e36eb5f8dc5f0058ce6.pdf) |
| [上海市住房和城乡建设管理委员会关于加强本市绿色建筑全过程管理的通知](https://zjw.sh.gov.cn/gfxwj/20260413/e35458a3af5c43f2a0cd5b2f3a03a631.html) | - | 上海市住房和城乡建设管理委员会 | 2026-04 | ✓ | [正文](docs/%E6%88%BF%E5%B1%8B%E4%B8%8E%E4%BD%8F%E6%88%BF/%E4%B8%8A%E6%B5%B7%E5%B8%82%E4%BD%8F%E6%88%BF%E5%92%8C%E5%9F%8E%E4%B9%A1%E5%BB%BA%E8%AE%BE%E7%AE%A1%E7%90%86%E5%A7%94%E5%91%98%E4%BC%9A%E5%85%B3%E4%BA%8E%E5%8A%A0%E5%BC%BA%E6%9C%AC%E5%B8%82%E7%BB%BF%E8%89%B2%E5%BB%BA%E7%AD%91%E5%85%A8%E8%BF%87%E7%A8%8B%E7%AE%A1%E7%90%86%E7%9A%84%E9%80%9A%E7%9F%A5.md) · [红头PDF](https://www.shanghai.gov.cn/cmsres/af/afb4162845ea454f8f242a31be23c6c7/fe9418aa659e621734a4934d10ceb5f9.pdf) |
| [关于批准《预应力装配式混凝土框架结构技术标准》为上海市工程建设规范的通知](https://zjw.sh.gov.cn/jsgl/20260302/7561149ba4124b5d9774749ef48472f4.html) | 沪建标定〔2026〕48 号 | 上海市住房和城乡建设管理委员会 | 2026-03-02 | ✓ | [正文](docs/%E5%B7%A5%E7%A8%8B%E5%BB%BA%E8%AE%BE%E7%AE%A1%E7%90%86/%E5%85%B3%E4%BA%8E%E6%89%B9%E5%87%86%E3%80%8A%E9%A2%84%E5%BA%94%E5%8A%9B%E8%A3%85%E9%85%8D%E5%BC%8F%E6%B7%B7%E5%87%9D%E5%9C%9F%E6%A1%86%E6%9E%B6%E7%BB%93%E6%9E%84%E6%8A%80%E6%9C%AF%E6%A0%87%E5%87%86%E3%80%8B%E4%B8%BA%E4%B8%8A%E6%B5%B7%E5%B8%82%E5%B7%A5%E7%A8%8B%E5%BB%BA%E8%AE%BE%E8%A7%84%E8%8C%83%E7%9A%84%E9%80%9A%E7%9F%A5.md) |
| [关于批准《绿色建筑检测技术标准》为上海市工程建设规范的通知](https://zjw.sh.gov.cn/jsgl/20260302/c7f9c0d48d7a488194841655305861b3.html) | 沪建标定〔2026〕528 号 | 上海市住房和城乡建设管理委员会 | 2026-03-02 | ✓ | [正文](docs/%E5%B7%A5%E7%A8%8B%E5%BB%BA%E8%AE%BE%E7%AE%A1%E7%90%86/%E5%85%B3%E4%BA%8E%E6%89%B9%E5%87%86%E3%80%8A%E7%BB%BF%E8%89%B2%E5%BB%BA%E7%AD%91%E6%A3%80%E6%B5%8B%E6%8A%80%E6%9C%AF%E6%A0%87%E5%87%86%E3%80%8B%E4%B8%BA%E4%B8%8A%E6%B5%B7%E5%B8%82%E5%B7%A5%E7%A8%8B%E5%BB%BA%E8%AE%BE%E8%A7%84%E8%8C%83%E7%9A%84%E9%80%9A%E7%9F%A5.md) |
| [上海市住房和城乡建设管理委员会关于进一步加强本市超低能耗建筑监督管理的通知](https://www.shanghai.gov.cn/zhengce/detail?businessId=42204a15fbe84d718968112f6114852f&siteId=0011) | 沪建建材〔2026〕66号 | 上海市住房和城乡建设管理委员会 | 2026-02-14 | ✓ | [正文](docs/%E6%88%BF%E5%B1%8B%E4%B8%8E%E4%BD%8F%E6%88%BF/%E4%B8%8A%E6%B5%B7%E5%B8%82%E4%BD%8F%E6%88%BF%E5%92%8C%E5%9F%8E%E4%B9%A1%E5%BB%BA%E8%AE%BE%E7%AE%A1%E7%90%86%E5%A7%94%E5%91%98%E4%BC%9A%E5%85%B3%E4%BA%8E%E8%BF%9B%E4%B8%80%E6%AD%A5%E5%8A%A0%E5%BC%BA%E6%9C%AC%E5%B8%82%E8%B6%85%E4%BD%8E%E8%83%BD%E8%80%97%E5%BB%BA%E7%AD%91%E7%9B%91%E7%9D%A3%E7%AE%A1%E7%90%86%E7%9A%84%E9%80%9A%E7%9F%A5.md) · [红头PDF](https://www.shanghai.gov.cn/gwk/resource/file?pathname=2/0011/41/41d981d695094bfd8686862f3bf39e01/b80791aa8c389e36eb5f8dc5f0058ce6.pdf&filename=%E4%B8%8A%E6%B5%B7%E5%B8%82%E4%BD%8F%E6%88%BF%E5%92%8C%E5%9F%8E%E4%B9%A1%E5%BB%BA%E8%AE%BE%E7%AE%A1%E7%90%86%E5%A7%94%E5%91%98%E4%BC%9A%E5%85%B3%E4%BA%8E%E8%BF%9B%E4%B8%80%E6%AD%A5%E5%8A%A0%E5%BC%BA%E6%9C%AC%E5%B8%82%E8%B6%85%E4%BD%8E%E8%83%BD%E8%80%97%E5%BB%BA%E7%AD%91%E7%9B%91%E7%9D%A3%E7%AE%A1%E7%90%86%E7%9A%84%E9%80%9A%E7%9F%A5.pdf) |
| [上海市奉贤区人民政府关于印发《奉贤区海绵城市规划建设管理办法》的通知](https://www.shanghai.gov.cn/zhengce/detail?businessId=00843743&siteId=0084) | 沪奉府发〔2026〕11号 | 上海市奉贤区人民政府 | 2026-01-27 | ✓ | [正文](docs/%E8%A7%84%E5%88%92%E4%B8%8E%E5%9C%9F%E5%9C%B0/%E4%B8%8A%E6%B5%B7%E5%B8%82%E5%A5%89%E8%B4%A4%E5%8C%BA%E4%BA%BA%E6%B0%91%E6%94%BF%E5%BA%9C%E5%85%B3%E4%BA%8E%E5%8D%B0%E5%8F%91%E3%80%8A%E5%A5%89%E8%B4%A4%E5%8C%BA%E6%B5%B7%E7%BB%B5%E5%9F%8E%E5%B8%82%E8%A7%84%E5%88%92%E5%BB%BA%E8%AE%BE%E7%AE%A1%E7%90%86%E5%8A%9E%E6%B3%95%E3%80%8B%E7%9A%84%E9%80%9A%E7%9F%A5.md) · [红头PDF](https://www.shanghai.gov.cn/gwk/resource/file?pathname=2/0084/ef/ef1a7efee1a6480fab22dc433312fbeb/79ece20c5150bd512144bd550b25cd6d.pdf&filename=%E4%B8%8A%E6%B5%B7%E5%B8%82%E5%A5%89%E8%B4%A4%E5%8C%BA%E4%BA%BA%E6%B0%91%E6%94%BF%E5%BA%9C%E5%85%B3%E4%BA%8E%E5%8D%B0%E5%8F%91%E3%80%8A%E5%A5%89%E8%B4%A4%E5%8C%BA%E6%B5%B7%E7%BB%B5%E5%9F%8E%E5%B8%82%E8%A7%84%E5%88%92%E5%BB%BA%E8%AE%BE%E7%AE%A1%E7%90%86%E5%8A%9E%E6%B3%95%E3%80%8B%E7%9A%84%E9%80%9A%E7%9F%A5.pdf) |

[→ 查看该主题全部条目](index/07-绿色低碳与节能.md)

### 既有建筑与城市更新

| 标题 | 文号 | 发布机关 | 日期 | 时效 | 正文 / 原件 |
|---|---|---|---|---|---|
| [上海市住房和城乡建设管理委员会关于进一步加强本市既有多层住宅加装电梯工程质量安全管理的通知](https://zjw.sh.gov.cn/jsgl/20260813/3962766e701b44238bd9400a24ef6e04.html) | 沪建质安〔2023〕579 号 | 上海市住房和城乡建设管理委员会 | 2026-08-13 | ✓ | [正文](docs/%E5%B7%A5%E7%A8%8B%E5%BB%BA%E8%AE%BE%E7%AE%A1%E7%90%86/%E4%B8%8A%E6%B5%B7%E5%B8%82%E4%BD%8F%E6%88%BF%E5%92%8C%E5%9F%8E%E4%B9%A1%E5%BB%BA%E8%AE%BE%E7%AE%A1%E7%90%86%E5%A7%94%E5%91%98%E4%BC%9A%E5%85%B3%E4%BA%8E%E8%BF%9B%E4%B8%80%E6%AD%A5%E5%8A%A0%E5%BC%BA%E6%9C%AC%E5%B8%82%E6%97%A2%E6%9C%89%E5%A4%9A%E5%B1%82%E4%BD%8F%E5%AE%85%E5%8A%A0%E8%A3%85%E7%94%B5%E6%A2%AF%E5%B7%A5%E7%A8%8B%E8%B4%A8%E9%87%8F%E5%AE%89%E5%85%A8%E7%AE%A1%E7%90%86%E7%9A%84%E9%80%9A%E7%9F%A5.md) · [附表附图](https://zjw.sh.gov.cn/cmsres/8f/8f9c89406c344e2d9cbadca3a1e71d89/65687c45bf8ca6d2bab3aae24c904ca6.pdf) |
| [上海市房屋管理局关于印发《上海市国有土地上征收居住房屋室内装饰装修评估分户报告（示范文本）》的通知](https://www.shanghai.gov.cn/zhengce/detail?businessId=816cfe6c251c4eae84804ab5cf7dcaca&siteId=0013) | 沪房市场〔2026〕125号 | 上海市房屋管理局 | 2026-08-11 | ✓ | [正文](docs/%E6%88%BF%E5%B1%8B%E4%B8%8E%E4%BD%8F%E6%88%BF/%E4%B8%8A%E6%B5%B7%E5%B8%82%E6%88%BF%E5%B1%8B%E7%AE%A1%E7%90%86%E5%B1%80%E5%85%B3%E4%BA%8E%E5%8D%B0%E5%8F%91%E3%80%8A%E4%B8%8A%E6%B5%B7%E5%B8%82%E5%9B%BD%E6%9C%89%E5%9C%9F%E5%9C%B0%E4%B8%8A%E5%BE%81%E6%94%B6%E5%B1%85%E4%BD%8F%E6%88%BF%E5%B1%8B%E5%AE%A4%E5%86%85%E8%A3%85%E9%A5%B0%E8%A3%85%E4%BF%AE%E8%AF%84%E4%BC%B0%E5%88%86%E6%88%B7%E6%8A%A5%E5%91%8A%EF%BC%88%E7%A4%BA%E8%8C%83%E6%96%87%E6%9C%AC%EF%BC%89%E3%80%8B%E7%9A%84%E9%80%9A%E7%9F%A5.md) · [红头PDF](https://www.shanghai.gov.cn/gwk/resource/file?pathname=2/0013/ab/ab1b0c3660004dc2a6cfef11f68b0954/043015616550390bbffd299167a0e392.pdf&filename=%E4%B8%8A%E6%B5%B7%E5%B8%82%E6%88%BF%E5%B1%8B%E7%AE%A1%E7%90%86%E5%B1%80%E5%85%B3%E4%BA%8E%E5%8D%B0%E5%8F%91%E3%80%8A%E4%B8%8A%E6%B5%B7%E5%B8%82%E5%9B%BD%E6%9C%89%E5%9C%9F%E5%9C%B0%E4%B8%8A%E5%BE%81%E6%94%B6%E5%B1%85%E4%BD%8F%E6%88%BF%E5%B1%8B%E5%AE%A4%E5%86%85%E8%A3%85%E9%A5%B0%E8%A3%85%E4%BF%AE%E8%AF%84%E4%BC%B0%E5%88%86%E6%88%B7%E6%8A%A5%E5%91%8A%EF%BC%88%E7%A4%BA%E8%8C%83%E6%96%87%E6%9C%AC%EF%BC%89%E3%80%8B%E7%9A%84%E9%80%9A%E7%9F%A5.pdf) |
| [上海市人民政府办公厅关于印发《上海市城市更新和住房发展“十五五”规划》的通知](https://www.shanghai.gov.cn/zhengce/detail?businessId=f584d873f87045148c7eccce1ae637b3&siteId=0001) | 沪府办发〔2026〕15号 | 上海市人民政府办公厅 | 2026-07-28 | ✓ | [正文](docs/%E6%88%BF%E5%B1%8B%E4%B8%8E%E4%BD%8F%E6%88%BF/%E4%B8%8A%E6%B5%B7%E5%B8%82%E4%BA%BA%E6%B0%91%E6%94%BF%E5%BA%9C%E5%8A%9E%E5%85%AC%E5%8E%85%E5%85%B3%E4%BA%8E%E5%8D%B0%E5%8F%91%E3%80%8A%E4%B8%8A%E6%B5%B7%E5%B8%82%E5%9F%8E%E5%B8%82%E6%9B%B4%E6%96%B0%E5%92%8C%E4%BD%8F%E6%88%BF%E5%8F%91%E5%B1%95%E2%80%9C%E5%8D%81%E4%BA%94%E4%BA%94%E2%80%9D%E8%A7%84%E5%88%92%E3%80%8B%E7%9A%84%E9%80%9A%E7%9F%A5.md) · [红头PDF](https://www.shanghai.gov.cn/gwk/resource/file?pathname=2/0001/82/82598f2838c947c08d1d55bc4d86edd9/1712db4521185ca6899a6477c7b163cb.pdf&filename=%E4%B8%8A%E6%B5%B7%E5%B8%82%E4%BA%BA%E6%B0%91%E6%94%BF%E5%BA%9C%E5%8A%9E%E5%85%AC%E5%8E%85%E5%85%B3%E4%BA%8E%E5%8D%B0%E5%8F%91%E3%80%8A%E4%B8%8A%E6%B5%B7%E5%B8%82%E5%9F%8E%E5%B8%82%E6%9B%B4%E6%96%B0%E5%92%8C%E4%BD%8F%E6%88%BF%E5%8F%91%E5%B1%95%E2%80%9C%E5%8D%81%E4%BA%94%E4%BA%94%E2%80%9D%E8%A7%84%E5%88%92%E3%80%8B%E7%9A%84%E9%80%9A%E7%9F%A5.pdf) |
| [闵行区人民政府关于印发《闵行区城市更新“十五五”规划》的通知](https://www.shanghai.gov.cn/zhengce/detail?businessId=9ce0e2a0-ff5a-41c8-9e91-341424340c4c&siteId=0079) | 闵府发〔2026〕26号 | 上海市闵行区人民政府 | 2026-07-28 | ✓ | [正文](docs/%E5%9F%8E%E5%B8%82%E6%9B%B4%E6%96%B0%E4%B8%8E%E5%8E%86%E5%8F%B2%E4%BF%9D%E6%8A%A4/%E9%97%B5%E8%A1%8C%E5%8C%BA%E4%BA%BA%E6%B0%91%E6%94%BF%E5%BA%9C%E5%85%B3%E4%BA%8E%E5%8D%B0%E5%8F%91%E3%80%8A%E9%97%B5%E8%A1%8C%E5%8C%BA%E5%9F%8E%E5%B8%82%E6%9B%B4%E6%96%B0%E2%80%9C%E5%8D%81%E4%BA%94%E4%BA%94%E2%80%9D%E8%A7%84%E5%88%92%E3%80%8B%E7%9A%84%E9%80%9A%E7%9F%A5.md) · [红头PDF](https://www.shanghai.gov.cn/gwk/resource/file?pathname=2/0079/29/293a725ad7104a5b8b2da08efdd3efa5/a01b070489f1fab98cd05d8e393257c8.pdf&filename=%E9%97%B5%E8%A1%8C%E5%8C%BA%E4%BA%BA%E6%B0%91%E6%94%BF%E5%BA%9C%E5%85%B3%E4%BA%8E%E5%8D%B0%E5%8F%91%E3%80%8A%E9%97%B5%E8%A1%8C%E5%8C%BA%E5%9F%8E%E5%B8%82%E6%9B%B4%E6%96%B0%E2%80%9C%E5%8D%81%E4%BA%94%E4%BA%94%E2%80%9D%E8%A7%84%E5%88%92%E3%80%8B%E7%9A%84%E9%80%9A%E7%9F%A5.pdf) |
| [黄浦区人民政府办公室关于印发 《黄浦区城市更新“十五五”规划》的通知](https://www.shanghai.gov.cn/zhengce/detail?businessId=1183fecf-8084-4ada-9aef-3115e4f9deb6&siteId=0071) | 黄府办发〔2026〕12号 | 上海市黄浦区人民政府办公室 | 2026-07-02 | ✓ | [正文](docs/%E5%9F%8E%E5%B8%82%E6%9B%B4%E6%96%B0%E4%B8%8E%E5%8E%86%E5%8F%B2%E4%BF%9D%E6%8A%A4/%E9%BB%84%E6%B5%A6%E5%8C%BA%E4%BA%BA%E6%B0%91%E6%94%BF%E5%BA%9C%E5%8A%9E%E5%85%AC%E5%AE%A4%E5%85%B3%E4%BA%8E%E5%8D%B0%E5%8F%91%20%E3%80%8A%E9%BB%84%E6%B5%A6%E5%8C%BA%E5%9F%8E%E5%B8%82%E6%9B%B4%E6%96%B0%E2%80%9C%E5%8D%81%E4%BA%94%E4%BA%94%E2%80%9D%E8%A7%84%E5%88%92%E3%80%8B%E7%9A%84%E9%80%9A%E7%9F%A5.md) · [红头PDF](https://www.shanghai.gov.cn/gwk/resource/file?pathname=2/0071/db/dbdc2ddb5d8e493086bbac79c2771901/e9abdd25ca25e503e1044dcab4991cf3.pdf&filename=%E9%BB%84%E6%B5%A6%E5%8C%BA%E4%BA%BA%E6%B0%91%E6%94%BF%E5%BA%9C%E5%8A%9E%E5%85%AC%E5%AE%A4%E5%85%B3%E4%BA%8E%E5%8D%B0%E5%8F%91+%E3%80%8A%E9%BB%84%E6%B5%A6%E5%8C%BA%E5%9F%8E%E5%B8%82%E6%9B%B4%E6%96%B0%E2%80%9C%E5%8D%81%E4%BA%94%E4%BA%94%E2%80%9D%E8%A7%84%E5%88%92%E3%80%8B%E7%9A%84%E9%80%9A%E7%9F%A5.pdf) · [附表附图](https://www.shanghai.gov.cn/gwk/resource/file?pathname=2/0071/14/1498c4daf3fa453ca2210be92257427d/1c4142295c8932eb5a76b595cf1b504a.pdf&filename=%E9%BB%84%E6%B5%A6%E5%8C%BA%E4%BA%BA%E6%B0%91%E6%94%BF%E5%BA%9C%E5%8A%9E%E5%85%AC%E5%AE%A4%E5%85%B3%E4%BA%8E%E5%8D%B0%E5%8F%91%E3%80%8A%E9%BB%84%E6%B5%A6%E5%8C%BA%E5%9F%8E%E5%B8%82%E6%9B%B4%E6%96%B0%E2%80%9C%E5%8D%81%E4%BA%94%E4%BA%94%E2%80%9D%E8%A7%84%E5%88%92%E3%80%8B%E7%9A%84%E9%80%9A%E7%9F%A5.pdf) |
| [宝山区既有多层住宅加装电梯设计方案公示工作的指导意见](https://www.shanghai.gov.cn/zhengce/detail?businessId=525719c9-eb5a-4ee0-b209-bcffce063a02&siteId=0078) | 宝规划资源〔2026〕1号 | 上海市宝山区规划和自然资源局 | 2026-06-08 | ✓ | [正文](docs/%E6%88%BF%E5%B1%8B%E4%B8%8E%E4%BD%8F%E6%88%BF/%E5%AE%9D%E5%B1%B1%E5%8C%BA%E6%97%A2%E6%9C%89%E5%A4%9A%E5%B1%82%E4%BD%8F%E5%AE%85%E5%8A%A0%E8%A3%85%E7%94%B5%E6%A2%AF%E8%AE%BE%E8%AE%A1%E6%96%B9%E6%A1%88%E5%85%AC%E7%A4%BA%E5%B7%A5%E4%BD%9C%E7%9A%84%E6%8C%87%E5%AF%BC%E6%84%8F%E8%A7%81.md) · [红头PDF](https://www.shanghai.gov.cn/gwk/resource/file?pathname=2/0078/2b/2bcc851ab01449df9713ff232063071c/a71f88478dff286c73d238ba47002442.pdf&filename=%E5%AE%9D%E5%B1%B1%E5%8C%BA%E6%97%A2%E6%9C%89%E5%A4%9A%E5%B1%82%E4%BD%8F%E5%AE%85%E5%8A%A0%E8%A3%85%E7%94%B5%E6%A2%AF%E8%AE%BE%E8%AE%A1%E6%96%B9%E6%A1%88%E5%85%AC%E7%A4%BA%E5%B7%A5%E4%BD%9C%E7%9A%84%E6%8C%87%E5%AF%BC%E6%84%8F%E8%A7%81.pdf) |
| [上海市住房和城乡建设管理委员会、上海市市场监督管理局、上海市房屋管理局、上海市装饰装修行业协会、上海市室内装饰行业协会关于推行使用《上海市住宅装饰装修施工合同示范文本》的通知](https://www.shanghai.gov.cn/zhengce/detail?businessId=69f5f927482d43998de868d718e121dc&siteId=0011) | 沪建城管联〔2026〕164号 | 上海市住房和城乡建设管理委员会 | 2026-05-09 | ✓ | [正文](docs/%E6%88%BF%E5%B1%8B%E4%B8%8E%E4%BD%8F%E6%88%BF/%E4%B8%8A%E6%B5%B7%E5%B8%82%E4%BD%8F%E6%88%BF%E5%92%8C%E5%9F%8E%E4%B9%A1%E5%BB%BA%E8%AE%BE%E7%AE%A1%E7%90%86%E5%A7%94%E5%91%98%E4%BC%9A%E3%80%81%E4%B8%8A%E6%B5%B7%E5%B8%82%E5%B8%82%E5%9C%BA%E7%9B%91%E7%9D%A3%E7%AE%A1%E7%90%86%E5%B1%80%E3%80%81%E4%B8%8A%E6%B5%B7%E5%B8%82%E6%88%BF%E5%B1%8B%E7%AE%A1%E7%90%86%E5%B1%80%E3%80%81%E4%B8%8A%E6%B5%B7%E5%B8%82%E8%A3%85%E9%A5%B0%E8%A3%85%E4%BF%AE%E8%A1%8C%E4%B8%9A%E5%8D%8F%E4%BC%9A%E3%80%81%E4%B8%8A%E6%B5%B7.md) · [红头PDF](https://www.shanghai.gov.cn/gwk/resource/file?pathname=2/0011/9f/9f2699e190ed499e81800c32ca1f0e41/466a8c479d5fbda8ff957dc2ce2d4c0b.pdf&filename=%E4%B8%8A%E6%B5%B7%E5%B8%82%E4%BD%8F%E6%88%BF%E5%92%8C%E5%9F%8E%E4%B9%A1%E5%BB%BA%E8%AE%BE%E7%AE%A1%E7%90%86%E5%A7%94%E5%91%98%E4%BC%9A%E3%80%81%E4%B8%8A%E6%B5%B7%E5%B8%82%E5%B8%82%E5%9C%BA%E7%9B%91%E7%9D%A3%E7%AE%A1%E7%90%86%E5%B1%80%E3%80%81%E4%B8%8A%E6%B5%B7%E5%B8%82%E6%88%BF%E5%B1%8B%E7%AE%A1%E7%90%86%E5%B1%80%E3%80%81%E4%B8%8A%E6%B5%B7%E5%B8%82%E8%A3%85%E9%A5%B0%E8%A3%85%E4%BF%AE%E8%A1%8C%E4%B8%9A%E5%8D%8F%E4%BC%9A%E3%80%81%E4%B8%8A%E6%B5%B7%E5%B8%82%E5%AE%A4%E5%86%85%E8%A3%85%E9%A5%B0%E8%A1%8C%E4%B8%9A%E5%8D%8F%E4%BC%9A%E5%85%B3%E4%BA%8E%E6%8E%A8%E8%A1%8C%E4%BD%BF%E7%94%A8%E3%80%8A%E4%B8%8A%E6%B5%B7%E5%B8%82%E4%BD%8F%E5%AE%85%E8%A3%85%E9%A5%B0%E8%A3%85%E4%BF%AE%E6%96%BD%E5%B7%A5%E5%90%88%E5%90%8C%E7%A4%BA%E8%8C%83%E6%96%87%E6%9C%AC%E3%80%8B%E7%9A%84%E9%80%9A%E7%9F%A5.pdf) · [附表附图](https://www.shanghai.gov.cn/gwk/resource/file?pathname=2/0011/a8/a8a5bd64710046fbb668e7006df94aca/8968879993ac73d175e152063e5a4c36.pdf&filename=%E4%B8%8A%E6%B5%B7%E5%B8%82%E4%BD%8F%E5%AE%85%E8%A3%85%E9%A5%B0%E8%A3%85%E4%BF%AE%E6%96%BD%E5%B7%A5%E5%90%88%E5%90%8C%E7%A4%BA%E8%8C%83%E6%96%87%E6%9C%AC.pdf) |
| [关于印发《2026年上海市城市更新规划资源行动方案》的通知](https://ghzyj.sh.gov.cn/zcwj/zhl/20260312/9c7de5f29d9142858506fa3d80c27c2b.html) | - | 上海市规划和自然资源局 | 2026-03-12 | ✓ | [正文](docs/%E5%9F%8E%E5%B8%82%E6%9B%B4%E6%96%B0%E4%B8%8E%E5%8E%86%E5%8F%B2%E4%BF%9D%E6%8A%A4/%E5%85%B3%E4%BA%8E%E5%8D%B0%E5%8F%91%E3%80%8A2026%E5%B9%B4%E4%B8%8A%E6%B5%B7%E5%B8%82%E5%9F%8E%E5%B8%82%E6%9B%B4%E6%96%B0%E8%A7%84%E5%88%92%E8%B5%84%E6%BA%90%E8%A1%8C%E5%8A%A8%E6%96%B9%E6%A1%88%E3%80%8B%E7%9A%84%E9%80%9A%E7%9F%A5.md) |

[→ 查看该主题全部条目](index/06-城市更新与历史保护.md)

### 房屋与住宅

| 标题 | 文号 | 发布机关 | 日期 | 时效 | 正文 / 原件 |
|---|---|---|---|---|---|
| [关于印发《虹口区住宅小区物业服务评价激励实施意见》的通知](https://www.shanghai.gov.cn/zhengce/detail?businessId=f3a3d159-da79-4d3f-9f09-6f0133bf34a9&siteId=0076) | 虹房管规〔2026〕1号 | 上海市虹口区住房保障和房屋管理局 | 2026-07-23 | ✓ | [正文](docs/%E6%88%BF%E5%B1%8B%E4%B8%8E%E4%BD%8F%E6%88%BF/%E5%85%B3%E4%BA%8E%E5%8D%B0%E5%8F%91%E3%80%8A%E8%99%B9%E5%8F%A3%E5%8C%BA%E4%BD%8F%E5%AE%85%E5%B0%8F%E5%8C%BA%E7%89%A9%E4%B8%9A%E6%9C%8D%E5%8A%A1%E8%AF%84%E4%BB%B7%E6%BF%80%E5%8A%B1%E5%AE%9E%E6%96%BD%E6%84%8F%E8%A7%81%E3%80%8B%E7%9A%84%E9%80%9A%E7%9F%A5.md) · [红头PDF](https://www.shanghai.gov.cn/gwk/resource/file?pathname=2/0076/70/70a59f76c82448b6b2eac567b209f5ee/2383f9aa0a3186f701376646db32d2b6.pdf&filename=%E5%85%B3%E4%BA%8E%E5%8D%B0%E5%8F%91%E3%80%8A%E8%99%B9%E5%8F%A3%E5%8C%BA%E4%BD%8F%E5%AE%85%E5%B0%8F%E5%8C%BA%E7%89%A9%E4%B8%9A%E6%9C%8D%E5%8A%A1%E8%AF%84%E4%BB%B7%E6%BF%80%E5%8A%B1%E5%AE%9E%E6%96%BD%E6%84%8F%E8%A7%81%E3%80%8B%E7%9A%84%E9%80%9A%E7%9F%A5.pdf) · [附表附图](https://www.shanghai.gov.cn/gwk/resource/file?pathname=2/0076/35/35a7e870ec7a4b5d8022ef556c5dcd39/8e076690f46cdaf9ee66933c157c4908.pdf&filename=%E9%99%84%E4%BB%B65-%E8%99%B9%E6%88%BF%E7%AE%A1%E8%A7%84%E3%80%942026%E3%80%951%E5%8F%B7-%E5%85%B3%E4%BA%8E%E5%8D%B0%E5%8F%91%E3%80%8A%E8%99%B9%E5%8F%A3%E5%8C%BA%E4%BD%8F%E5%AE%85%E5%B0%8F%E5%8C%BA%E7%89%A9%E4%B8%9A%E6%9C%8D%E5%8A%A1%E8%AF%84%E4%BB%B7%E6%BF%80%E5%8A%B1%E5%AE%9E%E6%96%BD%E6%84%8F%E8%A7%81%E3%80%8B%E7%9A%84%E9%80%9A%E7%9F%A50721.pdf)（5 个） |
| [关于印发《关于建立住宅小区业主委员会秘书制度的实施意见（试行）》的通知](https://www.shanghai.gov.cn/zhengce/detail?businessId=3eecb53566cf4e0c86869199d4bd0b56&siteId=0013) | 沪房物业〔2026〕84号 | 上海市房屋管理局 | 2026-06-04 | ✓ | [正文](docs/%E6%88%BF%E5%B1%8B%E4%B8%8E%E4%BD%8F%E6%88%BF/%E5%85%B3%E4%BA%8E%E5%8D%B0%E5%8F%91%E3%80%8A%E5%85%B3%E4%BA%8E%E5%BB%BA%E7%AB%8B%E4%BD%8F%E5%AE%85%E5%B0%8F%E5%8C%BA%E4%B8%9A%E4%B8%BB%E5%A7%94%E5%91%98%E4%BC%9A%E7%A7%98%E4%B9%A6%E5%88%B6%E5%BA%A6%E7%9A%84%E5%AE%9E%E6%96%BD%E6%84%8F%E8%A7%81%EF%BC%88%E8%AF%95%E8%A1%8C%EF%BC%89%E3%80%8B%E7%9A%84%E9%80%9A%E7%9F%A5.md) · [红头PDF](https://www.shanghai.gov.cn/gwk/resource/file?pathname=2/0013/13/135e3c21d12a4024a9b04356bfc3b502/ad9c6797ed6224d153116daf095b1b00.pdf&filename=%E5%85%B3%E4%BA%8E%E5%8D%B0%E5%8F%91%E3%80%8A%E5%85%B3%E4%BA%8E%E5%BB%BA%E7%AB%8B%E4%BD%8F%E5%AE%85%E5%B0%8F%E5%8C%BA%E4%B8%9A%E4%B8%BB%E5%A7%94%E5%91%98%E4%BC%9A%E7%A7%98%E4%B9%A6%E5%88%B6%E5%BA%A6%E7%9A%84%E5%AE%9E%E6%96%BD%E6%84%8F%E8%A7%81%EF%BC%88%E8%AF%95%E8%A1%8C%EF%BC%89%E3%80%8B%E7%9A%84%E9%80%9A%E7%9F%A5.pdf) |
| [关于印发《关于完善本市住宅小区业主大会、业主委员会规范化建设的实施意见》的通知](https://www.shanghai.gov.cn/zhengce/detail?businessId=b81adff0389b4a7c9ecb99bc0b3594dc&siteId=0013) | 沪房物业〔2026〕36号 | 上海市房屋管理局 | 2026-03-30 | ✓ | [正文](docs/%E6%88%BF%E5%B1%8B%E4%B8%8E%E4%BD%8F%E6%88%BF/%E5%85%B3%E4%BA%8E%E5%8D%B0%E5%8F%91%E3%80%8A%E5%85%B3%E4%BA%8E%E5%AE%8C%E5%96%84%E6%9C%AC%E5%B8%82%E4%BD%8F%E5%AE%85%E5%B0%8F%E5%8C%BA%E4%B8%9A%E4%B8%BB%E5%A4%A7%E4%BC%9A%E3%80%81%E4%B8%9A%E4%B8%BB%E5%A7%94%E5%91%98%E4%BC%9A%E8%A7%84%E8%8C%83%E5%8C%96%E5%BB%BA%E8%AE%BE%E7%9A%84%E5%AE%9E%E6%96%BD%E6%84%8F%E8%A7%81%E3%80%8B%E7%9A%84%E9%80%9A%E7%9F%A5.md) · [红头PDF](https://www.shanghai.gov.cn/gwk/resource/file?pathname=2/0013/75/75e56133e17748a5807dfc2745c5b888/3d323e85e2c5c46df94b73df3926e52e.pdf&filename=%E5%85%B3%E4%BA%8E%E5%8D%B0%E5%8F%91%E3%80%8A%E5%85%B3%E4%BA%8E%E5%AE%8C%E5%96%84%E6%9C%AC%E5%B8%82%E4%BD%8F%E5%AE%85%E5%B0%8F%E5%8C%BA%E4%B8%9A%E4%B8%BB%E5%A4%A7%E4%BC%9A%E3%80%81%E4%B8%9A%E4%B8%BB%E5%A7%94%E5%91%98%E4%BC%9A%E8%A7%84%E8%8C%83%E5%8C%96%E5%BB%BA%E8%AE%BE%E7%9A%84%E5%AE%9E%E6%96%BD%E6%84%8F%E8%A7%81%E3%80%8B%E7%9A%84%E9%80%9A%E7%9F%A5.pdf) |
| [关于印发《关于住宅小区业主大会账户资金及管理责任年度审计工作的实施意见》的通知](https://www.shanghai.gov.cn/zhengce/detail?businessId=fdf49964c58143fb9ef776f45e716c96&siteId=0013) | 沪房规范〔2025〕9号 | 上海市房屋管理局 | 2025-12-31 | ✓ | [正文](docs/%E6%88%BF%E5%B1%8B%E4%B8%8E%E4%BD%8F%E6%88%BF/%E5%85%B3%E4%BA%8E%E5%8D%B0%E5%8F%91%E3%80%8A%E5%85%B3%E4%BA%8E%E4%BD%8F%E5%AE%85%E5%B0%8F%E5%8C%BA%E4%B8%9A%E4%B8%BB%E5%A4%A7%E4%BC%9A%E8%B4%A6%E6%88%B7%E8%B5%84%E9%87%91%E5%8F%8A%E7%AE%A1%E7%90%86%E8%B4%A3%E4%BB%BB%E5%B9%B4%E5%BA%A6%E5%AE%A1%E8%AE%A1%E5%B7%A5%E4%BD%9C%E7%9A%84%E5%AE%9E%E6%96%BD%E6%84%8F%E8%A7%81%E3%80%8B%E7%9A%84%E9%80%9A%E7%9F%A5.md) · [红头PDF](https://www.shanghai.gov.cn/gwk/resource/file?pathname=2/0013/8f/8f84151853d546b796eb3fa750fa4443/a8bd831037cdb7b5e9a9988014d97428.pdf&filename=%E5%85%B3%E4%BA%8E%E5%8D%B0%E5%8F%91%E3%80%8A%E5%85%B3%E4%BA%8E%E4%BD%8F%E5%AE%85%E5%B0%8F%E5%8C%BA%E4%B8%9A%E4%B8%BB%E5%A4%A7%E4%BC%9A%E8%B4%A6%E6%88%B7%E8%B5%84%E9%87%91%E5%8F%8A%E7%AE%A1%E7%90%86%E8%B4%A3%E4%BB%BB%E5%B9%B4%E5%BA%A6%E5%AE%A1%E8%AE%A1%E5%B7%A5%E4%BD%9C%E7%9A%84%E5%AE%9E%E6%96%BD%E6%84%8F%E8%A7%81%E3%80%8B%E7%9A%84%E9%80%9A%E7%9F%A5.pdf) · [附表附图](https://www.shanghai.gov.cn/cmsres/policy_resources/fdf49964c58143fb9ef776f45e716c96/facff244b657403d9725b404ae7d9f6a/%E5%AE%A1%E8%AE%A1%E7%BB%93%E6%9E%9C%E5%85%AC%E5%91%8A%E6%A0%B7%E5%BC%A0.docx) |
| [上海市房屋管理局关于印发《上海市住宅小区公共收益管理办法》的通知](https://www.shanghai.gov.cn/zhengce/detail?businessId=8b8ad0526ae94db8a6c61b8aa6caf0c2&siteId=0013) | 沪房规范〔2025〕8号 | 上海市房屋管理局 | 2025-12-31 | ✓ | [正文](docs/%E6%88%BF%E5%B1%8B%E4%B8%8E%E4%BD%8F%E6%88%BF/%E4%B8%8A%E6%B5%B7%E5%B8%82%E6%88%BF%E5%B1%8B%E7%AE%A1%E7%90%86%E5%B1%80%E5%85%B3%E4%BA%8E%E5%8D%B0%E5%8F%91%E3%80%8A%E4%B8%8A%E6%B5%B7%E5%B8%82%E4%BD%8F%E5%AE%85%E5%B0%8F%E5%8C%BA%E5%85%AC%E5%85%B1%E6%94%B6%E7%9B%8A%E7%AE%A1%E7%90%86%E5%8A%9E%E6%B3%95%E3%80%8B%E7%9A%84%E9%80%9A%E7%9F%A5.md) · [红头PDF](https://www.shanghai.gov.cn/gwk/resource/file?pathname=2/0013/5d/5dbcd8de658549f09c5dbefe20021657/37f950ec41355edf1406134c5171362c.pdf&filename=%E4%B8%8A%E6%B5%B7%E5%B8%82%E6%88%BF%E5%B1%8B%E7%AE%A1%E7%90%86%E5%B1%80%E5%85%B3%E4%BA%8E%E5%8D%B0%E5%8F%91%E3%80%8A%E4%B8%8A%E6%B5%B7%E5%B8%82%E4%BD%8F%E5%AE%85%E5%B0%8F%E5%8C%BA%E5%85%AC%E5%85%B1%E6%94%B6%E7%9B%8A%E7%AE%A1%E7%90%86%E5%8A%9E%E6%B3%95%E3%80%8B%E7%9A%84%E9%80%9A%E7%9F%A5.pdf) |
| [关于印发《闵行区老旧公房小区物业管理共建活动实施办法》的通知](https://www.shanghai.gov.cn/zhengce/detail?businessId=eb985076-e7f0-4931-95ca-1abc91ac9f67&siteId=0079) | 闵房管规字〔2025〕1号 | 上海市闵行区住房保障和房屋管理局 | 2025-11-28 | ✓ | [正文](docs/%E6%88%BF%E5%B1%8B%E4%B8%8E%E4%BD%8F%E6%88%BF/%E5%85%B3%E4%BA%8E%E5%8D%B0%E5%8F%91%E3%80%8A%E9%97%B5%E8%A1%8C%E5%8C%BA%E8%80%81%E6%97%A7%E5%85%AC%E6%88%BF%E5%B0%8F%E5%8C%BA%E7%89%A9%E4%B8%9A%E7%AE%A1%E7%90%86%E5%85%B1%E5%BB%BA%E6%B4%BB%E5%8A%A8%E5%AE%9E%E6%96%BD%E5%8A%9E%E6%B3%95%E3%80%8B%E7%9A%84%E9%80%9A%E7%9F%A5.md) · [附表附图](https://www.shanghai.gov.cn/cmsres/policy_resources/eb985076-e7f0-4931-95ca-1abc91ac9f67/bc4957906f664c479a6eeade241e71ec/1%E5%8F%B7%E9%99%84%E4%BB%B6%EF%BC%9A1.1%20%E5%85%B3%E4%BA%8E%E5%8A%A0%E5%85%A5%E9%97%B5%E8%A1%8C%E5%8C%BA%E7%89%A9%E4%B8%9A%E7%AE%A1%E7%90%86%E5%85%B1%E5%BB%BA%E5%B0%8F%E5%8C%BA%E7%9A%84%E7%94%B3%E8%AF%B7.xls)（5 个） |
| [关于加强本市住宅物业管理与城管执法群租治理联动工作的通知](https://www.shanghai.gov.cn/zhengce/detail?businessId=41ed0c26bf464758af5c4620e2e85129&siteId=0013) | 沪房市场〔2025〕179号 | 上海市房屋管理局 | 2025-10-23 | ✓ | [正文](docs/%E6%88%BF%E5%B1%8B%E4%B8%8E%E4%BD%8F%E6%88%BF/%E5%85%B3%E4%BA%8E%E5%8A%A0%E5%BC%BA%E6%9C%AC%E5%B8%82%E4%BD%8F%E5%AE%85%E7%89%A9%E4%B8%9A%E7%AE%A1%E7%90%86%E4%B8%8E%E5%9F%8E%E7%AE%A1%E6%89%A7%E6%B3%95%E7%BE%A4%E7%A7%9F%E6%B2%BB%E7%90%86%E8%81%94%E5%8A%A8%E5%B7%A5%E4%BD%9C%E7%9A%84%E9%80%9A%E7%9F%A5.md) · [红头PDF](https://www.shanghai.gov.cn/gwk/resource/file?pathname=2/0013/72/7244776d9fb6498a83a6ecea1d7af328/f64e2ed6eb77c4581e3f8b3d2675a49b.pdf&filename=%E5%85%B3%E4%BA%8E%E5%8A%A0%E5%BC%BA%E6%9C%AC%E5%B8%82%E4%BD%8F%E5%AE%85%E7%89%A9%E4%B8%9A%E7%AE%A1%E7%90%86%E4%B8%8E%E5%9F%8E%E7%AE%A1%E6%89%A7%E6%B3%95%E7%BE%A4%E7%A7%9F%E6%B2%BB%E7%90%86%E8%81%94%E5%8A%A8%E5%B7%A5%E4%BD%9C%E7%9A%84%E9%80%9A%E7%9F%A5.pdf) · [附表附图](https://www.shanghai.gov.cn/cmsres/policy_resources/41ed0c26bf464758af5c4620e2e85129/877f517378394c1083b20701e7688619/________%E5%B0%8F%E5%8C%BA%E5%B7%B2%E6%95%B4%E6%94%B9%E6%95%B4%E6%B2%BB%E5%AE%8C%E6%AF%95%E7%BE%A4%E7%A7%9F%E6%88%BF%E6%B8%85%E5%8D%95.docx) |
| [关于印发《普陀区住宅小区物业服务达标激励机制的实施意见》的通知](https://www.shanghai.gov.cn/zhengce/detail?businessId=0075197540&siteId=0075) | 普房管规范〔2025〕1号 | 上海市普陀区住房保障和房屋管理局 | 2025-07-15 | ✓ | [正文](docs/%E6%88%BF%E5%B1%8B%E4%B8%8E%E4%BD%8F%E6%88%BF/%E5%85%B3%E4%BA%8E%E5%8D%B0%E5%8F%91%E3%80%8A%E6%99%AE%E9%99%80%E5%8C%BA%E4%BD%8F%E5%AE%85%E5%B0%8F%E5%8C%BA%E7%89%A9%E4%B8%9A%E6%9C%8D%E5%8A%A1%E8%BE%BE%E6%A0%87%E6%BF%80%E5%8A%B1%E6%9C%BA%E5%88%B6%E7%9A%84%E5%AE%9E%E6%96%BD%E6%84%8F%E8%A7%81%E3%80%8B%E7%9A%84%E9%80%9A%E7%9F%A5.md) · [红头PDF](https://www.shanghai.gov.cn/gwk/resource/file?pathname=2/0075/97/976b561943ce442ba369b73288a807d6/daf008845d46c5a04f8fd787a06eefde.pdf&filename=%E5%85%B3%E4%BA%8E%E5%8D%B0%E5%8F%91%E3%80%8A%E6%99%AE%E9%99%80%E5%8C%BA%E4%BD%8F%E5%AE%85%E5%B0%8F%E5%8C%BA%E7%89%A9%E4%B8%9A%E6%9C%8D%E5%8A%A1%E8%BE%BE%E6%A0%87%E6%BF%80%E5%8A%B1%E6%9C%BA%E5%88%B6%E7%9A%84%E5%AE%9E%E6%96%BD%E6%84%8F%E8%A7%81%E3%80%8B%E7%9A%84%E9%80%9A%E7%9F%A5.pdf) |

[→ 查看该主题全部条目](index/05-房屋与住房.md)

## 目录结构

```
Shanghai-Gov-Docs-Index/
├── README.md                 本文件（概览 + 渠道地图 + 速查）
├── index/                    按分类的完整索引（每条含官方链接）
├── docs/                     核心文件官方正文全文（Markdown，按分类分目录）
├── data/
│   ├── gov_docs.csv          全量清单（本库唯一数据源）
│   ├── raw_flk_sh_laws.tsv   上海地方性法规原始抓取（国家法律法规数据库）
│   ├── flk_fulltext/         地方性法规官方正文（纯文本，按 bbbs 命名）
│   ├── raw_gz_rules.tsv      市政府规章库原始抓取
│   ├── raw_zjw_gfxwj.tsv     市住建委规范性文件原始抓取
│   ├── raw_shrd_laws.tsv     上海人大「法规公布」原始抓取
│   └── raw_policy_all.json   统一政策平台原始抓取（10,518 条，未入库）
├── attachments/              原件（PDF/PNG），默认不提交；fetch_assets.py --download 生成
├── channels.py               官方渠道地图常量（16 区入口 + 已失效入口）
├── classify.py               主题分类与相关性判定规则
├── common.py                 抓取工具（零第三方依赖）
├── scrape_policy.py          抓统一政策发布平台全量
├── scrape_flk.py             抓上海地方性法规 + 官方正文（国家法律法规数据库）
├── scrape_shrd.py            抓上海人大「法规公布」栏目
├── build_docs_index.py       五源合并 → data/gov_docs.csv
├── fetch_fulltext.py         抓核心文件官方正文 → docs/
├── fetch_assets.py           抓红头 PDF / 附表附图 / 封面 直链（--download 可落盘）
├── build_readme.py           生成 README.md 与 index/
├── audit_validity.py         时效复核：从正文判现行有效/已届满/已废止
├── check_links.py            链接批量巡检
└── push_via_api.py           走 GitHub REST API 推送（git 443 不通时用）
```

## 怎么用 / 怎么维护

**查文件**：先看上面的分类索引，或直接搜 `data/gov_docs.csv`。

**要全文**：`docs/` 下按分类存放，文件名即标题。全量回采政府公开正文（极少数页面已下架或无正文的来源仅给官方链接）。

**重建流程**（需要联网）：

```bash
python scrape_policy.py        # 1. 抓统一政策平台全量（约 3 分钟）
python build_docs_index.py     # 2. 三源合并去重 → data/gov_docs.csv
python fetch_fulltext.py       # 3. 抓核心文件正文 → docs/（约 8 分钟）
python build_readme.py         # 4. 生成 README 与索引
python check_links.py          # 5. 巡检链接
```

**加新文件**：不要直接改 README —— 改 `data/gov_docs.csv` 后重跑 `build_readme.py`，否则下次生成会被冲掉。若某文件未被自动筛出，在 `classify.py` 的关键词表里补词。

## 数据来源与法律说明

**数据来源**（均为上海市官方发布渠道）：

- 上海市人民政府 · 现行市政府规章库：https://www.shanghai.gov.cn/xxzfgzwj/
- 上海市统一政策发布平台：https://www.shanghai.gov.cn/zhengce/list
- 上海市住房和城乡建设管理委员会 · 规范性文件：https://zjw.sh.gov.cn/gfxwj/index.html
- 上海市规划和自然资源局：https://ghzyj.sh.gov.cn/
- 上海市房屋管理局：https://fgj.sh.gov.cn/
- 国家法律法规数据库 · 上海地方性法规：https://flk.npc.gov.cn/
- 上海人大 · 法规公布：https://www.shrd.gov.cn/shrd/fggb/fggb.html
- 上海市人民政府 · 政府信息公开指南：https://www.shanghai.gov.cn/nw49252/index.html

**法律说明**

本库收录的文件属于**具有立法、行政、司法性质的文件**。依《中华人民共和国著作权法》**第五条第一项**，该类文件不适用著作权法，故本库**可全文收录**正文。

这与技术标准的情形不同：《工程建设标准》（GB / JGJ / DGJ08）属**受著作权保护的推荐性技术文件**，在 [Arch-Standards-Index](https://github.com/zhiyao87/Arch-Standards-Index) 中**只收录元数据与官方链接、不收录正文**。两个库的版权处理差异源于此。

正文由脚本自官方公开页面自动提取，可能因页面改版而与发布版本有差异，**请以每份文件中的官方链接为准**。
