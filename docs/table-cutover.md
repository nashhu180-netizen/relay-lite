# 现役总表切换回执

用户2026-10-07确认：“本次迁移最新总表，并协调原维护会话切换到新仓”。本卡仅迁移路径，原维护会话、业务状态、授权、信号和下一步不变。

目前状态：两原维护者已回执暂停旧表，最新两表候选已保存；旧表在新仓合入及原维护者确认路径前仍权威；禁止并写。`table-cutover.json`保存快照与哈希。AW原会话01a11500-d7f7-7e52-85e6-cb8459427549、WFP恢复会话01a11599-07ad-7b93-8097-042301220688，两次消息调用都返回“thread already has an active writer”，不算送达。当前不在Herdr pane，未从外部控制会话。

原维护者确认暂停旧表后，核对其提交及未提交改动；如源前进，追加精确快照/哈希并复核新变化。新仓PR2合入及合入态测试通过后，再由原维护者修改各自execution_strategy的总表路径，核对行状态/证据/下一步/日期并确认恢复；源PR157退休原表在切换确认后合入。未得到原维护者回执不宣称迁移完成。旧仓本地主树未推提交完整保留，不reset、不把无关提交推送为本卡成果。

| 表 | 原维护者 | 新路径 | 暂停回执 | 恢复新路径回执 |
|---|---|---|---|---|
| AW | AW_07 orchestrator#2 | /home/nash/work/relay-lite/docs/relay/agent-playground/agent-workbench/aw-mvp/relay_plan.md | 已收 evidence/rlt33-aw07-cutover-ack.md | 待新仓合入后由原维护者确认 |
| WFP | WFP_08 orchestrator | /home/nash/work/relay-lite/docs/relay/wf-analytics-platform/workflow-platform/wfp-p1-obd-p5/relay_plan.md | 已收 evidence/rlt33-wfp-cutover-ack.md | 待新仓合入后由原维护者确认 |

切换不会授权下一卡、部署、环境操作或当前角色模型变更；新角色名称映射须按skill登记，不改既有signal。

消息通道补充：用户明确要求“你想办法传达消息给他们”后，按既有session和核对后的实际身份使用Herdr终端通道：AW w62:p1提交并观察1583→1587/working；WFP实际已迁至w6F:p1，身份核对后提交，原已working，等待独立回执才证明处理。没有新建/重启/关闭终端。此通知不是回执，不提前切换。

2026-10-07暂停回执齐备：AW确认5a47主树无未提交改动；WFP确认PR158未合入65f87a0是其最新表，并暂停该PR合入；其delta已按原字节固定。两份回执在本卡evidence保存，字段hash见JSON。接下来按最新CI/复核合入新仓，然后由原维护者确认路径；旧仓退休及本地无损同步后通知恢复写入。

保真测试审计固定import_commit=9458e4f的新仓迁入版本，而不是永久冻结现役可维护表；验证该提交属于本仓历史、每表迁入正文与最新源快照同字节/hash。原维护者后续更新live表不改迁移快照/用户历史授权证据，未来CI不会因正常维护状态前进而拒绝。迁移库存archive仍逐字保留。
