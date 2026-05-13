#itertools functools
#itertools : count,cycle,chain,groupby,combinations
import itertools
#chain 把多个迭代对象拼成一个
list1=(1,2,3)
list2=(4,5,6)
for x in itertools.chain(list1,list2):
    print(x,end=" ")
#groupby 按key分组(需要先排序)
data=[("A",1),("A",2),("B",3),("B",4),("A",5)]
data.sort(key=lambda x:x[0])
for key,groub in itertools.groupby(data,key=lambda x:x[0]):
    print(f"{key}:{list(groub)}")
#combination/permutations:排列组合
print(list(itertools.combinations([1,2,3],2)))
print(list(itertools.permutations([1,2,3],2))) #全排列
#count 计数器
for i in itertools.count(10,2):
    if i>20:
        break
    print(i,end=' ')
#functools
import functools
#lru_cache 自动缓存
@functools.lru_cache(maxsize=None)
def fib(n):
    if n<2:
        return n
    return fib(n-1)+fib(n-2)
result=fib(30)
print(result)
#partial 固定函数的部分参数
def add(x,y):
    return x+y
add1=functools.partial(add,y=3)
print(add1(2))
#wraps 写装饰器时保留原函数元信息
def my_d(func):
    @functools.wraps(func)
    def wrapper(*args,**kwargs):
        return func(*args,**kwargs)
    return wrapper
@my_d
def hello():
    return "leo"
print(hello.__name__)