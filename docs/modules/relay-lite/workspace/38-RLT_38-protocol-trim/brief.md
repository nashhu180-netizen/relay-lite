<!-- dh:v1 -->
<!-- dh:workspace-contract:v2 -->
# brief — RLT_38

## 目标与范围
保留规则语义，去重与按需拆读。源卡：../../dev_plan/P6-协议精简.md#rlt_38。

## 本卡开工授权
2026-10-09，本对话在统计与范围说明后，用户：“嗯，建 issue 然后确认开工直到优化完成”。目标nashhu180-netizen/relay-lite，origin wt/RLT_38→master，完整远端交付。排除真实安装升级、业务卡、环境/生产操作及下一卡。

## 分类事实
production_operation=false：仅本仓协议/安装清单，临时home测试。
irreversible_migration=false：无业务迁移或删除能力。
metric_semantics=false：无数据指标。
security_or_shared_guarantee=false：权限、安全及共享写者边界原义保留。
behavior_or_rule_semantics_changed=true：改变读者加载/引用路径与受管安装文件集合，规则本身不变；非纯标点修改，normal标准档一轮fresh复核。

## 完成条件
- RL38-M1：统计同口径字符数，报告 skill 总量、核心入口、两 adapter 的前后变化，区分迁移与去重。
- RL38-M2：保留授权、角色、模型、写者、信号、计数、清理、恢复、跨卡与未知停止规则；逐节可追溯。
- RL38-M3：共用派单模板唯一，adapter 仅保留宿主差异与必要入口；按需文档触发条件明确且安装后可达。
- RL38-M4：受管安装包、适用回归与有效变异、独立复核、双平台CI、实际合入态复验及verify齐备。

## 人验
本卡验证协议保真、分发与字符计数，无新增主观人判项；不声称真实业务会话效果已经验证。

## 覆盖任务
RLT_38；源卡P6，RL38-M1–M4。

## 边界
同源卡允许路径。仅本仓协议/包/测试，临时home，不升级真实安装、不操作业务卡。
