<!-- dh:v1 -->
# execution_strategy — RLT_35

授权：brief.md#本卡开工授权；用户“确认”，随后通用 watcher 纠正；标准档 normal。
实施：/root；implementer_session_id=codex-root-rlt35-20261007。独立复核：fresh-context subagent，继承主会话模型/推理档，fork_turns=none，仅写指定 review 工件。AGENTS 允许，未使用 Herdr 终端编排，无额外 model-allocation 启动。
总表：无（独立单卡）。
worktree=/home/nash/work/relay-lite/.dh-worktrees/RLT_35；branch=wt/RLT_35；client=codex-cli；target=origin/master；Issue #12。
已有 AW_07-table-resume 与 /tmp/wfp08-relay-lite-table-g3-20261007 不触碰。
停止线：源卡/brief；不改安装副本/真实运行环境、不启下一卡。
环境配置产品：首次用户/派单明确 environment 优先，否则配置 default；恢复以 execution_strategy.environment 为准，工具 --expected 校验；选中环境与运行身份启动后读回核实。

<!-- dh:review-freeze:v2 -->
```json
{
  "schema": "dh.review-freeze.v2",
  "task_id": "RLT_35",
  "card_ref": "docs/modules/relay-lite/dev_plan/P3-环境派发与监控.md#rlt_35",
  "task_type_marker_sha256": "818b13bd390ce929e8b5cec3572206801c40ef1dc4f833b1d45d27814b90fbee",
  "classification_facts": {
    "production_operation": {
      "value": false,
      "evidence": "docs/modules/relay-lite/workspace/35-RLT_35-environment-dispatch/brief.md#分类事实"
    },
    "irreversible_migration": {
      "value": false,
      "evidence": "docs/modules/relay-lite/workspace/35-RLT_35-environment-dispatch/brief.md#分类事实"
    },
    "metric_semantics": {
      "value": false,
      "evidence": "docs/modules/relay-lite/workspace/35-RLT_35-environment-dispatch/brief.md#分类事实"
    },
    "security_or_shared_guarantee": {
      "value": false,
      "evidence": "docs/modules/relay-lite/workspace/35-RLT_35-environment-dispatch/brief.md#分类事实"
    },
    "behavior_or_rule_semantics_changed": {
      "value": true,
      "evidence": "docs/modules/relay-lite/workspace/35-RLT_35-environment-dispatch/brief.md#分类事实"
    }
  },
  "policy_version": "three-tier.v2",
  "policy_source_digest": "63aa731c4b136fe019078b7cf01917f8f1bef2563e703fee0b8464ad41a21382",
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
      "sha256": "ba1f41fa636e4b011b9c2a3c1421e4fce89123fb994745600744a08f956a8f82"
    },
    {
      "path": "tools/dh-check.mjs",
      "sha256": "05d2fe7b3503b41ab3b0287b140762b001ed45de291633d9f6ee0c5437d7abf2"
    },
    {
      "path": "tools/dh-nav.mjs",
      "sha256": "150577eb0fa8d14a66ef72da14b597de94481b976598af914d89507af78e4932"
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
      "sha256": "0f2b36cc019589ac9877720942ae53437b8bf0b2127639e41c9a496dc9edb57a"
    }
  ],
  "required_path_ids": [
    "code_review"
  ],
  "recipe_sha256": "ec67b80ab1cb91d250570188aff046f502f36efd6f8a2d808b48b0d255a4838b",
  "baseline_sha": "e473f1d6ca99b8ca8a2f0f31280290823cda1ee9",
  "target_sha": "20eb3797f80a451aa13c06675037f79c9aa6654b",
  "diff_sha256": "01dd4935c34c729025ce6f07f937fd64869ea7fc7a76dd2683a9bc5b5a24fc2c",
  "implementer_session_id": "codex-root-rlt35-20261007",
  "policy_authorization_ref": "docs/modules/relay-lite/workspace/35-RLT_35-environment-dispatch/brief.md#本卡开工授权"
}
```

策略来源刷新：等待CI/复核期间安装版 dh-check.mjs 从 6bee1b1b 更新为 05d2fe7b，仅两处 collectReviewGate cwd 改为实际 Git 根。旧闸 BLOCKED 原证和20行源diff保留。沿本卡既有授权、相同 three-tier.v2/normal/分类与额度，使用当前 collector 对同一20eb3797候选重新绑定；不修改复核原报告、不追加复核、不更换实现候选、不采用旧来源绕过闸。
