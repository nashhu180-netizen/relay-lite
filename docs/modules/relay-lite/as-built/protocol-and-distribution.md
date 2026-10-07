# relay-lite v2.0.0 实装

产品自包含于 skill/ 与 tools/；安装名 relay-lite，显式 --legacy-alias 同步 relay-light 同版入口。安装器 --all 分发 Claude/Codex/Agents 三侧，复制6文件及manifest；已核已合入7a3346f的Linux本机6侧逐字/hash一致并备份旧副本，未重启或更换任何在途进程。安装包不需要Git或旧仓；可选Git溯源字段读取独立仓HEAD。

协议只保留单卡与跨卡总表。编排直接派发；executor通用执行授权任务，保留phase/信号闭集、旧coder历史映射和模型确认；watcher固定workspace动态观察、零repo/workspace写入及通知确认；document只用户明确启用。完整模式账本/阶段入口不分发，archive只读，不用于恢复执行。

初始最新两表导入在9458e4f本仓提交，正文与AW5a47/WFP PR158未合入65f87a0原字节同hash；迁移审计核该固定提交及快照，现役表后续由原唯一维护者更新。审计测试需完整本仓Git历史，CI显式fetch-depth0；产品安装/运行不因此依赖Git。固定来源/ACK/切换证据见docs/table-cutover.json，原业务状态、授权、signal与维护权不变。

本卡独立clone/本地/双系统39项及合入态39项通过，有效安装器预检变异RED/精确恢复GREEN。没有新增真实Herdr watcher演练，不代完成旧卡验收。外部dh检查0失败2提示（命名建议及仅支持DH旧标题的R14）；源历史模块存量问题与暂停core观察失败保留，不宣称全平台/旧卡全绿。

源实现PR157/8cbff63与有限收口PR159/fde68d870b6bff25caf677a12343c923453ada67已实际合入，远端主干verify(dh-relay)可达；source本地普通merge2fb5b1e保留全部5a47/3940历史且同远端树，未push无关提交。独立主树机器verify(relay-lite)为bed13739844d9009f223e7c35212b8da97118fe2，由本次有限收口分支归远端；所有当次收口SHA以实际GitHub merge记录为准。
