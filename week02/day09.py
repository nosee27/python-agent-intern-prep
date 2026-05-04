#__call__实例像函数一样调用  类装饰器
import time
class Timer:
    def __init__(self,func):
        self.func=func
    def __call__(self,*args,**kwargs):
        start=time.perf_counter()
        result=self.func(*args,**kwargs)
        end=time.perf_counter()
        print(f"耗时{end-start:.4f}s")
        return result
@Timer
def slow_add(a,b):
    time.sleep(1)
    return a+b
print(slow_add(3,4))
#练习：用 __call__ 实现"带状态的计数器"
class counter:
    def __init__(self,start=0):
        self.count=start
    def __call__(self,step=1):
        self.count+=step
        return self.count
c=counter(10)
print(c())
print(c(5))