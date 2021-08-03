import aiohttp
import asyncio
import json

async def main():
    #sessiom = aiohttp.ClientSession()
    async with aiohttp.ClientSession() as session:
        respone = await session.get('http://httpbin.org/get')
        print(await respone.json())

        # respone = await session.get('https://api.github.com/events')
        # print(await respone.content.read(10))


loop = asyncio.get_event_loop()
loop.run_until_complete(main())
loop.close()