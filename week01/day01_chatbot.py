from openai import OpenAI
def chat(message,api_key="sk-7855c7d45b574425b81dfae0778dfaa8"):
    client=OpenAI(
        api_key=api_key,
base_url="https://dashscope.aliyuncs.com/compatible-mode/v1"
    )
#发送信息
    response=client.chat.completions.create(
        model="qwen-plus",
        messages=[{"role":"user","content":message}]
)
#打印AI的回复
    return response.choices[0].message.content
if __name__=="__main__":
    reply=chat("用一句话来解释什么是大模型agent")
    print(reply)
