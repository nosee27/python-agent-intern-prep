import sys
# 列表推导式：一次性生成所有元素
s_list=[x**2 for x in range(1000)]
print(sys.getsizeof(s_list))
# 生成器表达式：惰性生成
s_gen=(x**2 for x in range(1000))
print(sys.getsizeof(s_gen))
#需要多次遍历、随机访问 → 用列表
#只需要遍历一次，数据量大 → 用生成器

#itertools
import itertools
# 1. count：无限计数（配合 islice 使用）
for i in itertools.islice(itertools.count(10,2),5):
    print(i)
# 2. cycle：无限循环
for i,char in enumerate(itertools.cycle("ABC")):
    if i>6:
        break
    print(char)
# 3. chain：串联多个列表
all_items=itertools.chain([1,2],[3,4],[5,6])
print(list(all_items))
# 4. islice：惰性切片（大文件/流式数据常用）
with open("E:/text1.txt",'r',encoding='utf-8') as f:
    f_7=itertools.islice(f,7)
    for line in f_7:
        print(line.strip())
# 5. product：笛卡尔积（参数组合常用
colors=["蓝","红","紫"]
size=["S","M","L"]
for colors,size in itertools.product(colors,size):
    print(f"{colors}-{size}")
#任务：用 itertools 生成所有可能的 Agent 角色组合
roles = ["研究员", "写手", "审查员"]
tasks = ["收集资料", "撰写报告", "检查错误"]
for roles,tasks in itertools.product(roles,tasks):
    print(f"{roles}-{tasks}")