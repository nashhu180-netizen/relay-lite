<!-- dh:v1 -->
# review — RLT_34

## 独立复核区
normal=[code_review]；完整 fresh 初审已 approved，无 open P0/P1，独立回归 41 项通过；不再派新复核。

<!-- dh:review-result:v2 task=RLT_34 path=code_review attempt=1 artifact=docs/modules/relay-lite/workspace/34-RLT_34-session-clear/evidence/code-review.json artifact_sha256=880b82ef0cf46f986b8f1e9e4c74349ee67f3fbdde47fcf00c3c0fd1b574203c -->

**code_review 初审结论**：approved｜被审 SHA=e6adef4fe009972bc86071a636e03009e54337d0｜P0=0 P1=0 P2=0 P3=0｜派出=e:E-007｜原证=docs/modules/relay-lite/workspace/34-RLT_34-session-clear/evidence/code-review.json


## AI 提交区

**Confidence Challenge**：回归/变异已验证；仍待独立复核、CI 和实际合入复验。

## 完成条件逐条挂证据

| # | 完成条件 | 谁验 | 证据 | 达成? |
|---|---|---|---|---|
| RL34-M1 | 新批次派单前，前批 durable PASS 且工件齐全，executor 与 batch-reviewer 各 clear 一次并分别确认成功。 | AI | E-002、E-004 | 本地协议验证通过，独立结论 approved |
| RL34-M2 | 标签页接新的独立任务前保存前任务工件与 signal，清理旧会话并确认成功，再读取新派单；新建空会话不冒充复用会话的 clear。 | AI | E-002～E-004 | 本地协议验证通过，独立结论 approved |
| RL34-M3 | 同任务 FAIL/整改与 E2 定向复查保留原会话及计数；fresh reviewer 必须是未参与实施的独立新实例；常驻 watcher 不逐批 clear。 | AI | E-002、E-004 | 本地协议验证通过，独立结论 approved |
| RL34-M4 | 清理失败或结果未知时停止新派单，不盲重发；core 与两 adapter 一致；历史 signal、证据、计数及 RELAY_* 保留。 | AI | E-002、E-004 | 本地协议验证通过，独立结论 approved |
| RL34-M5 | 协议回归及变异 RED→还原 GREEN、fresh 独立复核、Ubuntu/Windows CI、PR 合入态复验和 verify(relay-lite) 齐备。 | AI | | 待验证 |

## 需求对齐证据
| 需求 / 人验项 | 场景与操作路径 | 证据 (E-00x) | 结论（满足 / 不满足 / 待人验） |
|---|---|---|---|
| 新批次 RL34-M1 | 核前批 signal/证据→清 executor/reviewer→确认→下一批 | E-002、E-004；skill/SKILL.md 清理闸 | 文本协议和回归满足，独立复核 approved |
| 新任务 RL34-M2 | 保存前任务→复用 tab 原生 clear→确认→投递/重读新合同 | E-002～E-004；两 adapter 启动投递 | 文本协议和回归满足，独立复核 approved |
| 例外 RL34-M3 | 原整改/E2 原会话继续；fresh 审核另起实例；watcher 常驻 | E-002、E-004；core 生命周期 | 文本协议和回归满足，独立复核 approved |
| 未知结果 RL34-M4 | 未确认清理→阻断新派单；保留证据/计数/RELAY_* | E-002、E-004 | 文本协议和回归满足，独立复核 approved |
| 交付 RL34-M5 | RED→还原 GREEN→fresh 审核→双平台 CI→合入复验→verify | E-003、E-004 | 不满足（待 CI/合入/verify，保留待验证） |

局限：本卡交付是书面流程约束与协议测试，没有自动强制拦截程序，不声称真实 Herdr 清理已执行。无 UI/可视化产品改动，无需渲染截图。


## 人类签名区
无人判结果项，不代签用户人验。

## 自动收口记录
未进入放行；待实际复核与 CI/合入态验证。

## 有效单测·变异点登记

| 变异点锚点(生产代码 path:line) | 原值→变异值 | 语义类别 | 对应测试 ID | 运行命令 | 施加 hash | 还原 hash | 登记人(重核须=轮2实例) | 施加后结果 |
|---|---|---|---|---|---|---|---|---|
| skill/SKILL.md:123 | 先 clear 并确认，再投递新派单 → 保留旧会话上下文，直接投递新派单 | 改边界 | test_contract.PackageTests.test_new_task_clear_is_a_predispatch_gate ▸ test_new_task_clear_is_a_predispatch_gate | python3 -m unittest discover -s tests -p test_contract.py -k test_new_task_clear_is_a_predispatch_gate -v | 8990dbd9ec3baca15eb0798fb9ec01f9c21d1e79 | 99ad89962d53d1b6d31b9dd188fea26b43d5b223 | codex-root-rlt34-20261007 | 断言失败 |

本卡生产入口是 skill/SKILL.md 协议文本；变异直接取消派单前置条件，指定契约测试断言失败，不是破坏测试或导入失败。hash 为被变异/还原文本的 Git blob SHA，原字节还原实证见 evidence/mutation.json。

- 契约无变化：RLT_33 独立迁移目标/验收未改；本维护增量的会话派单规则已直接同步 core 与两 adapter，范围和验收承接本轮用户需求与 P2 源卡。

## 验收项元数据表

| 命题 | 事实证明方式 | 最终裁决者(machine\|human) | 稳定 ID | 覆盖态 | 等价判据 | 实际执行结果 | 版本环境 | 独立 oracle | 未覆盖边界 | contractVersion | arbiterCapability | arbiterAuthorization |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| RL34-M1 | 协议断言/独立复核/CI/Git读回 | machine | RL34-M1 | 部分 | P2 同名验收条件 | 本地协议回归通过，后续交付待验证 | Python 3.12.3 / Linux | 用户原话与原协议边界、fresh复核报告 | 不承诺真实 Herdr 运行 | 1 | 文档与代码事实核验 | 本卡开工授权 |
| RL34-M2 | 协议断言/独立复核/CI/Git读回 | machine | RL34-M2 | 部分 | P2 同名验收条件 | 本地协议回归通过，后续交付待验证 | Python 3.12.3 / Linux | 用户原话与原协议边界、fresh复核报告 | 不承诺真实 Herdr 运行 | 1 | 文档与代码事实核验 | 本卡开工授权 |
| RL34-M3 | 协议断言/独立复核/CI/Git读回 | machine | RL34-M3 | 部分 | P2 同名验收条件 | 本地协议回归通过，后续交付待验证 | Python 3.12.3 / Linux | 用户原话与原协议边界、fresh复核报告 | 不承诺真实 Herdr 运行 | 1 | 文档与代码事实核验 | 本卡开工授权 |
| RL34-M4 | 协议断言/独立复核/CI/Git读回 | machine | RL34-M4 | 部分 | P2 同名验收条件 | 本地协议回归通过，后续交付待验证 | Python 3.12.3 / Linux | 用户原话与原协议边界、fresh复核报告 | 不承诺真实 Herdr 运行 | 1 | 文档与代码事实核验 | 本卡开工授权 |
| RL34-M5 | 协议断言/独立复核/CI/Git读回 | machine | RL34-M5 | 部分 | P2 同名验收条件 | 本地协议回归通过，后续交付待验证 | Python 3.12.3 / Linux | 用户原话与原协议边界、fresh复核报告 | 不承诺真实 Herdr 运行 | 1 | 文档与代码事实核验 | 本卡开工授权 |
<!-- dh:review-attempt:v1 task=RLT_34 attempt=1 kind=full reviewer_session_id=/root/rlt34_code_review status=punched -->
