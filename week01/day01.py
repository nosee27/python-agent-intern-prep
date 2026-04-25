#装饰器
"""
from functools import wraps
def my_decorator(func):
    @wraps(func)
    def wrapper(*args,**kwargs):
        print("Before")
        result=func(*args,**kwargs)
        print("After")
        return result
    return wrapper
    """
#练习1：写一个计时装饰器 timer，统计函数运行时间
"""
from functools import wraps
import time
def timer(func):
    @wraps(func)
    def wrapper(*args,**kwargs):
        start=time.perf_counter()
        result=func(*args,**kwargs)
        end=time.perf_counter()
        print(f"运行结果为{result}")
        print(f"函数运行为{func.__name__},运行时间为{end-start:.6f}")
        return result
    return wrapper
@timer
def add(a,b):
    return a+b
add(3,4)
"""
#练习2：写一个日志装饰器 logger，打印函数名和参数
"""
from functools import wraps
def logger(func):
    @wraps(func)
    def wrapper(*args,**kwargs):#args 位置传参 #kwargs 关键字传参
        print(f"函数名为{func.__name__}")
        print(f"位置参数为{args}")
        print(f"关键字参数为{kwargs}")
        result=func(*args,**kwargs)
        print(f"结果为{result}")
        return result
    return wrapper
@logger
def add(a,b):
    return a+b
add(a=33,b=4)
"""
#练习3（挑战）：写一个重试装饰器 retry，函数异常时自动重试3次
import time
from functools import wraps
def retry(func):
    @wraps(func)
    def wrapper(*args,**kwargs):
        for i in range(1,4):
            try:
                result=func(*args,**kwargs)
                return result
            except Exception as e:
                print(f"函数{func.__name__},调用了{i}次，失败原因为{e}")
                if i==3:
                    raise
                time.sleep(1)
    return wrapper
import random
@retry
def f():
    n=random.randint(1,10)
    if n<7:
        raise ValueError(f"数字太小: {n}")
    return n
print(f"结果为{f()}")
