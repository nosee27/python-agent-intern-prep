class Agent:
    def __init__(self,name,role,skill=None):
        self.name=name
        self.role=role
        self.skill=skill or []
        self.task_count=0
    def __str__(self):
        #给用户看的
        return f"Agent[{self.name}]|角色:{self.role}"
    def __repr__(self):
        #给同行看的
        return f"agent('{self.name}','{self.role}',{self.skill})"
    def __len__(self):
        return len(self.skill)
    def __eq__(self,other):
        if not isinstance(other,Agent):
            return False
        return self.name==other.name
    def __call__(self,task):
        self.task_count+=1
        return f"[{self.name}]执行第{self.task_count}个任务：{task}"

bot1=Agent("小猪","研究员",["python","数据分析"])
bot2=Agent("小猪","写手",["翻译"])
print(bot1)
print(repr(bot1))
print(len(bot1))
print(bot1==bot2)
print(bot1("查资料"))
print(bot1("喝奶茶"))