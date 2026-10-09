# relay-lite 持续监控与结果等待实装（RLT_36）

默认watcher主体为Herdr独立普通终端中的space_watch.py；无模型回合依赖。兼容旧agent-name入口，普通终端用继承pane ID + pane get核身份。服务端/space内存socket单实例保护，不生成文件；CLI错误/身份/RELAY_RECEIPT硬闸及凭据白名单保留。

通知向已核目标pane只提交一次；agent_prompted仅确认提交，working/seq不作消费证明。审批/unknown UI前置延后可合并；尝试后未知事件保留且不盲重发、观察继续；临时只读错误保留观察基线，下一节拍恢复。程序退出一次提示不重拉；主编排按task_wait.py的精确派单七字段/结果路径做0..60秒只读等待，不因watcher暂停结束整卡。READY不是PASS，BLOCKED结果也必须读原报告/signal；重复PENDING核实际worker状态和原停止线。

安装器三侧闭集新增task_wait.py，manifest与Git dirty来源包含它；临时home入口和协议可自包含运行。不安装用户真实副本，不改变AW_07/WFP_08/dev-harness在途监控。

本卡证据见workspace/36-RLT_36-watcher-reliability；当前本地76项与有效变异还原通过，真实隔离Herdr演练已证实同PID跨120秒、busy提交、monitor停止后3PENDING→READY核收与交接，最终独立复核/CI/合入/verify未完成。Linux实际终端验证不冒称Windows Herdr实态；Windows CI证明Python包与行为。

## v2.1.0 历史交付记录（原证保留）

# relay-lite v2.1.0 实装

配置入口 environments.toml，目前默认/注册仅Herdr；environment_config.py实际读取和校验配置、恢复环境、协议路径及运行前置，READY JSON交给agent读取对应协议。工具只读，不自动启动agent或执行配置命令。模型roles提案独立，缺件/未知/恢复冲突/RECEIPT拒绝，不fallback。

Herdr专属协议统一CLI：派发前读取安装版 herdr --skill，space→独立tab→交互agent→派单；复用tab的新任务/批次先原生clear并确认。模型原生命令支持从当前帮助/UI核实，state_change_seq不替代清理成功。原整改/E2/fresh/watcher例外、signal/证据/额度/RELAY_*保持。

所有agent共用核心watcher启动/确认/动态监控/通知/退出合同；Herdr固定space_watch.py行为不变，全部kind同一观察范围。Codex cell/session_id/write_stdin与Claude后台task_id仅adapter分层，不把包装工具运行中当脚本存活；通知只是提示，放行仍读durable signal和独立报告。

安装器三端封闭清单包含原六文件和新增环境配置、校验工具、Herdr协议，manifest逐字哈希与可选Git来源；只在临时home验证，本卡未更新真实安装副本。离线测试与协议审查不冒充live Herdr操作，本卡不实现Orca或自动派发引擎。

本卡真实测试/复核/CI/合入/verify证据见 workspace/35-RLT_35-environment-dispatch/，最终数量与SHA由实际证据记录，不预填通过。

## v2.0.0 历史交付记录（原证保留）

# relay-lite v2.0.0 实装

产品自包含于 skill/ 与 tools/；安装名 relay-lite，显式 --legacy-alias 同步 relay-light 同版入口。安装器 --all 分发 Claude/Codex/Agents 三侧，复制6文件及manifest；已核已合入7a3346f的Linux本机6侧逐字/hash一致并备份旧副本，未重启或更换任何在途进程。安装包不需要Git或旧仓；可选Git溯源字段读取独立仓HEAD。

协议只保留单卡与跨卡总表。编排直接派发；executor通用执行授权任务，保留phase/信号闭集、旧coder历史映射和模型确认；watcher固定workspace动态观察、零repo/workspace写入及通知确认；document只用户明确启用。完整模式账本/阶段入口不分发，archive只读，不用于恢复执行。

初始最新两表导入在9458e4f本仓提交，正文与AW5a47/WFP PR158未合入65f87a0原字节同hash；迁移审计核该固定提交及快照，现役表后续由原唯一维护者更新。审计测试需完整本仓Git历史，CI显式fetch-depth0；产品安装/运行不因此依赖Git。固定来源/ACK/切换证据见docs/table-cutover.json，原业务状态、授权、signal与维护权不变。

本卡独立clone/本地/双系统39项及合入态39项通过，有效安装器预检变异RED/精确恢复GREEN。没有新增真实Herdr watcher演练，不代完成旧卡验收。外部dh检查0失败2提示（命名建议及仅支持DH旧标题的R14）；源历史模块存量问题与暂停core观察失败保留，不宣称全平台/旧卡全绿。

源实现PR157/8cbff63与有限收口PR159/fde68d870b6bff25caf677a12343c923453ada67已实际合入，远端主干verify(dh-relay)可达；source本地普通merge2fb5b1e保留全部5a47/3940历史且同远端树，未push无关提交。独立主树机器verify(relay-lite)为bed13739844d9009f223e7c35212b8da97118fe2，由本次有限收口分支归远端；所有当次收口SHA以实际GitHub merge记录为准。
