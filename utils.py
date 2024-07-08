import asyncio

async def foo(i):
    print(f"Running foo with {i}")
    await asyncio.sleep(1)
    return i**2
