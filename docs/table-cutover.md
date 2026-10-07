# 现役总表切换回执

用户2026-10-07确认：“本次迁移最新总表，并协调原维护会话切换到新仓”。本卡仅迁移路径，原维护会话、业务状态、授权、信号和下一步不变。

目前状态：独立仓PR2已经合入7a3346f；两原维护者各核最新源正文同字节，更新原execution_strategy到新绝对路径，维护权不变。源PR157已退休旧表（8cbff63），本地主树普通merge保留全部未推历史5a47，未推无关提交。原表不再是现役写入点，不并写。切换正文与固定9458e4f快照审计见table-cutover.json。

| 表 | 原唯一维护者 | 新权威路径 | 暂停 / 新路径证据 | 恢复维护 |
|---|---|---|---|---|
| AW | AW_07 orchestrator#2 | /home/nash/work/relay-lite/docs/relay/agent-playground/agent-workbench/aw-mvp/relay_plan.md | evidence/rlt33-aw07-cutover-ack.md、active-ack.md | resumed-ack.md已收，原维护者独立分支维护，主干未改 |
| WFP | WFP_08 wfp08-orch / w6F:p1 | /home/nash/work/relay-lite/docs/relay/wf-analytics-platform/workflow-platform/wfp-p1-obd-p5/relay_plan.md | evidence/rlt33-wfp-cutover-ack.md、active-ack.md | resumed-ack.md已收，原维护者恢复新表维护 |

消息投递曾因active writer拒绝，用户明确授权自行传达后，核实际Herdr原session/pane提交通知。恢复通知WFP曾因原业务交互blocked拒绝，限定UUID短时排队在可接收时第19次成功投递；未代答业务对话。AW/WFP恢复ACK均已收到，通知投递和维护确认分开保留。

切换不会授权下一卡、部署、环境操作或当前角色模型变更；新角色名称映射须按skill登记，不改既有signal。

消息通道补充：用户明确要求“你想办法传达消息给他们”后，按既有session和核对后的实际身份使用Herdr终端通道：AW w62:p1提交并观察1583→1587/working；WFP实际已迁至w6F:p1，身份核对后提交，原已working，等待独立回执才证明处理。没有新建/重启/关闭终端。此通知不是回执，不提前切换。

2026-10-07暂停回执齐备：AW确认5a47主树无未提交改动；WFP确认PR158未合入65f87a0是其最新表，并暂停该PR合入；其delta已按原字节固定。两份回执在本卡evidence保存，字段hash见JSON。接下来按最新CI/复核合入新仓，然后由原维护者确认路径；旧仓退休及本地无损同步后通知恢复写入。

保真测试审计固定import_commit=9458e4f的新仓迁入版本，而不是永久冻结现役可维护表；验证该提交属于本仓历史、每表迁入正文与最新源快照同字节/hash。原维护者后续更新live表不改迁移快照/用户历史授权证据，未来CI不会因正常维护状态前进而拒绝。迁移库存archive仍逐字保留。

2026-10-07最终切换：两份active-path ACK与AW resumed ACK已存本卡evidence。原业务后续行同步由原维护者独立进行，RLT_33不改表体；AW新分支和WFP旧PR158均非本卡清理对象。

WFP最终恢复回执：evidence/rlt33-wfp-cutover-resumed-ack.md；新表唯一现役，wfp08-orch w6F:p1维护权保持。旧PR158仍OPEN由其原合同处理，不合入退休旧路径，不代签WFP人验。
