<!-- dh:v1 -->
# task_plan — RLT_38

## Context Packet
基线 0b08c18be09cd00e84ff214c582941593ca7c2ec；原入口skill/SKILL.md、两adapter；源卡P6。既有设计入口不变，archive与历史证据只读。

## 环境预检与待决
Git主干/index干净，origin/master与本地一致；GitHub CLI读回目标仓与默认master。CI仅Python3.12双平台unittest，不部署。rulesets=[]，protection查询404 Branch not protected；仍要求CI及独立复核。Python/Git可用，不安装依赖。

## 施工步骤
1. 基线统计；按原节抽出跨卡、文档、编排、取证、watcher正文并加入口触发路由，修正跨文件指代。保存逐节映射。
2. 两adapter只留宿主差异和必要入口；派单模板迁入唯一templates/dispatch.md。逐项核adapter独有语义保留。
3. 安装器显式清单增加引用文件；调整结构测试为安装消费者引用可达验证，保留硬闸断言。全量unittest及缺分发文件的语义变异RED→恢复GREEN。
4. 候选提交后冻结并派fresh独立code_review；按normal额度收敛。PR/双平台CI/合入，实际合入态复验，verify和本卡收口PR，远端读回再清本卡树。
