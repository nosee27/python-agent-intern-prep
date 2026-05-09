# 杨景乐

**手机**：19506146511 | **邮箱**：2309129591@qq.com | **GitHub**：github.com/nosee27/python-agent-intern-prep
**求职意向**：Python开发实习生 / AI应用实习生 | **到岗时间**：2026年7月11日 | **实习时长**：2个月

---

## 教育背景

**广西科技大学** | 软件工程 | 本科在读  
预计毕业：2028年6月 | 当前年级：大二

---

## 技能栈

- **Python**：熟悉装饰器、生成器、async/await、面向对象设计、@dataclass
- **LLM应用**：熟悉大模型API调用、Prompt Engineering（System Prompt / Few-shot / CoT）
- **工程能力**：Git版本控制、代码规范（PEP8）、black格式化
- **算法**：LeetCode Hot 100 进行中（已完成链表、栈、双指针、滑动窗口等15+题）

---

## 项目经历

### 智能对话机器人（命令行版）
**时间**：2026.04 — 2026.05  
**技术栈**：Python、通义千问API、Prompt Engineering、Git  
**GitHub**：github.com/nosee27/python-agent-intern-prep

**功能点**：
- 封装可复用的 `chat()` 函数，支持通义千问 API 调用，实现统一的LLM调用层
- System Prompt 角色设定：实现 Python导师/浪漫主义诗人/犀利评论家 等多种人格切换
- Few-shot Prompting：注入示例对话，让AI模仿特定语言风格（如翻译腔）
- CoT 思维链：引导AI分步思考，提升数学/逻辑题推理准确率
- 连续对话 + 历史记录查看（`history`命令）+ 异常处理与重试机制

**技术难点**：
- 多轮对话时，不同角色的上下文会互相污染，通过独立维护 `history` 列表隔离会话状态
- API偶尔超时或网络波动，通过 `try-except` + 用户提示实现优雅降级，避免程序崩溃

**个人收获**：
- 熟悉 LLM 应用开发全流程：API 调用 → Prompt 设计 → 多轮对话管理
- 理解 Agent 开发基础：角色定义、工具封装、状态管理

---

## 自我评价

- **学习能力强**：大二自学Python进阶+LLM Agent方向，制定78天学习计划，GitHub持续提交记录学习轨迹
- **执行力强**：项目代码累计500+行，涵盖装饰器/生成器/async/Agent等模块，代码遵循PEP8规范
- **对Agent方向有热情**：关注大模型应用落地，希望参与LLM Agent的工程化开发