# progress — RLT_38

## 日志 (Log)
| 时间 | 谁 | 做了什么 | 证据 | 下一步 |
|---|---|---|---|---|
| 2026-10-09 | 主会话 | Issue21及独立任务树落户 | brief / task_plan | 施工 |

## 证据账本 (Evidence Ledger)
| ID | 类型 | 命令 / 路径 | 结果 (pass/fail/observed/waived) | 支撑什么结论 |
|----|------|-----------|------|------|
| E-001 | inspection | git status / gh repo / workflow | observed | 干净基线、目标与普通CI确认 |
| E-002 | measurement | evidence/measure.py → evidence/size-ledger.json | pass | 同口径前后字符统计，含迁移文件 |
| E-003 | inspection | evidence/rule-map.md / section-map.json | observed | 规则与读取/分发路径映射 |
| E-004 | test | python3 -m unittest discover -s tests -v；evidence/tests-restored.log / mutation-red.log / mutation.json | pass | 80项通过，生产分发漏件真实RED与恢复 |
| E-005 | review-dispatch | dh dispatch | observed | 复核派出：fresh-context-subagent｜path=code_review target_sha=1ad96109b398776e99e25ed6f577e923e14a91cc diff_sha256=12ab5546bac62409f154df06ca2997f0212008f0eaaa2c0f734e8bfc7dcba5ea｜path=code_review｜attempt=1 kind=full session=/root/rlt38_code_review |
| E-006 | independent-review | evidence/code-review-1.md / code-review-1.json | pass | fresh完整approved，无open问题，独立80项及统计/引用通过 |
| E-007 | gate | evidence/review-gate.json / dh-check-reviewed.log | pass | collector PASS及dh-check零失败；12个命名/历史口径警告如实保留 |

## 计划检查裁决与施工补充（不回写已开工基线）
plan-check.md为独立计划检查，不是code_review。主会话直接施工、未派零上下文施工worker；检查返回前已开始范围内重组。采纳其证据细化建议，本卡目标/验收不变：
- 字符统计由evidence/measure.py取基线Git内容与当前skill内md/toml，输出size-ledger.json；包含新增references，字节解码UTF-8后len，不把拆分当净节省。
- evidence/rule-map.md逐条列旧章节、新落点、读取者及检查；section-map.json保存大节迁移。共同正文去重、条件/时序/角色保留由fresh完整复核核语义，字符/关键词不冒充语义证明。
- 安装闭集增card-chain/orchestration/verification/document-role/watcher及dispatch；三side加旧别名共六临时home副本。test_installed_reading_routes_are_closed_and_template_is_unique从真实安装入口沿相对链接遍历，不依赖SKILL_FILES作为oracle，核源字节及唯一模板字段；test_missing_routed_contract_rejects_before_install逐文件缺失拒绝。
- 有效变异：仅从生产SKILL_FILES漏掉references/card-chain.md，运行上述安装消费者测试，必须真实AssertionError；保存施加/还原Git blob hash并恢复原字节，再全量GREEN。不接受导入/语法失败。
- 环境协议旧章节引用随迁移修链接；test_space_watch仅改为沿链接读取合同，保留全部原断言。均属原安装/适用回归范围，精确路径已列源卡。
- 首轮80项中两条结构测试仍要求原文件承载正文而失败，保留tests-first.log；已改为核引用路径与实际被引用正文，不删除行为断言。

阶段汇报@实现验证：包50930→39236（-22.96%）、核心23312→10720（-54.01%）、两adapter16347→3143（-80.77%）；80项GREEN，有效分发变异RED→恢复GREEN；实现候选双平台CI通过。总量略低于约25%–35%目标，保留完整规则为先，最终实测不改口径。

本次miner产出1条候选 → evidence/miner-result.md；只作候选，未代用户裁决入正册。原lesson_candidates.md冻结不改，E6证据留此。
