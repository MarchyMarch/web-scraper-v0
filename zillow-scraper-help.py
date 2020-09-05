from bs4 import BeautifulSoup
import time
from datetime import datetime
from random import uniform, randint
import requests

# Randimization
MIN_RAND = 0.69
MAX_RAND = 1.34
LONG_MIN_RAND = 4.20
LONG_MAX_RAND = 11.13

def smallSleep():
    rand = uniform(MIN_RAND, MAX_RAND)
    time.sleep(rand)

print("----- Begin Scraping -----")

# Fake headers in order to not hit a captcha
headers = {
	'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36',
}

cardLinks = []

for pageNumber in range(15):
    print("--- Grabbing Page {} ---".format(pageNumber))

    response = requests.get("https://mercadopartners.com")

    if pageNumber == 0:
        pass
    elif pageNumber == 1:
        response = requests.get("https://www.zillow.com/san-francisco-ca/?searchQueryState=%7B%22mapBounds%22%3A%7B%22west%22%3A-122.58868254614258%2C%22east%22%3A-122.27797545385742%2C%22south%22%3A37.69630357602892%2C%22north%22%3A37.85419503060532%7D%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A20330%2C%22regionType%22%3A6%7D%5D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A13%7D", headers=headers, timeout=5)
    else:
        response = requests.get("https://www.zillow.com/san-francisco-ca/?searchQueryState=%7B%22mapBounds%22%3A%7B%22west%22%3A-122.58868254614258%2C%22east%22%3A-122.27797545385742%2C%22south%22%3A37.69630357602892%2C%22north%22%3A37.85419503060532%7D%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A20330%2C%22regionType%22%3A6%7D%5D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A13%2C%22pagination%22%3A%7B%22currentPage%22%3A{}%7D%7D".format(pageNumber), headers=headers, timeout=5)

    smallSleep()

    content = BeautifulSoup(response.content, "html.parser")

    body = content.body
    # print(body)

    # with open("sf-house-body-{}.txt".format(pageNumber), "w") as f:
    #     f.write(str(content))

    for currentCardLinks in body.find_all(class_="list-card-link list-card-img", href=True):
        print(currentCardLinks)
        cardLinks.extend(currentCardLinks['href'])

print("--- Writing Links to File ---")
with open("sf-house-links.txt", "w") as f:
    for link in cardLinks:
        f.write("{}\n".format(link))

print("--- Done Scraping ---")
