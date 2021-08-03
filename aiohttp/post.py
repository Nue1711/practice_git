import aiohttp
import asyncio
import json

async def main():
    payload= {'key': 'value1', 'key2': 'value2'}
    #sessiom = aiohttp.ClientSession()
    async with aiohttp.ClientSession() as session:
        respone = await session.post('http://httpbin.org/post', json = payload)
        print(await respone.text())

        # respone = await session.get('https://api.github.com/events')
        # print(await respone.content.read(10))


loop = asyncio.get_event_loop()
loop.run_until_complete(main())
loop.close()