<!-- dh:v1 -->
<!-- dh:workspace-contract:v2 -->
# RLT_33

## 覆盖任务

RLT_33；来源 [P1](../../dev_plan/P1-独立交付.md) §RLT_33。

Issue #1 / dh-relay #156。用户 2026-10-07：“建个issue 后开工”。任务源 P1-独立交付.md；档位标准、task_type=heavy、verify scope=relay-lite。目标 master，两仓远端交付含 commit/push/PR/CI/merge/verify/本卡清理，不含生产操作、其它卡收口或新配方 #154 实施。

完成条件逐字承接设计 RL33-M1～M6；工作树 /home/nash/work/relay-lite/.dh-worktrees/RLT_33，分支 wt/RLT_33-issue-1；源树 /home/nash/work/dh-relay/.dh-worktrees/RLT_33，分支 wt/RLT_33-issue-156。一个跨仓迁移卡，每仓唯一隔离树。

## 完成条件逐条展开（与来源设计/DevPlan同口径）

- RL33-M1：独立 Git 仓/目录、任务分支、PR/CI/合入及 verify 记录齐备；原仓迁出入口清楚。
- RL33-M2：孤立 clone 全测试与临时 home 安装成功，不依赖 dh-relay 路径；自包含安装包提供 watcher 和计划模板。
- RL33-M3：现役协议、两个 adapter、AGENTS 使用 executor；角色/phase/signal 一致，保留分配确认、写者、复核/人验闸、watcher 零写入与 RELAY_RECEIPT 拒绝。
- RL33-M4：现役包无账本、五阶段或 stage-lead 入口；仅单卡接力及跨卡总表。旧完整计划和日志逐字保留为历史，不能传给当前流程执行。
- RL33-M5：所有迁移历史字节符合清单，两份卡级总表的任务行、依赖/权限/状态字段不变；旧副本清楚指向新权威，不并写。
- RL33-M6：watcher 动态发现、通知确认/未知投递失败不重复、环境拒绝与无文件写入行为测试通过；独立代码轮1/2、需求、一致性、教训复核齐备，变异 RED→恢复 GREEN。

2026-10-07 补充用户决定：本次迁移最新总表，并协调原维护会话切换新仓。冻结 archive 清单不改；AW 最新表以 docs/table-cutover.json 与额外原字节证据固定，不把在途变更回写历史快照。原维护者确认前旧表仍权威，禁止并写；合入和清理不早于确认。

## 边界

仅本卡独立分发、源入口退休、历史及最新总表迁移；允许路径按P1闭集。原维护者保留独占写权，不改其它业务卡授权/signal/人验，不部署、不实施#154、不清理其它任务树。两原维护者最新源/暂停回执齐备；新仓实际合入后由原维护者确认新路径，旧表再退休，不并写。
