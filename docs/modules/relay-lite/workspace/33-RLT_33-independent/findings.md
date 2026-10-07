# 事实与决定

F1：当前 #151/#153 已有合入成果，但卡级出口与 #154 设计属原会话，迁移不代签。
F2：来源最新远端含默认模型；主 checkout 同时前进，本卡固定远端而非并发主树。
F3：历史留原仓及新仓只读副本，Git历史通过完整源SHA/路径可回查；新仓不开完整模式，也不偷偷启动旧计划。

F4：独立方案初审两P1（迁移闭集/负向验收）已补948项清单与兼容矩阵，原reviewer定向PASS；review.plan.md留原REVISE及复审。
F5：旧全量基线因源产品删除在运行中而无效，不是业务RED；已停止，日志保留。冻结相关44测试另跑GREEN，不冒充整套旧模式全回归。

F6：source PowerShell回归末尾专属relay-light-log.ps1发现对退役产品的路径依赖；必要联动只改该专属suite为退役断言，Runner套件和入口不删、不skip。证据source-pwsh-before.log，复验待补。

F7：源CI观察项relay-core在npm test（08:54:04 UTC）持续未退出；三项必需检查已绿。为让本卡workflow能有终态，CI范围内只为该现有观察测试命令加180秒timeout，保持job continue-on-error、不删任何必需检查、不修暂停中的产品。旧run待新同分支push按既有concurrency取消并保留远端历史；timeout不声称relay-core测试通过。

F8（待用户决定）：source主树被原维护会话继续更新AW_07总表，当前未推master=5a47a4f98d01e77f9a78994765dc59d8b54dd6a5；与冻结origin/master的唯一docs/relay差异是上述AW总表。为不覆盖唯一维护会话或迁移旧状态，已询问本次切换或原卡交棒后切换。最新表原字节取证独立保留(evidence/live-source-readback.json)，未擅自同步/清理/重置主树，未向维护人越权发消息。两PR保留Draft，等答复后采取依赖动作。

F9：用户选择本次迁移最新总表并协调维护会话。AW 额外快照5a47a4f98d01e77f9a78994765dc59d8b54dd6a5已保留；原会话消息接口返回 active writer，通知未送达，未假称收到确认。当前不在 Herdr pane，未从外部控制其终端；须可用会话消息渠道或维护者回执闭合切换。

F10：两原维护者ACK收到（evidence/*cutover-ack.md）；WFP原维护者提供PR158/65f87a0未合入最新记录，本次按用户迁最新指示收录，而非宣称source master已有；源PR158暂停，由原维护者自行后续处置。本卡不修改/关闭其PR。

F11：交付前发现迁移测试不应永久冻结可维护live总表；将字节审计绑定本仓首次最新表迁入9458e4f并校祖先，而非每次当前表body==快照。历史source/archive与import证据保持，避免以后正常维护被CI误拒。新包安装运行不依赖git；这项迁移审计测试需要本独立仓普通完整Git clone，不访问source仓。

F8/F9闭合：用户明确迁最新表并授权自行传达；原维护者暂停和active-path ACK均已收到。AW5a47/WFP未合入PR158-65f87a0额外精确源固定在table-cutover.json；新PR2合入、源PR157退休并无损同步后已发送恢复通知，AW已回执；WFP通知第19次成功投递，不当作恢复ACK。旧PR158与原业务失败/人判由原维护者自行处理，RLT_33不迁其业务写权。
