<!-- dh:v1 -->
# execution_strategy — RLT_36

本卡标准档 normal；implementer_session_id=codex-root-rlt36-20261009；本会话实施。
授权来源：用户“确认开始修复，建个issue”；模型确认来源本轮异步答复“确认这组分配”。Issue15已创建并读回，状态open。
目标 origin wt/RLT_36 → master，完整交付；隔离本地Herdr真实演练；不操作现有三业务space、不安装用户副本、不部署/下一卡。
reviewer=gpt-6.1-sol/high，实例待完整候选后fresh启动；隔离编排/worker/watcher=gpt-6-luna/medium，space/tab/pane均pending。普通监控进程无模型。
环境：Herdr，当前真实kpi-agg/w6X:p1；测试拓扑另建本卡独立space。现役安装版CLI为操作权威，不沿用历史ID。
派单与路由、真实Git/SHA/模型/清理仅在本文件登记；业务结论与问题在findings，原始证据在evidence。

隔离worktree=.dh-worktrees/RLT_36，branch=wt/RLT_36，baseline=dfbe56371b569ff768e7bcd82eeb8d204d55dfea；仅本卡治理先主树创建后精确迁入，主树恢复干净。
方案独立reviewer_session_id=/root/rlt36_plan_review，gpt-6.1-sol/high，fresh上下文，只写review.plan.md；该实例不承担最终fresh code_review。
新隔离Herdr space实际创建为w6Y（RLT_36-test），root pane=w6Y:p1；其它space未改。

隔离首次三角色startup失败：wrapper重复--no-daemon，三者agent_not_found且终端报精确参数错误，未启动模型回合；保留startup-failure.json。后续使用已继承wrapper默认，只透传模型/推理档，不改任何用户配置；不是未知投递重试。

隔离三模型修正后实际启动：rlt36-orch=w6Y:p1、rlt36-worker=w6Y:p2、rlt36-watcher=w6Y:p3；model=gpt-6-luna、effort=medium；实际argv含--yolo/--no-daemon/--no-alt-screen且cwd本卡树，见live/runtime-models.json。普通monitor=w6Y:p4，PID740665，源hash在monitor-start.json；初次PID737311在发模型派单前受控停止以对齐源码，已核消失，原证保留。
方案原reviewer定向追加PASS，仅关闭方案发现，不是最终code_review。S-A已派编排与watcher；worker尚未派单；现场实际watcher模型done、编排working且task_wait真实helper进程运行。

隔离S-A/S-B完成：monitor PID740665受控停止且消失；三角色均done。编排只初次派单一次、worker初次派单一次、watcher初次派单一次；未再prompt编排，3PENDING→READY原报告/最后signal/实态齐备。原证索引E-007/008。测试space只在证据归档与最终复核后清理，不动其它space。

<!-- dh:review-freeze:v2 -->
```json
{
  "schema": "dh.review-freeze.v2",
  "task_id": "RLT_36",
  "card_ref": "docs/modules/relay-lite/dev_plan/P4-watcher可靠性.md#rlt_36",
  "task_type_marker_sha256": "07dc19879cfdc664a773f8d0d7445553f8e0851d62b890af0d75c7917648942f",
  "classification_facts": {
    "production_operation": {
      "value": false,
      "evidence": "docs/modules/relay-lite/workspace/36-RLT_36-watcher-reliability/brief.md#分类事实"
    },
    "irreversible_migration": {
      "value": false,
      "evidence": "docs/modules/relay-lite/workspace/36-RLT_36-watcher-reliability/brief.md#分类事实"
    },
    "metric_semantics": {
      "value": false,
      "evidence": "docs/modules/relay-lite/workspace/36-RLT_36-watcher-reliability/brief.md#分类事实"
    },
    "security_or_shared_guarantee": {
      "value": false,
      "evidence": "docs/modules/relay-lite/workspace/36-RLT_36-watcher-reliability/brief.md#分类事实"
    },
    "behavior_or_rule_semantics_changed": {
      "value": true,
      "evidence": "docs/modules/relay-lite/workspace/36-RLT_36-watcher-reliability/brief.md#分类事实"
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
  "recipe_sha256": "6396e83a0416214cfc5a043d3d77aaeb4f3cd32014c89ec7243bfd122988e91e",
  "baseline_sha": "dfbe56371b569ff768e7bcd82eeb8d204d55dfea",
  "target_sha": "fa9c21fa2dcce7f55760ef19f93ac28a3188e34b",
  "diff_sha256": "9d351c5118e97824b9530b283d0186cb647a0f572078b12bec87c22aab9d149a",
  "implementer_session_id": "codex-root-rlt36-20261009",
  "policy_authorization_ref": "docs/modules/relay-lite/workspace/36-RLT_36-watcher-reliability/brief.md#本卡开工授权"
}
```

独立代码实例/root/rlt36_code_review完整attempt1 approved findings=[]；原报告及collector PASS见E-013/014。本卡源分支实现PR16；服务端采用允许的普通merge保留所审候选可达性，不绕保护。平台branch_protection404、rulesets=[]，无配置必需审批/检查；本卡仍要求Ubuntu/Windows CI，两侧PASS并最终最新source核验后合入。
