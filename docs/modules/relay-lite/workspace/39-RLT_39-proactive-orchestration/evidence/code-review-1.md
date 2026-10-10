# RLT_39 · normal 完整独立代码复核 · attempt 1

结论：**changes-requested**。候选的协议实现本身没有发现额外的 P0/P1/P2/P3；但 `RL39-M4` 明定有效变异为完成条件，而真实 R31 诊断仍为 `applicable=true, ok=false, no-mutation-registered`。该 P1 尚待用户对单项验收调整作出明确决定，不能把提案、既有 80 项回归或协议推演当作通过。因此本次 `code_review` 有 1 个 open P1，完整交付、合入和 verify 继续暂停。

复核实例 `/root/rlt39_code_review` 未参与实施，fresh context；实施实例为 `codex-root-rlt39-20261010`。派发为 `E-006`，normal 的首次完整复核（attempt 1）；本实例只写本报告和同名 JSON，没有修改产品或其它工件，没有联网、派活、启动模型或操作 Herdr。

## 绑定与范围

- baseline_sha=`9f7c2b2c15dca69ce39a780aa4b7c4bc64ea6c70`
- target_sha=`22b7f43c52ca4863a28dd04ad0f522271f84331e`
- diff_sha256=`4c3dc143ea14eae86f90f33bcd7542674147e876b6abc86d164d3bcd6def5e79`

已核实际 Git 对象、全量 baseline→target diff、允许路径和 `git diff --check`。当前工作树 HEAD 已有候选后的协调证据，未将其混入上述冻结产品 target。产品候选修改核心入口、`orchestration`、`decision-guide`、`watcher` 和 as-built，并新增本卡源卡/工作区证据；未改安装器、运行工具或测试实现。

## 产品核查

`skill/references/orchestration.md` 将结果后的责任闭环写成四个可执行分支：报告/signal/决定或插问之后核未完成项并派下一责任方；BLOCKED 时按缺证、路线和用户权限/外部条件解阻；范围内插问核实后继续原任务；仅在完成、明确停止线，或无独立可推进的授权工作且有真实外部缺口时等待。它同时保持 worker 的 DONE/BLOCKED 即停、原模型确认/写者/轮次、未知不重试，以及编排不代施工、测试、归因或验收。

核心入口把该职责加入 orchestrator 定义和 single-task 编排段；`decision-guide` 的消费段和正反例保持 DECIDED 不是授权/验收、用户待决不执行、独立许可工作可继续；`watcher` 仅把明确失败、审批阻塞或无 signal 的报告回链至编排解阻，仍规定 watcher 零写入、PENDING 有界等待、READY 非 PASS。两个 adapter 原本通过核心的按角色阅读矩阵消费共用合同，安装器清单已包含上述所有引用；因此没有产生重复且可能漂移的宿主条款。

逐项对照本卡 12 个协议场景和源卡 RL39-M1--M3：汇报、插问、范围外发现、缺证 BLOCKED、重复阻塞、用户待决与独立工作、身份/结果未知或预算耗尽、停止线、PENDING、未确认 decider、以及所有条件满足的收束均有路径，且没有将条款改动表述为真实 Codex/Claude 行为实测。

## 独立验证

运行 `python3 -m unittest discover -s tests -v`：80 tests，exit 0，OK。包括隔离安装后的文档闭环、已路由合同缺失时安装前拒绝、两 adapter 的前置清理要求、环境/RELAY_RECEIPT fail-closed、watcher 与 task_wait 行为测试。该结果只证明包和既有工具回归；它不证明真实模型会话的持续推进概率，也不满足 R31 的有效变异要求。

## findings

1. **P1 open — R31 有效变异未满足，且例外尚无用户明确决定。** 源卡将“有效变异”列为 `RL39-M4` 的必要条件（`docs/modules/relay-lite/dev_plan/P7-编排主动推进.md:38`），而候选的真实诊断记录 `applicable=true`、`ok=false`、`no-mutation-registered`（`docs/modules/relay-lite/workspace/39-RLT_39-proactive-orchestration/evidence/r31-diagnostic.json:5`）。当前仅有尚未生效的单项例外提案；不能将其、主干空 diff、临时未提交安装器变动或回归绿灯登记为有效变异。须等待用户明确决定：若同意，按其精确范围更新原验收并保留原失败诊断；若不同意，保留停止状态或在现有授权/允许路径内形成真实必要生产变更及对应有效变异记录。完成后可由同一 reviewer_session_id 作一次 targeted attempt 2；本初审不自行推定授权。

除该阻断项外，没有发现独立的协议一致性、安装读取链或适用性回归问题。本报告和 JSON 写完即停。
