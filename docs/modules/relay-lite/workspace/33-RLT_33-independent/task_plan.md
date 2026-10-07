# 施工基线

1. 冻结源 2246b16，记录文件/hash 与迁移目标，先保存历史后撤源现役入口。
2. 创建 skill/、tools/、tests/；保留单卡正文与两 adapter 的单卡段；executor 全部现役一致，保留存量别名及真实信号；删完整模式模板/账本配置。
3. 安装包复制自包含 watcher 与总表模板，临时 home 验 manifest 与失败恢复；历史 archive 原字节，当前两份表机械迁移且不动授权。
4. 按白名单更新旧仓入口/CI，测试 Runner 仍可运行；所有 tests 独立运行及 clone 安装，不访问旧树。
5. 独立复核、有效变异和需求境证据后，两仓依次 PR/CI/合入、合入态验、verify/回填/清理。

环境：Python3/stdlb、git/gh/pwsh 已有；不安装依赖。GitHub 权限 admin，源 master 当前未保护；新仓 master 空提交初始化，其它实质工件全走任务分支。真实 Herdr 不在本卡验收。模型分配闸仅用于启动产品协议会话，本卡为主会话维护并依 dev-harness 做独立复核，不启动 Herdr worker。

## 已冻结迁移闭集与负向判据（产品施工前）

逐文件合同：本目录 migration-plan.json，按 git archive 2246b16 的三棵 tracked 树生成；每项 source、sha256、archive、new_active、action、source_action 都已冻结。仅以下两表作为现役迁入，目标同路径，其全文在新增迁移说明之后须逐字相等（含所有自动接续授权、状态、模型确认、维护人和人验原话），不改正文 coder/旧通知历史：
- docs/relay/agent-playground/agent-workbench/aw-mvp/relay_plan.md
- docs/relay/wf-analytics-platform/workflow-platform/wfp-p1-obd-p5/relay_plan.md
其它 docs/relay 与模块内所有完整计划/log 只读归档，不转换、不启动。源 docs/relay 退役为 README 指针，源模块历史仍留原路径避免破坏在途卡。

产品闭集：源 tools/relay-light/{relay_log.py,test_relay_log.py,skill/dh-mapping.toml} 退役且不安装；source 全 tools/relay-light 退役。新 tools/{space_watch.py,install_skill.py}、tests/{test_space_watch.py,test_install_skill.py,test_contract.py}；新 skill/{SKILL.md,roles.toml,references/adapter-codex.md,references/adapter-claude-code.md,templates/card-chain.md}。源安装器重写为自定位 stdlib 实现，旧 installer API 测试迁入并按新包闭集调整，不沿用完整模式结构测试；watcher 行为测试保留。两个 adapter 只提取单卡段并补独立启动片段，删 stage-lead/账本/五阶段路由。源 AGENTS 删除旧协议段换独立仓链接，源 README、docs/relay/README、历史模块/design/dev_plan README 仅迁出说明；CI 同名 relay-light-python 改静态退役断言，PowerShell Windows/Ubuntu 两门不变。

兼容矩阵：新派单/角色配置/默认模型/signal role=executor；phase 九值不变，旧 coder signal 与已确认实例模型只读，恢复在 execution_strategy.md 登记旧实例→新角色的映射，禁止改写原信号或替新实例绕过确认。旧 [relay-light:single-task] 仅同协议存量别名；新标头 [relay-lite:single-task]。旧完整模式标头不接受，archive 不含任何安装文件。模板/通知/新安装目录 relay-lite；旧 skill 名只在显式 --legacy-alias 时同步，旧用户目录其它文件不擅自删除。

验收命令：python3 -m unittest discover -s tests -v（每条 archive 文件 SHA256 与冻结清单对照；现役两表移除新增 header 后全文与 archive 同字节；新包封闭清单无 relay_log.py/dh-mapping.toml；现役 SKILL/adapter 无 stage-lead、五阶段、账本命令或旧完整标头；临时HOME包 manifest 全文件可读且不依赖旧仓；旧目录不存在时安装成功）。孤立 clone 在临时目录完整跑同命令；不访问源树。测试必须明确包不复制 archive。

有效变异点由代码轮2 reviewer 指定；记录生产文件/替换点、断言失败命令/退出码/测试名、RED和精确恢复后GREEN及SHA。临时 home 不影响用户在途会话。新仓 PR#2、源仓PR#157 均保留 Draft 直到独立复核与测试通过。

范围内必要联动补漏（2026-10-07、产品退役后源回归实际发现）：源tools/tests/relay-light-log.ps1仍调用旧账本/安装器；加入本卡源允许路径，改为静态退役断言。保留run-relay-tests.ps1套件入口与全部Runner检查，旧Python产品测试由独立仓CI承接，本脚本不静默skip、不网络调用新仓。此为用户独立拆分目标的必要联动，不实现新功能或改变原业务卡验收。失败日志留证，focused后全量源回归及远端CI验证。
