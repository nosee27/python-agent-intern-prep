#asyncio事件循环深入
"""
task.done() 任务是否完成 完成返回True
task.cancelled() 任务是否被取消 终止返回True检查任务状态 
task.cancel() 手动取消正在运行的任务
task.wait_for(  ,timeout=) 任务超时会被自动取消
"""
import asyncio
async def risky_task(name):
    await asyncio.sleep(1)
    raise ValueError(f"{name}出错误")
async def long_task():
    await asyncio.sleep(10)
    return f"完成"
async def main():
    #异常捕获
    t1=asyncio.create_task(risky_task("T1"))
    try:
        await t1
    except Exception as e:
        print(f"捕获异常:{e}")
    print(f"t1.done()={t1.done()},t1.cancelled()={t1.cancelled()}")
    #手动取消任务 task.cancel()
    t2=asyncio.create_task(long_task())
    await asyncio.sleep(0.5)
    t2.cancel()
    try:
        await t2
    except asyncio.CancelledError:
        print("t2被成功取消")
    #超时控制（wait_for)
    try:
        await asyncio.wait_for(long_task(),timeout=1.5)
    except asyncio.TimeoutError:
        print("t3超时")
asyncio.run(main())
#任务：写一个 timeout_chat()，
# 调用 API 时如果超过5秒没返回，自动取消并返回 "超时"。
import asyncio
#模拟api获取
async def get_api():
    await asyncio.sleep(5)
    return f"success"
async def timeout_chat():
    try:
        result=await asyncio.wait_for(get_api(),timeout=1)
    except asyncio.TimeoutError:
        return "超时"
print(asyncio.run(timeout_chat()))