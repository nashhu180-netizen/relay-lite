# RLT_33 fresh-context 教训候选复核

审阅者：fresh-context `miner`（本会话未继承本卡父会话历史）；只读核对产品、设计、DevPlan、workspace、证据与现有候选。仅写本报告、模块候选区和本路径 signal；不改产品、测试、计划、任务状态、维护者表、PR/CI 或人验记录。

## 审阅范围与去重

- 读取 `/tmp/rlt33-mine.log`，以及本卡 `review.md`、`findings.md`、`progress.md`、`lesson_candidates.md` 与模块 `knowledge/教训库-候选.md`。
- 正册没有在册条目；候选区已有候选-001/002，故不重复新建。`mine.log` 的“候选区为空”是挖掘前的只读备料快照，不是当前状态。
- 同步只读核对 `AGENTS.md`、RLT_33 设计/DevPlan/brief 的治理补正、`docs/table-cutover.json`、两份维护者 ACK、`import_commit=9458e4f` 审计、`.github/workflows/ci.yml` 的 `fetch-depth: 0` 和 `dh relay-lite`。

## 候选裁定

| 候选 | fresh 结论 | 证据与可复用性 |
|---|---|---|
| 候选-001 | 保留，待裁决 | F6、L1 和 `review.code2.md` 都表明，源仓 PowerShell 专属 suite 在产品目录迁出后仍调用旧路径，完整回归末尾失败；随后改为明确退役边界断言并实跑通过。这是“文件迁移闭集没有反查外部测试/CI 入口”的重复风险，不是一次性笔误。 |
| 候选-002 | 保留，待裁决 | F5、L2 记载活动树删除文件与旧全量基线并发，使取证失去归因；无效日志被保留而未充作业务 RED，冻结 SHA 副本的相关回归另跑。这适用于所有会改动被测输入的长运行取证。 |
| 候选-003 | 新增，待裁决 | 固定迁入审计读取祖先 `9458e4f`；`fdcb6fc` 后 CI 37602646669 因默认 shallow checkout 在两个 matrix job 均缺对象而失败。定向复核复现 depth-1 的 exit 128/测试 ERROR；当前 workflow 显式 `fetch-depth: 0`，未删 matrix 或跳过审计。根因是 CI history 前提遗漏，适合作为可复用候选。 |

候选-001/002 的根因和动作均有实际证据，未发现应删除的无依据候选。候选-003 已追加到模块候选区，均维持“待裁决”，未进入正册。

## 同步事实核对

- `table-cutover.json` 记录 AW `5a47a4f...` 与 WFP 未合入 PR158 `65f87a0...`、两份 ACK，以及 `paused_ack_received_waiting_new_merge`；两表均固定 `import_commit=9458e4f...`。这只证明候选保真和暂停状态，不转移维护权、合入或路径恢复确认。
- 旧 `coder`/历史 signal schema 出现在迁入表的保真正文，`review.code2.md` 明确新实例仍使用 `executor`；它是历史字节保留，不能归因为权限漂移。
- 本次实跑 `dh relay-lite`：退出 0，`0 failures, 2 warnings`。warnings 为 R19 文件命名建议和 R14 reader 对 `RLT_33` 标题/编号的支持域限制；记录为 warnings，不能称 dh 全绿。

## 结论

**PASS（仅 fresh-context 教训挖掘与事实核对）**：三条候选均有可回查根因和跨类似任务的预防动作，仍待人裁决；本报告不构成产品复核、CI 成功结论、合入、verify、人验或部署放行。
