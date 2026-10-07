<!-- dh:v1 -->
# findings — RLT_35

## 授权与纠正
2026-10-07 用户“确认”，明确标准档 normal 开工、本卡完整交付。随后“不是 codex 的 watcher 针对所有agent都一样”；通用 watcher 合同适用于全部 kind，只有宿主工具差异分 adapter。对话时刻分钟未知，不伪造人验。

## 方案裁决
独立初审要求实际配置消费，已采用小型只读校验器；非自动执行引擎。初审/定向复审原报告在 review.plan.md，明确非机器只读；主树派出前后无修改。选中环境登记与恢复核验、原生 clear 实际 UI 判据、宿主工具分层、安装闭包和离线证据边界均采用。用户通用 watcher 纠正是同范围澄清，未增加 live 操作。

## 历史失败与恢复
开工前 GitHub GraphQL 创建服务异常，REST 创建 unexpected end of JSON input；两次读回未见新 Issue。开工确认后使用 GitHub connector 成功创建 #12，gh issue view 确认 open。保留此前失败，不宣称它们成功，不控制其它现场。

## 风险与待决
无 open 方向或需接受风险项；配置工具只校验，不执行任意配置命令。live Herdr 演练不在本卡验收，不能把协议/离线测试当实态证明。范围外发现单记，不顺手修。

## 实施取证与修正
首轮53项因旧watcher标题契约出现1 error，次轮58项因核心缺workspace_id参数映射出现1断言failure；两次失败保留为candidate-first/candidate-green，恢复兼容标题及通用参数映射后58项GREEN。helper补版本类型/默认注册项/所有协议路径/RECEIPT空值/固定错误JSON的负例；没有删除或跳过原测试。Windows若无symlink权限，该负例走已执行的路径越界断言后退出；Linux实测symlink逃逸拒绝，Windows CI不冒充该子路径。
