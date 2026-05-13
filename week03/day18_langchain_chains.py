from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate,MessagesPlaceholder
from langchain_core.output_parsers import StrOutputParser
from langchain_core.messages import HumanMessage,AIMessage
#基础chain 链
#模型
model=ChatOpenAI(
    model="qwen-plus",
    api_key="sk-bccddcda1cd44041b34b4fa1a93a9191",
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1"
)
#prompt模板
prompt=ChatPromptTemplate.from_messages([
    ("system","你是一位耐心的人生导师，用中文十五个字解释"),
    ("human","请解释什么是{concept}")
])
#输出解析器 把模型返回的复杂对象，直接转成字符串。
parser=StrOutputParser()

#管道组装 prompt渲染->model调用->parser解析 从左向右传递
chain=prompt|model|parser
print("===基础chain===")
# 使用 invoke 触发整条链
result=chain.invoke({"concept":"爱情"})
print(result)
print()

#=====带记忆的chain=====
prompt_with_history=ChatPromptTemplate.from_messages([
    ("system","你是一位人生导师,只用15个字回答问题"),
    MessagesPlaceholder(variable_name="history"),
    ("human","{input}")
])
chain_with_memory=prompt_with_history|model|parser

history=[
    HumanMessage(content="我叫乐乐"),
    AIMessage(content="你好乐乐，有什么可以帮助你的？")
]
print("====记忆====")
result=chain_with_memory.invoke({
    "history":history,
    "input":"我叫什么名字?" 
})
print(result)
print(history)
