<!-- dh:v1 -->
# task_plan — RLT_35

## Context Packet
来源：../../dev_plan/P3-环境派发与监控.md#rlt_35；正式设计 02 与 brief。基线 e473f1d6ca99b8ca8a2f0f31280290823cda1ee9；RLT_34 clear 门已交付，两 adapter 写死 Herdr，watcher 有固定脚本。
执行者 /root 为实施/集成；可委托独立路径的局部实现；独立 fresh code_review 未参与施工。本卡不启用 relay 终端编排，不启动真实 Herdr agents。

## 环境预检与待决
Python 3.12.3 / Node 22.22.1 / dh / gh 可用；本地主干与 origin/master 相同且干净。GitHub #12 已经 connector 创建且 gh 读回确认。此前 GraphQL/REST 创建失败保留于 findings。其它两 worktree 不触碰。无需安装依赖，测试使用临时 home；当前 CLI 的 herdr --skill 已只读核过，不控制现态。CI 双平台 unittest，无部署动作。没有待用户决定项。

## 施工步骤
1. 已落户 #12，创建 wt/RLT_35 / .dh-worktrees/RLT_35；正式输入/源卡/七件套先落盘，基线串行 `python3 -m unittest discover -s tests -v` 取证。
2. Create skill/environments.toml 与 tools/environment_config.py：Python stdlib tomllib、封闭 schema、可扩展环境注册、严格路径/缺件/环境/RECEIPT 校验，固定 JSON 与原因码；工具仅读取。Modify tools/install_skill.py 封闭文件清单/来源，Test tests/test_environment_config.py 与 test_install_skill.py：默认/显式/恢复冲突、错误停止、安装独立可解析、哈希、无副作用。恢复用 --expected 检查已登记环境避免静默切换。
3. Create references/environment-herdr.md 统一派发/通信/监控 CLI，先配置 gate 后 herdr --skill，按用户 space→tab→交互 agent；Modify SKILL 与两 adapter 去掉重复 Herdr CLI，保留模型/宿主差异与 clear/RLT_34 例外。通用 watcher 可照做的模板适用全部 kind；Codex cell/session 与 Claude后台任务差异只在各 adapter。同步 README、card-chain 模板和 as-built。
4. Test 协议契约与全回归，所有影响被测路径的写入完成后串行运行；保存失败原因。对工具未知环境拒绝作最小生产变异，指定测试断言 RED；精确原字节还原 GREEN，登记九字段。
5. 提交完整候选，原生 collector freeze，dh dispatch 绑定候选与真实 fresh reviewer 实例；normal 一次 full，无 P0/P1 即止；有 P0/P1 才原实例一次 targeted。review gate 原 JSON 和 dh check 取证。miner/as-built 只录本卡事实。
6. 推本卡分支与 PR，读取保护/必要审批/CI；检查全部通过后服务端 merge 保留候选可达性；干净主树 fast-forward 后复验，写 verify(relay-lite)，有限收口 PR 归档证据/机械状态；核远端完整后关 #12，仅清理本卡树/分支。

## 验证范围与边界
配置工具真实执行、安装临时三端、协议静态回归与既有 watcher fixture；不运行真实 space/tab/clear/通知演练。工具校验不自动启动任何 agent；原协议、signal、额度与权限不扩大。
