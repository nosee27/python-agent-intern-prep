#@dataclass 装饰器,自动生成 __init__、__repr__、__eq__ 等方法
"""
field
特性	              用法
default=	        不可变默认值(int, str)
default_factory=	可变默认值(list, dict),防止共享引用
repr=False	        该字段不显示在 __repr__ 中
eq=False	        该字段不参与 == 比较
frozen=True	        实例创建后不可修改(@dataclass(frozen=True))
"""
#把昨天的 Agent 类改成 @dataclass 版本：
from dataclasses import dataclass, field

@dataclass
class Agent:
    name:str
    role:str
    skills:list=field(default_factory=list)
    task_count:int=field(default=0,repr=False)
    
    def __call__(self, task):
        self.task_count += 1
        return f"[{self.name}] 执行第{self.task_count}个任务: {task}"

# 测试
bot1 = Agent("小猪", "研究员", ["python", "数据分析"])
print(bot1)  
bot2 = Agent("小助", "写手")  
print(bot2) 
bot1("查资料")
print(bot1.task_count)  
print(bot2.task_count) 