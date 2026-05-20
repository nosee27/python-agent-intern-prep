#文档问答机器人
#用户提问 → ChromaDB检索Top3相关片段 → 拼进Prompt → 模型生成回答
import chromadb
from openai import OpenAI
#配置
client=OpenAI(
    api_key="sk-6f33c99fe0204785b14b2805369b8d2",
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1"
)
chroma_client=chromadb.Client()
collection=chroma_client.create_collection("rag_docs")
#加载本地文档并切分
def load_and_split(filepath:str,chunk_size:int=50):
    with open(filepath,'r',encoding='utf-8') as f:
        text=f.read()
    chunks=[]
    for i in range(0,len(text),chunk_size):
        chunk=text[i:chunk_size+i].strip() #取出从 i 开始、长度为 chunk_size 的子串，并移除首尾空白字符
        if chunk:
            chunks.append(chunk)
    return chunks
#创建测试文档
test_doc="""
Python是一种高级编程语言，由Guido van Rossum于1991年创建。
它以简洁、易读的语法著称，适合快速开发。
Python广泛应用于Web开发、数据分析、人工智能和科学计算。
在AI领域，Python是主流语言，因为丰富的库如TensorFlow、PyTorch。
Python的asyncio模块支持异步编程，适合高并发网络应用。
"""

with open("test_doc.txt","w",encoding="utf-8") as f:
    f.write(test_doc)

chunks=load_and_split("test_doc.txt",chunk_size=40)
print(f"切分成{len(chunks)}")

#存入chromadb
for i,chunk in enumerate(chunks):
    collection.add(
        documents=[chunk],#传入一个列表，其中包含当前这一个文本块
        metadatas=[{"source":"test_doc","chunk_id":i}],
        ids=[f"doc_{i}"]
    )
print("入库成功")

#RAG问答函数
def rag_chat(question:str)->str:
    #检索相关片段
    results=collection.query(
        query_text=[question],#查询文本，这里传入的是包含用户问题的列表
        n_results=3,
        where={"source":"test_doc"}
    )
    #拼接上下文
    context="\n".join(results["documents"][0])

    #构建prompt
    messages=[
        {"role":"system","content":"你是一个文档问答助手。请根据以下上下文回答问题，如果上下文没有相关信息，请说'根据文档无法回答'。\n\n上下文：\n" + context},
        {"role":"user","content":question}
    ]
    #调用模型回答
    response=client.chat.completions.create(
        model="qwen-plus",
        messages=messages
    )
    return response.choices[0].message.content
#测试
if __name__ == "__main__":
    questions = [
        "Python是谁创建的？",           # 文档里有
        "Python在AI领域有什么优势？",    # 文档里有
        "Java和Python哪个更好？",        # 文档里没直接说，看模型怎么答
        "Python的异步编程用什么模块？"   # 文档里有 asyncio
    ]
    
    for q in questions:
        print(f"\n>>> 问题: {q}")
        print(f"<<< 回答: {rag_chat(q)}")