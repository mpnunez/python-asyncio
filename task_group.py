import asyncio

async def foo(i):
    print(f"Running foo with {i}")
    await asyncio.sleep(1)
    return i**2

async def main():
    
    async with asyncio.TaskGroup() as tg:
        task_1 = tg.create_task(foo(1))    # task 1 starts running
        task_2 = tg.create_task(foo(2))    # task 2 starts running
    # context waits for all tasks to finish - no need to await them!

    print(f"foo 1 result: {task_1.result()}")
    print(f"foo 2 result: {task_2.result()}")


if __name__ == "__main__":
    asyncio.run(main())
