<!-- dh:v1 -->
# review — RLT_36

## 独立复核区
normal=[code_review]，完整候选后fresh一轮；待候选提交后派出。

## AI 提交区
本卡机器验收通过（AI codex-root-rlt36-20261009依据开工授权；不代签用户体验）。原卡离线通过不证明本卡持续任务交接，本卡新增真实隔离证明。

## 完成条件逐条挂证据
| ID | 条件 | 谁验 | 证据 | 达成? |
|---|---|---|---|---|
| RL36-M1 | 常驻监控运行在 Herdr 独立普通终端，不依赖 watcher 模型回合；兼容旧 agent 身份入口并核真实 pane/space。 | AI | E-003/005/007；tests/test_space_watch.py；live/scene-A.json | 已满足 |
| RL36-M2 | 通知仅确认提交，不用主编排 working/seq 变化证明消费；忙碌可提交，审批阻塞延后，未知投递不盲重发且继续观察。 | AI | E-003/005/007；busy/deferred/unconfirmed单测及live/scene-A.json | 已满足 |
| RL36-M3 | 临时只读观察失败保留基线后恢复；身份/RELAY_RECEIPT 硬闸不放宽；同 space 监控重复启动有单实例保护。 | AI | E-005；观察恢复、receipt/身份、singleton行为单测 | 已满足 |
| RL36-M4 | 提供主编排只读有界 signal 等待入口；watcher 暂停/缺席时能发现精确本批结果，READY 不是 PASS，仍核原报告与 durable signal。 | AI | E-005/007；tests/test_task_wait.py；live/orch-report.md、精确信号与实态 | 已满足 |
| RL36-M5 | 隔离真实 Herdr 演练证明 watcher agent 空闲/暂停及通知忙碌场景下，worker 完成后主编排实际核结果并完成已授权交接。 | AI | E-007；live/scene-A.json、scene-B-monitor-stop.json、final.json及两角色原report/signal | 已满足 |
| RL36-M6 | 安装包闭集同步，行为回归/有效 RED→恢复 GREEN、fresh code_review、双平台 CI、实际合入复验与 verify 齐备。 | AI | E-005/013/014/015；本次verify提交及有限收口归档 | 机器验收已满足，远端收口归档待完成 |

## 需求对齐证据
| 需求 / 人验项 | 场景与操作路径 | 证据 (E-00x) | 结论（满足 / 不满足 / 待人验） |
|---|---|---|---|
| watcher暂停不阻断 | 独立程序存活与精确结果等待/交接 | E-005/007 | 满足（隔离演练） |
| 通知异常隔离/边界 | 状态与通知反例、有效单测、独立复核 | E-003/005/007 | 满足（行为证据；独立代码复核另核） |
| 安装与交付 | 三端临时home安装/CI/实际合入/verify | E-005/013/014/015 | 满足（实现PR16合入与实际主干复验；验收证据归档按有限收口PR） |

## 人类签名区
不代签；本卡机器证明进程/提交/交接事实，用户整体体验不预填通过。

- 契约同步：skill/SKILL.md、两adapter和environment-herdr已同步独立监控、提交确认及owner有界等待，安装闭集包含task_wait.py。

## 有效单测·变异点登记

| 变异点锚点(生产代码 path:line) | 原值→变异值 | 语义类别 | 对应测试 ID | 运行命令 | 施加 hash | 还原 hash | 登记人(重核须=轮2实例) | 施加后结果 |
|---|---|---|---|---|---|---|---|---|
| tools/task_wait.py:80 | 精确派单不匹配则忽略→if False放过不匹配 | 改边界 | test_task_wait.TaskWaitTests.test_wrong_dispatch_old_round_or_partial_write_never_ready | python3 -m unittest discover -s tests -p test_task_wait.py -k wrong_dispatch_old_round -v | 43d3c84dc8ea423be73f9e282aabc19f78f30e318f354770e7c50d4ed4951e47 | 5526592c267158079f3d549df7e409aa148c3a28f11946bba4dd1ccf894797a0 | codex-root-rlt36-20261009 | 业务断言失败，exit1；精确还原后76项通过exit0，见E-005 |

<!-- dh:review-attempt:v1 task=RLT_36 attempt=1 kind=full reviewer_session_id=/root/rlt36_code_review status=punched -->
完整候选fa9c21f已派fresh code_review，唯一允许报告路径evidence/code-review-1.md/json。

<!-- dh:review-result:v2 task=RLT_36 path=code_review attempt=1 artifact=docs/modules/relay-lite/workspace/36-RLT_36-watcher-reliability/evidence/code-review-1.json artifact_sha256=96c299b0bb1522bbb9b2da2bc96739325098af04ce34ddf5098076b458a5476d -->

独立/root/rlt36_code_review完整一轮approved，findings=[]，精确候选fa9c21f；原报告evidence/code-review-1.md/json只机械绑定，未改原字节。

## 自动验收与放行记录

2026-10-09，AI codex-root-rlt36-20261009核本卡开工授权未撤回；M1–M5行为证据、安装闭集、变异、独立复核、双平台CI和实际merge复验齐备；本卡结果项均为机器可证事实，没有代签任何用户判断，无未决方向/风险/遗留发现。Verification=full，Risk-Count=0，尾巴为空。用户整体体验仍无用户签名，不在本卡机器通过结论内。

当前实际主干b940ca0与所审fa9c21f产品同字节；76项、dh/check和collector PASS。as-built中“最终复核/CI/合入/verify未完成”为实施候选快照，最终交付状态以本工作区E-013起的真实证据与源卡status为准，保留原快照，不重写历史。

源码和协议交付不代表现有业务space或安装副本升级；本卡不部署、不重启、不开始下一卡。有限收口只归档本任务机器证据与源卡机械状态，不改变产品或验收合同。
