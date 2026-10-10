# RLT_39 · normal 定向代码复核 · attempt 2

结论：**approved**。这是 normal 初审唯一 open P1 `RLT39-CR-P1-R31-UNRESOLVED` 的唯一一次同实例定向复核；该 finding 已 **resolved**。本报告只核该修复和相关协调差异，不重做完整产品审核，不把原 R31 机器失败改写为通过，也不替代后续合入态复验、verify 或双设备同步审计。

复核实例仍为 `/root/rlt39_code_review`，未参与实施；实施实例仍为 `codex-root-rlt39-20261010`。派发为 `E-012`，attempt=2、kind=targeted；本实例只写本报告和同名 JSON。

## 定向绑定

- baseline_sha=`9f7c2b2c15dca69ce39a780aa4b7c4bc64ea6c70`
- target_sha=`f914dd011c484941121e25d27a2d4c1f0f9ff7d5`
- diff_sha256=`77b8059ab935e0f019a3145c752e4fa6739411fe79a412c38aa0b7455cf29127`
- repaired_finding_ref=`RLT39-CR-P1-R31-UNRESOLVED`

实际 Git 对象和完整 collector 格式 diff hash 与派单、更新后的 review-freeze 一致。`22b7f43..f914dd0` 不含 `skill/`、安装器、工具或测试实现的产品字节改动；差异仅落在本卡协调/收口工件及源卡/brief 的单项验收处置。

## P1 处置核查

首审原件仍保留同一 ref、P1、open 和当时的 `changes-requested` 结论。原 `evidence/r31-diagnostic.json` 仍忠实记录原候选 `22b7f43` 为 `applicable=true`、`ok=false`、`no-mutation-registered`；没有伪造变异、修改诊断、将失败改为 PASS，或借既有 80 项回归把 R31 机器规则倒写为通过。

用户对明确问题“是否同意本卡免除生产代码变异测试，继续收口和双设备同步？”的原话“同意”已在 `findings.md` 的 R31 用户裁决落账。源卡和 brief 只同步修改 `RL39-M4`：本卡生产代码变异不适用，协议场景对照仍为完成项；normal 类型、独立复核额度、回归、CI、主干复验、verify 和其余边界不变。该处置正是首审要求的用户明确决定，且没有外溢为一般性豁免。

因此，首审 P1 的阻断原因已消除：不是 R31 机器诊断转绿，而是用户针对这张纯 Markdown 协议卡明确调整该一项验收。无其它 finding 被重开或新发现。无需重复产品回归；完整初审已实际运行的 80 项回归与已登记双平台 CI 保持其原有证据边界。

## findings

`RLT39-CR-P1-R31-UNRESOLVED`：**P1 resolved**。解决依据是上述精确用户裁决及仅 RL39-M4 的验收调整；原机器失败、初审原件和额度历史保留。本报告和 JSON 写完即停。
