from openai import OpenAI
def chat(message,system=None,api_key="123"):
    client=OpenAI(
        api_key=api_key,
        base_url="www"
    )
    messages=[]
    if system:
        messages.append({"role":"system","content":system})
    messages.append({"role":"user","content":message})
    response=client.chat.completions.create(
        model="qwen-plus",
        messages=messages
    )
    return response.choices[0].message.content
if __name__=="__main__":
    question="什么是递归"
    print("====正常模式====")
    print(chat(question))
    print("\n=== 暴躁老哥模式 ===")
    print(chat(question,system="你是一位暴躁的程序员，说话简短直接，不超过30字。"))
    print("\n=====诗人模式======")
    print(chat(question,system="你是一位浪漫主义诗人，所有回答必须押韵,只能回答十个字"))
