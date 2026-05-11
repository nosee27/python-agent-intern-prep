#aiohttp异步请求
#async with session.get() 异步上下文
# ClientSession 复用连接的作用 复用已经建立的连接，不再握手
#任务：并发请求3个URL，对比串行 vs 并发的总耗时。
import aiohttp
import asyncio
import time
urls=[
    "https://httpbin.org/delay/1",  # 服务器故意延迟1秒
    "https://httpbin.org/delay/1",
    "https://httpbin.org/delay/1",
]
#串行版（requests)
async def serial_fetch(session):
    results=[]
    for url in urls:
        async with session.get(url) as resp:
            results.append(await resp.json())
    return results
#并发版
async def concurrent_fetch(session):
    tasks=[session.get(url) for url in urls]
    return await asyncio.gather(*tasks)
async def main():
    async with aiohttp.ClientSession() as session:
        t1=time.perf_counter()
        await serial_fetch(session)
        print(f"串行{time.perf_counter()-t1:.2f}s")

        t2=time.perf_counter()
        await concurrent_fetch(session)
        print(f"并发{time.perf_counter()-t2:.2f}s")
asyncio.run(main())
import aiohttp
import asyncio
import time
urls=[
    "https://httpbin.org/delay/1",  # 服务器故意延迟1秒
    "https://httpbin.org/delay/1",
    "https://httpbin.org/delay/1",
]
#串行
async def serial_fetch(session):
    results=[]
    for url in urls:
        async with session.get(url) as resp:
            results.append(await resp.json())
    return results
#并行
async def concurrent_fetch(session):
    tasks=[session.get(url) for url in urls]
    return await asyncio.gather(*tasks)
async def main():
    async with aiohttp.ClientSession() as session:
        t1=time.perf_counter()
        await serial_fetch(session)
        t2=time.perf_counter()
        print(f"{t2-t1}s")

        t3=time.perf_counter()
        await concurrent_fetch(session)
        t4=time.perf_counter()
        print(f"{t4-t3}s")
asyncio.run(main())
    