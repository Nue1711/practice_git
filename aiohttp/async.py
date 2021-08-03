import re
from aiohttp import ClientSession
import asyncio
import time 

api_key = 'P6U8FQVWJCRJQJ5D'
url = 'https://www.alphavantage.co/query?function=OVERVIEW&symbol={}&apikey={}'
result = []
symbols = ['GOOG', 'MFST', 'AAPL', 'TSLA', 'GOOG', 'MFST', 'AAPL', 'TSLA', 'GOOG', 'MFST', 'AAPL', 'TSLA', 'GOOG', 'MFST', 'AAPL', 'TSLA', 'GOOG', 'MFST', 'AAPL', 'TSLA', 'GOOG', 'MFST', 'AAPL', 'TSLA', 'GOOG', 'MFST', 'AAPL', 'TSLA','GOOG', 'MFST', 'AAPL', 'TSLA', 'GOOG', 'MFST', 'AAPL', 'TSLA', 'GOOG', 'MFST', 'AAPL', 'TSLA','GOOG', 'MFST', 'AAPL', 'TSLA', 'GOOG', 'MFST', 'AAPL', 'TSLA', 'GOOG', 'MFST', 'AAPL', 'TSLA','GOOG', 'MFST', 'AAPL', 'TSLA', 'GOOG', 'MFST', 'AAPL', 'TSLA','GOOG', 'MFST', 'AAPL', 'TSLA','GOOG', 'MFST', 'AAPL', 'TSLA']
# symbols = ['AAPL', 'GOOG', 'TSLA', 'MSFT', 'AAPL']

start = time.time()

async def get_task(session):
    tasks = []
    for symbol in symbols:
        tasks.append(asyncio.create_task(session.get(url.format(symbol, api_key), ssl = False)))
        # tasks.append(session.get(url.format(symbol, api_key), ssl = False))
    return tasks

async def main():
    try:
        async with ClientSession() as session:
            tasks = await get_task(session)
            response = await asyncio.gather(*tasks)
            # for response in response:
            #     a = response.url
            # print(a)
            for res in response:
                result.append(await res.json())

        print("Make {} api call in {}".format(len(result),time.time() - start))

        print("You did it")
    except KeyboardInterrupt:
        print('sozi')

asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
asyncio.run(main())