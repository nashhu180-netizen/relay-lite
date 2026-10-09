<!-- dh:v1 -->
# review — RLT_38

## 独立复核区
/root/rlt38_code_review完整fresh初审approved，findings=[]；原报告见E-006，未触发attempt2。

## AI 提交区
本地协议/分发证据与独立复核已通过；远端最新CI、实际合入复验及verify尚待完成。

## 完成条件逐条挂证据
| ID | 条件 | 谁验 | 证据 | 达成? |
|---|---|---|---|---|
| RL38-M1 | 统计同口径字符数，报告 skill 总量、核心入口、两 adapter 的前后变化，区分迁移与去重。 | AI | | 待验证 |
| RL38-M2 | 保留授权、角色、模型、写者、信号、计数、清理、恢复、跨卡与未知停止规则；逐节可追溯。 | AI | | 待验证 |
| RL38-M3 | 共用派单模板唯一，adapter 仅保留宿主差异与必要入口；按需文档触发条件明确且安装后可达。 | AI | | 待验证 |
| RL38-M4 | 受管安装包、适用回归与有效变异、独立复核、双平台CI、实际合入态复验及verify齐备。 | AI | | 待验证 |

## 人类签名区
无人判条目，不代签真实体验。

## 需求对齐证据
| 需求 / 人验项 | 场景与操作路径 | 证据 (E-00x) | 结论 |
|---|---|---|---|
| 字符负担 | 相同Unicode口径复算所有skill md/toml | E-002 | 满足（实测，见size-ledger） |
| 规则保真与按需读取 | 旧新节映射及安装入口遍历 | E-003 | 满足（安装闭环及独立原文对照通过） |
| 分发完整性 | 六临时副本、缺包拒绝及生产分发清单变异 | E-004 | 满足（80项通过、有效RED及恢复） |

## 有效单测·变异点登记
| 变异点锚点(生产代码 path:line) | 原值→变异值 | 语义类别 | 对应测试 ID | 运行命令 | 施加 hash | 还原 hash | 登记人(重核须=轮2实例) | 施加后结果 |
|---|---|---|---|---|---|---|---|---|
| tools/install_skill.py:23 | 分发card-chain→漏掉合同 | 改边界 | test_installed_reading_routes_are_closed_and_template_is_unique | python3 -m unittest discover -s tests -p test_contract.py -k installed_reading_routes -v | 015516cfcbc1fc6acb36d53a94a91f10d9d58c11 | 81ace255b44dbf0fedcaab1cf854967d1506866b | codex-root-rlt38-20261009 | 断言失败 |
<!-- dh:review-attempt:v1 task=RLT_38 attempt=1 kind=full reviewer_session_id=/root/rlt38_code_review status=punched -->

<!-- dh:review-result:v2 task=RLT_38 path=code_review attempt=1 artifact=docs/modules/relay-lite/workspace/38-RLT_38-protocol-trim/evidence/code-review-1.json artifact_sha256=e76c0ad86af1315ced789beb2a4c1313ca393deb7a2c9c1ca69ac3d80e4c9ce0 -->

Confidence Challenge：字符减少不直接证明真实agent表现；本卡只证协议语义保真、读取/安装完整与实际字符。没有新增人判项、方向待决或风险接受，远端交付完成前不标完成。
