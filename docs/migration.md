# 独立迁移

工作项 [relay-lite #1](https://github.com/nashhu180-netizen/relay-lite/issues/1) / [dh-relay #156](https://github.com/nashhu180-netizen/dh-relay/issues/156)。来源为 dh-relay `2246b16cb82f86a594f7b2c36365e7851fe11263`；新仓使用独立初始化提交，完整原始 Git 历史留在源仓，可按此 SHA + 迁移清单路径回查。不是滤出的 Git 历史。

- `tools/relay-light/skill/` 的现役单卡段 → `skill/`；旧完整段、账本脚本/专属配置不分发；源文件 URL 基于完整源 SHA。
- watcher → `tools/space_watch.py`，行为与安全边界不变，通知前缀用 relay-lite。
- 安装器 → `tools/install_skill.py`，自身定位，标准库实现；包中复制 watcher 和计划模板，manifest 记录当前独立仓 SHA。
- 两份卡级总表 → `docs/relay/` 同路径，原状态/授权/维护人不改；新派单 executor，旧 coder 仅原 signal/分配的历史身份，恢复先登记映射。
- 原模块所有设计、计划、工作区与所有接力计划 → `archive/dh-relay/` 原路径逐字归档；`docs/migration-inventory.json` 记录每文件 SHA256。归档不是现役入口，旧完整计划不执行、不启动、不代关闭业务卡。
- 旧仓历史模块仍可用于其在途 #151/#153/#154 恢复；本卡不收口这些工作。后续实质产品变更应在独立仓立户；迁移不启动业务 worker，也不修改它们独占的 execution_strategy.md。
- 用户级旧 skill 目录只在明确 `--legacy-alias` 时同步同版副本；非包文件不擅自清理；不修改运行中的 pane/角色/原 signal。

独立性由脱离源仓的 clone 测试及临时 home 安装证明；没有新增真实 Herdr 演练，fixture/CI 不代表旧卡真实环境人验。
