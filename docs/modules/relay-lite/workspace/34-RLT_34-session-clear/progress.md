<!-- dh:v1 -->
# progress — RLT_34

## 日志 (Log)

| 时间 | 谁 | 做了什么 | 证据 | 下一步 |
|---|---|---|---|---|
| 2026-10-07 | /root | 承接确认建 #7/#8；补齐核心及 adapter 清理门，回归/变异还原通过；阶段汇报@候选就绪 | E-001～E-004；GitHub #7/#8 | fresh 独立复核 |

## 证据账本 (Evidence Ledger)

| ID | 类型 | 命令 / 路径 | 结果 (pass/fail/observed/waived) | 支撑什么结论 |
|----|------|-----------|------|------|
| E-001 | test | python3 -m unittest discover -s tests -v；evidence/baseline.log | pass | 基线 39 项通过，退出码 0 |
| E-002 | test | python3 -m unittest discover -s tests -v；evidence/candidate-green.log | pass | 候选 41 项通过，退出码 0 |
| E-003 | test | python3 -m unittest discover -s tests -p test_contract.py -k test_new_task_clear_is_a_predispatch_gate -v；evidence/mutation-red.log | observed | 故意取消新任务 clear 门，断言失败，退出码 1 |
| E-004 | test | python3 -m unittest discover -s tests -v；evidence/restored-green.log | pass | 精确字节还原后 41 项通过，退出码 0 |
| E-005 | check | dh relay-lite；evidence/check-initial.log | fail | 初次工件缺需求对齐表 R12，原失败保留并补齐 |
| E-006 | check | dh relay-lite；evidence/check-second.log、check-candidate.log | pass | R12 第二次结论枚举缺失已补正，最终 exit 0；4 项非阻断警告保持 |
