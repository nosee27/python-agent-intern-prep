from openai import OpenAI
def chat(message,api_key="666"):
    client=OpenAI(
        api_key=api_key,
base_url="https://dashscope.aliyuncs.com/compatible-mode/v1"
    )
    response=client.chat.completions.create(
        model="qwen-plus",
        messages=[{"role":"user","content":message}]
    )
    return response.choices[0].message.content
def main():
    print("="*40)
    print("欢迎来聊天，有什么疑问随时提出来吧")
    print("输入history,可查看历史记录")
    print("输入exit或quit即可退出对话")
    print("="*40)

    history=[]

    while True:
        #用户输入
        user_input=input("你:").strip()
        #输入exit或quit退出
        if user_input.lower()in["quit","exit"]:
            print("退出成功")
            break
        #查看历史记录
        if user_input.lower() == "history":
            print("\n--- 本轮对话历史 ---")
            for role, content in history:
                print(f"{role}: {content}")
            continue
        
        if not user_input:
            continue
        #ai回复
        try:
            reply=chat(user_input)
            print(f"ai:{reply}")

            history.append(("你",user_input))
            history.append(("ai",reply))
        except Exception as e:
            print(f"出现了错误{e}")
if __name__=="__main__":
    main()