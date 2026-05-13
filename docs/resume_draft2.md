# 杨景乐

**手机**：19506146511 | **邮箱**：2309129591@qq.com | **GitHub**：github.com/nosee27/python-agent-intern-prep  
**求职意向**：Python开发实习生 / AI应用实习生 | **到岗时间**：2026.07.11 | **实习时长**：≥2个月

---

## 教育背景

**广西科技大学** | 软件工程 | 本科在读  
预计毕业：2028年6月 | 当前年级：大二

---

## 技能栈

- **Python 核心**：asyncio 并发编程、aiohttp 异步请求、装饰器/生成器/上下文管理器、OOP、typing 类型系统、异常与性能优化
- **LLM / Agent**：OpenAI API 标准调用、LangChain Chains 管道（PromptTemplate | LLM | OutputParser）、Qwen-plus、Prompt Engineering（System / Few-shot / CoT）
- **Web / 工程**：Flask 后端开发、RESTful API 设计、MySQL CRUD、Git 版本控制、PEP8 + black 代码规范、mypy 静态类型检查
- **算法基础**：LeetCode Hot 100 进行中（已完成链表、栈、双指针、滑动窗口、哈希、Kadane 等 20+ 题）

---

## 项目经历

### LLM Agent 对话引擎（命令行版）
**时间**：2026.04 — 2026.05  
**技术栈**：Python、asyncio、aiohttp、LangChain、通义千问 API、Git  
**GitHub**：github.com/nosee27/python-agent-intern-prep

- **统一 LLM 调用层**：基于 `openai` 库兼容通义千问 API，封装可复用 `chat()` 函数；支持 System Prompt 角色设定、Few-shot 示例注入、CoT 思维链，实现 Python 导师 / 浪漫主义诗人 / 犀利评论家等多人格切换
- **上下文与状态管理**：独立维护 `history` 列表实现多会话隔离，支持最近 5 轮对话记忆；通过长度截断防止 token 溢出，确保长对话稳定性
- **并发性能优化**：使用 `asyncio` + `aiohttp` 重构 API 调用层，3 个并发请求总耗时从串行 3s 降至 1s，性能提升 67%
- **鲁棒性设计**：自定义 `APIError` 异常类，结合 `try-except` 实现超时重试与优雅降级；使用 `@contextmanager` 封装资源释放逻辑，避免连接泄漏
- **工程规范**：代码遵循 PEP8，black 统一格式化，GitHub 保持每日 commit 记录，累计产出 500+ 行生产级 Python 代码

---

## 自我评价

学习能力强，大二自学 Python + LLM Agent 方向并制定 78 天打卡计划；执行力强，GitHub 持续提交记录学习轨迹；对 Agent 工程化开发有热情，关注大模型应用落地。