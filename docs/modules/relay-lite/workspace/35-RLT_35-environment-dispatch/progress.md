<!-- dh:v1 -->
# progress — RLT_35

## 日志 (Log)

| 时间 | 谁 | 做了什么 | 证据 | 下一步 |
|---|---|---|---|---|
| 2026-10-07 | /root | 确认承接；#12 落户与独立 worktree/正式输入/七件套 | brief、review.plan、GitHub #12 | 实施/测试 |

## 证据账本 (Evidence Ledger)

| ID | 类型 | 命令 / 路径 | 结果 (pass/fail/observed/waived) | 支撑什么结论 |
|----|------|-----------|------|------|
| E-001 | test | python3 -m unittest discover -s tests -v；evidence/baseline.log | pass | 开工基线41项，exit0；不证明live Herdr |
| E-002 | check | dh relay-lite；evidence/check-initial.log | fail | 初始规划marker/需求表预填格式17失败，原结果保留；按实际规划原报告补正 |
| E-003 | check | dh relay-lite；evidence/check-planning.log | pass | 规划/预填格式补正后0失败，警告非阻断 |
| E-004 | test | evidence/config-implementation.log | pass | 配置局部实现17项定向测试；三端工具闭包 |
| E-005 | test | evidence/candidate-first.log | fail | 首轮53项1 error：旧watcher标题引用；保持兼容标题修正 |
| E-006 | test | evidence/candidate-green.log | fail | 58项1 failure：核心漏workspace_id映射，补显式接口说明 |
| E-007 | test | evidence/candidate-final.log | pass | 全套58项exit0；包括动态发现/通知与安装/CLI |
| E-008 | test | evidence/mutation-red.log；mutation.json | observed | 未知环境回退变异，指定测试断言失败exit1，不是导入/环境失败 |
| E-009 | test | evidence/restored-green.log | pass | 生产代码精确原字节还原；全58项exit0 |
| E-010 | review-dispatch | dh dispatch | observed | 复核派出：fresh-context-subagent｜path=code_review target_sha=3e7797417a09c8a9e2ee96bf29fd731fed182966 diff_sha256=621d81ba88ce1fe87935318bd37c2390dfbabb7531c0655f91f5690e37dc18fe｜path=code_review｜attempt=1 kind=full session=/root/rlt35_code_review |
| E-011 | review-dispatch | dh dispatch | observed | 复核派出：fresh-context-subagent｜path=code_review target_sha=20eb3797f80a451aa13c06675037f79c9aa6654b diff_sha256=01dd4935c34c729025ce6f07f937fd64869ea7fc7a76dd2683a9bc5b5a24fc2c CR-001 targeted repair｜path=code_review｜attempt=2 kind=targeted session=/root/rlt35_code_review |
| E-012 | review | evidence/code-review.json/md | fail | 初次完整独立复核 CR-001 P1：Windows 短路径断言失败；原报告保留 |
| E-013 | CI | evidence/ci-windows-failure.log；ci-initial.json | fail | 初次 Ubuntu PASS / Windows 58项1失败，非产品路径逃逸 |
| E-014 | test | evidence/repair-green.log/json | pass | 断言按 helper 相同 resolve 规范口径比较；全58项 exit0，待双平台CI |

| E-015 | CI | evidence/ci-repair.json | pass | 修复候选20eb3797两平台58项SUCCESS；初次失败保留 |

| E-016 | review | evidence/code-review-attempt2.json/md、reviewer-tests-attempt2.log | pass | 同实例唯一定向复核approved，CR-001 resolved，安装器9项通过 |

| E-017 | check | evidence/review-gate-policy-drift.json | fail | 独立路径PASS但安装版dh-check在等待期间更新，引起冻结来源摘要漂移；不放行旧freeze |
| E-018 | policy-binding | evidence/policy-source-diff.patch | observed | 仅dh-check两处改为实际Git根cwd；normal额度/分类/collector及校验器均不变，同候选重生成当前源绑定 |

| E-019 | check | evidence/review-gate.json、check-premerge.log | pass | 当前策略来源重绑定后严格原证PASS/exit0；dh0失败6警告 |

| E-020 | integration | evidence/integration.json、integrated-tests.log、integrated-review-gate.json、integrated-check.log、ci-final-source.json | pass | 实际merge908d86ba；12个产品/测试文件与review候选逐字一致，58项、原证PASS、dh0失败；最终实现source两平台CI成功 |

| E-021 | verify | git show c03ca83d19591b83678400043e1e1cb773b947fd；evidence/preverify-gate.json、preverify-check.log | pass | 实际合入复验后verify(relay-lite)生成，授权/执行者/风险0/DoD齐备；有限归档后生效 |

| E-022 | check | evidence/check-closeout.log、check-closeout-corrected.log | fail | release_mode索引空列改full被R29识别为实质B调整；还原该列，正文既有full不变 |
| E-023 | check | evidence/check-closeout-final.log | pass | 仅状态/验收日期/verifySHA/现状块机械回填，冻结正文及合同不变，dh0失败6警告 |

## 实施验证命令矩阵（开工计划复核 P1 补充）

| 用途 | 精确命令 | 预期/证据 |
|---|---|---|
| 工具与三端安装 | python3 -m unittest discover -s tests -p test_environment_config.py -v；python3 -m unittest discover -s tests -p test_install_skill.py -v | 局部执行者串行完成，config-implementation.log |
| 协议/全回归 | python3 -m unittest discover -s tests -v | 全写入结束后root串行，candidate-green.log |
| 有效单测 | python3 -m unittest discover -s tests -p test_environment_config.py -k unknown -v | 未知环境拒绝语义变异必须断言失败；精确恢复GREEN |
| 原证闸/文档闸 | dh gate relay-lite 35-RLT_35-environment-dispatch --review-json；dh relay-lite | 当前worktree根调用；原JSON/实际退出码 |
| 合入复验 | python3 -m unittest discover -s tests -v；dh gate relay-lite 35-RLT_35-environment-dispatch --review-json | 主干实际merge后，完整Git元数据，同产品原字节 |

独立开工计划复核已确认设计/任务完整，命令矩阵P1采用；watcher通用流程适用全部kind，CLI能力在环境协议，宿主进程句柄在两adapter。

实施里程碑@候选就绪：环境gate/Herdr协议/通用watcher/安装闭包就绪，58项回归与有效单测完成，失败历史保留；下一步fresh code_review。

CR-001 同范围修复：仅测试期望路径规范化；候选登记 miner 两条草稿，不改验收/产品/正式知识库。

阶段汇报@独立复核收敛：完整初审P1→同实例唯一定向approved；双平台CI、当前源绑定原证闸PASS。采用仓库允许的merge commit保留被审候选祖先，便于合入后原证重建；范围和验收不变，待实际合入及verify，不提前完成。

收口汇报@合入复验：已解决环境入口及通用watcher步骤；58项本地/双平台CI及fresh初审→唯一修复复核通过，实际主干复验原证PASS。无未决P0/P1及风险；miner两条草稿留本卡待裁决；liveHerdr及真实副本不在本卡。完整交付授权未撤销，执行自动验收/verify/有限归档，不启下一卡。

有限归档只含真实集成/验收/verify原证及机械状态回填；不修改产品、冻结验收或正式知识库。销户/清理以远端实际合入及读回为准。
