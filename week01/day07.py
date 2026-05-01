#__str__ 用户
class student:
    def __init__(self,name,grade):
        self.name=name
        self.grade=grade

    def __str__(self):
        return f"{self.name}同学,成绩为{self.grade}"
    
s=student("乐乐",100)
print(s)
print(str(s))
#__repr__ 开发者
#如果没有定义 __str__，print() 会回退调用 __repr__
class Student:
    def __init__(self,name,grade):
        self.name=name
        self.grade=grade
    def __repr__(self):
        return f"Studne name={self.name},grade={self.grade}"
s=Student("小明",91)
print(s)
print(repr(s))
#__call__ 让实例像函数一样被调用
class Multiplier:
    def __init__(self,factor):
        self.factor=factor
    def __call__(self,x):
        return x*self.factor
double=Multiplier(2)
print(double(10))
#练习：写一个 Agent 类
class Agent:
    def __init__(self,name,role):
        self.name=name
        self.role=role
    def __str__(self):
        return f"Agent{self.name},角色={self.role}"
    def __repr__(self):
        return f"Agent(name={self.name},role={self.role})"
    def __call__(self,task):
        return f"{self.name}正在执行{task}"
a=Agent("小明","研究院")
print(a)
print(repr(a))
print(a("查资料"))