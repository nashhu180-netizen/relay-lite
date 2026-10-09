# relay-lite 协议读取与分发

RLT_38：核心保留共同硬闸与按角色路由；orchestration、verification、card-chain、document-role、watcher分文件按明确触发读取；唯一派单模板templates/dispatch.md。两adapter保留各宿主进程句柄和等待调用，引用共同规则。环境注册/模型提案/运行工具行为不变。

受管安装清单显式包含上述六个新文件。测试在临时home对三side及relay-light别名安装，沿实际入口验证引用闭环及源字节，逐件缺失拒绝，分发清单漏card-chain变异产生断言失败。真实用户安装目录未升级。

字符计数仅skill内md/toml，包含空白换行和迁移文件，不含安装后的Python工具。基线50930，当前结果见workspace/38-RLT_38-protocol-trim/evidence/size-ledger.json；协议语义审核与本卡交付状态以该workspace和P6为准。
