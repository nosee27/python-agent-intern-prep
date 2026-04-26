#任务1：带参装饰器
from functools import wraps
import time
def retry(max_attempts=5,delay=2):
    def decorator(func):
        @wraps(func)
        def wrapper(*args,**kwargs):
            for i in range(1,max_attempts+1):
                try:
                    result=func(*args,**kwargs)
                    return result
                except Exception as e:
                    print(f"调用{func.__name__},失败了{i}次，原因为{e}")
                    if i==max_attempts:
                        raise
                    time.sleep(delay)
        return wrapper
    return decorator
import random
@retry(max_attempts=5,delay=1)
def f():
    n=random.randint(1,10)
    if n<7:
        raise ValueError(f"数字太小: {n}")
    return n
print(f())
"""
任务2:类装饰器
用 __call__ 魔术方法（昨天刚学）把 Timer 做成类装饰器
目标：@Timer 能统计函数运行时间

import time
from functools import wraps
class Timer:
    def __init__(self,func):
        self.func=func
        self.__name__=func.__name__
    def __call__(self,*args,**kwargs):
        start=time.perf_counter()
        result=self.func(*args,**kwargs)
        end=time.perf_counter()
        print(f"调用{self.func.__name__}花了{end-start:.6f}秒")
        return result
@Timer
def add(a,b):
    return a+b
add(2,1)
#做一个装饰器 CountCalls,记录一个函数被调用了多少次

from functools import wraps
class CountCalls:
    def __init__(self,func):
        wraps(func)(self)
        self.func=func
        self.count=0
    def __call__(self,*args,**kwargs):
        self.count+=1
        print(f"{self.func.__name__}已被调用{self.count}")
        return  self.func(*args,**kwargs)
@CountCalls
def say():
    print("hello" )
say()
"""