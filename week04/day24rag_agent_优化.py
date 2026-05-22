#按句子切分
import chromadb
from openai import OpenAI

client=OpenAI(
    api_key="sk-6f33c99fe0204785b14b2805369b8d23",
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1"
)
chromadb_client=chromadb.Client()

#按句子划分
def split_by_sentence(text:str)->list:
    import re
    sentence=re.split(r'[。！？\n]+',text)
    return [s.strip() for s in sentence if s.strip()]
#支持多文档隔离
class SimpleRAG:
    def __init__(self,collection_name:str="rag_docs"):
        self.client=chromadb.Client()
        try:
            self.collection = self.client.get_collection(collection_name)
        except:
             self.collection = self.client.create_collection(collection_name)
    def add_document(self,text:str,doc_name:str):
        chunks=split_by_sentence(text)
        for i ,chunk in enumerate(chunks):
            self.collection.add(
                documents=[chunk],
                metadatas=[{"source":doc_name,"chunk_id":i}],
                ids=["f{doc_name}_{i}"]
            )
        print(f"文档 '{doc_name}' 入库完成，共 {len(chunks)} 段")   
    def ask(self,question:str,doc_name:str=None)->str:
        #"提问，可选指定文档
        where_filter = {"source": doc_name} if doc_name else None
        results=self.collection.query(
            query_texts=[question],
            n_results=3,
            where=where_filter
    )
        context='\n'.join(results["documents"][0])
        messages=[
            {
                "role":"system",
                "content":"你是一个文档问答助手。请严格根据以下上下文回答问题，如果上下文没有相关信息，请明确说'根据文档无法回答'。\n\n上下文：\n" + context
            },
            {
                "role":"user",
                "content":question
            }
        ]
        response=client.chat.completions.create(
            model="qwen-plus",
            messages=messages
        )
        return response.choices[0].message.content
if __name__ == "__main__":
    rag = SimpleRAG()
    
    # 文档1：Python介绍
    python_doc = """
    Python是一种高级编程语言，由Guido van Rossum于1991年创建。
    它以简洁、易读的语法著称，适合快速开发。
    Python广泛应用于Web开发、数据分析、人工智能和科学计算。
    """
    
    # 文档2：Java介绍
    java_doc = """
    Java是一种面向对象的编程语言，由Sun Microsystems于1995年发布。
    Java以"一次编写，到处运行"著称，广泛应用于企业级后端开发。
    Android应用开发主要使用Java和Kotlin。
    """
    
    rag.add_document(python_doc, "python_intro")
    rag.add_document(java_doc, "java_intro")
    # 测试1：问Python，指定文档
    print(">>> 问Python（指定文档）:")
    print(rag.ask("Python是谁创建的？", doc_name="python_intro"))
    # 测试2：问Java，指定文档
    print("\n>>> 问Java（指定文档）:")
    print(rag.ask("Java的特点是什么？", doc_name="java_intro"))
    # 测试3：不问指定文档（检索全部）
    print("\n>>> 问编程语言（不指定文档）:")
    print(rag.ask("哪种语言适合AI开发？"))