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
