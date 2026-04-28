#练习：用闭包写一个"计数器装饰器"
#要求：统计一个函数被调用了多少次。
from functools import wraps
def counter(func):
    count=0
    @wraps(func)
    def wrappers(*args,**kwargs):
        nonlocal count
        result=func(*args,**kwargs)
        count+=1
        print(f"{func.__name__} used {count} times")
        return result
    return wrappers

@counter
def hello(name):
    return f"nihao,{name}"
greet=hello
print(greet("lele"))
print(greet("agent"))