# 派单 prompt 模板（orchestrator → worker）

派单前读[核心协议](../SKILL.md)的标头/phase、模型、清理、signal 与写者闸及按角色阅读路由。以下字段不能因精简而省略；无关项写不适用并说明。decider另读[决策指南](../references/decision-guide.md)。

```text
[relay-lite:single-task] worker · phase=<phase> · agent=<角色>#<实例> · batch=<n|na> · round=<n> · workspace=<任务工作区>
读：<repo>/AGENTS.md → <任务工作区>/brief.md、task_plan.md（及派单指定的其它工件）
目标与当前位置：<原目标/验收引用；本棒解决什么；当前结果与剩余缺口>
授权与停止线：<用户原始来源；可执行范围/资源/预算/已耗额度；明确停止条件>
边界：<本棒 allowed-paths 一句话>
验证责任：<执行者；独立核验者；不涉及验证则写不适用>
对照基线：<整卡/批次用途；完整 SHA；选择依据；不适用须说明>
执行合同：<cwd；解释器；完整命令；必要环境/依赖；收集范围；串行要求>
临时现场：<允许位置/准备方式；所需资源；证据保存与清理责任；无则写无>
证据与写者：<精确路径/章节及本次唯一写者；findings 的决定记录由编排或获派 executor 错开追加，基线归因仍仅 executor 写、review 由 reviewer 写；启用 document 时按确认代笔，原始结论/signal 仍由原角色写>
决定引用：<findings 条目与用户/decision 原始来源；无则写无；缺源/冲突/待决定时不推进依赖动作，回报编排澄清>
通过/阻塞：<必需通过项；允许失败集合及审核/授权引用；缺证或新增失败的 BLOCKED 出口>
后续去向：<成功/失败后交谁；可预见依赖与待决项，未知如实标明，不据此扩权>
decision专用：<需要判断的变化及历史同类阻塞；按决策指南交完整路径、备选/推荐、验证/收束及剩余审批点；非decision不填>
硬规则：你是 worker：不拉终端、不派活、不回头问用户；先跑 RELAY_RECEIPT preflight；
卡住写本角色精确 BLOCKED 单行 signal 不憋死；凭据/密钥值永不写进任何工件。
完成：只写派单指向的产出与本角色单行 DONE/BLOCKED signal 即停；无 node_closed，
不创建/读写 relay_plan.md、relay_log.jsonl。
```

- durable signal 单行 schema：`DONE|BLOCKED task=<t> phase=<p> agent=<r>#<i> batch=<1|2|3|na> path=<path|na> review_round=<n> remediation_count=<0|1|2> verdict=<v> evidence=<repo 相对路径[,...]>`，BLOCKED 另含 `reason=<snake_case>`；值无空白。产出型 builder/executor/reviewer/decider（含已启用的 document）写完 signal 即停；orchestrator 只按 durable signal 与独立 review/decision 工件机械分发/路由，不把终端状态当真相。
