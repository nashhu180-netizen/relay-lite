# RLT_33 源仓有限收口独立复核

审阅者：`code_review2`（独立只读）。范围仅为 dh-relay 源仓 `8cbff631af90198484036f60c2a82a2b032ff680..0238a13d4e1f166e7b8dfdae008398f2aef1d95c` 的有限收口记录、verify 留痕和 PR159 边界；不复审独立 relay-lite 主收口，也不代替两仓最终结论。以下初核快照保留为历史，primary 当前状态以文末「PR4 时态更新」为准。

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

## 更新：源实际合入与 primary 有限收口候选

审阅范围：独立仓 `7a3346f3c2f1f6cd010df382ccd06f96b513e453..bd2509b13838df1faa34b51d68612a7c6cf99647`，以及源 PR159 实际合入/readback 与两维护者恢复回执。除本报告和 DONE 外未写其它文件。

- primary 差异仅含验收/状态/证据/as-built/知识回填和 `table-cutover` 收口记录；不含 `skill/`、`tools/`、`tests/`、`archive/` 或 `docs/relay/**` 业务 live 表修改。`git diff --check` 无输出。
- `verify(relay-lite)` `bed13739844d9009f223e7c35212b8da97118fe2` 是在 primary 合入态 `7a3346f` 后创建，且是当前候选祖先。其机器验收声明仍受冻结 RL33-M1～M6 约束：full、H=0、六项 Linux 安装副本 hash 已核、39 tests/两系统 CI/有效变异 RED→精确恢复 GREEN 与五条独立路径证据均有指针；不代替其它业务卡人验。
- 源 PR159 已实际 server squash 合入 `fde68d870b6bff25caf677a12343c923453ada67`。GitHub readback 与 `source-closeout-ci.json` 一致：Windows/Ubuntu Runner、relay-light Python 三项成功；relay-core timeout/FAILURE 继续作为暂停观测，不被改写为绿。`source-closeout-sync.json` 记录本地 `2fb5b1e` 与远端树相同，并保留 `5a47` 与 `3940ad5` 祖先，未推无关历史。
- AW 与 WFP 的 resumed ACK 均已入证据。WFP ACK 明确恢复的是新表维护权；它不声明 H1～H3、任何真实业务人验或 PR158 完成。PR158 仍 OPEN。六份 Linux 安装副本均由 `skill-readback.json` 读回同一 `7a3346f` source/hash；证据标记 `live_process_changes=none`，未出现 Windows 副本或进程变更主张。
- `dh-check-final.log` 为 0 failure / 2 warnings。primary 当前尚无新的 PR/远端 CI/服务端 merge，故本结论不把 `bd2509b` 视为已合入，且不关闭 Issue 或清理工作树。

| 级别 | 结论 |
|---|---|
| P0 | 无 |
| P1 | 无 |
| P2 | 无 |
| P3 | 无 |

更新 verdict：`PASS`，分层结论如下：源有限收口已实际合入；primary `bd2509b` 的有限收口候选内容和 verify 前提通过只读复核，但仍待创建 PR、完整 CI、服务端合入及合入态读回。两层不得互相替代。

## PR4 时态更新

此节覆盖上文 primary “待创建 PR/CI”的初核时态。PR4 已建立，head 仍为 `bd2509b13838df1faa34b51d68612a7c6cf99647`；GitHub CI `37607279283` 的 Ubuntu 与 Windows `relay-lite-python` 均为 `SUCCESS`。PR4 当前仍 OPEN，`mergedAt=null`、`mergeCommit=null`，故实际服务端 merge、合入态读回、最终 verify/Issue 收口仍待后续核验。本更新不改变已完成的源 PR159 子结论，也不授权合入。
