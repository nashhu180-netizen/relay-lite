<!-- dh:v1 -->
# brief — RLT_37

## 目标与范围
维护Issue18，任务口径见../../dev_plan/P5-角色职责维护.md#rlt_37。修改提示协议及分发闭集，不增加运行决策引擎。

## 本卡开工授权
2026-10-09，本对话用户先认可角色职责提案：“我觉得可以。提issue，优化下 relay-lite”；提单后明确：“继续优化”。同范围直接承接，不重复索权。
已说明标准档/常规复核，目标仓nashhu180-netizen/relay-lite，remote=origin，wt/RLT_37→master；完整远端交付。本卡不升级用户安装副本、不动业务space、目标机、数据库或生产环境。

## 分类事实
production_operation=false：只修改本仓协议和受管包，测试只用临时目录。
irreversible_migration=false：无迁移或删除业务数据能力。
metric_semantics=false：不含数据指标。
security_or_shared_guarantee=false：保留既有权限和安全闸，咨询职责扩展不扩展决策/执行权限。
behavior_or_rule_semantics_changed=true：明确编排转交触发及decider完整路径责任。
任务类型normal，标准档，非light；一轮fresh code_review。仓库AGENTS明确允许fresh-context subagent独立复核，只写本路径原报告；不冒称机器只读。

## 完成条件
- RL37-M1：各角色交接明确，编排识别偏离，decider负责完整路径与调整，执行/复核/观察/代笔边界保持。
- RL37-M2：decider咨询范围宽于决定权限；授权内知会推进，授权外充分准备后集中请用户裁决。
- RL37-M3：覆盖完整路径、后续依赖、失败分支、有效性与可预见审批点；正常推进不新增决策闸。
- RL37-M4：同类阻塞触发整体复盘；身份未知/预算耗尽/新风险不自动重试或扩权，旧停止线保持。
- RL37-M5：核心、两adapter派单模板和受管安装包一致；情景推演、包分发回归、独立复核、CI、合入态复验及verify齐备。

## 人验
无新增用户主观判断项；核协议一致性、场景推演及分发事实。不得把文字验证说成已证明真实业务会话审批次数下降。
