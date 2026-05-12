#collections模块
from collections import Counter,deque,defaultdict
#Counter 计数，找频率最高的
word=["apple","banana","apple","oragne"]
cnt=Counter(word)
print(cnt)
print(cnt.most_common(2)) #找频率最高的两个
#deque 队列 双端操作
dq=deque([1,2,3])
dq.appendleft(0)
dq.append(4)
dq.popleft()
dq.pop()
print(dq)
#defaultdict 自动创建默认值
graph=defaultdict(list)
graph['A'].append('B')
graph['A'].append('C')
graph['A'].append('4')
print(graph)