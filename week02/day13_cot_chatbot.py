#CoT 先分析再给出答案
from openai import OpenAI
def chat(message,system=None,use_cot=False,api_key="sk-e2c9e2893eb6421586c3dc6d7443bb20"):
    client=OpenAI(
        api_key=api_key,
        base_url="https://dashscope.aliyuncs.com/compatible-mode/v1"
    )
    messages=[]
    if system:
        messages.append({"role":"system","content":system})
    
    #CoT 核心
    if use_cot:
        message=message+"\n\n请一步步思考,先分析再给出答案"

    messages.append({"role":"user","content":message})
    
    response=client.chat.completions.create(
        model="qwen-plus",
        messages=messages
    )
    return response.choices[0].message.content
if __name__=="__main__":
    question="13+17+2=?"
    print("===直接回答===")
    print(chat(question,system="只回复答案"))
    #print("\n===CoT思维链==")
   # print(chat(question,use_cot=True))