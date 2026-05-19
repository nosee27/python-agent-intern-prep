import chromadb
from openai import OpenAI
client=OpenAI(
    api_key="sk-bccddcda1cd44041b34b4fa1a93a9191",
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
)
chroma_client=chromadb.Client()

#创建带元数据的集合
collection=chroma_client.create_collection("documents")

#长文档
long_text= """
Python是一种高级编程语言，由Guido van Rossum于1991年创建。
它以简洁、易读的语法著称，适合快速开发。
Python广泛应用于Web开发、数据分析、人工智能和科学计算。
在AI领域，Python是主流语言，因为丰富的库如TensorFlow、PyTorch。
"""
#切分
chunks=[chunk.strip() for chunk in long_text.strip().split("。")if chunk.strip()]
print(f"切分成{len(chunks)}")

#入库
documents=[]
metadatas=[]
ids=[]
for i,chunk in enumerate(chunks):
    documents.append(chunk+"。")
    metadatas.append({"source":"python_intro","chunk_id":i})
    ids.append(f"chunk_{i}")
collection.add(
    documents=documents,
    metadatas=metadatas,
    ids=ids
)
print(f"入库成功")

#查询
results=collection.query(
    query_texts=["Python在AI领域有什么应用？"],
    n_results=2,
    where={"source":"python_intro"}
)
print("查询结果")
for doc,met in zip(results["documents"][0],results["metadatas"][0]):
    print(f"内容：{doc}")
    print(f"来源{met['source']},块ID:{met['chunk_id']}")
    print()
#删除
collection.delete(where={"source":"python_intro"})
print(f"已删除全部文件")