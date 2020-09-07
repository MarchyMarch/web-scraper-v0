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

def longSleep():
    rand = uniform(LONG_MIN_RAND, LONG_MAX_RAND)
    time.sleep(rand)

print("----- Begin Scraping -----")

# Fake headers in order to not hit a captcha
headers = {
	"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36" ,'referer':'https://www.google.com/','Accept-Encoding': 'identity'
}

cardLinks = []

for pageNumber in range(10):
    print("--- Grabbing Page {} ---".format(pageNumber))

    # if (pageNumber%2) == 0:
    # 	if pageNumber != 0:
    # 		time.sleep(30)
    smallSleep()

    if (pageNumber%2) == 0 and pageNumber != 0:
        longSleep()

    response = requests.get("https://mercadopartners.com")

    url = ""

    if pageNumber == 0:
        pass
    elif pageNumber == 1:
        url = "https://www.realtor.com/realestateandhomes-search/San-Francisco_CA/sby-6/"
    else:
        url = "https://www.realtor.com/realestateandhomes-search/San-Francisco_CA/sby-6/pg-{}".format(pageNumber)

    response = requests.get(url, headers=headers, timeout=5)


    content = BeautifulSoup(response.content, "html.parser")

    body = content.body
    # print(body)

    # with open("sf-house-body-{}.txt".format(pageNumber), "w") as f:
    #     f.write(str(content))

    for currentCardLinks in body.find_all(attrs={"data-testid":"property-anchor"}, href=True):
        print(currentCardLinks)
        cardLinks.append(currentCardLinks['href'])

print("--- Writing Links to File ---")
with open("sf-house-links-relator.txt", "w") as f:
    for link in cardLinks:
        f.write("{}\n".format(link))

print("--- Done Scraping ---")
