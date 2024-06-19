import asyncio

async def foo(i):
    print(f"Running foo with {i}")
    await asyncio.sleep(1)
    return i**2

async def main():
    result1 = await foo(1)          # wait for the result of foo(1)
    result2 = await foo(2)          # wait for the result of foo(2)
    print(f"foo 1 result: {result1}")
    print(f"foo 2 result: {result2}")


if __name__ == "__main__":
    asyncio.run(main())
