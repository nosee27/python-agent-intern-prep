"""
LeetCode  155. 最小栈
链接: https://leetcode.cn/problems/min-stack/
日期: 2026-05-05
"""
#双栈 主栈加辅助栈
class MinStack:

    def __init__(self):
        self.stack=[]
        self.min_stack=[]

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.min_stack:
            self.min_stack.append(val)
        else:
            self.min_stack.append(min(val,self.min_stack[-1]))
    

    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop() 

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]

