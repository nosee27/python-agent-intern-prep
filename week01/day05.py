my_list=[1,2,3]
for x in my_list:
    print(x)
# 迭代器：有 __next__() 方法的对象
it=iter(my_list) # 把列表转成迭代器
print(next(it))
print(next(it))
print(next(it))

#迭代器
class countdown:
    def __init__(self,start):
        self.start=start
    def __iter__(self):
        return self
    def __next__(self):
        if self.start<=0:
            raise StopIteration
        self.start-=1
        return self.start+1
for num in countdown(5):
    print(num)

#生成器 yield
def get_squares_gen(n):
    for i in range(n):
        yield i**2
gen=get_squares_gen(5)
for x in gen:
    print(x)
#生成器表达式
squares_gen=(x**2 for x in range(500000))
for x in squares_gen:
    if x>100:
        break
    else:
        print(x)

#任务1：用生成器实现斐波那契数列
def fei(n):
    a,b=0,1
    for i in range(n):
        yield a
        a,b=b,a+b
for num in fei(10):
    print(num)
#任务2：用生成器读大文件（一行一行读，不一次性加载）
def read_large_file(filepath):
    with open(filepath,'r',encoding='utf-8') as f:
        for line in f:
            yield line.rstrip('\n')
for line in read_large_file("E:/text1.txt"):
    print(line)