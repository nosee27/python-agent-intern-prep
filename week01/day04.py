#偏函数 functools.partial
#把一个函数的某些参数固定住，生成一个新的函数。
from functools import partial
def power(base,exponent):
    return base**exponent
s=partial(power,exponent=2)
print(s(5))

def send_message(to,content,priority="normal"):
    print(f"发送给{to}:{content}-优先级{priority}")
send_message_admin=partial(send_message,to="admin")

send_message_admin(content="警告")
send_message_admin(content="危险",priority="high")

int2=partial(int,base=2)
print(list(map(int2,["1010","1111"])))
"""
from day01_chatbot import chat
chat_with_plus=partial(chat,model="qwen-plus")
reply=chat_with_plus("你好")
"""
#任务：用 partial 实现一个"乘以固定数"的函数。
def multipy(a,b):
    return a*b
multiply_by_10=partial(multipy,b=10)
print(multiply_by_10(5))
