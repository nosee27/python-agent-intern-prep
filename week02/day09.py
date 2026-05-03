#@property 它可以把类的方法变成“属性”一样来访问。
# 简单说：让你用访问属性的写法，去调用方法。
#getter setter deleter 取 改 删
"""
class Agent:
    def __init__(self,name,role):
        self._name=name
        self._role=role
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self,value):
        if len(value)<2:
            raise ValueError("名字至少两个字")
        self._name=value
    @property
    def role(self):
        return self._role
    @role.setter
    def role(self,value):
        self._role=value
    @role.deleter
    def role(self):
        print("删除职位")
        del self._role
bot=Agent("小猪","研究员")
print(bot.name)
print(bot.role)
bot.name="小米"
print(bot.name)
#bot.name="x"
bot.role="码农"
print(bot.role)
del bot.role
"""
#任务：给昨天的 Agent 类加 @property
class Agent:
    def __init__(self,name,role,skill=None):
        self._name=name
        self._role=role
        self._skill=skill or []
        self._task_count=0
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self,value):
        if len(value)<2:
            raise ValueError("名字需要大于2个字")
        self._name=value
    @property
    def role(self):
        return self._role
    @property
    def skill(self):
        return self._skill
    @skill.setter
    def skill(self,value):
        if not isinstance(value,list):
            raise TypeError("技能必须是列表类型")
        self._skill=value
    @property
    def task_count(self):
        return self._task_count
    
    def __call__(self,task):
        self._task_count+=1
        return f"[{self._name}]执行第{self._task_count}个任务{task}"
bot = Agent("小猪", "研究员", ["python", "数据分析"])
print(bot.name)  
bot.name="大猪"
print(bot.name)
try:
    bot.name = "x"    
except ValueError as e:
    print(f"报错：{e}")
print(bot.role)
try:
    bot.role = "写手" 
except AttributeError as e:
    print(f"报错：{e}")
print(bot.task_count)
bot("查资料")
print(bot.task_count)
try:
    bot.task_count = 100  
except AttributeError as e:
    print(f"报错：{e}")