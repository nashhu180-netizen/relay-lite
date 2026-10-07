# RLT_33 独立代码轮 1

审阅者：fresh context `code_review1`（未参与实施）。

审阅对象：独立仓候选 `db18185b160c653eebe2121727b9f9f85c22716b`（含产品提交 `dd15a7077ed2121de38bb4b717aef50864f24d69`，相对新仓初始 `60bc7ea`）；源仓迁出候选 `d8f88ae`（相对冻结源 `2246b16cb82f86a594f7b2c36365e7851fe11263`）。最终增量只加入孤立 clone/源回归证据、`archive/** -text` 与源专属 suite 的精确允许路径，不改变产品行为。本报告只审当前迁出/分发实现，不构成需求、人验、一致性、教训、代码轮 2、变异、PR/CI、合入或 verify 放行。

## 覆盖与证据

- 对照 `brief.md`、`task_plan.md`、设计 RL33-M1～M6 和 P1 卡合同，检查独立包、安装器、两侧 adapter、迁出入口与 CI 边界。
- `python3 -m unittest discover -s tests -v`：39 tests / exit 0。覆盖三侧安装、显式 `--legacy-alias`、受管理退役 `dh-mapping.toml` 的只删未改保护、孤立目录安装、watcher 的 workspace 动态发现、投递确认与 `RELAY_RECEIPT` fail-closed。
- 独立复算 `migration-plan.json` 的 948 条记录：逐条读取 `/tmp/rlt33-frozen-source` 的冻结源，SHA256 与清单一致；archive 字节及两份现役总表移除迁移头后的正文均一致；mismatches=0。
- 对比旧/新 `space_watch.py`：行为实现仅把通知前缀从 `[relay-light]` 改为 `[relay-lite]`；轮询、动态发现、watcher/主编排排除、失败投递不消费基线、无文件写入与环境拒绝保持。
- 审阅源仓 `tools/tests/relay-light-log.ps1` 的补漏：保留 `run-relay-tests.ps1` 的原 Runner suite 汇总入口，替换的末项只断言产品目录已迁出、`docs/relay` 无现役重复总表、并有独立仓指针；不触及 Runner 产品代码。候选归档的 `evidence/source-pwsh-final.log` 记录完整 PowerShell 汇总终态为 `RELAY ALL PASS (SKIPPED: 1)`，其中真实 psmux 沿原条件 skip。

## Findings

| 级别 | 结论 |
|---|---|
| P0 | 无 |
| P1 | 无 |
| P2 | 无 |
| P3 | 无 |

## Verdict

`PASS`：当前候选满足本轮代码安全/隔离/兼容性审阅的范围。后续仍必须完成 heavy 卡的 fresh 代码轮 2、需求、一致性、教训、有效变异 RED→恢复 GREEN，以及两仓 PR/CI/合入态复验与 verify；本结论不代替其中任何闸门。

## 定向补审：源 CI 观察项（2026-10-07）

审阅源仓追加候选 `6a431e9f4097eb68d31da1ddba1dff17515a8085`。`.github/workflows/ci.yml` 的唯一行为改动是 `relay-core` 的 `npm test` 改为 `timeout 180s npm test`。该 job 原有 `continue-on-error: true` 保留，仍明确是暂停模块的观察项；PowerShell Windows/Ubuntu matrix 和 `relay-light-python` 迁出边界硬门均未改变，顶层 `concurrency` 的 `cancel-in-progress: true` 也未变。因此超时只保证 workflow 能抵达终态，不将 relay-core timeout/失败表述为 core PASS，也不降低必要门。

同时读回独立仓：最终提交仍为 `db18185b160c653eebe2121727b9f9f85c22716b`，之后无提交；工作树变化仅为后续复核、变异与交付证据/报告，未见 `skill/`、`tools/`、`tests/` 或产品合同文件变化。

定向结论：`PASS`，无新增 P0～P3。该结论仍不代替 GitHub Actions 的实际最新 run 终态或其它收口闸门。
