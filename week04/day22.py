from openai import OpenAI
import json
client=OpenAI(
    api_key="sk-bccddcda1cd44041b34b4fa1a93a919",
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1"
)
#tool 工具
def get_weather(location:str)->str:
    return f"{location}今天晴朗，24度"
def calculate(expression:str)->str:
    try:
        allowed=set("0123456789+-/.()")
        if not all(c in allowed for c in expression):
            return "非法字符"
        return str(eval(expression))
    except:
        return "错误"

tools=[
    {
        "type":"function",
        "function":{
            "name":"get_weather",
            "description":"查询天气",
            "parameters":{
                "type":"object",
                "properties":{
                    "location":{"type":"string","description":"城市名"}
                },
                "required":["location"]
            }
        }
    },
    {
        "type":"function",
        "function":{
            "name":"calculate",
            "description":"计算数学表达式",
            "parameters":{
                "type":"object",
                "properties":{
                    "expression":{"type":"string","description":"数学表达式"}
                },
                "required":["expression"]
            }
        }
    },

]
#工具映射
tool_map={
    "get_weather":get_weather,
    "calculate":calculate,
    "get_sex":get_sex
}
def agent_chat(user_input):
    messages = [
        {"role": "system", "content": "你是助手，可以查天气或做计算或判断别的性别。"},
        {"role": "user", "content": user_input}
    ]
    
    # 第一次请求：模型决定调什么
    while True:
        response = client.chat.completions.create(
            model="qwen-plus", messages=messages, tools=tools
    )
        msg = response.choices[0].message
        if not msg.tool_calls:
            return msg.content
    
    # 执行工具
        for tool_call in msg.tool_calls:
            func_name = tool_call.function.name
            args = json.loads(tool_call.function.arguments)
            
            if func_name in tool_map:
                result = tool_map[func_name](**args)
                messages.append({
                    "role": "tool",
                    "tool_call_id": tool_call.id,
                    "content": str(result)
                })
        
        # 第二次请求：生成最终回答
       # final = client.chat.completions.create(
       #     model="qwen-plus", messages=messages, tools=tools
      #  )
      #  return final.choices[0].message.content

if __name__=="__main__":
    print(">>>", agent_chat("北京天气怎么样？"))
    print(">>>", agent_chat("1+1等于几？"))
    print(">>>", agent_chat("你好"))