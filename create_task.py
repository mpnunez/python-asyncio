import asyncio

from utils import FooError, foo


async def main():
    task_1 = asyncio.create_task(foo(1))    # task 1 starts running
    task_2 = asyncio.create_task(foo(2))    # task 2 starts running
    
    try:
        result1 = await task_1          # wait for task_1 to finish
        print(f"foo 1 result: {task_1.result()}")
    except FooError as e:
        result1 = e

    try:
        result2 = await task_2          # wait for task_2 to finish
        print(f"foo 2 result: {task_2.result()}")
    except FooError as e:
        result2 = e


if __name__ == "__main__":
    asyncio.run(main())
