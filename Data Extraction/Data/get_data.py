import config,csv
from binance.client import Client
from datetime import datetime
import pandas as pd

client = Client(config.API_KEY, config.API_SECRET)

# prices = client.get_all_tickers()

# for price in prices:                      TEST Ettiğimde verilerin hepsi geldi.
#     print(price)

# candles = client.get_klines(symbol='BTCUSDT', interval=Client.KLINE_INTERVAL_15MINUTE)

# csvFile = open('June_August.csv', 'w', newline='')
# candleStick_writer = csv.writer(csvFile, delimiter=",")

# for candleStick in candles:
#     print(candleStick)

#     candleStick_writer.writerow(candleStick)      5 dakikalık 500 adet veri geldi.

# print(len(candles))       500 veri olduğunu buradan görüyorum.

# candleSticks = client.get_historical_klines("BTCUSDT", Client.KLINE_INTERVAL_5MINUTE, "14 June,2022", "14 August,2022")

# for candleStick in candleSticks:
#     candleStick_writer.writerow(candleStick)

   
tickers = client.get_all_tickers()
print(tickers)
tickers[1]['price']
ticker_df = pd.DataFrame(tickers)


            
# timestamp = 1660374000
# dt_obj = datetime.fromtimestamp(timestamp)

# print("date:",dt_obj)
# print("type of dt:",type(dt_obj))


# TODO: CandleStick'lerin ortalamasından price'ın %20 üzerine geldiği dataları çek.
# TODO: Bütün Price'ların 15 dakikalık periyotlarda ne kadar değiştiğinin verilerini çek.
# TODO: Max Price değerlerini alacağız.
# TODO: Bir anda fırladığı an önceki 30 candleStick'in avgPrice değerini al.
# TODO: Max Volume değerlerini alacağız.
# TODO: Bir anda fırladığı an önceki 30 candleStick'in avgVolume değerini al.


# TODO: "volume kendinden önceki 30adet 15dakikalık volume'ların ortalamasına göre (+%1000) yaptığında, fiyat da kendinden 1 önceki 15dakikalık mumdan (+%10)'dan fazla ise"

# bir sonraki mum %10 çıkar? (true/false)
# BOT: volume %1000+ yaparsa (15 daikalık mum attıktan sonra) satın al +%10 yapınca sat.