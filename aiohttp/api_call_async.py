import asyncio
from asyncio.tasks import create_task
import re
from aiohttp import ClientSession


base_url = 'http://httpbin.org'

async def count():
    sets = [1,2,3,4,5]
    for i in sets:
        print(i)
        await asyncio.sleep(1)

async def get_delay(seconds):
    endpoint = f'/delay/{seconds}'
    print(f'getting with {seconds} delay..')
    async with ClientSession() as session:
        respone = await session.get(base_url + endpoint)
        print(type(respone))
        respone = respone.status
        print(respone)
async def main():
    await asyncio.gather(get_delay(5), count())
    # task1 = asyncio.create_task(get_delay(5))
    # task2 = asyncio.create_task(count())
    # await task1, task2

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
loop.close()