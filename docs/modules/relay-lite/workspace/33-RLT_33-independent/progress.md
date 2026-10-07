# 进度

2026-10-07：Issue 两仓建立；源冻结 2246b16；新仓空提交初始化，两仓任务树已建。待方案复核后实施。

2026-10-07 实施：948 文件库存固定，历史 937 文件 archive 原字节保存；新协议/两 adapter/安装器/watch脚本/模板/两表已迁入。新仓39测试PASS（evidence/local-tests.log）；冻结源2246b16相关44测试PASS（evidence/frozen-baseline.log）。最初全量旧账本基线在退休删除并发读取后失效并终止，保留 invalidated-baseline.log，不用于归因/放行；有效相关基线另在冻结Git副本运行。源Runner PowerShell回归仍进行中。

2026-10-07：源专属suite路径耦合已替换，完整PowerShell回归 RELAY ALL PASS (SKIPPED: 1)，证据source-pwsh-final.log；孤立Git clone39测试PASS，证据isolated-clone-tests.log。新仓大包两次HTTP408，远端仍c6daa0c，未假称推送成功；source d8f88ae已推，CI进行中。

2026-10-07：五路独立报告PASS，代码轮2选点；隔离db18185 clone执行install_all预检删环，指定测试真正AssertionError RED，原字节恢复后GREEN。三次大包HTTP408历史保留，分批同卡上传对象后正式分支已读回db18185；临时branch尚待cleanup。新仓Windows/Ubuntu CI37597719316成功；源观察项挂起新增180s上限后等最新run。

2026-10-07：新仓两系统CI通过，源完整CI已终止；必需三job成功，relay-core观察项timeout保留FAILURE，workflow结论需记录success读回。发现AW_07原维护者继续写source本地主树（未推提交），已向用户集中询问总表切换时机；dependent merge/主树同步/cleanup暂不执行。代码/库存/五路/变异证据不冒充完成。

2026-10-07：源workflow37598189335结论SUCCESS读回（观察项FAILURE保持）；用户确认本次迁入最新AW表。补充表候选与cutover清单已写，原维护会话通知未送达（active writer），旧表仍权威；等待确认后合入，未改源主树。

2026-10-07：用户要求自行传达；已核原session IDs，Herdr现有终端AW w62:p1投递并working/seq前进；WFP已迁w6F:p1投递，等待两方durable ack，不把agent_prompted当维护确认。

2026-10-07：AW/WFP暂停ACK均收到；WFP追加原维护者未合入PR158/65f87a0原字节快照，新候选两表依照各自最新源和回执迁入。等待定向复核/最新CI后合入独立仓；原维护权保持，源主树未动。
