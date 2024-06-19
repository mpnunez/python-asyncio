import asyncio

async def foo(i):
    print(f"Running foo with {i}")
    await asyncio.sleep(1)
    return i**2

async def main():
    results = await asyncio.gather(foo(1),foo(2))
    result1 = results[0]
    result2 = results[1]
    print(f"foo 1 result: {result1}")
    print(f"foo 2 result: {result2}")


if __name__ == "__main__":
    asyncio.run(main())
