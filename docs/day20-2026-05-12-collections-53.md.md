## Day 20 | 2026-05-12 | collections模块 + 53.最大子数组和

### collections
- `Counter`: 自动计数，`most_common(n)` 找频率最高的n个
- `deque`: 双端队列，`appendleft/popleft` O(1)，`list.pop(0)` 是O(n)
- `defaultdict(list)`: 自动创建空列表，做邻接表不用判断key存在

### 算法：53. 最大子数组和（Kadane）
- `current = max(num, current + num)`: 负数拖累就重新开始
- `max_sum` 跟踪全局最大
- 时间O(n)，空间O(1)