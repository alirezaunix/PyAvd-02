import asyncio

async def task(name, delay):
    print(f"Task {name} started")
    await asyncio.sleep(delay)  # Simulate an asynchronous task
    print(f"Task {name} finished after {delay} seconds")

async def main():
    # Run tasks concurrently
    await asyncio.gather(
        task("A", 3),
        task("B", 5),
        task("C", 1)
    )

# Run the asyncio event loop
asyncio.run(main())