import requests
import csv
from bs4 import BeautifulSoup
import time
from random import randint

for numb in range(1, 3):

    result = requests.get(f"https://thetoyshop.ge/collections/0-3-%E1%83%AC%E1%83%9A%E1%83%90%E1%83%9B%E1%83%93%E1%83%94/0-3-%E1%83%AC%E1%83%9A%E1%83%90%E1%83%9B%E1%83%93%E1%83%94?page={numb}")

    soup = BeautifulSoup(result.text, "html.parser")

    satamashoeebi = soup.find_all("li", class_="grid__item scroll-trigger animate--slide-in")

    information = []

    for satamasho in satamashoeebi:
        price = satamasho.find("span", class_="price-item price-item--regular").text.strip()
        name = satamasho.find("a", class_="full-unstyled-link").text.strip()

        information.append((price, name))

        time.sleep(randint(15,20))


with open('konteineri.csv', 'w', encoding="utf-8_sig", newline='\n') as csvfile:
    writer = csv.writer(csvfile, delimiter=',')
    for row in information:
        writer.writerow([row[0], row[1]])