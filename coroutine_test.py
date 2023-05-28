import asyncio
import time

# async def crawl_page(url):
#     print('crawling {}'.format(url))
#     sleep_time = int(url.split('_')[-1])
#     await asyncio.sleep(sleep_time)
#     print('OK {}'.format(url))

# async def main(urls):
#     tasks = [asyncio.create_task(crawl_page(url)) for url in urls]
#     await asyncio.gather(*tasks)

# asyncio.run(main(['url_1', 'url_2', 'url_3', 'url_4']))

async def work_1():
    await asyncio.sleep(1)
    return 1

async def work_2():
    await asyncio.sleep(2)
    return 2 / 0

async def work_3():
    print("Work 3 start")
    await asyncio.sleep(3)
    print("Work 3 end")
    return 3

async def main():
    task_1 = asyncio.create_task(work_1())
    task_2 = asyncio.create_task(work_2())
    task_3 = asyncio.create_task(work_3())

    await asyncio.sleep(2)
    # task_3.cancel()

    res = await asyncio.gather(task_1, task_2, task_3, return_exceptions=True)
    print(res)
    print(time.time())

print(time.time())
asyncio.run(main())
