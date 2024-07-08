import asyncio

from utils import FooError, foo


async def main():
    results = await asyncio.gather(foo(1),foo(2))
    result1 = results[0]
    result2 = results[1]
    print(f"foo 1 result: {result1}")
    print(f"foo 2 result: {result2}")

# Let's do exception handling next
if __name__ == "__main__":
    asyncio.run(main())
