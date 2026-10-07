<!-- dh:v1 -->
# execution_strategy — RLT_34

授权：brief.md#本卡开工授权；用户“确认开工”。标准档 normal。
角色：主会话 /root 负责实施/测试/集成，implementer_session_id=codex-root-rlt34-20261007；独立复核用 fresh-context subagent（继承主会话模型/推理档，fork_turns=none），只写指定 review 报告。AGENTS.md 明确允许此种独立复核；不启用 relay single-task 终端编排，无额外 Herdr/model-allocation 启动。
总表：无（独立单卡）。
分支：wt/RLT_34；worktree：/home/nash/work/relay-lite/.dh-worktrees/RLT_34；目标：origin/master。
GitHub Issue：#7。原现场另有 AW_07-table-resume worktree，本卡不清理。
停止线：沿 brief/task_plan，不派下一卡，不部署、不安装。

Draft PR：[GitHub #8](https://github.com/nashhu180-netizen/relay-lite/pull/8)，开工提交 126c82e。

<!-- dh:review-freeze:v2 -->
```json
{
  "schema": "dh.review-freeze.v2",
  "task_id": "RLT_34",
  "card_ref": "docs/modules/relay-lite/dev_plan/P2-会话清理维护.md#rlt_34",
  "task_type_marker_sha256": "1217c1d7543b3abcff2c4492dc4fcf0d10e51036b40afc55b251cbb1a59e2fa4",
  "classification_facts": {
    "production_operation": {
      "value": false,
      "evidence": "docs/modules/relay-lite/workspace/34-RLT_34-session-clear/brief.md#分类事实"
    },
    "irreversible_migration": {
      "value": false,
      "evidence": "docs/modules/relay-lite/workspace/34-RLT_34-session-clear/brief.md#分类事实"
    },
    "metric_semantics": {
      "value": false,
      "evidence": "docs/modules/relay-lite/workspace/34-RLT_34-session-clear/brief.md#分类事实"
    },
    "security_or_shared_guarantee": {
      "value": false,
      "evidence": "docs/modules/relay-lite/workspace/34-RLT_34-session-clear/brief.md#分类事实"
    },
    "behavior_or_rule_semantics_changed": {
      "value": true,
      "evidence": "docs/modules/relay-lite/workspace/34-RLT_34-session-clear/brief.md#分类事实"
    }
  },
  "policy_version": "three-tier.v2",
  "policy_source_digest": "9a775ca60a54bd6bd6647f18acf2d01c87760d304ee37bf8cf9643321990da7a",
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
      "sha256": "6bee1b1bea5e96474368a812ad65eeed1c6858eafda9585dc26697472e928240"
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
  "recipe_sha256": "ba5ffa507abcaaee80ebff2cc1a5155a8c0cc6d3ac9549c728e082d987ff1430",
  "baseline_sha": "43f68e0822785e57d640aa32d885148ba97ff8ac",
  "target_sha": "e6adef4fe009972bc86071a636e03009e54337d0",
  "diff_sha256": "7acbd4404927f0b053aae0874293636a15f778cd9b8af995765beed7f9ea1da6",
  "implementer_session_id": "codex-root-rlt34-20261007",
  "policy_authorization_ref": "docs/modules/relay-lite/workspace/34-RLT_34-session-clear/brief.md#本卡开工授权"
}
```

复核 gate 调用定位：cwd=/home/nash/work/relay-lite/.dh-worktrees/RLT_34；命令 `dh gate relay-lite 34-RLT_34-session-clear --review-json`；原 JSON= evidence/review-gate.json，schema=dh.review-gate.v2，实际 exit=0。

PR8 已服务端合入：6abcacd5d5e3fc7e514b804cdbb7d97893ae6d38；master 已 fast-forward。同原候选逐字一致与集成复验见 evidence/integration.json。
