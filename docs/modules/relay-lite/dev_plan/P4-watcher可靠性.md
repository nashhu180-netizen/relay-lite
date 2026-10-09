<!-- dh:v1 -->
# P4 · watcher 可靠性维护

<!-- dh:status
汇报: RLT_36 标准档可靠性修复已开工。
现状: Issue15 已创建并读回；用户确认修复范围与模型分配。
进行到: P4 / RLT_36 实施准备。
下一步: 持久监控、通知异常隔离与主编排有界结果等待；隔离真实演练。
看什么: workspace/36-RLT_36-watcher-reliability/task_plan.md。
阻塞: 无；产品效果尚未验证。
-->

<!-- dh:tasks -->
| 任务ID | 任务 | 档位 | 状态 | 工作区 | 验收时间 | verify SHA | release_mode |
|---|---|---|---|---|---|---|---|
| RLT_36 | watcher 暂停不阻断任务接力 | 标准 | 进行中 | workspace/36-RLT_36-watcher-reliability/ | | | |

#### RLT_36

Issue：https://github.com/nashhu180-netizen/relay-lite/issues/15。
来源：用户反馈“watcher 的体验不好，一直会暂停，然后整个任务就停了”；确认修复提案后于 2026-10-09 原话“确认开始修复，建个issue”。这是新维护卡，不覆盖 RLT_35 的已完成离线合同。
目标：持久监控与 watcher 模型回合解耦；通知异常不终止全部观察；主编排发现精确结果后继续已授权交接。
档位标准，任务类型 normal。origin wt/RLT_36 → master，本卡开工授权覆盖 Issue、实施/验证/独立复核、PR/必要CI/服务端合入、合入态复验、verify/回填/本卡清理。已确认隔离真实 Herdr 演练。
非目标：现有 AW_07/WFP_08/dev-harness 的重启或改动、用户 skill 副本安装、部署/生产操作、下一卡、放宽业务验收/角色写权/审批授权。
交付消费接口：独立 Herdr 监控终端、space_watch.py 与 task_wait.py、核心协议/两 adapter/环境协议、受管安装包。
<!-- dh:task-type:v2 task=RLT_36 type=normal policy=three-tier -->
<!-- dh:classification-fact:v2 task=RLT_36 name=production_operation value=false evidence="docs/modules/relay-lite/workspace/36-RLT_36-watcher-reliability/brief.md#分类事实" -->
<!-- dh:classification-fact:v2 task=RLT_36 name=irreversible_migration value=false evidence="docs/modules/relay-lite/workspace/36-RLT_36-watcher-reliability/brief.md#分类事实" -->
<!-- dh:classification-fact:v2 task=RLT_36 name=metric_semantics value=false evidence="docs/modules/relay-lite/workspace/36-RLT_36-watcher-reliability/brief.md#分类事实" -->
<!-- dh:classification-fact:v2 task=RLT_36 name=security_or_shared_guarantee value=false evidence="docs/modules/relay-lite/workspace/36-RLT_36-watcher-reliability/brief.md#分类事实" -->
<!-- dh:classification-fact:v2 task=RLT_36 name=behavior_or_rule_semantics_changed value=true evidence="docs/modules/relay-lite/workspace/36-RLT_36-watcher-reliability/brief.md#分类事实" -->

- **验收口径**：

- RL36-M1：常驻监控运行在 Herdr 独立普通终端，不依赖 watcher 模型回合；兼容旧 agent 身份入口并核真实 pane/space。
- RL36-M2：通知仅确认提交，不用主编排 working/seq 变化证明消费；忙碌可提交，审批阻塞延后，未知投递不盲重发且继续观察。
- RL36-M3：临时只读观察失败保留基线后恢复；身份/RELAY_RECEIPT 硬闸不放宽；同 space 监控重复启动有单实例保护。
- RL36-M4：提供主编排只读有界 signal 等待入口；watcher 暂停/缺席时能发现精确本批结果，READY 不是 PASS，仍核原报告与 durable signal。
- RL36-M5：隔离真实 Herdr 演练证明 watcher agent 空闲/暂停及通知忙碌场景下，worker 完成后主编排实际核结果并完成已授权交接。
- RL36-M6：安装包闭集同步，行为回归/有效 RED→恢复 GREEN、fresh code_review、双平台 CI、实际合入复验与 verify 齐备。

- **允许路径**：<!-- dh:allowed-paths:v1 task=RLT_36 -->
  - `tools/space_watch.py`
  - `tools/task_wait.py`
  - `tools/install_skill.py`
  - `tests/test_space_watch.py`
  - `tests/test_task_wait.py`
  - `tests/test_install_skill.py`
  - `tests/test_contract.py`
  - `skill/SKILL.md`
  - `skill/references/environment-herdr.md`
  - `skill/references/adapter-codex.md`
  - `skill/references/adapter-claude-code.md`
  - `README.md`
  - `docs/modules/relay-lite/dev_plan/P4-watcher可靠性.md`
  - `docs/modules/relay-lite/design/evidence/03-交叉审核记录-RLT_36.md`
  - `docs/modules/relay-lite/workspace/36-RLT_36-watcher-reliability/**`
  - `docs/modules/relay-lite/as-built/protocol-and-distribution.md`

停止线：未解 P0/P1、范围/验收/权限变化、访问/CI阻塞；未知投递保留，不自动重发；不修改其它卡历史。

增量边界：依赖已交付RLT_35，仅新增本卡持续监控与结果等待，不改其历史离线验收。

<!-- dh:planning-event:v1 id=RLT36-B-20261009 stage=B-new artifact=dev_plan/P4-watcher可靠性.md review=../design/evidence/03-交叉审核记录-RLT_36.md#review understanding=../design/evidence/03-交叉审核记录-RLT_36.md#understanding -->
