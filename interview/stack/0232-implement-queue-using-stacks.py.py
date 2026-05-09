"""
LeetCode  232.用栈实现队列
链接: https://leetcode.cn/problems/implement-queue-using-stacks/
日期: 2026-05-06
"""
#双栈实现队列的先进先出
class MyQueue:

    def __init__(self):
       self.stack1=[] #输入栈
       self.stack2=[] #输出栈

    def push(self, x: int) -> None:
        self.stack1.append(x)

    def pop(self) -> int:
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2.pop()

    def peek(self) -> int:
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2[-1]

    def empty(self) -> bool:
        return not self.stack1 and not self.stack2
