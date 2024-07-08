import asyncio

from utils import foo

async def main():
    task_1 = asyncio.create_task(foo(1))    # task 1 starts running
    task_2 = asyncio.create_task(foo(2))    # task 2 starts running
    
    result1 = await task_1          # wait for task_1 to finish
    print(f"foo 1 result: {task_1.result()}")

    result2 = await task_2          # wait for task_2 to finish
    print(f"foo 2 result: {task_2.result()}")


if __name__ == "__main__":
    asyncio.run(main())
