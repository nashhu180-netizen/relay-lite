# 进度

2026-10-07：Issue 两仓建立；源冻结 2246b16；新仓空提交初始化，两仓任务树已建。待方案复核后实施。

2026-10-07 实施：948 文件库存固定，历史 937 文件 archive 原字节保存；新协议/两 adapter/安装器/watch脚本/模板/两表已迁入。新仓39测试PASS（evidence/local-tests.log）；冻结源2246b16相关44测试PASS（evidence/frozen-baseline.log）。最初全量旧账本基线在退休删除并发读取后失效并终止，保留 invalidated-baseline.log，不用于归因/放行；有效相关基线另在冻结Git副本运行。源Runner PowerShell回归仍进行中。
