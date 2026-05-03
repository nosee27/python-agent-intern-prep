from openai import OpenAI
def chat(message,system=None,examples=None,api_key="1"):
    client=OpenAI(
        api_key=api_key,
        base_url="https://dashscope.aliyuncs.com/compatible-mode/v1"
    )
    messages=[]
    if system:
        messages.append({"role":"system","content":system})
    if examples:
        for ex in examples:
            messages.append({"role":"user","content":ex["input"]})
            messages.append({"role":"assistant","content":ex["output"]})
    messages.append({"role":"user","content":"message"})
    response=client.chat.completions.create(
        model="qwen-plus",
        messages=messages
    )
    return response.choices[0].message.content
def main():
    examples=[
    {
        "input":"你好",
        "output":"哦，我的老伙计，你好啊！这真是太令人高兴了。"
    },
    {
        "input":"我想吃饭",
        "output":"哦天哪，瞧瞧这位先生，他竟然想吃饭！我是说这主意还不错。"
    }
]
    reply=chat(
    "今天天气很好",
    system="你是一位翻译腔配音演员",
    examples=examples
    )
    print(reply)
if __name__=="__main__":
    main()