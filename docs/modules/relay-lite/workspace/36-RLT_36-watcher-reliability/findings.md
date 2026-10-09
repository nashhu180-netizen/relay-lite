<!-- dh:v1 -->
# findings — RLT_36

## 用户决定
2026-10-09：“watcher 的体验不好，一直会暂停，然后整个任务就停了”。用户确认标准档三项修复目标和真实隔离演练，随后“确认开始修复，建个issue”；模型提案回复“确认这组分配”。分钟未登记，不伪造人验。

## 原始现场
WFP_08 watcher历史输出包含SPACE_WATCH_BLOCKED reason=notification_unconfirmed及exit2。原space_watch在通知后要求5秒内working+seq推进，失败终止整个循环；这不等于通知未发送。此次不改原失败或在途监控。原模型guardian结束回合与实际监控子进程存活是两个事实，当前两处监控实查存活不证明长期可靠。

## 待决/停止线
无新增方向待决；若需扩大真实业务space/安装/权限/验收，停止并登记。独立演练未执行，不写PASS。

## 方案复核与整改
独立review.plan初审REVISE：PR36-01 P1要求排除通知/人工唤醒假阳性，PR36-02/03 P2要求证据清单和有限演练预算/真实失败出口。已在task_plan第5步补S-A busy通知与S-B无通知多轮PENDING→READY的时序、防假阳性、400秒预算及真实worker停止核验；原报告保留，待原reviewer定向方案复审。不消耗最终code_review额度。

## 真实隔离演练
S-A同monitor PID740665存活169秒，watcher actor已done，主编排working且seq3055未推进，普通monitor单次提交新变化。S-B先受控停止该PID并核消失，再首次派worker；没有再次prompt主编排。原角色产物证明3次PENDING→READY、读取报告/signal/hash与实际worker done，生成本演练预授权交接signal。final.json及原产物保留；不冒称业务卡验收或其它space已升级。首次duplicate--no-daemon失败另存，纠正冗余启动参数后实际argv核验，不改wrapper配置。

补充状态：方案原实例定向PASS，真实隔离演练已完成，以上“未执行/待复审”保留为当时现场。miner候选仅落本工作区草稿，知识库不在本卡允许路径内，未写正册或入册裁决。
