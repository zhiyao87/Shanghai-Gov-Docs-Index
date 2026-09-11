# 上海建设工程政府发文索引

上海市 **建筑、规划、工程建设** 领域的**地方性法规**、政府规章与行政规范性文件索引。
只收录**元数据 + 官方链接**，并为有实质约束力的文件附上**官方正文全文**与**红头文件 PDF / 附表附图**直链（可全文收录，见文末法律说明）。

> 配套仓库：[Arch-Standards-Index](https://github.com/zhiyao87/Arch-Standards-Index) —— 上海及全国**工程建设标准**（DGJ08 / GB / JGJ）索引。
> 本库管「政府发文」，标准库管「技术标准」，两者互补。

## 数据概览

| 指标 | 数量 |
|---|---|
| 收录文件总数 | **2618** |
| 其中的核心文件（地方性法规/规章/办法/规定/细则/导则/审查许可规则） | **1054** |
| 已附官方正文全文 | **2612** |
| 已登记红头 PDF / 附表附图 | **0** / **0** |
| 地方性法规（市人大制定，效力最高） | **46** |
| 市级 ／ 区级 ／ 街镇级 ／ 未标注 | 2003 ／ 505 ／ 63 ／ 47 |
| 时间跨度 | 2009 – 2026 |
| 覆盖区 | 16 / 16 个区有收录 |
| 数据抓取日 | 2026-09-11 |

**按来源**

| 来源 | 条数 |
|---|---|
| 统一政策发布平台 | 2436 |
| 市住建委规范性文件 | 91 |
| 市政府规章库 | 51 |
| 国家法律法规数据库（flk.npc.gov.cn） | 40 |

**按文件类型**

| 类型 | 条数 | 已附全文 | 说明 |
|---|---|---|---|
| 通知公告 | 988 | 985 |  |
| 办法 | 448 | 447 | ★ 有实质约束力 |
| 实施意见 | 375 | 374 |  |
| 技术规定与导则 | 181 | 181 | ★ 有实质约束力 |
| 规划与计划 | 157 | 157 |  |
| 规定 | 130 | 130 | ★ 有实质约束力 |
| 实施细则 | 113 | 113 | ★ 有实质约束力 |
| 审查与许可规则 | 82 | 82 | ★ 有实质约束力 |
| 政府规章 | 54 | 54 | ★ 有实质约束力 |
| 地方性法规 | 46 | 45 | ★ 有实质约束力 |
| 其他 | 44 | 44 |  |

**按分类**

| # | 分类 | 条数 | 索引 |
|---|---|---|---|
| 一 | 规划与土地 | 214 | [查看](index/01-规划与土地.md) |
| 二 | 建筑设计与报建 | 30 | [查看](index/02-建筑设计与报建.md) |
| 三 | 工程建设管理 | 1021 | [查看](index/03-工程建设管理.md) |
| 四 | 消防与人防 | 94 | [查看](index/04-消防与人防.md) |
| 五 | 房屋与住房 | 562 | [查看](index/05-房屋与住房.md) |
| 六 | 城市更新与历史保护 | 43 | [查看](index/06-城市更新与历史保护.md) |
| 七 | 绿色低碳与节能 | 55 | [查看](index/07-绿色低碳与节能.md) |
| 八 | 市政与基础设施 | 408 | [查看](index/08-市政与基础设施.md) |
| 九 | 市容绿化与景观 | 174 | [查看](index/09-市容绿化与景观.md) |
| 十 | 建筑垃圾与材料 | 17 | [查看](index/10-建筑垃圾与材料.md) |
| 11 | 街镇级发文（单独成册） | 63 | [查看](index/11-街镇级发文.md) |
| 12 | **主题速查**（屋顶绿化/光伏/绿建/海绵/既有建筑改造） | - | [查看](index/12-主题速查.md) |

## 每条文件都挂三种取用方式

政府发文详情页上其实有**三样**东西，只抓网页正文会丢掉最有用的那部分：

| 取用方式 | 说明 | 已收录 |
|---|---|---|
| **正文** | 网页正文，转为 Markdown 便于检索与全文搜 | 2612 条 |
| **红头PDF** | 盖章红头文件原件，认文号、对版式、报建送审都用它 | 0 条 |
| **附表附图** | 技术规范真正的操作部分（参数表、取值表、图示）——只在附件里 | 0 条 |

**为什么专门标出附表附图**：以《上海市日照分析技术规范》（沪规划资源建〔2021〕437 号）为例，日照计算参数、窗台高度取值、图示全在随文的「附表、附图、附件.pdf」里，**网页正文一个字都没有**。只存正文，等于把这份规范最有用的部分丢了。

各类索引表的「正文 / 原件」列即按 **正文 · 红头PDF · 附表附图** 三种链接并排给出。

> 二进制原件（PDF/PNG）默认**只登记官方直链、不镜像进本仓库**，以免把公开索引撑成 GB 级。需要离线留存就跑 `python fetch_assets.py --download`，原件会落到本地 `attachments/`，并生成 `attachment_manifest.csv` 清单。

### 单独一册：街镇级发文（63 条 / 42 个街镇）

**为什么要把街镇级单独拎出来**：限额以下的小型建设工程，依据往往既不是国标、也不是市里的文件，而是**项目所在街镇自己出的办法**。这类文件在市、区两级栏目里**根本检索不到**，但报建时最能卡人。

| 街镇 / 街道 | 条数 | ｜ | 街镇 / 街道 | 条数 |
|---|---|---|---|---|
| 吴泾镇 | 6 | ｜ | 城桥镇 | 1 |
| 月浦镇 | 4 | ｜ | 塘桥街道办事处 | 1 |
| 古美路街道办事处 | 3 | ｜ | 头桥街道办事处 | 1 |
| 吴淞街道办事处 | 3 | ｜ | 奉浦街道办事处 | 1 |
| 南码头路街道办事处 | 2 | ｜ | 山阳镇 | 1 |
| 周浦镇 | 2 | ｜ | 庄行镇 | 1 |
| 广中路街道办事处 | 2 | ｜ | 张庙街道办事处 | 1 |
| 张江镇 | 2 | ｜ | 新浜镇 | 1 |
| 新虹街道办事处 | 2 | ｜ | 朱家角镇 | 1 |
| 杨行镇 | 2 | ｜ | 永丰街道办事处 | 1 |
| 柘林镇 | 2 | ｜ | 江桥镇 | 1 |
| 罗店镇 | 2 | ｜ | 洋泾街道办事处 | 1 |
| 莘庄镇 | 2 | ｜ | 浦江镇 | 1 |
| 七宝镇 | 1 | ｜ | 港沿镇 | 1 |
| 万祥镇 | 1 | ｜ | 竖新镇 | 1 |
| 东明路街道办事处 | 1 | ｜ | 航头镇 | 1 |
| 书院镇 | 1 | ｜ | 赵巷镇 | 1 |
| 南桥镇 | 1 | ｜ | 金汇镇 | 1 |
| 友谊路街道办事处 | 1 | ｜ | 金泽镇 | 1 |
| 向化镇 | 1 | ｜ | 长寿路街道办事处 | 1 |
| 四川北路街道办事处 | 1 | ｜ | 高行镇 | 1 |

[→ 查看街镇级全部条目](index/11-街镇级发文.md)

其中「限额以下 / 小型建设工程」专题共 **16 份**，各街镇一套，**用前先确认项目所属街镇**：

| 街镇 | 标题 | 发布日期 | 正文 / 原件 |
|---|---|---|---|
| 张江镇 | [关于废止《张江镇限额以下小型建设工程管理办法（试行）》的通知](https://www.shanghai.gov.cn/zhengce/detail?businessId=0070350765&siteId=0070) | 2026-01-22 | [正文](docs/%E5%B7%A5%E7%A8%8B%E5%BB%BA%E8%AE%BE%E7%AE%A1%E7%90%86/%E5%85%B3%E4%BA%8E%E5%BA%9F%E6%AD%A2%E3%80%8A%E5%BC%A0%E6%B1%9F%E9%95%87%E9%99%90%E9%A2%9D%E4%BB%A5%E4%B8%8B%E5%B0%8F%E5%9E%8B%E5%BB%BA%E8%AE%BE%E5%B7%A5%E7%A8%8B%E7%AE%A1%E7%90%86%E5%8A%9E%E6%B3%95%EF%BC%88%E8%AF%95%E8%A1%8C%EF%BC%89%E3%80%8B%E7%9A%84%E9%80%9A%E7%9F%A5.md) |
| 庄行镇 | [关于调整庄行镇小型建设工程项目管理实施意见的通知](https://www.shanghai.gov.cn/zhengce/detail?businessId=00843751&siteId=0084) | 2026-01-09 | [正文](docs/%E5%B7%A5%E7%A8%8B%E5%BB%BA%E8%AE%BE%E7%AE%A1%E7%90%86/%E5%85%B3%E4%BA%8E%E8%B0%83%E6%95%B4%E5%BA%84%E8%A1%8C%E9%95%87%E5%B0%8F%E5%9E%8B%E5%BB%BA%E8%AE%BE%E5%B7%A5%E7%A8%8B%E9%A1%B9%E7%9B%AE%E7%AE%A1%E7%90%86%E5%AE%9E%E6%96%BD%E6%84%8F%E8%A7%81%E7%9A%84%E9%80%9A%E7%9F%A5.md) |
| 奉浦街道办事处 | [关于印发《上海市奉贤区奉浦街道小型建设工程项目管理实施办法》的通知](https://www.shanghai.gov.cn/zhengce/detail?businessId=00843456&siteId=0084) | 2025-11-22 | [正文](docs/%E5%B7%A5%E7%A8%8B%E5%BB%BA%E8%AE%BE%E7%AE%A1%E7%90%86/%E5%85%B3%E4%BA%8E%E5%8D%B0%E5%8F%91%E3%80%8A%E4%B8%8A%E6%B5%B7%E5%B8%82%E5%A5%89%E8%B4%A4%E5%8C%BA%E5%A5%89%E6%B5%A6%E8%A1%97%E9%81%93%E5%B0%8F%E5%9E%8B%E5%BB%BA%E8%AE%BE%E5%B7%A5%E7%A8%8B%E9%A1%B9%E7%9B%AE%E7%AE%A1%E7%90%86%E5%AE%9E%E6%96%BD%E5%8A%9E%E6%B3%95%E3%80%8B%E7%9A%84%E9%80%9A%E7%9F%A5.md) |
| 朱家角镇 | [上海市青浦区朱家角镇人民政府关于印发《朱家角镇小额建设工程实施办法》的通知](https://www.shanghai.gov.cn/zhengce/detail?businessId=00831346134&siteId=0083) | 2025-10-29 | [正文](docs/%E5%B7%A5%E7%A8%8B%E5%BB%BA%E8%AE%BE%E7%AE%A1%E7%90%86/%E4%B8%8A%E6%B5%B7%E5%B8%82%E9%9D%92%E6%B5%A6%E5%8C%BA%E6%9C%B1%E5%AE%B6%E8%A7%92%E9%95%87%E4%BA%BA%E6%B0%91%E6%94%BF%E5%BA%9C%E5%85%B3%E4%BA%8E%E5%8D%B0%E5%8F%91%E3%80%8A%E6%9C%B1%E5%AE%B6%E8%A7%92%E9%95%87%E5%B0%8F%E9%A2%9D%E5%BB%BA%E8%AE%BE%E5%B7%A5%E7%A8%8B%E5%AE%9E%E6%96%BD%E5%8A%9E%E6%B3%95%E3%80%8B%E7%9A%84%E9%80%9A%E7%9F%A5.md) |
| 南桥镇 | [上海市奉贤区南桥镇人民政府关于进一步加强南桥镇小型建设工程项目规范管理的实施办法（试行）](https://www.shanghai.gov.cn/zhengce/detail?businessId=00842818&siteId=0084) | 2025-09-04 | [正文](docs/%E5%B7%A5%E7%A8%8B%E5%BB%BA%E8%AE%BE%E7%AE%A1%E7%90%86/%E4%B8%8A%E6%B5%B7%E5%B8%82%E5%A5%89%E8%B4%A4%E5%8C%BA%E5%8D%97%E6%A1%A5%E9%95%87%E4%BA%BA%E6%B0%91%E6%94%BF%E5%BA%9C%E5%85%B3%E4%BA%8E%E8%BF%9B%E4%B8%80%E6%AD%A5%E5%8A%A0%E5%BC%BA%E5%8D%97%E6%A1%A5%E9%95%87%E5%B0%8F%E5%9E%8B%E5%BB%BA%E8%AE%BE%E5%B7%A5%E7%A8%8B%E9%A1%B9%E7%9B%AE%E8%A7%84%E8%8C%83%E7%AE%A1%E7%90%86%E7%9A%84%E5%AE%9E%E6%96%BD%E5%8A%9E%E6%B3%95%EF%BC%88%E8%AF%95%E8%A1%8C%EF%BC%89.md) |
| 金泽镇 | [上海市青浦区金泽镇人民政府关于调整《关于金泽镇小额建设工程实施的工作方案》等五个工作方案的通知](https://www.shanghai.gov.cn/zhengce/detail?businessId=00831328204&siteId=0083) | 2025-07-22 | [正文](docs/%E5%B7%A5%E7%A8%8B%E5%BB%BA%E8%AE%BE%E7%AE%A1%E7%90%86/%E4%B8%8A%E6%B5%B7%E5%B8%82%E9%9D%92%E6%B5%A6%E5%8C%BA%E9%87%91%E6%B3%BD%E9%95%87%E4%BA%BA%E6%B0%91%E6%94%BF%E5%BA%9C%E5%85%B3%E4%BA%8E%E8%B0%83%E6%95%B4%E3%80%8A%E5%85%B3%E4%BA%8E%E9%87%91%E6%B3%BD%E9%95%87%E5%B0%8F%E9%A2%9D%E5%BB%BA%E8%AE%BE%E5%B7%A5%E7%A8%8B%E5%AE%9E%E6%96%BD%E7%9A%84%E5%B7%A5%E4%BD%9C%E6%96%B9%E6%A1%88%E3%80%8B%E7%AD%89%E4%BA%94%E4%B8%AA%E5%B7%A5%E4%BD%9C%E6%96%B9%E6%A1%88%E7%9A%84%E9%80%9A%E7%9F%A5.md) |
| 城桥镇 | [关于印发《城桥镇限额以下小型建设工程安全监督管理办法（试行）》的通知](https://www.shanghai.gov.cn/zhengce/detail?businessId=test_4e5b8caf-bf90-4dbf-ae70-36aa52452c61&siteId=0085) | 2025-03-31 | [正文](docs/%E5%B7%A5%E7%A8%8B%E5%BB%BA%E8%AE%BE%E7%AE%A1%E7%90%86/%E5%85%B3%E4%BA%8E%E5%8D%B0%E5%8F%91%E3%80%8A%E5%9F%8E%E6%A1%A5%E9%95%87%E9%99%90%E9%A2%9D%E4%BB%A5%E4%B8%8B%E5%B0%8F%E5%9E%8B%E5%BB%BA%E8%AE%BE%E5%B7%A5%E7%A8%8B%E5%AE%89%E5%85%A8%E7%9B%91%E7%9D%A3%E7%AE%A1%E7%90%86%E5%8A%9E%E6%B3%95%EF%BC%88%E8%AF%95%E8%A1%8C%EF%BC%89%E3%80%8B%E7%9A%84%E9%80%9A%E7%9F%A5.md) |
| 港沿镇 | [上海市崇明区港沿镇人民政府关于印发《港沿镇政府投资小型建设工程项目管理办法》的通知](https://www.shanghai.gov.cn/zhengce/detail?businessId=test_b65c850f-03f9-4c60-80d7-a60da58f5fe7&siteId=0085) | 2025-02-18 | [正文](docs/%E5%B7%A5%E7%A8%8B%E5%BB%BA%E8%AE%BE%E7%AE%A1%E7%90%86/%E4%B8%8A%E6%B5%B7%E5%B8%82%E5%B4%87%E6%98%8E%E5%8C%BA%E6%B8%AF%E6%B2%BF%E9%95%87%E4%BA%BA%E6%B0%91%E6%94%BF%E5%BA%9C%E5%85%B3%E4%BA%8E%E5%8D%B0%E5%8F%91%E3%80%8A%E6%B8%AF%E6%B2%BF%E9%95%87%E6%94%BF%E5%BA%9C%E6%8A%95%E8%B5%84%E5%B0%8F%E5%9E%8B%E5%BB%BA%E8%AE%BE%E5%B7%A5%E7%A8%8B%E9%A1%B9%E7%9B%AE%E7%AE%A1%E7%90%86%E5%8A%9E%E6%B3%95%E3%80%8B%E7%9A%84%E9%80%9A%E7%9F%A5.md) |
| 月浦镇 | [月浦镇限额以下小型建设工程管理办法（试行）](https://www.shanghai.gov.cn/zhengce/detail?businessId=aa665b46-ec91-4310-9785-7b1dbf8ef617&siteId=0078) | 2025-02-17 | [正文](docs/%E5%B7%A5%E7%A8%8B%E5%BB%BA%E8%AE%BE%E7%AE%A1%E7%90%86/%E6%9C%88%E6%B5%A6%E9%95%87%E9%99%90%E9%A2%9D%E4%BB%A5%E4%B8%8B%E5%B0%8F%E5%9E%8B%E5%BB%BA%E8%AE%BE%E5%B7%A5%E7%A8%8B%E7%AE%A1%E7%90%86%E5%8A%9E%E6%B3%95%EF%BC%88%E8%AF%95%E8%A1%8C%EF%BC%89.md) |
| 吴淞街道办事处 | [关于印发《吴淞街道限额以下建设工程管理若干意见（试行）》的通知](https://www.shanghai.gov.cn/zhengce/detail?businessId=c9de9d98-2f04-4c6c-b2e2-efe0921ef29d&siteId=0078) | 2024-10-08 | [正文](docs/%E5%B7%A5%E7%A8%8B%E5%BB%BA%E8%AE%BE%E7%AE%A1%E7%90%86/%E5%85%B3%E4%BA%8E%E5%8D%B0%E5%8F%91%E3%80%8A%E5%90%B4%E6%B7%9E%E8%A1%97%E9%81%93%E9%99%90%E9%A2%9D%E4%BB%A5%E4%B8%8B%E5%BB%BA%E8%AE%BE%E5%B7%A5%E7%A8%8B%E7%AE%A1%E7%90%86%E8%8B%A5%E5%B9%B2%E6%84%8F%E8%A7%81%EF%BC%88%E8%AF%95%E8%A1%8C%EF%BC%89%E3%80%8B%E7%9A%84%E9%80%9A%E7%9F%A5.md) |
| 浦江镇 | [关于调整浦江镇限额以下小型建设工程管理的实施意见](https://www.shanghai.gov.cn/zhengce/detail?businessId=33872FED-3697-11ED-951B-1BD88B3C7FDC&siteId=0079) | 2021-06-30 | [正文](docs/%E5%B7%A5%E7%A8%8B%E5%BB%BA%E8%AE%BE%E7%AE%A1%E7%90%86/%E5%85%B3%E4%BA%8E%E8%B0%83%E6%95%B4%E6%B5%A6%E6%B1%9F%E9%95%87%E9%99%90%E9%A2%9D%E4%BB%A5%E4%B8%8B%E5%B0%8F%E5%9E%8B%E5%BB%BA%E8%AE%BE%E5%B7%A5%E7%A8%8B%E7%AE%A1%E7%90%86%E7%9A%84%E5%AE%9E%E6%96%BD%E6%84%8F%E8%A7%81.md) |
| 古美路街道办事处 | [关于印发《古美路街道限额以下小型建设工程实施细则》的通知](https://www.shanghai.gov.cn/zhengce/detail?businessId=8D4C2E83-3697-11ED-9C78-D153B5173FE7&siteId=0079) | 2021-01-18 | [正文](docs/%E5%B7%A5%E7%A8%8B%E5%BB%BA%E8%AE%BE%E7%AE%A1%E7%90%86/%E5%85%B3%E4%BA%8E%E5%8D%B0%E5%8F%91%E3%80%8A%E5%8F%A4%E7%BE%8E%E8%B7%AF%E8%A1%97%E9%81%93%E9%99%90%E9%A2%9D%E4%BB%A5%E4%B8%8B%E5%B0%8F%E5%9E%8B%E5%BB%BA%E8%AE%BE%E5%B7%A5%E7%A8%8B%E5%AE%9E%E6%96%BD%E7%BB%86%E5%88%99%E3%80%8B%E7%9A%84%E9%80%9A%E7%9F%A5.md) |
| 七宝镇 | [七宝镇限额以下小型建设工程管理的实施意见](https://www.shanghai.gov.cn/zhengce/detail?businessId=B8AE27CB-3697-11ED-AC45-3DB7F69B5DBD&siteId=0079) | 2020-09-27 | [正文](docs/%E5%B7%A5%E7%A8%8B%E5%BB%BA%E8%AE%BE%E7%AE%A1%E7%90%86/%E4%B8%83%E5%AE%9D%E9%95%87%E9%99%90%E9%A2%9D%E4%BB%A5%E4%B8%8B%E5%B0%8F%E5%9E%8B%E5%BB%BA%E8%AE%BE%E5%B7%A5%E7%A8%8B%E7%AE%A1%E7%90%86%E7%9A%84%E5%AE%9E%E6%96%BD%E6%84%8F%E8%A7%81.md) |
| 杨行镇 | [关于杨行镇村级集体投资小型工程建设项目管理办法（试行）](https://www.shanghai.gov.cn/zhengce/detail?businessId=c8ab6a86-dae0-452d-98c3-7c805ffedbab&siteId=0078) | 2020-03-13 | [正文](docs/%E5%B7%A5%E7%A8%8B%E5%BB%BA%E8%AE%BE%E7%AE%A1%E7%90%86/%E5%85%B3%E4%BA%8E%E6%9D%A8%E8%A1%8C%E9%95%87%E6%9D%91%E7%BA%A7%E9%9B%86%E4%BD%93%E6%8A%95%E8%B5%84%E5%B0%8F%E5%9E%8B%E5%B7%A5%E7%A8%8B%E5%BB%BA%E8%AE%BE%E9%A1%B9%E7%9B%AE%E7%AE%A1%E7%90%86%E5%8A%9E%E6%B3%95%EF%BC%88%E8%AF%95%E8%A1%8C%EF%BC%89.md) |
| 金汇镇 | [上海市奉贤区金汇镇人民政府关于印发加强金汇镇小型建设工程项目管理实施意见的通知](https://www.shanghai.gov.cn/zhengce/detail?businessId=00845245&siteId=0084) | 2019-04-03 | [正文](docs/%E5%B7%A5%E7%A8%8B%E5%BB%BA%E8%AE%BE%E7%AE%A1%E7%90%86/%E4%B8%8A%E6%B5%B7%E5%B8%82%E5%A5%89%E8%B4%A4%E5%8C%BA%E9%87%91%E6%B1%87%E9%95%87%E4%BA%BA%E6%B0%91%E6%94%BF%E5%BA%9C%E5%85%B3%E4%BA%8E%E5%8D%B0%E5%8F%91%E5%8A%A0%E5%BC%BA%E9%87%91%E6%B1%87%E9%95%87%E5%B0%8F%E5%9E%8B%E5%BB%BA%E8%AE%BE%E5%B7%A5%E7%A8%8B%E9%A1%B9%E7%9B%AE%E7%AE%A1%E7%90%86%E5%AE%9E%E6%96%BD%E6%84%8F%E8%A7%81%E7%9A%84%E9%80%9A%E7%9F%A5.md) |
| 新虹街道办事处 | [关于印发《新虹街道限额以下小型建设工程管理实施细则（试行）》的通知](https://www.shanghai.gov.cn/zhengce/detail?businessId=a3d57cb0-7217-4067-aac0-815205fc047f&siteId=0079) | 2014-02-13 | [正文](docs/%E5%B7%A5%E7%A8%8B%E5%BB%BA%E8%AE%BE%E7%AE%A1%E7%90%86/%E5%85%B3%E4%BA%8E%E5%8D%B0%E5%8F%91%E3%80%8A%E6%96%B0%E8%99%B9%E8%A1%97%E9%81%93%E9%99%90%E9%A2%9D%E4%BB%A5%E4%B8%8B%E5%B0%8F%E5%9E%8B%E5%BB%BA%E8%AE%BE%E5%B7%A5%E7%A8%8B%E7%AE%A1%E7%90%86%E5%AE%9E%E6%96%BD%E7%BB%86%E5%88%99%EF%BC%88%E8%AF%95%E8%A1%8C%EF%BC%89%E3%80%8B%E7%9A%84%E9%80%9A%E7%9F%A5.md) |

## 时效复核：这几条现在还算数吗

上海的建设类规范性文件普遍带**有效期**（多为 5 年），到期若不续期就自动失效。所以「一条还灵不灵」**不能只看发布日期** —— 本库从官方正文里挖出**有效期止**，逐条判定：

| 判定 | 条数 | 含义 |
|---|---|---|
| 现行有效 | 2493 | 有效期止在今天之后，或未标有效期但平台状态为「有效」 |
| ⚠ 有效期已届满 | 61 | 有效期止已过，**须核对是否已发续期通知** |
| ⚠ 正文含废止表述 | 19 | 正文出现「本X…废止/失效」，可能只是**废止他文**，须人工确认 |
| 已废止/失效 | 37 | 平台明确标注废止或失效，**不要再引用** |
| 未标注 | 8 | 无正文且平台无状态 |

索引各表的「**时效**」列就是这张表的缩略：**✓** 现行有效 ／ **⚠** 需人工确认 ／ **✗** 已废止 ／ **?** 未标注。

**⚠ 有效期已届满的 61 条，按届满年份**（越靠后越可能是「刚过期、续期还没上网」）：

| 届满年份 | 条数 |
|---|---|
| 2015 | 1 |
| 2017 | 1 |
| 2021 | 1 |
| 2022 | 1 |
| 2023 | 8 |
| 2024 | 18 |
| 2025 | 17 |
| 2026 | 14 |

最近到期的 12 条：

| 有效期止 | 标题 | 发布机关 |
|---|---|---|
| 2026-08-31 | [上海市住房和城乡建设管理委员会关于修订印发《上海市建设工程评标专家和评标专家库管理办法》的通知](https://zjw.sh.gov.cn/gfxwj/20210930/c0789a87c1664e139f9b913cbdea9ee9.html) | 上海市住房和城乡建设管理委员会 |
| 2026-08-31 | [关于印发《本市公安机关行使有关消防行政处罚权事项清单》的通知](https://www.shanghai.gov.cn/zhengce/detail?businessId=GKXX-20210907084806321--5667&siteId=0033) | 上海市公安局 |
| 2026-08-31 | [关于修订《上海市共有产权保障住房价格管理办法》的通知](https://www.shanghai.gov.cn/zhengce/detail?businessId=8e1bd8818a7c408f9389551fda8c4f9f&siteId=0025) | 上海市发展和改革委员会 |
| 2026-08-31 | [上海市普陀区人民政府关于印发《上海市普陀区公共租赁住房实施办法》的通知](https://www.shanghai.gov.cn/zhengce/detail?businessId=007590789&siteId=0075) | 上海市普陀区人民政府 |
| 2026-07-05 | [关于印发《上海市绿化和市容管理局科研项目管理办法》的通知](https://www.shanghai.gov.cn/zhengce/detail?businessId=f5c8adfe-e52a-4e91-89cd-b7274a7ed510&siteId=0039) | 上海市绿化和市容管理局 |
| 2026-06-30 | [关于印发《吴泾镇既有多层住宅加装电梯后续维保补贴实施意见》的通知](https://www.shanghai.gov.cn/zhengce/detail?businessId=fd213ff2-36cd-4f66-9ceb-7918b72f05e6&siteId=0079) | 上海市闵行区吴泾镇人民政府 |
| 2026-06-30 | [关于本市城市基础设施配套费征收标准和使用范围等有关事项的通知](https://zjw.sh.gov.cn/gfxwj/20211109/c3bbd05093f24a398f673b3420618e3e.html) | 上海市住房和城乡建设管理委员会 |
| 2026-06-30 | [关于印发《上海市共有产权保障住房供后管理实施细则》的通知](https://www.shanghai.gov.cn/zhengce/detail?businessId=484934a3ccdb4ed988e2c2e4d7004d83&siteId=0013) | 上海市房屋管理局 |
| 2026-06-30 | [关于印发《上海市住宅物业管理区域机动车停放管理规定》的通知](https://www.shanghai.gov.cn/zhengce/detail?businessId=dba44d90510b4216b4be4cbe779dbf8d&siteId=0013) | 上海市房屋管理局 |
| 2026-06-30 | [关于印发《上海市共有产权保障住房销售差额资金管理办法》的通知](https://www.shanghai.gov.cn/zhengce/detail?businessId=6c8a3f8d6646459da2e971a2cce3b939&siteId=0013) | 上海市房屋管理局 |
| 2026-06-30 | [关于印发《关于进一步贯彻实施〈上海市住宅物业管理规定〉的若干意见》的通知](https://www.shanghai.gov.cn/zhengce/detail?businessId=c01bf90254bb4429826e5ee4771e580b&siteId=0013) | 上海市房屋管理局 |
| 2026-05-31 | [上海市住房和城乡建设管理委员会关于印发《上海市建设工程勘察设计单位项目主要负责人工程质量违法违规行为记分管理办法》的通知](https://zjw.sh.gov.cn/gfxwj/20210930/0ed5658e5dd24edba5ad53b479359436.html) | 上海市住房和城乡建设管理委员会 |

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
| 浦东新区 | [打开](https://www.pudong.gov.cn/xxgk_gkzn/index.html) | 60 条 |
| 黄浦区 | [打开](https://www.shhuangpu.gov.cn/zw/govopen/goverGuide.html) | 53 条 |
| 静安区 | [打开](https://www.jingan.gov.cn/dynamic/infoOpenFile.html) | 36 条 |
| 徐汇区 | [打开](https://www.xuhui.gov.cn/zfxxgk/wj/index.html) | 12 条 |
| 长宁区 | [打开](https://zwgk.shcn.gov.cn/xxgk/zcwj-zfxxgk/index.html) | 16 条 |
| 普陀区 | [打开](https://www.shpt.gov.cn/zhengwu/zfxxgkzn-zfxxgk/index.html) | 35 条 |
| 虹口区 | [打开](https://www.shhk.gov.cn/hkxxgk/zdgknr/policydoc.html) | 24 条 |
| 杨浦区 | [打开](https://www.shyp.gov.cn/shypq/xxgkzn/) | 18 条 |
| 宝山区 | [打开](http://xxgk.shbsq.gov.cn/zfxxgk/pubguide.html) | 61 条 |
| 闵行区 | [打开](https://zwgk.shmh.gov.cn/mh-xxgk-cms/website/mh_xxgk/zfxxgk_index/List/index.htm?tab=divzcwj) | 42 条 |
| 嘉定区 | [打开](http://www.jiading.gov.cn/publicity/zfxxgk/zfxxgkzn2) | 19 条 |
| 金山区 | [打开](https://www.jinshan.gov.cn/zhengwu/zwgk-zfxxgkzn/index.html) | 27 条 |
| 松江区 | [打开](https://www.songjiang.gov.cn/Template/dynamic/zfxxgk/zfxxgk.html) | 41 条 |
| 青浦区 | [打开](https://www.shqp.gov.cn/shqp/zwgk/zwgkzt/zf/index.html) | 22 条 |
| 奉贤区 | [打开](https://www.fengxian.gov.cn/zwgk/xxgk/zn/index.html) | 49 条 |
| 崇明区 | [打开](http://www.shcm.gov.cn/goverDetail.html?deptcode=004&categorynum=004) | 37 条 |

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

另外，部分区级老数据的 businessId 是 **8–11 位纯数字**（多为浦东新区、普陀、奉贤、青浦、长宁），与主流 32 位 hash 不同。这类条目已在 CSV 的「链接形态」列标为 `short`（共 168 条），若个别仍打不开，请：

1. **看库内正文** —— `docs/` 已存官方全文，不受影响；
2. 到**对应区政府门户**站内检索标题；
3. 或在 [统一政策发布平台](https://www.shanghai.gov.cn/zhengce/list) 搜标题。

## 设计报建高频文件速查

按实务环节整理的常用依据（全部来自本库，含正文）：


### 规划条件与方案报建

| 标题 | 文号 | 发布机关 | 日期 | 时效 | 正文 / 原件 |
|---|---|---|---|---|---|
| [关于《上海市城市规划管理技术规定（土地使用 建筑管理）应用解释》继续适用的通知](https://www.shanghai.gov.cn/zhengce/detail?businessId=72d2cd5662b54f14b2375a5e984867a3&siteId=0032) | 沪规划资源建〔2025〕131号 | 上海市规划和自然资源局 | 2025-04-16 | ✓ | [正文](docs/%E8%A7%84%E5%88%92%E4%B8%8E%E5%9C%9F%E5%9C%B0/%E5%85%B3%E4%BA%8E%E3%80%8A%E4%B8%8A%E6%B5%B7%E5%B8%82%E5%9F%8E%E5%B8%82%E8%A7%84%E5%88%92%E7%AE%A1%E7%90%86%E6%8A%80%E6%9C%AF%E8%A7%84%E5%AE%9A%EF%BC%88%E5%9C%9F%E5%9C%B0%E4%BD%BF%E7%94%A8%20%E5%BB%BA%E7%AD%91%E7%AE%A1%E7%90%86%EF%BC%89%E5%BA%94%E7%94%A8%E8%A7%A3%E9%87%8A%E3%80%8B%E7%BB%A7%E7%BB%AD%E9%80%82%E7%94%A8%E7%9A%84%E9%80%9A%E7%9F%A5.md) |
| [关于印发《上海市建设工程设计方案批后调整和建设规划许可变更管理办法》的通知](https://www.shanghai.gov.cn/zhengce/detail?businessId=61b934dade3e4fbaab573e01f115db0e&siteId=0032) | 沪规划资源规〔2025〕1号 | 上海市规划和自然资源局 | 2025-01-26 | ✓ | [正文](docs/%E5%B7%A5%E7%A8%8B%E5%BB%BA%E8%AE%BE%E7%AE%A1%E7%90%86/%E5%85%B3%E4%BA%8E%E5%8D%B0%E5%8F%91%E3%80%8A%E4%B8%8A%E6%B5%B7%E5%B8%82%E5%BB%BA%E8%AE%BE%E5%B7%A5%E7%A8%8B%E8%AE%BE%E8%AE%A1%E6%96%B9%E6%A1%88%E6%89%B9%E5%90%8E%E8%B0%83%E6%95%B4%E5%92%8C%E5%BB%BA%E8%AE%BE%E8%A7%84%E5%88%92%E8%AE%B8%E5%8F%AF%E5%8F%98%E6%9B%B4%E7%AE%A1%E7%90%86%E5%8A%9E%E6%B3%95%E3%80%8B%E7%9A%84%E9%80%9A%E7%9F%A5.md) |
| [杨浦区规划和自然资源局转发《上海市建设工程设计方案规划公示规定》的通知](https://www.shanghai.gov.cn/zhengce/detail?businessId=007705f58e9f300cdee2270da0a4138ea3a2&siteId=0077) | 杨规划资源〔2024〕1号 | 杨浦区规划和自然资源局 | 2024-06-25 | ✓ | [正文](docs/%E5%B7%A5%E7%A8%8B%E5%BB%BA%E8%AE%BE%E7%AE%A1%E7%90%86/%E6%9D%A8%E6%B5%A6%E5%8C%BA%E8%A7%84%E5%88%92%E5%92%8C%E8%87%AA%E7%84%B6%E8%B5%84%E6%BA%90%E5%B1%80%E8%BD%AC%E5%8F%91%E3%80%8A%E4%B8%8A%E6%B5%B7%E5%B8%82%E5%BB%BA%E8%AE%BE%E5%B7%A5%E7%A8%8B%E8%AE%BE%E8%AE%A1%E6%96%B9%E6%A1%88%E8%A7%84%E5%88%92%E5%85%AC%E7%A4%BA%E8%A7%84%E5%AE%9A%E3%80%8B%E7%9A%84%E9%80%9A%E7%9F%A5.md) |
| [关于印发《上海市建设工程设计方案规划公示规定》的通知](https://www.shanghai.gov.cn/zhengce/detail?businessId=f0f8f01b2ac44cbea21900feab80c34e&siteId=0032) | 沪规划资源规〔2024〕2号 | 上海市规划和自然资源局 | 2024-03-26 | ✓ | [正文](docs/%E5%B7%A5%E7%A8%8B%E5%BB%BA%E8%AE%BE%E7%AE%A1%E7%90%86/%E5%85%B3%E4%BA%8E%E5%8D%B0%E5%8F%91%E3%80%8A%E4%B8%8A%E6%B5%B7%E5%B8%82%E5%BB%BA%E8%AE%BE%E5%B7%A5%E7%A8%8B%E8%AE%BE%E8%AE%A1%E6%96%B9%E6%A1%88%E8%A7%84%E5%88%92%E5%85%AC%E7%A4%BA%E8%A7%84%E5%AE%9A%E3%80%8B%E7%9A%84%E9%80%9A%E7%9F%A5.md) |
| [关于印发《上海市日照分析技术规范》的通知](https://www.shanghai.gov.cn/zhengce/detail?businessId=6802a03eb7184253bb5c9b39f9181443&siteId=0032) | 沪规划资源建〔2021〕437号 | 上海市规划和自然资源局 | 2021-11-26 | ✓ | [正文](docs/%E8%A7%84%E5%88%92%E4%B8%8E%E5%9C%9F%E5%9C%B0/%E5%85%B3%E4%BA%8E%E5%8D%B0%E5%8F%91%E3%80%8A%E4%B8%8A%E6%B5%B7%E5%B8%82%E6%97%A5%E7%85%A7%E5%88%86%E6%9E%90%E6%8A%80%E6%9C%AF%E8%A7%84%E8%8C%83%E3%80%8B%E7%9A%84%E9%80%9A%E7%9F%A5.md) |
| [上海市城市规划管理技术规定（土地使用建筑管理）](https://www.shanghai.gov.cn/xxzfgzwj/20210608/7c162f6f13f64d9ba26f21db7a11503b.html) | - | 上海市人民政府 | - | ✓ | [正文](docs/%E8%A7%84%E5%88%92%E4%B8%8E%E5%9C%9F%E5%9C%B0/%E4%B8%8A%E6%B5%B7%E5%B8%82%E5%9F%8E%E5%B8%82%E8%A7%84%E5%88%92%E7%AE%A1%E7%90%86%E6%8A%80%E6%9C%AF%E8%A7%84%E5%AE%9A%EF%BC%88%E5%9C%9F%E5%9C%B0%E4%BD%BF%E7%94%A8%E5%BB%BA%E7%AD%91%E7%AE%A1%E7%90%86%EF%BC%89.md) |

[→ 查看该主题全部条目](index/02-建筑设计与报建.md)

### 面积计算与容积率

| 标题 | 文号 | 发布机关 | 日期 | 时效 | 正文 / 原件 |
|---|---|---|---|---|---|
| [上海市绿化和市容管理局关于优化我市住宅品质提升项目配套绿化面积计算规则的通知](https://www.shanghai.gov.cn/zhengce/detail?businessId=f056628b-4183-497c-b41c-59b4977266c1&siteId=0039) | 沪绿容〔2026〕21号 | 上海市绿化和市容管理局 | 2026-02-27 | ✓ | [正文](docs/%E6%88%BF%E5%B1%8B%E4%B8%8E%E4%BD%8F%E6%88%BF/%E4%B8%8A%E6%B5%B7%E5%B8%82%E7%BB%BF%E5%8C%96%E5%92%8C%E5%B8%82%E5%AE%B9%E7%AE%A1%E7%90%86%E5%B1%80%E5%85%B3%E4%BA%8E%E4%BC%98%E5%8C%96%E6%88%91%E5%B8%82%E4%BD%8F%E5%AE%85%E5%93%81%E8%B4%A8%E6%8F%90%E5%8D%87%E9%A1%B9%E7%9B%AE%E9%85%8D%E5%A5%97%E7%BB%BF%E5%8C%96%E9%9D%A2%E7%A7%AF%E8%AE%A1%E7%AE%97%E8%A7%84%E5%88%99%E7%9A%84%E9%80%9A%E7%9F%A5.md) |
| [关于印发《上海市建筑面积计算规划管理规定》的通知](https://www.shanghai.gov.cn/zhengce/detail?businessId=146691b797364f4288d7945446adc057&siteId=0032) | 沪规划资源建〔2021〕363号 | 上海市规划和自然资源局 | 2021-09-30 | ✓ | [正文](docs/%E8%A7%84%E5%88%92%E4%B8%8E%E5%9C%9F%E5%9C%B0/%E5%85%B3%E4%BA%8E%E5%8D%B0%E5%8F%91%E3%80%8A%E4%B8%8A%E6%B5%B7%E5%B8%82%E5%BB%BA%E7%AD%91%E9%9D%A2%E7%A7%AF%E8%AE%A1%E7%AE%97%E8%A7%84%E5%88%92%E7%AE%A1%E7%90%86%E8%A7%84%E5%AE%9A%E3%80%8B%E7%9A%84%E9%80%9A%E7%9F%A5.md) |

[→ 查看该主题全部条目](index/01-规划与土地.md)

### 第五立面与屋面

| 标题 | 文号 | 发布机关 | 日期 | 时效 | 正文 / 原件 |
|---|---|---|---|---|---|
| [关于印发《关于加强城市第五立面规划建设的指导意见》的通知](https://www.shanghai.gov.cn/zhengce/detail?businessId=39b001a3f37d48cbbdd5dd1eb2ccc5e6&siteId=0032) | 沪规划资源建〔2023〕361号 | 上海市规划和自然资源局 | 2023-09-22 | ✓ | [正文](docs/%E8%A7%84%E5%88%92%E4%B8%8E%E5%9C%9F%E5%9C%B0/%E5%85%B3%E4%BA%8E%E5%8D%B0%E5%8F%91%E3%80%8A%E5%85%B3%E4%BA%8E%E5%8A%A0%E5%BC%BA%E5%9F%8E%E5%B8%82%E7%AC%AC%E4%BA%94%E7%AB%8B%E9%9D%A2%E8%A7%84%E5%88%92%E5%BB%BA%E8%AE%BE%E7%9A%84%E6%8C%87%E5%AF%BC%E6%84%8F%E8%A7%81%E3%80%8B%E7%9A%84%E9%80%9A%E7%9F%A5.md) |
| [上海市住房和城乡建设管理委员会关于批准《多层住宅平屋面改坡屋面工程技术标准》为上海市工程建设规范的通知](https://www.shanghai.gov.cn/zhengce/detail?businessId=559a2baba51742b5bdf097b76014cf7d&siteId=0011) | 沪建标定〔2022〕78号 | 上海市住房和城乡建设管理委员会 | 2022-01-28 | ✓ | [正文](docs/%E5%B7%A5%E7%A8%8B%E5%BB%BA%E8%AE%BE%E7%AE%A1%E7%90%86/%E4%B8%8A%E6%B5%B7%E5%B8%82%E4%BD%8F%E6%88%BF%E5%92%8C%E5%9F%8E%E4%B9%A1%E5%BB%BA%E8%AE%BE%E7%AE%A1%E7%90%86%E5%A7%94%E5%91%98%E4%BC%9A%E5%85%B3%E4%BA%8E%E6%89%B9%E5%87%86%E3%80%8A%E5%A4%9A%E5%B1%82%E4%BD%8F%E5%AE%85%E5%B9%B3%E5%B1%8B%E9%9D%A2%E6%94%B9%E5%9D%A1%E5%B1%8B%E9%9D%A2%E5%B7%A5%E7%A8%8B%E6%8A%80%E6%9C%AF%E6%A0%87%E5%87%86%E3%80%8B%E4%B8%BA%E4%B8%8A%E6%B5%B7%E5%B8%82%E5%B7%A5%E7%A8%8B%E5%BB%BA%E8%AE%BE%E8%A7%84%E8%8C%83%E7%9A%84%E9%80%9A.md) |
| [上海市住房和城乡建设管理委员会关于批准《既有建筑外立面整治设计标准》为上海市工程建设规范的通知](https://www.shanghai.gov.cn/zhengce/detail?businessId=3d979b039e6a4782820a47c16cc22e43&siteId=0011) | 沪建标定〔2021〕335号 | 上海市住房和城乡建设管理委员会 | 2021-05-31 | ✓ | [正文](docs/%E5%B7%A5%E7%A8%8B%E5%BB%BA%E8%AE%BE%E7%AE%A1%E7%90%86/%E4%B8%8A%E6%B5%B7%E5%B8%82%E4%BD%8F%E6%88%BF%E5%92%8C%E5%9F%8E%E4%B9%A1%E5%BB%BA%E8%AE%BE%E7%AE%A1%E7%90%86%E5%A7%94%E5%91%98%E4%BC%9A%E5%85%B3%E4%BA%8E%E6%89%B9%E5%87%86%E3%80%8A%E6%97%A2%E6%9C%89%E5%BB%BA%E7%AD%91%E5%A4%96%E7%AB%8B%E9%9D%A2%E6%95%B4%E6%B2%BB%E8%AE%BE%E8%AE%A1%E6%A0%87%E5%87%86%E3%80%8B%E4%B8%BA%E4%B8%8A%E6%B5%B7%E5%B8%82%E5%B7%A5%E7%A8%8B%E5%BB%BA%E8%AE%BE%E8%A7%84%E8%8C%83%E7%9A%84%E9%80%9A%E7%9F%A5.md) |
| [关于印发《苏州河沿岸街区建筑立面整治设计要求》的通知](https://www.shanghai.gov.cn/zhengce/detail?businessId=6d3f04a598c6488a9157a852597fc6b9&siteId=0013) | 沪房更新〔2021〕175号 | 上海市房屋管理局 | 2021-10-22 | ✓ | [正文](docs/%E6%88%BF%E5%B1%8B%E4%B8%8E%E4%BD%8F%E6%88%BF/%E5%85%B3%E4%BA%8E%E5%8D%B0%E5%8F%91%E3%80%8A%E8%8B%8F%E5%B7%9E%E6%B2%B3%E6%B2%BF%E5%B2%B8%E8%A1%97%E5%8C%BA%E5%BB%BA%E7%AD%91%E7%AB%8B%E9%9D%A2%E6%95%B4%E6%B2%BB%E8%AE%BE%E8%AE%A1%E8%A6%81%E6%B1%82%E3%80%8B%E7%9A%84%E9%80%9A%E7%9F%A5.md) |
| [关于印发2021年上海市整街道（镇、乡）屋顶分布式光伏开发试点名单的通知](https://www.shanghai.gov.cn/zhengce/detail?businessId=f186a4d372c14ba88304457fab6d3b52&siteId=0025) | 沪发改能源〔2021〕210号 | 上海市发展和改革委员会 | 2021-10-11 | ✓ | [正文](docs/%E7%BB%BF%E8%89%B2%E4%BD%8E%E7%A2%B3%E4%B8%8E%E8%8A%82%E8%83%BD/%E5%85%B3%E4%BA%8E%E5%8D%B0%E5%8F%912021%E5%B9%B4%E4%B8%8A%E6%B5%B7%E5%B8%82%E6%95%B4%E8%A1%97%E9%81%93%EF%BC%88%E9%95%87%E3%80%81%E4%B9%A1%EF%BC%89%E5%B1%8B%E9%A1%B6%E5%88%86%E5%B8%83%E5%BC%8F%E5%85%89%E4%BC%8F%E5%BC%80%E5%8F%91%E8%AF%95%E7%82%B9%E5%90%8D%E5%8D%95%E7%9A%84%E9%80%9A%E7%9F%A5.md) |

[→ 查看该主题全部条目](index/06-城市更新与历史保护.md)

### 施工图审查

| 标题 | 文号 | 发布机关 | 日期 | 时效 | 正文 / 原件 |
|---|---|---|---|---|---|
| [关于印发《上海市建设工程施工图设计文件“多图联审”管理办法》的通知](https://zjw.sh.gov.cn/gfxwj/20260807/00978e58c73143b9989ddbfa3308525b.html) | - | 上海市住房和城乡建设管理委员会 | 2026-08 | ✓ | [正文](docs/%E5%BB%BA%E7%AD%91%E8%AE%BE%E8%AE%A1%E4%B8%8E%E6%8A%A5%E5%BB%BA/%E5%85%B3%E4%BA%8E%E5%8D%B0%E5%8F%91%E3%80%8A%E4%B8%8A%E6%B5%B7%E5%B8%82%E5%BB%BA%E8%AE%BE%E5%B7%A5%E7%A8%8B%E6%96%BD%E5%B7%A5%E5%9B%BE%E8%AE%BE%E8%AE%A1%E6%96%87%E4%BB%B6%E2%80%9C%E5%A4%9A%E5%9B%BE%E8%81%94%E5%AE%A1%E2%80%9D%E7%AE%A1%E7%90%86%E5%8A%9E%E6%B3%95%E3%80%8B%E7%9A%84%E9%80%9A%E7%9F%A5.md) |
| [上海市住房和城乡建设管理委员会关于开展2026—2027年度上海市建设工程施工图设计文件审查机构认定工作的通知](https://www.shanghai.gov.cn/zhengce/detail?businessId=f1e10105d8854d51abb48613a8d7345f&siteId=0011) | 沪建建管〔2025〕318号 | 上海市住房和城乡建设管理委员会 | 2025-06-16 | ✓ | [正文](docs/%E5%BB%BA%E7%AD%91%E8%AE%BE%E8%AE%A1%E4%B8%8E%E6%8A%A5%E5%BB%BA/%E4%B8%8A%E6%B5%B7%E5%B8%82%E4%BD%8F%E6%88%BF%E5%92%8C%E5%9F%8E%E4%B9%A1%E5%BB%BA%E8%AE%BE%E7%AE%A1%E7%90%86%E5%A7%94%E5%91%98%E4%BC%9A%E5%85%B3%E4%BA%8E%E5%BC%80%E5%B1%952026%E2%80%942027%E5%B9%B4%E5%BA%A6%E4%B8%8A%E6%B5%B7%E5%B8%82%E5%BB%BA%E8%AE%BE%E5%B7%A5%E7%A8%8B%E6%96%BD%E5%B7%A5%E5%9B%BE%E8%AE%BE%E8%AE%A1%E6%96%87%E4%BB%B6%E5%AE%A1%E6%9F%A5%E6%9C%BA%E6%9E%84%E8%AE%A4%E5%AE%9A.md) |
| [上海市住房和城乡建设管理委员会关于印发《上海市房屋建筑施工图信息模型（BIM）交付要求》的通知](https://www.shanghai.gov.cn/zhengce/detail?businessId=d7c39dbb0d3d4d5e87f6f2dc5b1da7cb&siteId=0011) | 沪建建管〔2025〕290号 | 上海市住房和城乡建设管理委员会 | 2025-05-30 | ✓ | [正文](docs/%E5%BB%BA%E7%AD%91%E8%AE%BE%E8%AE%A1%E4%B8%8E%E6%8A%A5%E5%BB%BA/%E4%B8%8A%E6%B5%B7%E5%B8%82%E4%BD%8F%E6%88%BF%E5%92%8C%E5%9F%8E%E4%B9%A1%E5%BB%BA%E8%AE%BE%E7%AE%A1%E7%90%86%E5%A7%94%E5%91%98%E4%BC%9A%E5%85%B3%E4%BA%8E%E5%8D%B0%E5%8F%91%E3%80%8A%E4%B8%8A%E6%B5%B7%E5%B8%82%E6%88%BF%E5%B1%8B%E5%BB%BA%E7%AD%91%E6%96%BD%E5%B7%A5%E5%9B%BE%E4%BF%A1%E6%81%AF%E6%A8%A1%E5%9E%8B%EF%BC%88BIM%EF%BC%89%E4%BA%A4%E4%BB%98%E8%A6%81%E6%B1%82%E3%80%8B%E7%9A%84%E9%80%9A%E7%9F%A5.md) |
| [上海市住房和城乡建设管理委员会关于进一步明确本市工程建设项目施工图设计文件审查改革有关要求的通知](https://www.shanghai.gov.cn/zhengce/detail?businessId=f100d1e962294a0da699397877684ea6&siteId=0011) | 沪建建管〔2025〕55号 | 上海市住房和城乡建设管理委员会 | 2025-01-26 | ✓ | [正文](docs/%E5%BB%BA%E7%AD%91%E8%AE%BE%E8%AE%A1%E4%B8%8E%E6%8A%A5%E5%BB%BA/%E4%B8%8A%E6%B5%B7%E5%B8%82%E4%BD%8F%E6%88%BF%E5%92%8C%E5%9F%8E%E4%B9%A1%E5%BB%BA%E8%AE%BE%E7%AE%A1%E7%90%86%E5%A7%94%E5%91%98%E4%BC%9A%E5%85%B3%E4%BA%8E%E8%BF%9B%E4%B8%80%E6%AD%A5%E6%98%8E%E7%A1%AE%E6%9C%AC%E5%B8%82%E5%B7%A5%E7%A8%8B%E5%BB%BA%E8%AE%BE%E9%A1%B9%E7%9B%AE%E6%96%BD%E5%B7%A5%E5%9B%BE%E8%AE%BE%E8%AE%A1%E6%96%87%E4%BB%B6%E5%AE%A1%E6%9F%A5%E6%94%B9%E9%9D%A9%E6%9C%89%E5%85%B3%E8%A6%81%E6%B1%82%E7%9A%84%E9%80%9A%E7%9F%A5.md) |
| [关于印发《上海市人防建设工程施工图设计和审查质量检查工作细则》的通知](https://www.shanghai.gov.cn/zhengce/detail?businessId=6d70099434a24148947652caab4ce5c4&siteId=0026) | 沪国动规〔2023〕3号 | 上海市国防动员办公室 | 2023-11-29 | ✓ | [正文](docs/%E5%BB%BA%E7%AD%91%E8%AE%BE%E8%AE%A1%E4%B8%8E%E6%8A%A5%E5%BB%BA/%E5%85%B3%E4%BA%8E%E5%8D%B0%E5%8F%91%E3%80%8A%E4%B8%8A%E6%B5%B7%E5%B8%82%E4%BA%BA%E9%98%B2%E5%BB%BA%E8%AE%BE%E5%B7%A5%E7%A8%8B%E6%96%BD%E5%B7%A5%E5%9B%BE%E8%AE%BE%E8%AE%A1%E5%92%8C%E5%AE%A1%E6%9F%A5%E8%B4%A8%E9%87%8F%E6%A3%80%E6%9F%A5%E5%B7%A5%E4%BD%9C%E7%BB%86%E5%88%99%E3%80%8B%E7%9A%84%E9%80%9A%E7%9F%A5.md) |

[→ 查看该主题全部条目](index/02-建筑设计与报建.md)

### 抗震与人防

| 标题 | 文号 | 发布机关 | 日期 | 时效 | 正文 / 原件 |
|---|---|---|---|---|---|
| [关于印发《上海市人民防空工程档案管理规定》的通知](https://www.shanghai.gov.cn/zhengce/detail?businessId=ad371e463ee241f48278e5a0a72daf47&siteId=0026) | 沪国动规〔2026〕2号 | 上海市国防动员办公室 | 2026-06-11 | ✓ | [正文](docs/%E6%B6%88%E9%98%B2%E4%B8%8E%E4%BA%BA%E9%98%B2/%E5%85%B3%E4%BA%8E%E5%8D%B0%E5%8F%91%E3%80%8A%E4%B8%8A%E6%B5%B7%E5%B8%82%E4%BA%BA%E6%B0%91%E9%98%B2%E7%A9%BA%E5%B7%A5%E7%A8%8B%E6%A1%A3%E6%A1%88%E7%AE%A1%E7%90%86%E8%A7%84%E5%AE%9A%E3%80%8B%E7%9A%84%E9%80%9A%E7%9F%A5.md) |
| [上海市住房和城乡建设管理委员会关于批准《人民防空工程安全风险评估技术标准》为上海市工程建设规范的通知](https://www.shanghai.gov.cn/zhengce/detail?businessId=44d1af2c147444e8bb3d6c4d1dcab86a&siteId=0011) | 沪建标定〔2025〕135号 | 上海市住房和城乡建设管理委员会 | 2025-03-05 | ✓ | [正文](docs/%E5%B7%A5%E7%A8%8B%E5%BB%BA%E8%AE%BE%E7%AE%A1%E7%90%86/%E4%B8%8A%E6%B5%B7%E5%B8%82%E4%BD%8F%E6%88%BF%E5%92%8C%E5%9F%8E%E4%B9%A1%E5%BB%BA%E8%AE%BE%E7%AE%A1%E7%90%86%E5%A7%94%E5%91%98%E4%BC%9A%E5%85%B3%E4%BA%8E%E6%89%B9%E5%87%86%E3%80%8A%E4%BA%BA%E6%B0%91%E9%98%B2%E7%A9%BA%E5%B7%A5%E7%A8%8B%E5%AE%89%E5%85%A8%E9%A3%8E%E9%99%A9%E8%AF%84%E4%BC%B0%E6%8A%80%E6%9C%AF%E6%A0%87%E5%87%86%E3%80%8B%E4%B8%BA%E4%B8%8A%E6%B5%B7%E5%B8%82%E5%B7%A5%E7%A8%8B%E5%BB%BA%E8%AE%BE%E8%A7%84%E8%8C%83%E7%9A%84%E9%80%9A%E7%9F%A5.md) |
| [关于印发《上海市人民防空工程防护设备检验检测管理办法》的通知](https://www.shanghai.gov.cn/zhengce/detail?businessId=2ece4cf42c6d44a9942cbe9cdff5a295&siteId=0026) | 沪国动规〔2025〕5号 | 上海市国防动员办公室 | 2025-12-30 | ✓ | [正文](docs/%E6%B6%88%E9%98%B2%E4%B8%8E%E4%BA%BA%E9%98%B2/%E5%85%B3%E4%BA%8E%E5%8D%B0%E5%8F%91%E3%80%8A%E4%B8%8A%E6%B5%B7%E5%B8%82%E4%BA%BA%E6%B0%91%E9%98%B2%E7%A9%BA%E5%B7%A5%E7%A8%8B%E9%98%B2%E6%8A%A4%E8%AE%BE%E5%A4%87%E6%A3%80%E9%AA%8C%E6%A3%80%E6%B5%8B%E7%AE%A1%E7%90%86%E5%8A%9E%E6%B3%95%E3%80%8B%E7%9A%84%E9%80%9A%E7%9F%A5.md) |
| [关于印发《上海市人民防空领域行政处罚裁量基准实施办法（2025版）》的通知](https://www.shanghai.gov.cn/zhengce/detail?businessId=e4bb3d835cca4fe0867e34f824fd185b&siteId=0026) | 沪国动规〔2025〕3号 | 上海市国防动员办公室 | 2025-12-05 | ✓ | [正文](docs/%E6%B6%88%E9%98%B2%E4%B8%8E%E4%BA%BA%E9%98%B2/%E5%85%B3%E4%BA%8E%E5%8D%B0%E5%8F%91%E3%80%8A%E4%B8%8A%E6%B5%B7%E5%B8%82%E4%BA%BA%E6%B0%91%E9%98%B2%E7%A9%BA%E9%A2%86%E5%9F%9F%E8%A1%8C%E6%94%BF%E5%A4%84%E7%BD%9A%E8%A3%81%E9%87%8F%E5%9F%BA%E5%87%86%E5%AE%9E%E6%96%BD%E5%8A%9E%E6%B3%95%EF%BC%882025%E7%89%88%EF%BC%89%E3%80%8B%E7%9A%84%E9%80%9A%E7%9F%A5.md) |
| [关于印发《上海市人民防空防护设备管理实施办法》的通知](https://www.shanghai.gov.cn/zhengce/detail?businessId=440927b062ec48fd842de526e6fc53d1&siteId=0026) | 沪国动规〔2025〕2号 | 上海市国防动员办公室 | 2025-10-30 | ✓ | [正文](docs/%E6%B6%88%E9%98%B2%E4%B8%8E%E4%BA%BA%E9%98%B2/%E5%85%B3%E4%BA%8E%E5%8D%B0%E5%8F%91%E3%80%8A%E4%B8%8A%E6%B5%B7%E5%B8%82%E4%BA%BA%E6%B0%91%E9%98%B2%E7%A9%BA%E9%98%B2%E6%8A%A4%E8%AE%BE%E5%A4%87%E7%AE%A1%E7%90%86%E5%AE%9E%E6%96%BD%E5%8A%9E%E6%B3%95%E3%80%8B%E7%9A%84%E9%80%9A%E7%9F%A5.md) |
| [关于印发《上海市人民防空领域轻微违法行为依法不予行政处罚清单》的通知](https://www.shanghai.gov.cn/zhengce/detail?businessId=6f2651e58ab649bf85e5d861425e4e9b&siteId=0026) | 沪国动规〔2025〕1号 | 上海市国防动员办公室 | 2025-07-30 | ✓ | [正文](docs/%E6%B6%88%E9%98%B2%E4%B8%8E%E4%BA%BA%E9%98%B2/%E5%85%B3%E4%BA%8E%E5%8D%B0%E5%8F%91%E3%80%8A%E4%B8%8A%E6%B5%B7%E5%B8%82%E4%BA%BA%E6%B0%91%E9%98%B2%E7%A9%BA%E9%A2%86%E5%9F%9F%E8%BD%BB%E5%BE%AE%E8%BF%9D%E6%B3%95%E8%A1%8C%E4%B8%BA%E4%BE%9D%E6%B3%95%E4%B8%8D%E4%BA%88%E8%A1%8C%E6%94%BF%E5%A4%84%E7%BD%9A%E6%B8%85%E5%8D%95%E3%80%8B%E7%9A%84%E9%80%9A%E7%9F%A5.md) |
| [上海市住房和城乡建设管理委员会关于印发《上海市建筑工程设计文件抗震设防审查管理办法》的通知](https://zjw.sh.gov.cn/gfxwj/20240329/e73493bfaec14851bc904eac1d59e9d4.html) | - | 上海市住房和城乡建设管理委员会 | 2024-03 | ✓ | [正文](docs/%E5%BB%BA%E7%AD%91%E8%AE%BE%E8%AE%A1%E4%B8%8E%E6%8A%A5%E5%BB%BA/%E4%B8%8A%E6%B5%B7%E5%B8%82%E4%BD%8F%E6%88%BF%E5%92%8C%E5%9F%8E%E4%B9%A1%E5%BB%BA%E8%AE%BE%E7%AE%A1%E7%90%86%E5%A7%94%E5%91%98%E4%BC%9A%E5%85%B3%E4%BA%8E%E5%8D%B0%E5%8F%91%E3%80%8A%E4%B8%8A%E6%B5%B7%E5%B8%82%E5%BB%BA%E7%AD%91%E5%B7%A5%E7%A8%8B%E8%AE%BE%E8%AE%A1%E6%96%87%E4%BB%B6%E6%8A%97%E9%9C%87%E8%AE%BE%E9%98%B2%E5%AE%A1%E6%9F%A5%E7%AE%A1%E7%90%86%E5%8A%9E%E6%B3%95%E3%80%8B%E7%9A%84%E9%80%9A%E7%9F%A5.md) |
| [关于印发《上海市重点地区人民防空工程统筹建设管理规定》的通知](https://www.shanghai.gov.cn/zhengce/detail?businessId=2da5ce7e92df467089da954e28784c5a&siteId=0026) | 沪国动规〔2024〕1号 | 上海市国防动员办公室 | 2024-07-03 | ✓ | [正文](docs/%E6%B6%88%E9%98%B2%E4%B8%8E%E4%BA%BA%E9%98%B2/%E5%85%B3%E4%BA%8E%E5%8D%B0%E5%8F%91%E3%80%8A%E4%B8%8A%E6%B5%B7%E5%B8%82%E9%87%8D%E7%82%B9%E5%9C%B0%E5%8C%BA%E4%BA%BA%E6%B0%91%E9%98%B2%E7%A9%BA%E5%B7%A5%E7%A8%8B%E7%BB%9F%E7%AD%B9%E5%BB%BA%E8%AE%BE%E7%AE%A1%E7%90%86%E8%A7%84%E5%AE%9A%E3%80%8B%E7%9A%84%E9%80%9A%E7%9F%A5.md) |

[→ 查看该主题全部条目](index/04-消防与人防.md)

### 施工许可与验收

| 标题 | 文号 | 发布机关 | 日期 | 时效 | 正文 / 原件 |
|---|---|---|---|---|---|
| [上海市住房和城乡建设管理委员会关于开展BIM辅助综合竣工验收的通知](https://www.shanghai.gov.cn/zhengce/detail?businessId=ae9330e3f9a3428588a413d192f2a0f7&siteId=0011) | 沪建建管〔2026〕293号 | 上海市住房和城乡建设管理委员会 | 2026-07-01 | ✓ | [正文](docs/%E5%B7%A5%E7%A8%8B%E5%BB%BA%E8%AE%BE%E7%AE%A1%E7%90%86/%E4%B8%8A%E6%B5%B7%E5%B8%82%E4%BD%8F%E6%88%BF%E5%92%8C%E5%9F%8E%E4%B9%A1%E5%BB%BA%E8%AE%BE%E7%AE%A1%E7%90%86%E5%A7%94%E5%91%98%E4%BC%9A%E5%85%B3%E4%BA%8E%E5%BC%80%E5%B1%95BIM%E8%BE%85%E5%8A%A9%E7%BB%BC%E5%90%88%E7%AB%A3%E5%B7%A5%E9%AA%8C%E6%94%B6%E7%9A%84%E9%80%9A%E7%9F%A5.md) |
| [关于开展2026年度杨浦区工程总承包、全过程工程咨询政策申报的通知](https://www.shanghai.gov.cn/zhengce/detail?businessId=00773563&siteId=0077) | 杨科经〔2026〕13号 | 上海市杨浦区科技和经济委员会 | 2026-07-03 | ✓ | [正文](docs/%E5%B7%A5%E7%A8%8B%E5%BB%BA%E8%AE%BE%E7%AE%A1%E7%90%86/%E5%85%B3%E4%BA%8E%E5%BC%80%E5%B1%952026%E5%B9%B4%E5%BA%A6%E6%9D%A8%E6%B5%A6%E5%8C%BA%E5%B7%A5%E7%A8%8B%E6%80%BB%E6%89%BF%E5%8C%85%E3%80%81%E5%85%A8%E8%BF%87%E7%A8%8B%E5%B7%A5%E7%A8%8B%E5%92%A8%E8%AF%A2%E6%94%BF%E7%AD%96%E7%94%B3%E6%8A%A5%E7%9A%84%E9%80%9A%E7%9F%A5.md) |
| [上海市住房和城乡建设管理委员会关于延长《上海市建设项目工程总承包管理办法》有效期的通知](https://www.shanghai.gov.cn/zhengce/detail?businessId=0e0118fce71542fcb6c3dafe41eee6d0&siteId=0011) | 沪建建管〔2026〕84号 | 上海市住房和城乡建设管理委员会 | 2026-03-10 | ✓ | [正文](docs/%E5%B7%A5%E7%A8%8B%E5%BB%BA%E8%AE%BE%E7%AE%A1%E7%90%86/%E4%B8%8A%E6%B5%B7%E5%B8%82%E4%BD%8F%E6%88%BF%E5%92%8C%E5%9F%8E%E4%B9%A1%E5%BB%BA%E8%AE%BE%E7%AE%A1%E7%90%86%E5%A7%94%E5%91%98%E4%BC%9A%E5%85%B3%E4%BA%8E%E5%BB%B6%E9%95%BF%E3%80%8A%E4%B8%8A%E6%B5%B7%E5%B8%82%E5%BB%BA%E8%AE%BE%E9%A1%B9%E7%9B%AE%E5%B7%A5%E7%A8%8B%E6%80%BB%E6%89%BF%E5%8C%85%E7%AE%A1%E7%90%86%E5%8A%9E%E6%B3%95%E3%80%8B%E6%9C%89%E6%95%88%E6%9C%9F%E7%9A%84%E9%80%9A%E7%9F%A5.md) |
| [关于印发《上海市建筑工程综合竣工验收管理办法》的通知](https://zjw.sh.gov.cn/gfxwj/20251112/f4594be5e90c4facacf5a548cb06717f.html) | - | 上海市住房和城乡建设管理委员会 | 2025-11 | ✓ | [正文](docs/%E5%B7%A5%E7%A8%8B%E5%BB%BA%E8%AE%BE%E7%AE%A1%E7%90%86/%E5%85%B3%E4%BA%8E%E5%8D%B0%E5%8F%91%E3%80%8A%E4%B8%8A%E6%B5%B7%E5%B8%82%E5%BB%BA%E7%AD%91%E5%B7%A5%E7%A8%8B%E7%BB%BC%E5%90%88%E7%AB%A3%E5%B7%A5%E9%AA%8C%E6%94%B6%E7%AE%A1%E7%90%86%E5%8A%9E%E6%B3%95%E3%80%8B%E7%9A%84%E9%80%9A%E7%9F%A5.md) |
| [上海市住房和城乡建设管理委员会关于进一步规范建设单位竣工验收消防查验工作的通知](https://www.shanghai.gov.cn/zhengce/detail?businessId=52453bd2c6a540b8a768847a6e225719&siteId=0011) | 沪建质安〔2025〕173号 | 上海市住房和城乡建设管理委员会 | 2025-03-24 | ✓ | [正文](docs/%E5%B7%A5%E7%A8%8B%E5%BB%BA%E8%AE%BE%E7%AE%A1%E7%90%86/%E4%B8%8A%E6%B5%B7%E5%B8%82%E4%BD%8F%E6%88%BF%E5%92%8C%E5%9F%8E%E4%B9%A1%E5%BB%BA%E8%AE%BE%E7%AE%A1%E7%90%86%E5%A7%94%E5%91%98%E4%BC%9A%E5%85%B3%E4%BA%8E%E8%BF%9B%E4%B8%80%E6%AD%A5%E8%A7%84%E8%8C%83%E5%BB%BA%E8%AE%BE%E5%8D%95%E4%BD%8D%E7%AB%A3%E5%B7%A5%E9%AA%8C%E6%94%B6%E6%B6%88%E9%98%B2%E6%9F%A5%E9%AA%8C%E5%B7%A5%E4%BD%9C%E7%9A%84%E9%80%9A%E7%9F%A5.md) |
| [上海市住房和城乡建设管理委员会关于进一步规范和完善建筑工程施工许可审批管理工作的通知](https://www.shanghai.gov.cn/zhengce/detail?businessId=99e62fa9be3d461d8c6758c6df875073&siteId=0011) | 沪建建管〔2024〕484号 | 上海市住房和城乡建设管理委员会 | 2024-09-19 | ✓ | [正文](docs/%E5%BB%BA%E7%AD%91%E8%AE%BE%E8%AE%A1%E4%B8%8E%E6%8A%A5%E5%BB%BA/%E4%B8%8A%E6%B5%B7%E5%B8%82%E4%BD%8F%E6%88%BF%E5%92%8C%E5%9F%8E%E4%B9%A1%E5%BB%BA%E8%AE%BE%E7%AE%A1%E7%90%86%E5%A7%94%E5%91%98%E4%BC%9A%E5%85%B3%E4%BA%8E%E8%BF%9B%E4%B8%80%E6%AD%A5%E8%A7%84%E8%8C%83%E5%92%8C%E5%AE%8C%E5%96%84%E5%BB%BA%E7%AD%91%E5%B7%A5%E7%A8%8B%E6%96%BD%E5%B7%A5%E8%AE%B8%E5%8F%AF%E5%AE%A1%E6%89%B9%E7%AE%A1%E7%90%86%E5%B7%A5%E4%BD%9C%E7%9A%84%E9%80%9A%E7%9F%A5.md) |
| [上海市住房和城乡建设管理委员会关于修订印发《上海市建设项目工程总承包招标评标办法》的通知](https://zjw.sh.gov.cn/gfxwj/20240329/97df46c3253a42149d1efa714d28a03b.html) | - | 上海市住房和城乡建设管理委员会 | 2024-03 | ✓ | [正文](docs/%E5%B7%A5%E7%A8%8B%E5%BB%BA%E8%AE%BE%E7%AE%A1%E7%90%86/%E4%B8%8A%E6%B5%B7%E5%B8%82%E4%BD%8F%E6%88%BF%E5%92%8C%E5%9F%8E%E4%B9%A1%E5%BB%BA%E8%AE%BE%E7%AE%A1%E7%90%86%E5%A7%94%E5%91%98%E4%BC%9A%E5%85%B3%E4%BA%8E%E4%BF%AE%E8%AE%A2%E5%8D%B0%E5%8F%91%E3%80%8A%E4%B8%8A%E6%B5%B7%E5%B8%82%E5%BB%BA%E8%AE%BE%E9%A1%B9%E7%9B%AE%E5%B7%A5%E7%A8%8B%E6%80%BB%E6%89%BF%E5%8C%85%E6%8B%9B%E6%A0%87%E8%AF%84%E6%A0%87%E5%8A%9E%E6%B3%95%E3%80%8B%E7%9A%84%E9%80%9A%E7%9F%A5.md) |
| [关于印发《上海市造林项目竣工验收办法》的通知](https://www.shanghai.gov.cn/zhengce/detail?businessId=0ca86a93-9fc0-4219-8807-8abd75951fbc&siteId=0039) | 沪绿容〔2024〕182号 | 上海市绿化和市容管理局 | 2024-05-06 | ✓ | [正文](docs/%E5%B7%A5%E7%A8%8B%E5%BB%BA%E8%AE%BE%E7%AE%A1%E7%90%86/%E5%85%B3%E4%BA%8E%E5%8D%B0%E5%8F%91%E3%80%8A%E4%B8%8A%E6%B5%B7%E5%B8%82%E9%80%A0%E6%9E%97%E9%A1%B9%E7%9B%AE%E7%AB%A3%E5%B7%A5%E9%AA%8C%E6%94%B6%E5%8A%9E%E6%B3%95%E3%80%8B%E7%9A%84%E9%80%9A%E7%9F%A5.md) |

[→ 查看该主题全部条目](index/03-工程建设管理.md)

### 绿色建筑与节能

| 标题 | 文号 | 发布机关 | 日期 | 时效 | 正文 / 原件 |
|---|---|---|---|---|---|
| [上海市奉贤区人民政府关于印发《奉贤区海绵城市规划建设管理办法》的通知](https://www.shanghai.gov.cn/zhengce/detail?businessId=00843743&siteId=0084) | 沪奉府发〔2026〕11号 | 上海市奉贤区人民政府 | 2026-01-27 | ✓ | [正文](docs/%E8%A7%84%E5%88%92%E4%B8%8E%E5%9C%9F%E5%9C%B0/%E4%B8%8A%E6%B5%B7%E5%B8%82%E5%A5%89%E8%B4%A4%E5%8C%BA%E4%BA%BA%E6%B0%91%E6%94%BF%E5%BA%9C%E5%85%B3%E4%BA%8E%E5%8D%B0%E5%8F%91%E3%80%8A%E5%A5%89%E8%B4%A4%E5%8C%BA%E6%B5%B7%E7%BB%B5%E5%9F%8E%E5%B8%82%E8%A7%84%E5%88%92%E5%BB%BA%E8%AE%BE%E7%AE%A1%E7%90%86%E5%8A%9E%E6%B3%95%E3%80%8B%E7%9A%84%E9%80%9A%E7%9F%A5.md) |
| [关于印发《金山区海绵城市规划建设管理实施细则》的通知](https://www.shanghai.gov.cn/zhengce/detail?businessId=00816794&siteId=0081) | 金建规〔2026〕1号 | 上海市金山区建设和管理委员会 | 2026-01-07 | ✓ | [正文](docs/%E8%A7%84%E5%88%92%E4%B8%8E%E5%9C%9F%E5%9C%B0/%E5%85%B3%E4%BA%8E%E5%8D%B0%E5%8F%91%E3%80%8A%E9%87%91%E5%B1%B1%E5%8C%BA%E6%B5%B7%E7%BB%B5%E5%9F%8E%E5%B8%82%E8%A7%84%E5%88%92%E5%BB%BA%E8%AE%BE%E7%AE%A1%E7%90%86%E5%AE%9E%E6%96%BD%E7%BB%86%E5%88%99%E3%80%8B%E7%9A%84%E9%80%9A%E7%9F%A5.md) |
| [上海市住房和城乡建设管理委员会关于印发《上海市装配式混凝土建筑工程质量管理规定》的通知](https://zjw.sh.gov.cn/gfxwj/20260407/6ec441a8c774415da7b9076487ffdaa4.html) | - | 上海市住房和城乡建设管理委员会 | 2026-04 | ✓ | [正文](docs/%E5%B7%A5%E7%A8%8B%E5%BB%BA%E8%AE%BE%E7%AE%A1%E7%90%86/%E4%B8%8A%E6%B5%B7%E5%B8%82%E4%BD%8F%E6%88%BF%E5%92%8C%E5%9F%8E%E4%B9%A1%E5%BB%BA%E8%AE%BE%E7%AE%A1%E7%90%86%E5%A7%94%E5%91%98%E4%BC%9A%E5%85%B3%E4%BA%8E%E5%8D%B0%E5%8F%91%E3%80%8A%E4%B8%8A%E6%B5%B7%E5%B8%82%E8%A3%85%E9%85%8D%E5%BC%8F%E6%B7%B7%E5%87%9D%E5%9C%9F%E5%BB%BA%E7%AD%91%E5%B7%A5%E7%A8%8B%E8%B4%A8%E9%87%8F%E7%AE%A1%E7%90%86%E8%A7%84%E5%AE%9A%E3%80%8B%E7%9A%84%E9%80%9A%E7%9F%A5.md) |
| [上海市住房和城乡建设管理委员会关于批准《装配式外挂墙板应用技术标准》为上海市工程建设规范的通知](https://www.shanghai.gov.cn/zhengce/detail?businessId=8d4bff46a30d4de280e319f8332cc898&siteId=0011) | 沪建标定〔2026〕294号 | 上海市住房和城乡建设管理委员会 | 2026-07-01 | ✓ | [正文](docs/%E5%B7%A5%E7%A8%8B%E5%BB%BA%E8%AE%BE%E7%AE%A1%E7%90%86/%E4%B8%8A%E6%B5%B7%E5%B8%82%E4%BD%8F%E6%88%BF%E5%92%8C%E5%9F%8E%E4%B9%A1%E5%BB%BA%E8%AE%BE%E7%AE%A1%E7%90%86%E5%A7%94%E5%91%98%E4%BC%9A%E5%85%B3%E4%BA%8E%E6%89%B9%E5%87%86%E3%80%8A%E8%A3%85%E9%85%8D%E5%BC%8F%E5%A4%96%E6%8C%82%E5%A2%99%E6%9D%BF%E5%BA%94%E7%94%A8%E6%8A%80%E6%9C%AF%E6%A0%87%E5%87%86%E3%80%8B%E4%B8%BA%E4%B8%8A%E6%B5%B7%E5%B8%82%E5%B7%A5%E7%A8%8B%E5%BB%BA%E8%AE%BE%E8%A7%84%E8%8C%83%E7%9A%84%E9%80%9A%E7%9F%A5.md) |
| [上海市住房和城乡建设管理委员会关于加强本市绿色建筑全过程管理的通知](https://zjw.sh.gov.cn/gfxwj/20260413/e35458a3af5c43f2a0cd5b2f3a03a631.html) | - | 上海市住房和城乡建设管理委员会 | 2026-04 | ✓ | [正文](docs/%E6%88%BF%E5%B1%8B%E4%B8%8E%E4%BD%8F%E6%88%BF/%E4%B8%8A%E6%B5%B7%E5%B8%82%E4%BD%8F%E6%88%BF%E5%92%8C%E5%9F%8E%E4%B9%A1%E5%BB%BA%E8%AE%BE%E7%AE%A1%E7%90%86%E5%A7%94%E5%91%98%E4%BC%9A%E5%85%B3%E4%BA%8E%E5%8A%A0%E5%BC%BA%E6%9C%AC%E5%B8%82%E7%BB%BF%E8%89%B2%E5%BB%BA%E7%AD%91%E5%85%A8%E8%BF%87%E7%A8%8B%E7%AE%A1%E7%90%86%E7%9A%84%E9%80%9A%E7%9F%A5.md) |
| [上海市住房和城乡建设管理委员会关于印发上海市绿色建筑全过程管理相关格式文本的通知](https://www.shanghai.gov.cn/zhengce/detail?businessId=63d5b03228d34b55a08786cb4138645e&siteId=0011) | 沪建建材〔2026〕229号 | 上海市住房和城乡建设管理委员会 | 2026-05-26 | ✓ | [正文](docs/%E6%88%BF%E5%B1%8B%E4%B8%8E%E4%BD%8F%E6%88%BF/%E4%B8%8A%E6%B5%B7%E5%B8%82%E4%BD%8F%E6%88%BF%E5%92%8C%E5%9F%8E%E4%B9%A1%E5%BB%BA%E8%AE%BE%E7%AE%A1%E7%90%86%E5%A7%94%E5%91%98%E4%BC%9A%E5%85%B3%E4%BA%8E%E5%8D%B0%E5%8F%91%E4%B8%8A%E6%B5%B7%E5%B8%82%E7%BB%BF%E8%89%B2%E5%BB%BA%E7%AD%91%E5%85%A8%E8%BF%87%E7%A8%8B%E7%AE%A1%E7%90%86%E7%9B%B8%E5%85%B3%E6%A0%BC%E5%BC%8F%E6%96%87%E6%9C%AC%E7%9A%84%E9%80%9A%E7%9F%A5.md) |
| [上海市住房和城乡建设管理委员会关于进一步加强本市超低能耗建筑监督管理的通知](https://www.shanghai.gov.cn/zhengce/detail?businessId=42204a15fbe84d718968112f6114852f&siteId=0011) | 沪建建材〔2026〕66号 | 上海市住房和城乡建设管理委员会 | 2026-02-14 | ✓ | [正文](docs/%E6%88%BF%E5%B1%8B%E4%B8%8E%E4%BD%8F%E6%88%BF/%E4%B8%8A%E6%B5%B7%E5%B8%82%E4%BD%8F%E6%88%BF%E5%92%8C%E5%9F%8E%E4%B9%A1%E5%BB%BA%E8%AE%BE%E7%AE%A1%E7%90%86%E5%A7%94%E5%91%98%E4%BC%9A%E5%85%B3%E4%BA%8E%E8%BF%9B%E4%B8%80%E6%AD%A5%E5%8A%A0%E5%BC%BA%E6%9C%AC%E5%B8%82%E8%B6%85%E4%BD%8E%E8%83%BD%E8%80%97%E5%BB%BA%E7%AD%91%E7%9B%91%E7%9D%A3%E7%AE%A1%E7%90%86%E7%9A%84%E9%80%9A%E7%9F%A5.md) |
| [上海市住房和城乡建设管理委员会关于批准《装配式混凝土居住建筑设计标准》为上海市工程建设规范的通知](https://www.shanghai.gov.cn/zhengce/detail?businessId=2bddab68d3ef4d8ea8eb37b9aab40950&siteId=0011) | 沪建标定〔2025〕613号 | 上海市住房和城乡建设管理委员会 | 2025-12-12 | ✓ | [正文](docs/%E5%BB%BA%E7%AD%91%E8%AE%BE%E8%AE%A1%E4%B8%8E%E6%8A%A5%E5%BB%BA/%E4%B8%8A%E6%B5%B7%E5%B8%82%E4%BD%8F%E6%88%BF%E5%92%8C%E5%9F%8E%E4%B9%A1%E5%BB%BA%E8%AE%BE%E7%AE%A1%E7%90%86%E5%A7%94%E5%91%98%E4%BC%9A%E5%85%B3%E4%BA%8E%E6%89%B9%E5%87%86%E3%80%8A%E8%A3%85%E9%85%8D%E5%BC%8F%E6%B7%B7%E5%87%9D%E5%9C%9F%E5%B1%85%E4%BD%8F%E5%BB%BA%E7%AD%91%E8%AE%BE%E8%AE%A1%E6%A0%87%E5%87%86%E3%80%8B%E4%B8%BA%E4%B8%8A%E6%B5%B7%E5%B8%82%E5%B7%A5%E7%A8%8B%E5%BB%BA%E8%AE%BE%E8%A7%84%E8%8C%83%E7%9A%84%E9%80%9A%E7%9F%A5.md) |

[→ 查看该主题全部条目](index/07-绿色低碳与节能.md)

### 既有建筑与城市更新

| 标题 | 文号 | 发布机关 | 日期 | 时效 | 正文 / 原件 |
|---|---|---|---|---|---|
| [上海市人民政府办公厅关于印发《上海市城市更新和住房发展“十五五”规划》的通知](https://www.shanghai.gov.cn/zhengce/detail?businessId=f584d873f87045148c7eccce1ae637b3&siteId=0001) | 沪府办发〔2026〕15号 | 上海市人民政府办公厅 | 2026-07-28 | ✓ | [正文](docs/%E6%88%BF%E5%B1%8B%E4%B8%8E%E4%BD%8F%E6%88%BF/%E4%B8%8A%E6%B5%B7%E5%B8%82%E4%BA%BA%E6%B0%91%E6%94%BF%E5%BA%9C%E5%8A%9E%E5%85%AC%E5%8E%85%E5%85%B3%E4%BA%8E%E5%8D%B0%E5%8F%91%E3%80%8A%E4%B8%8A%E6%B5%B7%E5%B8%82%E5%9F%8E%E5%B8%82%E6%9B%B4%E6%96%B0%E5%92%8C%E4%BD%8F%E6%88%BF%E5%8F%91%E5%B1%95%E2%80%9C%E5%8D%81%E4%BA%94%E4%BA%94%E2%80%9D%E8%A7%84%E5%88%92%E3%80%8B%E7%9A%84%E9%80%9A%E7%9F%A5.md) |
| [上海市房屋管理局关于印发《上海市国有土地上征收居住房屋室内装饰装修评估分户报告（示范文本）》的通知](https://www.shanghai.gov.cn/zhengce/detail?businessId=816cfe6c251c4eae84804ab5cf7dcaca&siteId=0013) | 沪房市场〔2026〕125号 | 上海市房屋管理局 | 2026-08-11 | ✓ | [正文](docs/%E6%88%BF%E5%B1%8B%E4%B8%8E%E4%BD%8F%E6%88%BF/%E4%B8%8A%E6%B5%B7%E5%B8%82%E6%88%BF%E5%B1%8B%E7%AE%A1%E7%90%86%E5%B1%80%E5%85%B3%E4%BA%8E%E5%8D%B0%E5%8F%91%E3%80%8A%E4%B8%8A%E6%B5%B7%E5%B8%82%E5%9B%BD%E6%9C%89%E5%9C%9F%E5%9C%B0%E4%B8%8A%E5%BE%81%E6%94%B6%E5%B1%85%E4%BD%8F%E6%88%BF%E5%B1%8B%E5%AE%A4%E5%86%85%E8%A3%85%E9%A5%B0%E8%A3%85%E4%BF%AE%E8%AF%84%E4%BC%B0%E5%88%86%E6%88%B7%E6%8A%A5%E5%91%8A%EF%BC%88%E7%A4%BA%E8%8C%83%E6%96%87%E6%9C%AC%EF%BC%89%E3%80%8B%E7%9A%84%E9%80%9A%E7%9F%A5.md) |
| [宝山区既有多层住宅加装电梯设计方案公示工作的指导意见](https://www.shanghai.gov.cn/zhengce/detail?businessId=525719c9-eb5a-4ee0-b209-bcffce063a02&siteId=0078) | 宝规划资源〔2026〕1号 | 上海市宝山区规划和自然资源局 | 2026-06-08 | ✓ | [正文](docs/%E6%88%BF%E5%B1%8B%E4%B8%8E%E4%BD%8F%E6%88%BF/%E5%AE%9D%E5%B1%B1%E5%8C%BA%E6%97%A2%E6%9C%89%E5%A4%9A%E5%B1%82%E4%BD%8F%E5%AE%85%E5%8A%A0%E8%A3%85%E7%94%B5%E6%A2%AF%E8%AE%BE%E8%AE%A1%E6%96%B9%E6%A1%88%E5%85%AC%E7%A4%BA%E5%B7%A5%E4%BD%9C%E7%9A%84%E6%8C%87%E5%AF%BC%E6%84%8F%E8%A7%81.md) |
| [上海市住房和城乡建设管理委员会、上海市市场监督管理局、上海市房屋管理局、上海市装饰装修行业协会、上海市室内装饰行业协会关于推行使用《上海市住宅装饰装修施工合同示范文本》的通知](https://www.shanghai.gov.cn/zhengce/detail?businessId=69f5f927482d43998de868d718e121dc&siteId=0011) | 沪建城管联〔2026〕164号 | 上海市住房和城乡建设管理委员会 | 2026-05-09 | ✓ | [正文](docs/%E6%88%BF%E5%B1%8B%E4%B8%8E%E4%BD%8F%E6%88%BF/%E4%B8%8A%E6%B5%B7%E5%B8%82%E4%BD%8F%E6%88%BF%E5%92%8C%E5%9F%8E%E4%B9%A1%E5%BB%BA%E8%AE%BE%E7%AE%A1%E7%90%86%E5%A7%94%E5%91%98%E4%BC%9A%E3%80%81%E4%B8%8A%E6%B5%B7%E5%B8%82%E5%B8%82%E5%9C%BA%E7%9B%91%E7%9D%A3%E7%AE%A1%E7%90%86%E5%B1%80%E3%80%81%E4%B8%8A%E6%B5%B7%E5%B8%82%E6%88%BF%E5%B1%8B%E7%AE%A1%E7%90%86%E5%B1%80%E3%80%81%E4%B8%8A%E6%B5%B7%E5%B8%82%E8%A3%85%E9%A5%B0%E8%A3%85%E4%BF%AE%E8%A1%8C%E4%B8%9A%E5%8D%8F%E4%BC%9A%E3%80%81%E4%B8%8A%E6%B5%B7.md) |
| [闵行区人民政府关于印发《闵行区城市更新“十五五”规划》的通知](https://www.shanghai.gov.cn/zhengce/detail?businessId=9ce0e2a0-ff5a-41c8-9e91-341424340c4c&siteId=0079) | 闵府发〔2026〕26号 | 上海市闵行区人民政府 | 2026-07-28 | ✓ | [正文](docs/%E5%9F%8E%E5%B8%82%E6%9B%B4%E6%96%B0%E4%B8%8E%E5%8E%86%E5%8F%B2%E4%BF%9D%E6%8A%A4/%E9%97%B5%E8%A1%8C%E5%8C%BA%E4%BA%BA%E6%B0%91%E6%94%BF%E5%BA%9C%E5%85%B3%E4%BA%8E%E5%8D%B0%E5%8F%91%E3%80%8A%E9%97%B5%E8%A1%8C%E5%8C%BA%E5%9F%8E%E5%B8%82%E6%9B%B4%E6%96%B0%E2%80%9C%E5%8D%81%E4%BA%94%E4%BA%94%E2%80%9D%E8%A7%84%E5%88%92%E3%80%8B%E7%9A%84%E9%80%9A%E7%9F%A5.md) |
| [黄浦区人民政府办公室关于印发 《黄浦区城市更新“十五五”规划》的通知](https://www.shanghai.gov.cn/zhengce/detail?businessId=1183fecf-8084-4ada-9aef-3115e4f9deb6&siteId=0071) | 黄府办发〔2026〕12号 | 上海市黄浦区人民政府办公室 | 2026-07-02 | ✓ | [正文](docs/%E5%9F%8E%E5%B8%82%E6%9B%B4%E6%96%B0%E4%B8%8E%E5%8E%86%E5%8F%B2%E4%BF%9D%E6%8A%A4/%E9%BB%84%E6%B5%A6%E5%8C%BA%E4%BA%BA%E6%B0%91%E6%94%BF%E5%BA%9C%E5%8A%9E%E5%85%AC%E5%AE%A4%E5%85%B3%E4%BA%8E%E5%8D%B0%E5%8F%91%20%E3%80%8A%E9%BB%84%E6%B5%A6%E5%8C%BA%E5%9F%8E%E5%B8%82%E6%9B%B4%E6%96%B0%E2%80%9C%E5%8D%81%E4%BA%94%E4%BA%94%E2%80%9D%E8%A7%84%E5%88%92%E3%80%8B%E7%9A%84%E9%80%9A%E7%9F%A5.md) |
| [上海市住房和城乡建设管理委员会关于批准《优秀历史建筑数字化测绘技术标准》为上海市工程建设规范的通知](https://www.shanghai.gov.cn/zhengce/detail?businessId=4853f556bce74c938b66de1eee65d0cb&siteId=0011) | 沪建标定〔2025〕300号 | 上海市住房和城乡建设管理委员会 | 2025-06-11 | ✓ | [正文](docs/%E8%A7%84%E5%88%92%E4%B8%8E%E5%9C%9F%E5%9C%B0/%E4%B8%8A%E6%B5%B7%E5%B8%82%E4%BD%8F%E6%88%BF%E5%92%8C%E5%9F%8E%E4%B9%A1%E5%BB%BA%E8%AE%BE%E7%AE%A1%E7%90%86%E5%A7%94%E5%91%98%E4%BC%9A%E5%85%B3%E4%BA%8E%E6%89%B9%E5%87%86%E3%80%8A%E4%BC%98%E7%A7%80%E5%8E%86%E5%8F%B2%E5%BB%BA%E7%AD%91%E6%95%B0%E5%AD%97%E5%8C%96%E6%B5%8B%E7%BB%98%E6%8A%80%E6%9C%AF%E6%A0%87%E5%87%86%E3%80%8B%E4%B8%BA%E4%B8%8A%E6%B5%B7%E5%B8%82%E5%B7%A5%E7%A8%8B%E5%BB%BA%E8%AE%BE%E8%A7%84%E8%8C%83%E7%9A%84%E9%80%9A%E7%9F%A5.md) |
| [上海市住房和城乡建设管理委员会关于印发《上海市既有建筑装饰装修工程建设程序若干规定》的通知](https://zjw.sh.gov.cn/gfxwj/20250925/ff0c97d945a243cc9133ca6f52d6d326.html) | - | 上海市住房和城乡建设管理委员会 | 2025-09 | ✓ | [正文](docs/%E5%B7%A5%E7%A8%8B%E5%BB%BA%E8%AE%BE%E7%AE%A1%E7%90%86/%E4%B8%8A%E6%B5%B7%E5%B8%82%E4%BD%8F%E6%88%BF%E5%92%8C%E5%9F%8E%E4%B9%A1%E5%BB%BA%E8%AE%BE%E7%AE%A1%E7%90%86%E5%A7%94%E5%91%98%E4%BC%9A%E5%85%B3%E4%BA%8E%E5%8D%B0%E5%8F%91%E3%80%8A%E4%B8%8A%E6%B5%B7%E5%B8%82%E6%97%A2%E6%9C%89%E5%BB%BA%E7%AD%91%E8%A3%85%E9%A5%B0%E8%A3%85%E4%BF%AE%E5%B7%A5%E7%A8%8B%E5%BB%BA%E8%AE%BE%E7%A8%8B%E5%BA%8F%E8%8B%A5%E5%B9%B2%E8%A7%84%E5%AE%9A%E3%80%8B%E7%9A%84%E9%80%9A%E7%9F%A5.md) |

[→ 查看该主题全部条目](index/06-城市更新与历史保护.md)

### 房屋与住宅

| 标题 | 文号 | 发布机关 | 日期 | 时效 | 正文 / 原件 |
|---|---|---|---|---|---|
| [关于印发《虹口区住宅小区物业服务评价激励实施意见》的通知](https://www.shanghai.gov.cn/zhengce/detail?businessId=f3a3d159-da79-4d3f-9f09-6f0133bf34a9&siteId=0076) | 虹房管规〔2026〕1号 | 上海市虹口区住房保障和房屋管理局 | 2026-07-23 | ✓ | [正文](docs/%E6%88%BF%E5%B1%8B%E4%B8%8E%E4%BD%8F%E6%88%BF/%E5%85%B3%E4%BA%8E%E5%8D%B0%E5%8F%91%E3%80%8A%E8%99%B9%E5%8F%A3%E5%8C%BA%E4%BD%8F%E5%AE%85%E5%B0%8F%E5%8C%BA%E7%89%A9%E4%B8%9A%E6%9C%8D%E5%8A%A1%E8%AF%84%E4%BB%B7%E6%BF%80%E5%8A%B1%E5%AE%9E%E6%96%BD%E6%84%8F%E8%A7%81%E3%80%8B%E7%9A%84%E9%80%9A%E7%9F%A5.md) |
| [关于印发《关于建立住宅小区业主委员会秘书制度的实施意见（试行）》的通知](https://www.shanghai.gov.cn/zhengce/detail?businessId=3eecb53566cf4e0c86869199d4bd0b56&siteId=0013) | 沪房物业〔2026〕84号 | 上海市房屋管理局 | 2026-06-04 | ✓ | [正文](docs/%E6%88%BF%E5%B1%8B%E4%B8%8E%E4%BD%8F%E6%88%BF/%E5%85%B3%E4%BA%8E%E5%8D%B0%E5%8F%91%E3%80%8A%E5%85%B3%E4%BA%8E%E5%BB%BA%E7%AB%8B%E4%BD%8F%E5%AE%85%E5%B0%8F%E5%8C%BA%E4%B8%9A%E4%B8%BB%E5%A7%94%E5%91%98%E4%BC%9A%E7%A7%98%E4%B9%A6%E5%88%B6%E5%BA%A6%E7%9A%84%E5%AE%9E%E6%96%BD%E6%84%8F%E8%A7%81%EF%BC%88%E8%AF%95%E8%A1%8C%EF%BC%89%E3%80%8B%E7%9A%84%E9%80%9A%E7%9F%A5.md) |
| [关于印发《关于完善本市住宅小区业主大会、业主委员会规范化建设的实施意见》的通知](https://www.shanghai.gov.cn/zhengce/detail?businessId=b81adff0389b4a7c9ecb99bc0b3594dc&siteId=0013) | 沪房物业〔2026〕36号 | 上海市房屋管理局 | 2026-03-30 | ✓ | [正文](docs/%E6%88%BF%E5%B1%8B%E4%B8%8E%E4%BD%8F%E6%88%BF/%E5%85%B3%E4%BA%8E%E5%8D%B0%E5%8F%91%E3%80%8A%E5%85%B3%E4%BA%8E%E5%AE%8C%E5%96%84%E6%9C%AC%E5%B8%82%E4%BD%8F%E5%AE%85%E5%B0%8F%E5%8C%BA%E4%B8%9A%E4%B8%BB%E5%A4%A7%E4%BC%9A%E3%80%81%E4%B8%9A%E4%B8%BB%E5%A7%94%E5%91%98%E4%BC%9A%E8%A7%84%E8%8C%83%E5%8C%96%E5%BB%BA%E8%AE%BE%E7%9A%84%E5%AE%9E%E6%96%BD%E6%84%8F%E8%A7%81%E3%80%8B%E7%9A%84%E9%80%9A%E7%9F%A5.md) |
| [关于印发《关于住宅小区业主大会账户资金及管理责任年度审计工作的实施意见》的通知](https://www.shanghai.gov.cn/zhengce/detail?businessId=fdf49964c58143fb9ef776f45e716c96&siteId=0013) | 沪房规范〔2025〕9号 | 上海市房屋管理局 | 2025-12-31 | ✓ | [正文](docs/%E6%88%BF%E5%B1%8B%E4%B8%8E%E4%BD%8F%E6%88%BF/%E5%85%B3%E4%BA%8E%E5%8D%B0%E5%8F%91%E3%80%8A%E5%85%B3%E4%BA%8E%E4%BD%8F%E5%AE%85%E5%B0%8F%E5%8C%BA%E4%B8%9A%E4%B8%BB%E5%A4%A7%E4%BC%9A%E8%B4%A6%E6%88%B7%E8%B5%84%E9%87%91%E5%8F%8A%E7%AE%A1%E7%90%86%E8%B4%A3%E4%BB%BB%E5%B9%B4%E5%BA%A6%E5%AE%A1%E8%AE%A1%E5%B7%A5%E4%BD%9C%E7%9A%84%E5%AE%9E%E6%96%BD%E6%84%8F%E8%A7%81%E3%80%8B%E7%9A%84%E9%80%9A%E7%9F%A5.md) |
| [上海市房屋管理局关于印发《上海市住宅小区公共收益管理办法》的通知](https://www.shanghai.gov.cn/zhengce/detail?businessId=8b8ad0526ae94db8a6c61b8aa6caf0c2&siteId=0013) | 沪房规范〔2025〕8号 | 上海市房屋管理局 | 2025-12-31 | ✓ | [正文](docs/%E6%88%BF%E5%B1%8B%E4%B8%8E%E4%BD%8F%E6%88%BF/%E4%B8%8A%E6%B5%B7%E5%B8%82%E6%88%BF%E5%B1%8B%E7%AE%A1%E7%90%86%E5%B1%80%E5%85%B3%E4%BA%8E%E5%8D%B0%E5%8F%91%E3%80%8A%E4%B8%8A%E6%B5%B7%E5%B8%82%E4%BD%8F%E5%AE%85%E5%B0%8F%E5%8C%BA%E5%85%AC%E5%85%B1%E6%94%B6%E7%9B%8A%E7%AE%A1%E7%90%86%E5%8A%9E%E6%B3%95%E3%80%8B%E7%9A%84%E9%80%9A%E7%9F%A5.md) |
| [关于印发《闵行区老旧公房小区物业管理共建活动实施办法》的通知](https://www.shanghai.gov.cn/zhengce/detail?businessId=eb985076-e7f0-4931-95ca-1abc91ac9f67&siteId=0079) | 闵房管规字〔2025〕1号 | 上海市闵行区住房保障和房屋管理局 | 2025-11-28 | ✓ | [正文](docs/%E6%88%BF%E5%B1%8B%E4%B8%8E%E4%BD%8F%E6%88%BF/%E5%85%B3%E4%BA%8E%E5%8D%B0%E5%8F%91%E3%80%8A%E9%97%B5%E8%A1%8C%E5%8C%BA%E8%80%81%E6%97%A7%E5%85%AC%E6%88%BF%E5%B0%8F%E5%8C%BA%E7%89%A9%E4%B8%9A%E7%AE%A1%E7%90%86%E5%85%B1%E5%BB%BA%E6%B4%BB%E5%8A%A8%E5%AE%9E%E6%96%BD%E5%8A%9E%E6%B3%95%E3%80%8B%E7%9A%84%E9%80%9A%E7%9F%A5.md) |
| [莘庄镇人民政府关于印发《莘庄镇住宅小区业委会规范化运作综合评估工作实施方案》的通知](https://www.shanghai.gov.cn/zhengce/detail?businessId=00ddcfe7-f49c-443a-87a8-a8bb435885ca&siteId=0079) | 闵莘府发〔2025〕4号 | 上海市闵行区莘庄镇人民政府 | 2025-11-07 | ✓ | [正文](docs/%E6%88%BF%E5%B1%8B%E4%B8%8E%E4%BD%8F%E6%88%BF/%E8%8E%98%E5%BA%84%E9%95%87%E4%BA%BA%E6%B0%91%E6%94%BF%E5%BA%9C%E5%85%B3%E4%BA%8E%E5%8D%B0%E5%8F%91%E3%80%8A%E8%8E%98%E5%BA%84%E9%95%87%E4%BD%8F%E5%AE%85%E5%B0%8F%E5%8C%BA%E4%B8%9A%E5%A7%94%E4%BC%9A%E8%A7%84%E8%8C%83%E5%8C%96%E8%BF%90%E4%BD%9C%E7%BB%BC%E5%90%88%E8%AF%84%E4%BC%B0%E5%B7%A5%E4%BD%9C%E5%AE%9E%E6%96%BD%E6%96%B9%E6%A1%88%E3%80%8B%E7%9A%84%E9%80%9A%E7%9F%A5.md) |
| [关于加强本市住宅物业管理与城管执法群租治理联动工作的通知](https://www.shanghai.gov.cn/zhengce/detail?businessId=41ed0c26bf464758af5c4620e2e85129&siteId=0013) | 沪房市场〔2025〕179号 | 上海市房屋管理局 | 2025-10-23 | ✓ | [正文](docs/%E6%88%BF%E5%B1%8B%E4%B8%8E%E4%BD%8F%E6%88%BF/%E5%85%B3%E4%BA%8E%E5%8A%A0%E5%BC%BA%E6%9C%AC%E5%B8%82%E4%BD%8F%E5%AE%85%E7%89%A9%E4%B8%9A%E7%AE%A1%E7%90%86%E4%B8%8E%E5%9F%8E%E7%AE%A1%E6%89%A7%E6%B3%95%E7%BE%A4%E7%A7%9F%E6%B2%BB%E7%90%86%E8%81%94%E5%8A%A8%E5%B7%A5%E4%BD%9C%E7%9A%84%E9%80%9A%E7%9F%A5.md) |

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
