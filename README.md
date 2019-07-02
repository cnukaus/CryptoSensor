pyspider based cryptoSensor

## to do list
#### 1. 值得分析并自动匹配答案的市场:Augur，类似https://predictions.global/augur-markets/-will-the-moon-exist-at-end-of-april-24th-0x156eedfa2d05548ae41e7dda34d2b09e2a2f6132 还有50%Fee的利润模型\
#### 2. cok wechat recovery to do text analysis 
(key group for time series of MX, Kcash, LAMB, BOLT, ANKR, BIKI, RIF, MVT, VBT, VDS, FDS
#### 3.最低风险量化在DAI

模型的灵感来自于 Willy Woo 的工作，Willy 第一个提出使用谷歌趋势服务的数据来预测比特币价格的走向。
新闻检测价格模型：https://www.kaggle.com/c/two-sigma-financial-news
市场预判
套利判定：peregrine或https://hackernoon.com/bch-pre-fork-arbitrage-trading-idea-fcac026255d5
套利执行：Triangle-arbitrage.



多币种共存只会愈演愈烈，比特币相对份额将继续下跌，传统Quant的势力未必足以覆盖niche币种（他们觉得只有比特币有足够量化数据？）.机构投资者短期仍决定走势但长期未必（Lawmaster看Grayscale Bitcoin Trust流入判断机构投资者）

按有效市场理论，趋势不可预测，但是可以及时检测并利用。The charts never lie or die (nor give you any useful strategic decision support) 






基本面数据
团队背景，技术实力，规划，生态
技术面数据
资金，价格波动，市场情绪，炒作hype


从Loom/ENJ走势可以看出技术实力未必能决定中期走势（6个月-1年）。近期价格和大资金及市场追捧关系更大(辣鸡PAI, WICC, Incompetent TRON)，所以以上两套检测标准必须并行。




假设：有些平台和Key Opinion Leader是更有效的

What is Effective: Scammer and bad (how to define?) opinion leader can be effective

拟监测：TG, Cryptopanic, Coinmetrics.io, Exchange公告/API监控原型urlmonitor
热点：discord power user是哪些，移动到哪个主题/币种,coinbase公告
市场热度：老Twitter/微博用户第一次提起BTC 人/天；王团长的阅读量;

可（作为兴趣研发）：白皮书\MileStone和实际进度的自动语义匹配；团队人员的变动(Linkedin, 媒体通告）；关键coder类似BM是否身兼多值。各支持资本的风格

有伪命题要排除（ not washing trading. 新近辞职-重大未披露？/早期宣传airdop/豪羊毛力度、早期持币成本）


其他可选方向：
看算力（约等于资金）认同哪个算法，最后哪个算法能更高效地自循环（促进经济循环，然后吸引到更多算力）。算力比市场资金对热点先敏感
交易所价差
市场交易之外获得Top100 Crypto的机会（quiz, faucet, airdrop)
场外交易数据（抹茶，CEO,火狐狸？）

可用数据集： [ETH data] (https://console.cloud.google.com/bigquery?project=aqueous-charger-188403&folder&organizationId&p=bigquery-public-data&d=crypto_ethereum_classic&page=dataset) (注意改过名字） 大约季度更新



维度通用分类：
币种级别coinmarketcap筛选：两个宏观量：市值爬升/Total Cap (of top 100)；大额交易占比
1.创始人过往经验，能力和声誉
2.团队的技术厚度，广度，营销能力
3.技术线路-vision,已有突破
4.项目资源-已募集资金，dapp,行业合作伙伴，可核实的board或advisor
5.项目前景-是否已有竞争对手


Tested metrics in 2018 prototype design

