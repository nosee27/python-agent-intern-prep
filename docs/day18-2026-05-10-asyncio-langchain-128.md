## Day 18 | 2026-05-10 | asyncio事件循环 + LangChain Chains + 128.最长连续序列

### asyncio 事件循环深入
- `task.cancel()`: 发送取消信号，等下一个await点触发CancelledError
- `asyncio.wait_for()`: 封装超时取消，超时报TimeoutError
- 异常在await处重新抛出，必须用try/except捕获

### LangChain Chains
- Chain = 组件管道: PromptTemplate | LLM | OutputParser
- `ChatPromptTemplate.from_messages()`: 定义带变量的消息模板
- `StrOutputParser()`: 把ChatMessage解析成纯字符串
- LCEL (`|` 符号) 是现代LangChain推荐写法

### 算法：128. 最长连续序列
- 哈希集合去重，O(1)查询
- 只从序列起点(num-1不在集合)开始往下数
- 时间O(n)，空间O(n)