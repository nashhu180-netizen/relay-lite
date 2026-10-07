<!-- dh:v1 -->
# RLT_33 自动验收与独立复核

本卡原授权：2026-10-07 用户“建个issue 后开工”，Issue relay-lite #1 / dh-relay #156。施工/自动验收执行者 Codex /root；未把施工会话冒充独立 reviewer，无新增人类签名。产品候选 db18185b160c653eebe2121727b9f9f85c22716b；源代码 d8f88ae，CI必要终态联动6a431e9。补充用户决定及最新AW表迁移由定向复核另记；切换仍待原维护者确认。

## AI 提交区

| ID | 命题/事实证明方式 | 实际结果/证据 | 最终裁决者 | 未覆盖边界 |
|---|---|---|---|---|
| RL33-M1 | 独立仓/目录、PR/CI/merge/verify；GitHub读回 | Issue已建、两任务分支及Draft PR#2/#157；merge/verify待执行 | 自动验收，依据两仓服务端证据 | 不能用本地PASS替代合入 |
| RL33-M2 | 独立clone及临时home安装；封闭包测试 | PASS：isolated-clone-tests.log 39项；安装覆盖Claude/Codex/Agents三侧和明确alias | 自动验收 | 未改变用户级安装副本或运行中的会话 |
| RL33-M3 | 协议/两adapter/roles/AGENTS与写权一致 | PASS：review.code1/code2/requirement/consistency；九phase与新executor一致、旧signal只读 | 独立reviewer，自动记录 | 不实施另案#154复核配方 |
| RL33-M4 | 包中无旧mode/账本专属文件，不装archive | PASS：test_contract PackageTests；现役无stage-lead/五阶段入口 | 自动验收+独立reviewer | archive旧文字不作現役 |
| RL33-M5 | 948项源闭集/937文档archive和两表原字节 | 冻结archive PASS（948项/937原字节）；AW5a47/WFP PR158-65f87a0最新正文/快照/hash保真定向复核PASS；两暂停ACK已收，待实际新仓合入后原维护者确认新路径；见table-cutover.json | 自动验收+独立reviewer | 不改原卡状态/授权/人验、不关闭旧卡 |
| RL33-M6 | watcher回归、heavy五路与有效变异、CI | 本地39、冻结相关44、source PowerShell PASS（原真实终端skip1）；五路均PASS；effective-test.json业务RED/精确恢复/GREEN | 独立reviewer+自动验收 | 两仓必要CI成功，source整体SUCCESS/relay-core观察失败保留；没有新真实Herdr演练 |

**需求对齐证据**

| 需求 / 人验项 | 场景与操作路径 | 证据 (E-00x) | 结论 |
|---|---|---|---|
| RL33-M2 独立可用 | 独立Git clone → 无源checkout的临时HOME安装 → 模板/观察器help | E-001 isolated-clone-tests.log / test_contract.py | 满足 |
| RL33-M3/M4 执行者与仅单卡 | 安装包读取协议/两个adapter/roles → 核dispatch/历史兼容/无完整模式入口 | E-002 review.code1/code2/requirement / local-tests.log | 满足 |
| RL33-M5 最新表保真 | 两维护者暂停ACK → 逐字核AW5a47、WFP PR158-65f87a0候选/快照/hash | E-003 table-cutover.json / 两ACK / 定向review | 满足候选保真；实际合入与路径切换尚待执行 |

需求境证据：操作路径“独立clone→运行39项测试→无源checkout的隔离包/临时HOME安装→读取模板及watcher CLI”；证据isolated-clone-tests.log、test_contract.py与五份独立报告；结论分发/术语/历史保全满足本卡需求。任务不含UI，不用DOM/截图替代。旧卡#151真实Herdr验收仍归原合同。

## 独立复核区

独立路径矩阵（启动冻结heavy，无openP0/P1）：
- 方案：plan_review 初审REVISE（2P1），补948闭集后定向PASS，保留全部历史。
- code_round_1：code_review1，review.code1.md，PASS；源CI后续边界联动定向复查另附。
- code_round_2：fresh code_review2，review.code2.md，PASS，指定有效变异；未继承轮1会话。
- requirement_direction：requirement_review，review.requirement.md，PASS。
- consistency_review：consistency_lessons_review，review.consistency.md，PASS。
- lessons：同独立实例consistency_lessons_review，review.lessons.md，PASS，两路径分报告不冒充两个实例。

Review Batch RB-RLT33-2 同批并发；Mode inline_registration，所有子实例只写指定报告，侦测型只读降级、非机器沙箱；审前后Git读回只多上述report，无产品变化。未启用document，无Binding降级。有效变异独立选择生产install_all全target预检循环，隔离exact-SHA副本执行，真正断言失败而非setup/import；effective-test.json和mutation-red/green.log；恢复前后sha256相同。

历史保留：invalidated-baseline.log是运行中删除源文件后的无效取证，不算业务RED、不支持基线归因；另冻结原源44项相关测试PASS。初次source retired-suite失败与修复GREEN日志均保留，不制造假绿。

## 人类签名区

本卡RL33-M1～M6为已冻结机器验收，无新业务人判项；无人类签名、未代签其它卡。用户的迁移时机选择与通知授权已在brief/findings回链，不冒充人验。
