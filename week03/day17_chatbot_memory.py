from openai import OpenAI
def chat(message,history=None,system=None,api_key="sk"):
    """
    带记忆功能的对话机器人
    Args:
        message: 本轮用户输入
        history: [{"role": "user", "content": "..."}, {"role": "assistant", "content": "..."}]
        system: 系统角色设定
        api_key: API密钥
    Returns:
        (reply, new_history)  # 返回回复 + 更新后的历史
    """
    client=OpenAI(
          api_key=api_key,
          base_url="https://dashscope.aliyuncs.com/compatible-mode/v1"
     )
    messages=[]
    if system:
          messages.append({"role":"system","content":system})
    if history:
         messages.extend(history[-10:])
    
    messages.append({"role":"user","content":message})

    response=client.chat.completions.create(
         model="qwen-plus",
         messages=messages
    )         
    reply=response.choices[0].message.content

    #更新历史
    new_history=history or []
    new_history.append({"role":"user","content":message})
    new_history.append({"role":"assistant","content":reply})
    # 防止历史无限增长（只保留最近10轮 = 20条）
    if len(new_history)>20:
         new_history=new_history[-20:]
    return reply,new_history
if __name__=="__main__":
    history = []
    system_prompt = "你是一位耐心的Python导师,回答问题只需要10个字之内"
    
    # 第一轮
    reply, history = chat("我叫杨景乐", history=history, system=system_prompt)
    print(f"AI: {reply}")
    
    # 第二轮（AI应该记得名字）
    reply, history = chat("我叫什么名字？", history=history, system=system_prompt)
    print(f"AI: {reply}")
    
    # 第三轮
    reply, history = chat("我想学装饰器", history=history, system=system_prompt)
    print(f"AI: {reply}")