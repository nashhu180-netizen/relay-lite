# RLT_38 code review — attempt 1

## 结论

**approved**。本轮为 normal 的一次完整 fresh code_review；未发现 open P0–P3。审阅者未参与实现，未修改候选产品或其它工件。

## 冻结对象与独立性

- baseline：`0b08c18be09cd00e84ff214c582941593ca7c2ec`
- target：`1ad96109b398776e99e25ed6f577e923e14a91cc`
- dispatch diff SHA-256：`12ab5546bac62409f154df06ca2997f0212008f0eaaa2c0f734e8bfc7dcba5ea`
- dispatch：`E-005`；reviewer session：`/root/rlt38_code_review`；implementer session：`codex-root-rlt38-20261009`

审阅从基线原始 `skill/SKILL.md`、两份 adapter 原文和候选完整 diff 独立比对；`rule-map.md` 与 `section-map.json` 只作定位索引，没有作为保真结论的替代证据。候选产品、安装器和测试相对 target 无漂移；工作树中其它未提交 workspace/evidence 现场不纳入本次候选结论。

## 覆盖与结果

- 核心硬闸仍直接保留授权边界、模型确认、signal/`RELAY_RECEIPT` 两分支、生命周期与 reviewer 计数、native clear、sole writer、四类恢复权威和未知不重试。E2 仍限初审 open P0/P1 后由同一 `reviewer_session_id` 做一次 targeted attempt 2。
- `card-chain.md` 保留唯一维护会话、非维护卡通知、接收方确认的维护移交、四项交棒核对、用户来源的自动接续、五步开局、半成品/失败不重试、并行冲突串行及唯一询问者。入口在核心的关联/待定位总表场景强制触发。
- `document-role.md` 保留默认不启用、职责和唯一写者、`READY_FOR_DOCUMENT → SYNCED → 同一 reviewer 确认` 顺序、原 FAIL/REVISE 不得翻 PASS、请求标识保留历史、冻结/恢复和四类权威；核心仅在用户明确启用时触发必读。
- 两 adapter 只保留宿主差异（真实句柄、短等待和运行方式），其余规则回链核心与合同。三份入口均能到达共用 dispatch、watcher、环境和决策入口；递归相对链接检查通过，未见逃逸或缺件。
- `tools/install_skill.py` 的显式闭集覆盖五份新合同与唯一 dispatch。安装消费者测试覆盖三侧和 legacy alias，且缺少路由合同在安装前 fail closed；派单模板只有 `skill/templates/dispatch.md` 一份。
- `measure.py` 已独立复算，结果与 `size-ledger.json` 字节一致：`50930 → 39236` Unicode code points，减少 `11694`（`22.96%`）。这低于源卡约 25%–35% 的目标表述，但源卡要求验收报告实际结果，未把该近似值设为硬性通过阈值；未据此报问题。

## 验证

在新建临时 HOME 中运行：

```bash
HOME=<fresh-temp-home> python3 -m unittest discover -s tests -v
```

结果：80 tests passed。输出中的 `error:` 行来自故障注入和 fail-closed 场景的预期 stderr，unittest 总结为 `OK`。另执行：

```bash
python3 docs/modules/relay-lite/workspace/38-RLT_38-protocol-trim/evidence/measure.py
```

输出与 `size-ledger.json` 的 SHA-256 同为 `5033429482e922122523ee59a078ad78e55be31e94528850537a81f31015c150`；Markdown 相对链接闭合检查为 PASS。

## 限制

本次只验证本地候选、协议语义、安装闭环和单元测试；未执行真实安装、远端、业务仓、CI、合入态或人验。它们仍须按本卡后续授权和闸门独立完成。
