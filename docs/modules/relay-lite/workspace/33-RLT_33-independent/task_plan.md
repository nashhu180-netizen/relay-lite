# 施工基线

1. 冻结源 2246b16，记录文件/hash 与迁移目标，先保存历史后撤源现役入口。
2. 创建 skill/、tools/、tests/；保留单卡正文与两 adapter 的单卡段；executor 全部现役一致，保留存量别名及真实信号；删完整模式模板/账本配置。
3. 安装包复制自包含 watcher 与总表模板，临时 home 验 manifest 与失败恢复；历史 archive 原字节，当前两份表机械迁移且不动授权。
4. 按白名单更新旧仓入口/CI，测试 Runner 仍可运行；所有 tests 独立运行及 clone 安装，不访问旧树。
5. 独立复核、有效变异和需求境证据后，两仓依次 PR/CI/合入、合入态验、verify/回填/清理。

环境：Python3/stdlb、git/gh/pwsh 已有；不安装依赖。GitHub 权限 admin，源 master 当前未保护；新仓 master 空提交初始化，其它实质工件全走任务分支。真实 Herdr 不在本卡验收。模型分配闸仅用于启动产品协议会话，本卡为主会话维护并依 dev-harness 做独立复核，不启动 Herdr worker。
