#async/await异步编程
#异步函数 async def 函数名
import asyncio
async def async_hello():
    return "hello"
result=asyncio.run(async_hello())
#await：等待异步操作完成
#await 后面的代码会暂停，让出 CPU 去执行其他任务
# 等后面的异步操作完成后，再回来继续执行
import asyncio
async def fetch_data():
    print("获取数据中")
    await asyncio.sleep(1)
    print("数据获取完成")
    return "data"
async def main():
    result=await fetch_data()
    print(f"结果是{result}")
asyncio.run(main())
#并发执行：多个任务同时进行
import asyncio
async def task(name,delay):
    print(f"{name}开始")
    await asyncio.sleep(delay)
    print(f"{name}结束")
    return name
async def main():
    #顺序执行
    await task("A",2)
    await task("B",2)
    #并发执行
    t1=asyncio.create_task(task("A",2))
    t2=asyncio.create_task(task("B",2))
    result1=await t1
    result2=await t2
asyncio.run(main())
#任务：并发调用两个 chat() 函数
import asyncio
async def chat(message):
    await asyncio.sleep(1)
    print(f"回复{message}")
    return message
async def main():
    #顺序执行
    await chat("你好")
    await chat("再见")
    #并发执行
    t1=asyncio.create_task(chat("你好"))
    t2=asyncio.create_task(chat("再见"))
    r1=await t1
    r2=await t2

asyncio.run(main())