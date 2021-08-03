import requests
import json
import time

api_key = 'P6U8FQVWJCRJQJ5D'
url = 'https://www.alphavantage.co/query?function=OVERVIEW&symbol={}&apikey={}'
result = []
symbols = ['GOOG', 'MFST', 'AAPL', 'TSLA', 'GOOG', 'MFST', 'AAPL', 'TSLA', 'GOOG', 'MFST', 'AAPL', 'TSLA', 'GOOG', 'MFST', 'AAPL', 'TSLA', 'GOOG', 'MFST', 'AAPL', 'TSLA', 'GOOG', 'MFST', 'AAPL', 'TSLA', 'GOOG', 'MFST', 'AAPL', 'TSLA','GOOG', 'MFST', 'AAPL', 'TSLA', 'GOOG', 'MFST', 'AAPL', 'TSLA', 'GOOG', 'MFST', 'AAPL', 'TSLA','GOOG', 'MFST', 'AAPL', 'TSLA', 'GOOG', 'MFST', 'AAPL', 'TSLA', 'GOOG', 'MFST', 'AAPL', 'TSLA','GOOG', 'MFST', 'AAPL', 'TSLA', 'GOOG', 'MFST', 'AAPL', 'TSLA','GOOG', 'MFST', 'AAPL', 'TSLA','GOOG', 'MFST', 'AAPL', 'TSLA']

start = time.time()

try:
    for symbol in symbols:
        print("Working on symbol {}".format(symbol))
        respone = requests.get(url.format(symbol, api_key))
        print(type(respone))
        result.append(respone.url)
except KeyboardInterrupt:
    print('sozi')
  
print("Make {} api call in {}".format(len(result),time.time() - start))

print("You did it")