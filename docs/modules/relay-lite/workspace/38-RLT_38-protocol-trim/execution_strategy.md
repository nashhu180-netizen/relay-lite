<!-- dh:v1 -->
# execution_strategy — RLT_38

主会话直接实施本仓维护任务，不担任业务relay orchestrator，不启动Herdr角色。AGENTS允许fresh-context subagent独立复核，继承当前模型，仅写本路径review原件；非机器沙盒只读。
implementer_session_id=codex-root-rlt38-20261009。
基线=0b08c18be09cd00e84ff214c582941593ca7c2ec；任务树=.dh-worktrees/RLT_38；origin wt/RLT_38→master。
总表：无（独立维护卡）。授权见brief。normal一轮完整fresh code_review，仅初审open P0/P1才同实例一次targeted。

<!-- dh:review-freeze:v2 -->
```json
{
  "schema": "dh.review-freeze.v2",
  "task_id": "RLT_38",
  "card_ref": "docs/modules/relay-lite/dev_plan/P6-协议精简.md#rlt_38",
  "task_type_marker_sha256": "1cf121c545a69491a403c4771f201dfb1537ff16069b5dc258c9313d1425dc44",
  "classification_facts": {
    "production_operation": {
      "value": false,
      "evidence": "docs/modules/relay-lite/workspace/38-RLT_38-protocol-trim/brief.md#分类事实"
    },
    "irreversible_migration": {
      "value": false,
      "evidence": "docs/modules/relay-lite/workspace/38-RLT_38-protocol-trim/brief.md#分类事实"
    },
    "metric_semantics": {
      "value": false,
      "evidence": "docs/modules/relay-lite/workspace/38-RLT_38-protocol-trim/brief.md#分类事实"
    },
    "security_or_shared_guarantee": {
      "value": false,
      "evidence": "docs/modules/relay-lite/workspace/38-RLT_38-protocol-trim/brief.md#分类事实"
    },
    "behavior_or_rule_semantics_changed": {
      "value": true,
      "evidence": "docs/modules/relay-lite/workspace/38-RLT_38-protocol-trim/brief.md#分类事实"
    }
  },
  "policy_version": "three-tier.v2",
  "policy_source_digest": "1e02aeb3100185fd8541d24db5f25729a7b4e5769ce0424581ee9e46a8a9faa6",
  "policy_sources": [
    {
      "path": "tools/dh-policy/three-tier.mjs",
      "sha256": "86193917583b697c59a6e871e32e3426e3a277ac8d3c7c4d4dbc008847a08914"
    },
    {
      "path": "tools/dh-policy/task-type.mjs",
      "sha256": "a24074db98a9a0e68fc768c6475a80b312dd2ad3a2ded0d6b34ede2d61089ddd"
    },
    {
      "path": "tools/dh-policy/registry.mjs",
      "sha256": "3f584e35c059a8fd4455a6ff098c50e55e57c9d29580b9a7828b9c2849688fe2"
    },
    {
      "path": "tools/dh-policy/review-policy.mjs",
      "sha256": "2d82aa02cfa870659e8647443be3da570bef7f59b438705ba7f73caefc23e886"
    },
    {
      "path": "tools/dh-policy/review-gate.mjs",
      "sha256": "4673dca40e8f4dbb24ada4b72318d3ce57dc1de788abd4aaae56cfe022ca94d4"
    },
    {
      "path": "tools/dh-policy/policy.mjs",
      "sha256": "694de48b3bd64459af89b9ec8497db35f256ec320f59c2f6ae21ca0a9c88ff4d"
    },
    {
      "path": "tools/dh-policy/migration.mjs",
      "sha256": "5f3b09e793a5e5f763f315384f1be86e873ff6f31da06fc1226106ba9c488c06"
    },
    {
      "path": "tools/dh-core.mjs",
      "sha256": "0c6d4bcfff6f47b8327c0beb07ae8decbb60e4e001f505956fe2542a356d2c47"
    },
    {
      "path": "tools/dh-check.mjs",
      "sha256": "0e8b97517325dde560cc4ae7d085f5da08e07db2d68775b6920fca16ecd35e1b"
    },
    {
      "path": "tools/dh-nav.mjs",
      "sha256": "d4f1ac1fbb205a4cc4df2b4b511ecf0b8375ad2dc3c71a8fb9babb671e3345f7"
    },
    {
      "path": "tools/dh-r18.mjs",
      "sha256": "13b0ebd91627c1f65aa25117774162a9ca1f79eac49d6a4a529321dabb00fc6b"
    },
    {
      "path": "tools/dh-dispatch.mjs",
      "sha256": "5155f285ca6198a5082a77d22e466d8d8bee17b0b4ad8961d1c228c448c041ba"
    },
    {
      "path": "tools/dh-release.mjs",
      "sha256": "0ec53acaa6b50f0fb7f9134832c62202fefa8dd05fb45f7f91adb97ea72d94e9"
    },
    {
      "path": "tools/dh-snapshot.mjs",
      "sha256": "620dcb35401cfe969a47b451767255aaa282147682bf640b0c36bdabfccb5328"
    },
    {
      "path": "tools/dh-console/scan.mjs",
      "sha256": "0eb22d2970790113534c2c297cca7a87003bde5f7c69b6f74dc48190e0f1a848"
    }
  ],
  "required_path_ids": [
    "code_review"
  ],
  "recipe_sha256": "f024eac087ef235c1273b4b0b532dba279d460c47744f6d9a8748de99a3f3447",
  "baseline_sha": "0b08c18be09cd00e84ff214c582941593ca7c2ec",
  "target_sha": "1ad96109b398776e99e25ed6f577e923e14a91cc",
  "diff_sha256": "12ab5546bac62409f154df06ca2997f0212008f0eaaa2c0f734e8bfc7dcba5ea",
  "implementer_session_id": "codex-root-rlt38-20261009",
  "policy_authorization_ref": "docs/modules/relay-lite/workspace/38-RLT_38-protocol-trim/brief.md#本卡开工授权"
}
```

实施Draft PR=https://github.com/nashhu180-netizen/relay-lite/pull/22，Issue21；平台允许merge commit/squash/rebase，rulesets=[]，保护查询404 Branch not protected。仍要求本卡独立复核与Ubuntu/Windows CI，不绕检查。为collector保留实际所审候选祖先，实施采用平台普通merge；本卡为仓库维护，不是业务relay运行派单。

精确任务树根调用 `dh gate relay-lite 38-RLT_38-protocol-trim --review-json`，原JSON见evidence/review-gate.json，退出0/PASS；完整原输出如下。
```json
{"schema":"dh.review-gate.v2","task_id":"RLT_38","card_ref":"docs/modules/relay-lite/dev_plan/P6-协议精简.md#rlt_38","task_type_marker_sha256":"1cf121c545a69491a403c4771f201dfb1537ff16069b5dc258c9313d1425dc44","policy_version":"three-tier.v2","policy_source_digest":"1e02aeb3100185fd8541d24db5f25729a7b4e5769ce0424581ee9e46a8a9faa6","recipe_sha256":"f024eac087ef235c1273b4b0b532dba279d460c47744f6d9a8748de99a3f3447","baseline_sha":"0b08c18be09cd00e84ff214c582941593ca7c2ec","target_sha":"1ad96109b398776e99e25ed6f577e923e14a91cc","diff_sha256":"12ab5546bac62409f154df06ca2997f0212008f0eaaa2c0f734e8bfc7dcba5ea","artifact_refs":[{"kind":"source-card","ref":"docs/modules/relay-lite/dev_plan/P6-协议精简.md#rlt_38","sha256":"cf9775e48f4edf890e8fb016353b61d58758ae3187c128dab7fa369671eb2b72"},{"kind":"classification-fact:production_operation","ref":"docs/modules/relay-lite/workspace/38-RLT_38-protocol-trim/brief.md#分类事实","sha256":"18d070c9b820d61852bfa176a8d485dbae85b39faa4d4bf4a5e5e9117b3ddaf5"},{"kind":"classification-fact:irreversible_migration","ref":"docs/modules/relay-lite/workspace/38-RLT_38-protocol-trim/brief.md#分类事实","sha256":"18d070c9b820d61852bfa176a8d485dbae85b39faa4d4bf4a5e5e9117b3ddaf5"},{"kind":"classification-fact:metric_semantics","ref":"docs/modules/relay-lite/workspace/38-RLT_38-protocol-trim/brief.md#分类事实","sha256":"18d070c9b820d61852bfa176a8d485dbae85b39faa4d4bf4a5e5e9117b3ddaf5"},{"kind":"classification-fact:security_or_shared_guarantee","ref":"docs/modules/relay-lite/workspace/38-RLT_38-protocol-trim/brief.md#分类事实","sha256":"18d070c9b820d61852bfa176a8d485dbae85b39faa4d4bf4a5e5e9117b3ddaf5"},{"kind":"classification-fact:behavior_or_rule_semantics_changed","ref":"docs/modules/relay-lite/workspace/38-RLT_38-protocol-trim/brief.md#分类事实","sha256":"18d070c9b820d61852bfa176a8d485dbae85b39faa4d4bf4a5e5e9117b3ddaf5"},{"kind":"freeze","ref":"docs/modules/relay-lite/workspace/38-RLT_38-protocol-trim/execution_strategy.md","sha256":"b8fa5a6f7263a7f8dbfef277ab4c276d9eb0e9a7703da9f5722c2012ae3af739"},{"kind":"policy-authorization","ref":"docs/modules/relay-lite/workspace/38-RLT_38-protocol-trim/brief.md#本卡开工授权","sha256":"bba4f12c84380995994100f3c6f0d5a459fc6f652ce0ed5c944e3b720d26fe64"},{"kind":"review","ref":"docs/modules/relay-lite/workspace/38-RLT_38-protocol-trim/review.md","sha256":"42e6ad43225998dfaed20b123ff59fa1fa4fe37d5da7fcf772acb017c0814ff1"},{"kind":"dispatch","ref":"docs/modules/relay-lite/workspace/38-RLT_38-protocol-trim/progress.md","sha256":"84b116278eb86d71b78e1ec998e463471a262c10f08ec24e3d767afd654860d0"},{"kind":"findings","ref":"docs/modules/relay-lite/workspace/38-RLT_38-protocol-trim/findings.md","sha256":"bcdc0e1daec26f09a2d1d3798fc99461b249ddd1d855ce4d75551ef1c0169e92"},{"kind":"review-raw","ref":"docs/modules/relay-lite/workspace/38-RLT_38-protocol-trim/evidence/code-review-1.json","sha256":"e76c0ad86af1315ced789beb2a4c1313ca393deb7a2c9c1ca69ac3d80e4c9ce0"}],"task_type_marker":"<!-- dh:task-type:v2 task=RLT_38 type=normal policy=three-tier -->","classification_facts":{"production_operation":{"value":false,"evidence":"docs/modules/relay-lite/workspace/38-RLT_38-protocol-trim/brief.md#分类事实"},"irreversible_migration":{"value":false,"evidence":"docs/modules/relay-lite/workspace/38-RLT_38-protocol-trim/brief.md#分类事实"},"metric_semantics":{"value":false,"evidence":"docs/modules/relay-lite/workspace/38-RLT_38-protocol-trim/brief.md#分类事实"},"security_or_shared_guarantee":{"value":false,"evidence":"docs/modules/relay-lite/workspace/38-RLT_38-protocol-trim/brief.md#分类事实"},"behavior_or_rule_semantics_changed":{"value":true,"evidence":"docs/modules/relay-lite/workspace/38-RLT_38-protocol-trim/brief.md#分类事实"}},"required_path_ids":["code_review"],"validator_sha256":"4673dca40e8f4dbb24ada4b72318d3ce57dc1de788abd4aaae56cfe022ca94d4","input_sha256":"61b3c27fa24c13e00796120220800bea8166be9aaee3a4ebe20a9f6b8d7fb632","path_verdicts":[{"path_id":"code_review","state":"PASS","artifact_refs":["docs/modules/relay-lite/workspace/38-RLT_38-protocol-trim/evidence/code-review-1.json"],"finding_refs":[],"reason_codes":[],"reviewer_session_id":"/root/rlt38_code_review"}],"open_blockers":[],"state":"PASS","reason_codes":[]}
```

完整fresh初审已approved，normal路径闭合，不再派code_review。产品/工具/测试相对候选1ad9610无增量。

有限收口branch=closeout/RLT_38，复用本卡任务树，基于master verify=dda18d101c3522f0ec45b71f36ce859eca579330。仅源卡状态与W证据回填，无产品/验收增量；不另发代码复核。
