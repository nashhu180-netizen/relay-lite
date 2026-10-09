<!-- dh:v1 -->
<!-- dh:workspace-contract:v2 -->
# brief — RLT_36

## 覆盖任务
RLT_36；../../dev_plan/P4-watcher可靠性.md#rlt_36；Issue #15。

## 目标
watcher 暂停不使整个已授权任务停滞；监控持续、通知异常隔离、主编排有界核结果。

## 本卡开工授权
2026-10-09 用户“确认开始修复，建个issue”，此前明确标准档提案及本卡独立复核、真实隔离演练；origin wt/RLT_36 → master 全程交付。其它三个 space 的在途任务保持原样。
用户随后确认模型：独立 reviewer gpt-6.1-sol/high；隔离演练编排/worker/watcher gpt-6-luna/medium。普通监控程序不启动模型。

## 分类事实
production_operation=false：只修仓库及独立本地测试 space，不操作生产或在途环境。
irreversible_migration=false：兼容旧 watcher 调用，不删除业务数据/能力。
metric_semantics=false：无业务指标口径。
security_or_shared_guarantee=false：RELAY_RECEIPT、身份核验、凭据过滤、审批/写权/验收硬闸保留；未知投递不盲重发。
behavior_or_rule_semantics_changed=true：监控生命周期和通知确认/兜底等待规则发生变化。因此 normal=[code_review]。

## 边界
仅源卡允许路径；隔离 Herdr 演练是获授权本卡测试，不替代业务卡人验。不安装真实用户副本、不重启现有监控、不派下一卡。

## 完成条件
- RL36-M1：常驻监控运行在 Herdr 独立普通终端，不依赖 watcher 模型回合；兼容旧 agent 身份入口并核真实 pane/space。
- RL36-M2：通知仅确认提交，不用主编排 working/seq 变化证明消费；忙碌可提交，审批阻塞延后，未知投递不盲重发且继续观察。
- RL36-M3：临时只读观察失败保留基线后恢复；身份/RELAY_RECEIPT 硬闸不放宽；同 space 监控重复启动有单实例保护。
- RL36-M4：提供主编排只读有界 signal 等待入口；watcher 暂停/缺席时能发现精确本批结果，READY 不是 PASS，仍核原报告与 durable signal。
- RL36-M5：隔离真实 Herdr 演练证明 watcher agent 空闲/暂停及通知忙碌场景下，worker 完成后主编排实际核结果并完成已授权交接。
- RL36-M6：安装包闭集同步，行为回归/有效 RED→恢复 GREEN、fresh code_review、双平台 CI、实际合入复验与 verify 齐备。
