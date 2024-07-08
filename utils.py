import asyncio

class FooError(Exception):
    pass

async def foo(i):
    try:
        print(f"Running foo with {i}")
        if i == 1:
            raise FooError(f"Task {i} failed!")
        await asyncio.sleep(1)
        return i**2
    except asyncio.CancelledError:
        print(f"Task {i} cancelled!")
        raise
