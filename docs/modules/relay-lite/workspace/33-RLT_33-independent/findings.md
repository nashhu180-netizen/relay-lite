# 事实与决定

F1：当前 #151/#153 已有合入成果，但卡级出口与 #154 设计属原会话，迁移不代签。
F2：来源最新远端含默认模型；主 checkout 同时前进，本卡固定远端而非并发主树。
F3：历史留原仓及新仓只读副本，Git历史通过完整源SHA/路径可回查；新仓不开完整模式，也不偷偷启动旧计划。

F4：独立方案初审两P1（迁移闭集/负向验收）已补948项清单与兼容矩阵，原reviewer定向PASS；review.plan.md留原REVISE及复审。
F5：旧全量基线因源产品删除在运行中而无效，不是业务RED；已停止，日志保留。冻结相关44测试另跑GREEN，不冒充整套旧模式全回归。

F6：source PowerShell回归末尾专属relay-light-log.ps1发现对退役产品的路径依赖；必要联动只改该专属suite为退役断言，Runner套件和入口不删、不skip。证据source-pwsh-before.log，复验待补。

F7：源CI观察项relay-core在npm test（08:54:04 UTC）持续未退出；三项必需检查已绿。为让本卡workflow能有终态，CI范围内只为该现有观察测试命令加180秒timeout，保持job continue-on-error、不删任何必需检查、不修暂停中的产品。旧run待新同分支push按既有concurrency取消并保留远端历史；timeout不声称relay-core测试通过。
