import chromadb
#创建客户端
client=chromadb.Client()
#创建集合
collection=client.create_collection("test")
#添加文档
documents=[
    "Python是一种编程语言",
    "Java也是一种编程语言",
    "Python适合AI开发",
    "Java适合企业级后端"
]
ids=["id1","id2", "id3", "id4"]
collection.add(documents=documents,ids=ids)
#查询
result=collection.query(
    query_texts=["Python能做什么?"],
    n_results=2
)
print("查询结果",result)
#删除
collection.delete(ids=["id4"])

result2=collection.query(
    query_texts=["Java企业应用"],
    n_results=2
)
print("删除后查询",result2)