# Day 17 | 2026-05-09 | asyncio事件循环 + 机器人记忆 + 49.字母异位词

## asyncio 事件循环
- create_task: 立即安排进事件循环，不阻塞
- gather: 等所有任务完成，按顺序返回结果
- wait: 等任务完成，返回(done, pending)，支持超时

## 机器人记忆
- history 参数传入最近对话
- 只保留最近10轮（20条消息），防止token超限
- 返回 reply + new_history，方便下一轮使用

## 算法：49. 字母异位词分组
- 排序后的字符串作为字典键
- defaultdict(list) 自动创建空列表
- 时间 O(n * klogk)，空间 O(nk)