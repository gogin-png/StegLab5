import random
import string
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

N = 150
site = 'https://limewire.com/invite/'

options = webdriver.ChromeOptions()
options.add_argument('headless')
driver = webdriver.Chrome('D:/StegLab5/chromedriver', chrome_options=options)
letters = string.ascii_lowercase + string.ascii_uppercase
invites = [

    '7e538c98ccff9fab5ab0',
    'dbb39e798c6035b8d749',
    'e909ed33c54534f5dbe6',
    '140420d76f9db513671f',
    'cff992896d783b32e0fd',
    '7c33f5e94f81802174c1',
    '0bcf5af31c38593ddb80',
    '075e6eeb3baf0fa4a7b0',
    'bed094ab5ec402e54570',
    'b4e2d4bb048a59eafb0b',
]

for invite in invites:
    for i in range(N):
        while True:
            try:
                driver.get(site + invite + '#waitlist')
                break
            except:
                print('Error')
        inputElement = driver.find_element(By.XPATH, '//*[@id="waitlist"]/div[1]/form/div[1]/div[2]/input')
        print(inputElement)
        time.sleep(2)
        inputElement.click()
        mail = ''.join(random.choice(letters) for _ in range(15)) + '@gmail.com'
        inputElement.send_keys(mail)
        driver.find_element(By.XPATH, '//*[@id="waitlist"]/div[1]/form/div[3]/button').click()
        print(invite + ' (' + str(i + 1) + '/' + str(N) + ')')
        driver.delete_all_cookies()
driver.quit()
