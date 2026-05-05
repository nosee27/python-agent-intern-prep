#@classmethod 类方法 cls
# 替代构造器（工厂方法）、需要访问/修改类属性的操作。
class Date:
    def __init__(self,year,month,day):
        self.year=year
        self.month=month
        self.day=day
    @classmethod
    def from_string(cls,date_str):
        #替代构造器
        year,month,day=map(int,date_str.split('-'))
        return cls(year,month,day)
    @classmethod
    def set_default_format(cls,fmt):
        #修改类属性
        cls.default_format=fmt
#使用工厂方法
d=Date.from_string('2025-12-31')
print(d.year)
#类方法修改类状态
Date.set_default_format('%Y-%m-%d')
print(Date.default_format)

#@staticmethod 静态方法
#放在类命名空间里的普通函数
class MathUtils:
    @staticmethod
    def add(a,b):
        return a+b
    @staticmethod
    def is_even(value):
        return value % 2==0
#通过类或实例调用
print(MathUtils.add(3,4))
m=MathUtils()
print(m.is_even(10))

#抽象基类 ABC (Abstract Base Class)
#定义接口规范，强制子类必须实现某些方法，无法实例化抽象类
from abc import ABC,abstractmethod
class BaseAgent(ABC):
    @abstractmethod
    def chat(self,message):
        pass
class ChatBot(BaseAgent):
    def chat(self,message):
        return f"回复{message}"
bot=ChatBot()

from abc import ABC,abstractmethod
from dataclasses import dataclass
@dataclass
class BaseTool(ABC):
    name:str
    @abstractmethod
    def run(self,input_data:str)->str:
        pass
    @classmethod
    def tool_type(cls):
        return cls.__name__
    @staticmethod
    def validate_input(data):
        return bool(data)
class SearchTool(BaseTool):
    def run(self,input_data:str)->str:
        return f"搜索：{input_data}的结果"
tool=SearchTool(name="乐乐")
print(tool.name)
print(tool.run("python"))
print(SearchTool.tool_type())
print(SearchTool.validate_input("hello"))