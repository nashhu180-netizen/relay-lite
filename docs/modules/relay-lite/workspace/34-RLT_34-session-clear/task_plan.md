<!-- dh:v1 -->
# task_plan — RLT_34

## Context Packet
来源：../../dev_plan/P2-会话清理维护.md#rlt_34；brief.md。基线 origin/master 43f68e0822785e57d640aa32d885148ba97ff8ac。core 原有 batch PASS 后 clear 闸，新任务入口缺失。两 adapter 在启动投递处指向新增核心段。
执行者：当前主会话 /root，自干实施与本卡集成；fresh 子会话独立 code_review，只写指定 review 工件。本任务不启用 relay orchestrator/worker 常驻角色或 Herdr 拓扑。

## 环境预检与待决
Python 3.12.3、Node v22.22.1、gh、dh 可用；本仓 master 干净，origin/master 与本地相同；GitHub master protected=false，CI 为 Ubuntu/Windows unittest，无部署步骤；一个其它任务 worktree 不触碰。Chrome CDP proxy 连接超时，保留该结果；GitHub 使用已成功核实的原生 gh API，不依赖浏览器。无需安装依赖、无待用户决策。

## 施工步骤
1. 从最新 origin/master 建 wt/RLT_34 与 .dh-worktrees/RLT_34，七件套/源卡随树保存；建 Draft PR 关联 #7。
2. Modify skill/SKILL.md：统一会话清理入口，写批次、新独立任务、未闭合整改、fresh 复核和未知清理结果边界；Modify 两 adapter：启动投递处明确引用核心清理门，投递与清理分开复验。
3. Modify tests/test_contract.py：检查核心清理门及两 adapter 引用不丢失；先 python3 -m unittest discover -s tests -v；对新任务清理命令作协议语义变异，指定测试必须断言失败；还原原字节，再同命令 GREEN。证据在 evidence/，验证期间串行冻结编辑。
4. 提交完整候选；用同版 collector freeze + dh dispatch 登记；派未参与实施的 fresh 子会话 code_review，normal 初审无 open P0/P1 后停止派发；有 open P0/P1 才原实例定向 attempt2。
5. dh gate --review-json、git diff --check、PR 两平台 CI 通过后 squash；主树 fast-forward，合入态复验；写 verify 与机械状态有限收口 PR，核远端后关闭 #7，只清理本卡树。

## 验证范围与边界
静态文档协议、孤立安装到临时 home 的既有回归、独立文档语义复核；不声称有自动 clear 拦截或真实 Herdr 演练。clear 是会话上下文清理，历史证据/计数与 RELAY_* 均保留。各 agent kind 原生命令支持在实际运行时核实，不臆造 CLI 支持。
