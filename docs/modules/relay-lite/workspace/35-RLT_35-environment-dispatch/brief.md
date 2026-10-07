<!-- dh:v1 -->
<!-- dh:workspace-contract:v2 -->
# brief — RLT_35 环境派发与通用 watcher

## 覆盖任务
RLT_35；来源：../../dev_plan/P3-环境派发与监控.md#rlt_35；Issue #12。

## 目标 (Outcome)
环境配置由工具实际校验；Herdr 派发前加载内置 skill；所有 agent 共用明确的 watcher 启动/确认/报信/退出步骤。

## 本卡开工授权
用户于 2026-10-07 回复“确认”，承接已展示标准档 normal 单卡范围；随后纠正“不是 codex 的 watcher 针对所有agent都一样”，统一通用流程。目标 origin wt/RLT_35 → master；完整交付，不含真实环境/安装操作或下一卡。

## 分类事实
四项最高危事实均 false：本卡无生产实操作、不可逆业务迁移、指标口径变化或权限/共享保证改变；保持 RELAY_RECEIPT、凭据与写权原边界。行为/规则语义 true：配置校验及环境路由新增；故 normal。

## 边界 (Boundaries)
In scope：源卡精确允许路径中的协议、配置工具、安装器、测试及本卡工件。
Out of scope：Orca 实现、space_watch.py 行为变更、用户 skill 副本、真实 Herdr 操作、archive、其它卡及其 worktree。

## 完成条件

| # | 条件 | 谁验（AI / 人） | 出处 |
|---|---|---|---|
| RL35-M1 | 安装包配置目前有且只有 herdr；默认与显式选择一致；未知环境、配置错误或协议缺失阻止派发，不能回退。 | AI | P3 / RLT_35 / RL35-M1 |
| RL35-M2 | 核心及两模型 adapter 先读取环境配置再走专属协议；Herdr 派发/通信入口只在其专属协议维护；原有调用点无遗漏。 | AI | P3 / RLT_35 / RL35-M2 |
| RL35-M3 | Herdr 首次按 space -> tab -> 交互式 agent -> 派单；复用同 tab 的新任务/新批次先模型原生 clear、核成功，再派单；失败/未知阻止派单。 | AI | P3 / RLT_35 / RL35-M3 |
| RL35-M4 | RLT_34 完成条件、整改/E2/fresh/watcher 例外以及历史证据、计数和 RELAY_* 保留；配置选择不扩大模型、角色或开工授权。 | AI | P3 / RLT_35 / RL35-M4 |
| RL35-M5 | 三端隔离安装包含配置、校验工具和环境协议，并纳入 manifest 哈希；安装缺件失败，安装后引用可独立解析，不依赖此仓 checkout。 | AI | P3 / RLT_35 / RL35-M5 |
| RL35-M6 | Herdr 派发前明确加载当前 herdr --skill；有环境/实际 ID/当前 CLI 语法核对及用户拓扑优先级，缺失时停止。 | AI | P3 / RLT_35 / RL35-M6 |
| RL35-M7 | 所有 agent 的 watcher 入口覆盖启动、真实子进程确认、120 秒动态监控、通知确认/退出处置与 durable signal 路由；复用现有脚本测试对新增/离开/状态变化/排除项/未知通知/无写入的证明，协议样例无工具调用层级混淆。 | AI | P3 / RLT_35 / RL35-M7 |
| RL35-M8 | 适用回归、有效单测 RED -> 恢复 GREEN、fresh 独立代码复核、必要 CI、合入态复验及 verify 齐备。 | AI | P3 / RLT_35 / RL35-M8 |

## 三档分类引用
源卡 normal=[code_review]；一轮 fresh 完整初审，仅真实 open P0/P1 才同人 targeted attempt2。

## 触及子系统
环境配置工具与书面派发/监控协议、安装闭包；不承诺 live Herdr 演练。无人判产品结果项。
