import requests
import time
import pyautogui
from datetime import datetime


def read(file_name):
    file = open(file_name, "r")
    c = file.read()
    s = float(c)
    return s

def write(file_name, b):
    file_1 = open(file_name, "w")
    file_1.write(b)
    file_1.close()

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


while True:
    p = price_BTC()
    time.sleep(1)
    z = price_BTC()
    f = read("+-price")
    x = p - z
    b = f + x

    write("+-price", str(b))
    print(b)


