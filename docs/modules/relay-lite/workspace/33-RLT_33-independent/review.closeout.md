# RLT_33 源仓有限收口独立复核

审阅者：`code_review2`（独立只读）。范围仅为 dh-relay 源仓 `8cbff631af90198484036f60c2a82a2b032ff680..0238a13d4e1f166e7b8dfdae008398f2aef1d95c` 的有限收口记录、verify 留痕和 PR159 边界；不复审独立 relay-lite 主收口，也不代替两仓最终结论。

## 覆盖与证据

- `8cbff63..0238a13` 只修改源模块 P1 的 RLT_33 状态记录与本卡 `progress.md`，没有产品、测试、总表或旧卡状态差异；`3dd817e` 是空的 `verify(dh-relay)` 提交，`7082766` 和 `0238a13` 只补收口事实/候选状态。
- 实现 PR157 已实际 squash 合入 `8cbff63`。`source-sync.json` 记录本地整合 `3b8a0e` 保留本地 `5a47` 历史、与远端合入树相同、未推无关提交；本次候选树干净。
- `/tmp/rlt33-source-verify-message.txt` 的 verify 明确把 `relay-core` 观察失败和历史 dh 失败保留为非绿，不把它们写成产品通过；源合入态 PowerShell 证据为 `RELAY ALL PASS (SKIPPED: 1)`，并与独立仓 `source-merged-tests.log` / `source-sync.json` 对应。
- GitHub PR159 当前为 `OPEN`，`mergedAt=null`、`mergeCommit=null`，head 为 `0238a13`。此前 `7082766` 的完整 workflow 是 success，但该 head 前进后已重新触发 CI；当前 relay-light Python 已成功，Windows/Ubuntu Runner 仍 `IN_PROGRESS`，relay-core 仍 `QUEUED`。因此不把旧 run 的结果移植为新 head 的 CI 结论。
- P1 的“已完成（PR159待合入候选，仅合入后生效）”与 progress 的“最终 SHA 以 PR159 `merge_commit_sha` 为准”共同保留了实际合入边界。WFP 的第 19 次恢复通知仅记录投递，ACK 仍待原维护者确认；不把投递写成恢复或维护权转移。

## Findings

| 级别 | 结论 |
|---|---|
| P0 | 无 |
| P1 | 无 |
| P2 | 无 |
| P3 | 无 |

## Verdict

`PASS`（仅源仓有限收口候选）。源实现合入和 source verify 留痕的事实一致，且 PR159/新 head CI/最终 merge SHA/WFP 恢复 ACK 均未被提前宣称完成。新仓 primary 收口、两仓实际合入态和最终 verify/Issue 收口仍是独立后续闸门。
