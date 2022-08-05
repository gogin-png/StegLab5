import requests
import time
import pyautogui
from datetime import datetime



variable_sales = 0
#time.sleep(10)
while True:

    try:

        if variable_sales == 1:
            variable_sales = variable_sales - 1

        time_start = time.time()

        time.sleep(1)

        txt_1 = str(1)
        txt_2 = str(111111111)
        txt_3 = str(0)
        txt_4 = str(1)

        file = open("price.txt", "w")
        file.write(txt_1)
        file.close()

        file = open("price_m.txt", "w")
        file.write(txt_2)
        file.close()

        file = open("price_purchase.txt", "w")
        file.write(txt_3)
        file.close()

        file = open("max_price_after_purchase.txt", "w")
        file.write(txt_4)
        file.close()

        # variable_sales = 0

        def distribution_of_support(arg_2):
            per_2 = (max(arg_2)-min(arg_2))/100
            return per_2

        def percent(arg):    # выводит % раздницу между значение txt и BTC
            per = ((max(arg) / min(arg)) - 1)
            return per

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

        def read(file_name):
            file = open(file_name, "r")
            c = file.read()
            s = float(c)
            return s

        def write(file_name, b):
            file_1 = open(file_name, "w")
            file_1.write(b)
            file_1.close()

        pyautogui.PAUSE = 1
        pyautogui.FAILSAFE = True

        pyautogui.size()
        pyautogui.position()

        while variable_sales < 1:

            time_start = time.time()

            now = datetime.now()
            current_time = now.strftime("%H:%M:%S")

            time.sleep(0.5)

            p = price_BTC() # сравнивает значение в price_txt и входящее из BTC

            s = float(read("price.txt"))

            if p >= s: # записывает наибольшее значение в price.txt
                cur_time = time.time()
                #print('cur_time = ', cur_time)
                b = str(p)
                write("price.txt", b)
                #print("больше")

            arg = p, s
            print('Падение цены в % =', float(percent(arg)))

            if percent(arg) >= 0.0015: #падение цены

                price_min = float(read("price_M.txt"))  # извлекает значение price_M

                cur_time_2 = time.time()
                print('cur_time_2 = ', cur_time_2)

                if p < price_min and p < s and cur_time - cur_time_2 < 0: #заносит наименьшее значение в фаил

                    z = str(p)
                    write("price_M.txt", z)

                else:
                    print("нет покупки", "Current Time =", current_time)

                max_price = float(read("price.txt"))


                the_difference_between_max_min = (max_price - price_min)*0.1 # извлекает 10% от разности max и min значения
                price_dif = p - price_min

                # print('hof =', price_dif)
                # print('proz_pric_fx =', the_difference_between_max_min)
                if price_dif >= the_difference_between_max_min and p > price_min: # запоминает значение покупки

                    p_2 = str(p)
                    write("price_purchase.txt", p_2)

                    # pyautogui.moveTo(935, 465, duration=0.001) # левый скрол
                    # pyautogui.click(clicks=1)
                    # pyautogui.moveTo(750, 600, duration=0.001) # покупка левая кнопка
                    # pyautogui.click(clicks=1)

                    while variable_sales < 1:

                        p = price_BTC()

                        now = datetime.now()
                        current_time = now.strftime("%H:%M:%S")

                        time.sleep(0.01)

                        max_purchase = float(read("max_price_after_purchase.txt"))
                        price_purchase = float(read("price_purchase.txt"))

                        print('максимальная цена после покупки =', max_purchase, "Current Time =", current_time)
                        print('цена покупки =', price_purchase, "Current Time =", current_time)
                        print('#' * 60)

                        if p >= max_purchase:
                            write("max_price_after_purchase.txt", str(p)) #ищит максимальную цену после покупки

                        # time.sleep(300)

                        if p < price_purchase:

                            # pyautogui.moveTo(1485, 465, duration=0.001)  # правый ползунок
                            # pyautogui.click(clicks=1)
                            # pyautogui.moveTo(1150, 600, duration=0.001)  # прая кнопка продажи
                            # pyautogui.click(clicks=1)

                            price_purchase = float(read("price_purchase.txt"))
                            p = price_BTC()
                            difference = str(p - price_purchase)
                            zx = str(p - price_purchase)
                            print(zx)

                            price_for_all = float(read("price_for_all_time.txt"))
                            zx_float = float(zx)
                            price_for_all_time = price_for_all + zx_float
                            write("price_for_all_time.txt", str(price_for_all_time))

                            print("ПРОДАЖА цена меньше p=", p, "Цена покупки =", price_purchase, "разница =", difference)
                            print('#' * 60)

                            while True:
                                time.sleep(0.01)
                                p = price_BTC()
                                price_purchase = float(read("price_purchase.txt"))
                                price_Mix = float(read("price_M.txt"))
                                price_mamx = float(read("price.txt"))

                                if p >= price_purchase:

                                    # pyautogui.moveTo(935, 465, duration=0.001)  # левый скрол
                                    # pyautogui.click(clicks=1)
                                    # pyautogui.moveTo(750, 600, duration=0.001)  # покупка левая кнопка
                                    # pyautogui.click(clicks=1)

                                    print("лохххххххххххххххххххххххххххххххххххх")

                                    p = price_BTC()
                                    write("price_purchase.txt", p)

                                    break
                                else:
                                    p = price_BTC()
                                    print("Цена меньше покупки =", p)

                                if (price_mamx - price_Mix) < (price_purchase - p):
                                    variable_sales = variable_sales + 1
                                    break

                        if variable_sales == 1:
                            break
                        max_price_after_purchase = float(read("max_price_after_purchase.txt"))  # извлекает значение max_price_after_purchase.txt
                        file_price_purchase = float(read("price_purchase.txt")) #извлекает значение price_purchase.txt цена покупки

                        growth_purchase = (max_price_after_purchase - file_price_purchase)*0.3 # 30% от цены роста после покупки

                        the_price_of_falling = max_price_after_purchase - p

                        print('цена приемлема', "Current Time =", current_time)

                        if the_price_of_falling > growth_purchase:

                            # pyautogui.moveTo(1485, 465, duration=0.001)# правый ползунок
                            # pyautogui.click(clicks=1)
                            # pyautogui.moveTo(1150, 600, duration=0.001)# прая кнопка продажи
                            # pyautogui.click(clicks=1)

                            price_purchase = float(read("price_purchase.txt"))

                            p = price_BTC()
                            zx = str(p - price_purchase)
                            print(zx)
                            price_for_all = float(read("price_for_all_time.txt"))
                            zx_float = float(zx)
                            price_for_all_time = price_for_all + zx_float
                            write("price_for_all_time.txt", str(price_for_all_time))

                            print("#продажа =", p, "Цена покупки =", price_purchase, "разница цены = ", zx)

                            variable_sales = variable_sales + 1

            else:
                print("ждём", p, "Current Time =", current_time,  "price.txt =", s, "price_M =", price_min,)
                print('#' * 60)

    except:
        print("hi")
        # pyautogui.moveTo(1485, 465, duration=0.001)  # правый ползунок
        # pyautogui.click(clicks=1)
        # pyautogui.moveTo(1150, 600, duration=0.001)  # прая кнопка продажи
        # pyautogui.click(clicks=1)
