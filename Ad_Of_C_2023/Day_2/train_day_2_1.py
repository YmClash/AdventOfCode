import numpy as np
import pandas as pd
from pycoingecko import CoinGeckoAPI


Geck = CoinGeckoAPI()

bitcoin_data = Geck.get_coin_market_chart_by_id(id='bitcoin', vs_currency='usd',days=30)
bitcoin_data_price = [bitcoin_data]

print(bitcoin_data_price)

# data = pd.DataFrame(bitcoin_data,columns=['TimeStamp','Price'])
# data.head()
for price in bitcoin_data_price:

    print(price)





"""
a=np.array([-1,1])
b=np.array([1,1])

Z= np.dot(a,b)


print(Z)


text = "Hello, World!"
words = text.split()
print(words)


text = "apple,banana,cherry"
fruits = text.split(",")
print(fruits)


text = "   Hello, World!!!!!   "
print(text)
trimmed_text = text.strip().split()
print(trimmed_text)

"""