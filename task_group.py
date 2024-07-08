import asyncio

from utils import FooError, foo

async def main():
    
    async with asyncio.TaskGroup() as tg:
        task_1 = tg.create_task(foo(1))    # task 1 starts running
        task_2 = tg.create_task(foo(2))    # task 2 starts running
    # context waits for all tasks to finish - no need to await them!

    print(f"foo 1 result: {task_1.result()}")
    print(f"foo 2 result: {task_2.result()}")


if __name__ == "__main__":
    asyncio.run(main())
