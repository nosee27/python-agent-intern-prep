# Day 13 | 2026-05-05 | 类方法/静态方法/ABC + CoT + 最小栈复习

## @classmethod vs @staticmethod
- classmethod: 第一个参数是 cls，操作类本身，常用于替代构造函数 from_dict
- staticmethod: 无 self/cls，只是挂在类名下的工具函数
- 普通方法: 操作实例

## ABC 抽象基类
- from abc import ABC, abstractmethod
- 抽象类不能被实例化，子类必须实现所有 @abstractmethod
- 用途：定义接口，多 Agent/多工具系统的基础

## CoT 思维链
- 在 Prompt 里加"请一步步思考"
- 强制 AI 输出中间推理步骤，减少跳步错误
- 适用：数学计算、逻辑推理、复杂决策

## 复习：155. 最小栈
- 辅助栈同步存储当前最小值
- push: 主栈入栈，辅助栈入当前最小（或重复最小）
- getMin: O(1) 取辅助栈顶