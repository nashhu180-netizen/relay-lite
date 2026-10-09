<!-- dh:v1 -->
# progress — RLT_36

## 证据账本 (Evidence Ledger)
| ID | 类型 | 命令 / 路径 | 结果 (pass/fail/observed/waived) | 支撑什么结论 |
|----|------|-----------|------|------|
| E-001 | authorization | 用户“确认开始修复，建个issue”；异步确认reviewer及隔离三角色模型。 | observed | 本卡实际证据；具体通过/失败见原始日志。 |
| E-002 | issue | GitHub Issue15 create+fetch成功，状态open。 | observed | 本卡实际证据；具体通过/失败见原始日志。 |
| E-003 | test | baseline.log/json：原主干58项通过；initial-red.log：新增两项通知可靠性业务负例触发WatchError，不是setup/import失败。 | observed | 本卡实际证据；具体通过/失败见原始日志。 |
| E-004 | test | candidate-green.log/json：75项通过；安装闭集及新等待入口已覆盖。 | observed | 本卡实际证据；具体通过/失败见原始日志。 |
| E-005 | test | mutation.json/red.log/restored-green.log：精确派单匹配有效变异红（exit1）→原hash恢复，全76项绿。 | observed | 本卡实际证据；具体通过/失败见原始日志。 |
| E-006 | planning-review | 独立review.plan初审REVISE及定向PASS保留；只闭合方案，最终code_review未派。 | observed | 本卡实际证据；具体通过/失败见原始日志。 |
| E-007 | test | evidence/live/scene-A.json、scene-B-monitor-stop.json、final.json及原角色report/signal | pass | 普通monitor同PID169秒/actor结束，busy提交无seq要求；monitor停止后主编排3PENDING→READY、实核worker done、生成本演练预授权交接；未再次派单编排。 |
| E-008 | observed | evidence/live/startup-failure.json与runtime-models.json | observed | duplicate--no-daemon启动失败保留，修正重复参数后三角色实argv/cwd/模型确认；未改用户配置。 |
| E-010 | test | evidence/candidate-final.log、check-candidate.log；76项，exit0，dh exit0 | pass | 完整候选本地验证；未替代独立复核和远端CI。 |
| E-011 | miner | evidence/miner-input.txt；fresh实例/root/rlt36_miner→lesson_candidates.md | observed | dh mine只读备料exit0；候选草稿留本工作区，不越界写知识库，不代替独立代码复核。 |
| E-009 | review-dispatch | session=/root/rlt36_code_review path=code_review target_sha=fa9c21fa2dcce7f55760ef19f93ac28a3188e34b diff_sha256=9d351c5118e97824b9530b283d0186cb647a0f572078b12bec87c22aab9d149a baseline_sha=dfbe56371b569ff768e7bcd82eeb8d204d55dfea; attempt=1 kind=full fresh=true | observed | 完整候选绑定独立gpt-6.1-sol/high实例；只允许写两份原报告。 |
| E-012 | ci | evidence/pr16-candidate-ci.json；候选fa9c21f两平台SUCCESS，PR16为draft | pass | 初始候选平台CI；证据提交后须读取最新source检查，未合入。 |
| E-013 | review-result | evidence/code-review-1.md/json；fresh独立实例原报告approved，无findings，另跑76项通过 | pass | normal完整代码复核一次闭合，无定向复查资格/必要。 |
| E-014 | gate | evidence/review-gate.json；dh.review-gate.v2 PASS exit0 | pass | 原报告、Git候选/diff/派出身份/政策摘要由共享collector核验，未自造PASS。 |
| E-015 | integration | evidence/pr16-final-ci.json、pr16-merge.json、integration.json及integration-tests/check/gate | pass | PR16最新source双平台SUCCESS，实际merge b940ca0；干净master76项/check/gate均exit0，产品与独立所审候选同字节。 |
| E-016 | cleanup | evidence/cleanup-space.json | pass | 仅自建w6Y关闭；初次非JSON返回异常保留，只读list证实不存在，PID740665消失；未重复close或操作其它space。 |
