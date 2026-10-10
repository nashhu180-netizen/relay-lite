<!-- dh:v1 -->
# task_plan — RLT_39

## Context Packet
基线 9f7c2b2c15dca69ce39a780aa4b7c4bc64ea6c70；核心skill/SKILL.md与共用orchestration/decision-guide/watcher；两adapter已要求读共用合同。源卡P7，既有正式设计与archive不变。

## 环境预检
主干/index干净；origin/master与本地一致；GitHub默认master，rulesets=[]、protection返回404未保护；CI仅Python3.12 Ubuntu/Windows unittest，不部署。现有Python/Git/dh可用。已建Issue24。

## 施工步骤
1. 产品修改前完成fresh计划交叉审核并落实必要修正；登记授权与停止线。
2. 共用编排合同增加推进循环、BLOCKED解阻、插问续做和真正等待输出；核心职责加短入口提示，decider场景补齐，watcher结果消费回链。保持角色边界，不复制两份adapter。
3. 全量python3 -m unittest discover -s tests -v；现有安装消费者test_installed_reading_routes_are_closed_and_template_is_unique验证合同可达。临时变异安装清单漏掉orchestration.md，确认断言RED后恢复GREEN；只作测试证据，不提交工具改动。逐场景核边界，记录Unicode字符增量。
4. 更新as-built、miner；候选提交冻结后fresh独立code_review；原normal额度适用。PR双平台CI、服务端合入、实际主干复验与verify、有限收口PR/Issue归档、本卡清理。
5. 沿先前双设备安装授权同步最终主干的已登记副本，逐真实路径/hash/入口回读，记录部署审计；不改业务卡或启动agent。
