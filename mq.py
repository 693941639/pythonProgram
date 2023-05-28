import asyncio

async def customer(queue, id):
    while True:
        val = await queue.get()
        print(f"{id} handle {val}")
        # await asyncio.sleep(1)

async def producer(queue, id):
    for i in range(0, 10):
        await queue.put(id + "_val_" + str(i))
        print(f"{id} put {i} to queue")
        # await asyncio.sleep(1)

async def main():
    queue = asyncio.Queue()
    
    consumer_1 = asyncio.create_task(customer(queue, "consumer_1"))
    consumer_2 = asyncio.create_task(customer(queue, "consumer_2"))

    producer_1 = asyncio.create_task(producer(queue, "producer_1"))
    producer_2 = asyncio.create_task(producer(queue, "producer_2"))

    await asyncio.sleep(10)
    consumer_1.cancel()
    consumer_2.cancel()

    await asyncio.gather(consumer_1, consumer_2, producer_1, producer_2, return_exceptions=True)

asyncio.run(main())
