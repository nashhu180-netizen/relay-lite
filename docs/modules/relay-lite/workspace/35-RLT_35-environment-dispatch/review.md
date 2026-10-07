<!-- dh:v1 -->
# review — RLT_35

## 独立复核区
normal=[code_review]；待完整候选 fresh 初审，不由施工方自审。

## AI 提交区
**Confidence Challenge**：配置选择与安装包需真实执行负例；协议/fixtures不证明live Herdr。本地58项与变异还原通过，仍待fresh复核/CI/合入复验/verify。

## 完成条件逐条挂证据

| # | 完成条件 | 谁验 | 证据 | 达成? |
|---|---|---|---|---|
| RL35-M1 | 安装包配置目前有且只有 herdr；默认与显式选择一致；未知环境、配置错误或协议缺失阻止派发，不能回退。 | AI | E-007、E-009（协议/CLI/隔离安装） | 通过：E-007～009、E-015～016、E-019～020 |
| RL35-M2 | 核心及两模型 adapter 先读取环境配置再走专属协议；Herdr 派发/通信入口只在其专属协议维护；原有调用点无遗漏。 | AI | E-007、E-009（协议/CLI/隔离安装） | 通过：E-007～009、E-015～016、E-019～020 |
| RL35-M3 | Herdr 首次按 space -> tab -> 交互式 agent -> 派单；复用同 tab 的新任务/新批次先模型原生 clear、核成功，再派单；失败/未知阻止派单。 | AI | E-007、E-009（协议/CLI/隔离安装） | 通过：E-007～009、E-015～016、E-019～020 |
| RL35-M4 | RLT_34 完成条件、整改/E2/fresh/watcher 例外以及历史证据、计数和 RELAY_* 保留；配置选择不扩大模型、角色或开工授权。 | AI | E-007、E-009（协议/CLI/隔离安装） | 通过：E-007～009、E-015～016、E-019～020 |
| RL35-M5 | 三端隔离安装包含配置、校验工具和环境协议，并纳入 manifest 哈希；安装缺件失败，安装后引用可独立解析，不依赖此仓 checkout。 | AI | E-007、E-009（协议/CLI/隔离安装） | 通过：E-007～009、E-015～016、E-019～020 |
| RL35-M6 | Herdr 派发前明确加载当前 herdr --skill；有环境/实际 ID/当前 CLI 语法核对及用户拓扑优先级，缺失时停止。 | AI | E-007、E-009（协议/CLI/隔离安装） | 通过：E-007～009、E-015～016、E-019～020 |
| RL35-M7 | 所有 agent 的 watcher 入口覆盖启动、真实子进程确认、120 秒动态监控、通知确认/退出处置与 durable signal 路由；复用现有脚本测试对新增/离开/状态变化/排除项/未知通知/无写入的证明，协议样例无工具调用层级混淆。 | AI | E-007、E-009（协议/CLI/隔离安装） | 通过：E-007～009、E-015～016、E-019～020 |
| RL35-M8 | 适用回归、有效单测 RED -> 恢复 GREEN、fresh 独立代码复核、必要 CI、合入态复验及 verify 齐备。 | AI | E-007～E-009 | 未齐备（本地取证结束，待复核及Git交付） |

## 需求对齐证据

| 需求 / 人验项 | 场景与操作路径 | 证据 (E-00x) | 结论（满足 / 不满足 / 待人验） |
|---|---|---|---|
| 环境配置 RL35-M1/M2/M5 | 工具读取→校验→协议定位→安装后复跑 | E-007～E-009 | 满足（本地配置/协议/安装、独立复核、双平台CI及合入复验） |
| Herdr skill/派发 RL35-M3/M6 | 配置gate→加载skill→space/tab/交互agent；复用clear确认 | E-007～E-009 | 满足（本地配置/协议/安装、独立复核、双平台CI及合入复验） |
| 通用 watcher RL35-M7 | 全kind通用启动/确认→动态观察→通知/异常处理 | E-007～E-009 | 满足（本地配置/协议/安装、独立复核、双平台CI及合入复验） |
| 原边界与交付 RL35-M4/M8 | clear例外/权限保留→回归/变异→复核/CI/合入复验/verify | E-007～E-009 | 满足（本地配置/协议/安装、独立复核、双平台CI及合入复验） |

## 人类签名区
无人判结果项；不代签。协议合同与fixture测试不冒充live演练。

## 验收项元数据表

| 命题 | 事实证明方式 | 最终裁决者(machine\|human) | 稳定 ID | 覆盖态 | 等价判据 | 实际执行结果 | 版本环境 | 独立 oracle | 未覆盖边界 | contractVersion | arbiterCapability | arbiterAuthorization |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| RL35-M1 | CLI负例/隔离安装/协议测试/独立复核/CI/Git | machine | RL35-M1 | 等价覆盖 | P3 同名验收 | 本地、独立复核及实际合入复验证据通过 | Python3.12/Linux | 用户需求/独立review | live Herdr不在合同 | 1 | 代码/协议事实核验 | 本卡开工授权 |
| RL35-M2 | CLI负例/隔离安装/协议测试/独立复核/CI/Git | machine | RL35-M2 | 等价覆盖 | P3 同名验收 | 本地、独立复核及实际合入复验证据通过 | Python3.12/Linux | 用户需求/独立review | live Herdr不在合同 | 1 | 代码/协议事实核验 | 本卡开工授权 |
| RL35-M3 | CLI负例/隔离安装/协议测试/独立复核/CI/Git | machine | RL35-M3 | 等价覆盖 | P3 同名验收 | 本地、独立复核及实际合入复验证据通过 | Python3.12/Linux | 用户需求/独立review | live Herdr不在合同 | 1 | 代码/协议事实核验 | 本卡开工授权 |
| RL35-M4 | CLI负例/隔离安装/协议测试/独立复核/CI/Git | machine | RL35-M4 | 等价覆盖 | P3 同名验收 | 本地、独立复核及实际合入复验证据通过 | Python3.12/Linux | 用户需求/独立review | live Herdr不在合同 | 1 | 代码/协议事实核验 | 本卡开工授权 |
| RL35-M5 | CLI负例/隔离安装/协议测试/独立复核/CI/Git | machine | RL35-M5 | 等价覆盖 | P3 同名验收 | 本地、独立复核及实际合入复验证据通过 | Python3.12/Linux | 用户需求/独立review | live Herdr不在合同 | 1 | 代码/协议事实核验 | 本卡开工授权 |
| RL35-M6 | CLI负例/隔离安装/协议测试/独立复核/CI/Git | machine | RL35-M6 | 等价覆盖 | P3 同名验收 | 本地、独立复核及实际合入复验证据通过 | Python3.12/Linux | 用户需求/独立review | live Herdr不在合同 | 1 | 代码/协议事实核验 | 本卡开工授权 |
| RL35-M7 | CLI负例/隔离安装/协议测试/独立复核/CI/Git | machine | RL35-M7 | 等价覆盖 | P3 同名验收 | 本地、独立复核及实际合入复验证据通过 | Python3.12/Linux | 用户需求/独立review | live Herdr不在合同 | 1 | 代码/协议事实核验 | 本卡开工授权 |
| RL35-M8 | CLI负例/隔离安装/协议测试/独立复核/CI/Git | machine | RL35-M8 | 部分覆盖 | P3 同名验收 | 合入复验完成，验收记录随本verify提交归档 | Python3.12/Linux | 用户需求/独立review | live Herdr不在合同 | 1 | 代码/协议事实核验 | 本卡开工授权 |

## 有效单测·变异点登记

| 变异点锚点(生产代码 path:line) | 原值→变异值 | 语义类别 | 对应测试 ID | 运行命令 | 施加 hash | 还原 hash | 登记人(重核须=轮2实例) | 施加后结果 |
|---|---|---|---|---|---|---|---|---|
| tools/environment_config.py:114 | 显式未知环境拒绝→未知值回退default | 改边界 | test_environment_config.EnvironmentConfigTests.test_unknown_empty_and_recovery_conflict_stop | python3 -m unittest discover -s tests -p test_environment_config.py -k test_unknown_empty_and_recovery_conflict_stop -v | c328ffdde94d533e1f6fbb132dd4f15a1b3359227095b6d75941258680410fdf | d8e269e045ef5388c6e6d2c891e81ee0433256c46c79151f4502879258a847b7 | codex-root-rlt35-20261007 | 断言失败 |

证据为mutation.json及mutation-red.log；精确还原hash等于原值，restored-green.log 58项通过。无live Herdr操作或真实副本安装。
<!-- dh:review-attempt:v1 task=RLT_35 attempt=1 kind=full reviewer_session_id=/root/rlt35_code_review status=punched -->

<!-- dh:review-result:v2 task=RLT_35 path=code_review attempt=1 artifact=docs/modules/relay-lite/workspace/35-RLT_35-environment-dispatch/evidence/code-review.json artifact_sha256=4f3792cfc9bf40da5bc9116e2b3755540969c81d90773cda3b29e0090420ddf2 -->
<!-- dh:review-attempt:v1 task=RLT_35 attempt=2 kind=targeted reviewer_session_id=/root/rlt35_code_review status=punched -->

<!-- dh:review-result:v2 task=RLT_35 path=code_review attempt=2 artifact=docs/modules/relay-lite/workspace/35-RLT_35-environment-dispatch/evidence/code-review-attempt2.json artifact_sha256=df826290af89e6bdec4cd46948d9e4e91f69641fefc9a0ed5f6d3020447036eb -->

独立复核结论：初次 CR-001 P1 原证保留；同 reviewer 唯一 attempt2 定向 approved、CR-001 resolved；修复候选双平台 CI SUCCESS。

## 自动验收记录
实际执行者：codex-root-rlt35-20261007。验收时间：2026-10-08T00:19:47+08:00（Asia/Shanghai）。授权：brief.md#本卡开工授权；用户确认及随后继续，未撤销/缩窄。机器项RL35-M1～M7由协议/CLI/隔离安装、独立复核、双平台CI及实际主干58项/原证PASS覆盖；RL35-M8的verify由本提交留痕，再有限PR归档。无人判项，不代签。风险0；Verification=full。本次未更新真实skill副本或操作Herdr。
