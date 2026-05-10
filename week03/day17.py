#asyncio 事件循环
"""
import asyncio
async def main():
# 1. create_task: 创建任务，立即加入事件循环
    t1=asyncio.create_task(task("A"),1)
    # 2. gather: 并发执行多个任务，等全部完成
    result= await asyncio.gather(t1,t2)
     # 3. wait: 等任务完成，返回已完成和未完成的
    done,pending=await asyncio.wait([t1,t2],timeout=5)
asyncio.run(main())
"""
#任务：并发调用3个 chat()，带超时控制
import asyncio
async def chat_bot(message,delay):
    await asyncio.sleep(delay)
    return f"回复{message}"
async def main():
    tasks=[
        asyncio.create_task(chat_bot("乐乐",1)),
        asyncio.create_task(chat_bot("谢谢",1)),
        asyncio.create_task(chat_bot("拜拜",2))
    ]
    results=await asyncio.gather(*tasks)
    for r in results:
        print(r)
asyncio.run(main())