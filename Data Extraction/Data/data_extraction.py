from tracemalloc import start
import pandas as pd
import numpy as np
import config,csv
from binance.client import Client
from datetime import datetime, timedelta

client = Client(config.API_KEY, config.API_SECRET)

csvFile = open("deneme.csv", 'w', newline='')
candleStick_writer = csv.writer(csvFile, delimiter=',')

DAYS = 5
end = datetime.now()
end = end - timedelta(days=0)
start = end - timedelta(days=DAYS)
start = start.strftime('%d %b, %y')
end = end.strftime('%d %b, %y')



klines = client.get_historical_klines("BTCUSDT", Client.KLINE_INTERVAL_1HOUR, start)

for candle in klines:
    candleStick_writer.writerows(klines)
    print(len(klines))

# data.head(20).volume

data = pd.DataFrame(
    data =[row[1:7] for row in klines],
    columns = ['open', 'high', 'low', 'close', 'volume', 'time'],
).set_index('time')
data.index = pd.to_datetime(data.index + 1, unit = 'ms')
data = data.sort_index()
data = data.apply(pd.to_numeric, axis = 1)


summary = 0
for item in data.head(5).open:
    summary += item

avgOpen = summary/5



