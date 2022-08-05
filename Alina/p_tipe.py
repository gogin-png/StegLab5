import requests
import time
import pyautogui
from datetime import datetime

def price_BTC():
    url = "https://api.binance.com/api/v3/ticker/price"
    data = requests.get(url)
    data.raise_for_status()
    data_1 = data.json()
    st = (next(x for x in data_1 if x["symbol"] == "BTCBUSD"))
    price_1 = (st.get('price'))
    sp = []
    sp.append(price_1)
    cr = float(sp[0])
    return cr

time.sleep(5)

while True:

    try:
        time.sleep(0.2)
        b = str(price_BTC())
        print(b)
        file_1 = open("Price_p", "w")
        file_1.write(b)
        file_1.close()
    except:
        print("№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№")




