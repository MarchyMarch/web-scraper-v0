from bs4 import BeautifulSoup
import requests

from datetime import datetime
from time import sleep, time
from random import uniform, randint

# URL: 'www.zillow.com'
# Response: get(URL)
# Content: BeautifulSoup(response.content, "html.parser")

print("----- Begin Scraping -----")

# Fake headers in order to not hit a captcha
headers = {
	'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36',
}

# Array for all list card links
cardLinks = []

# Iterate over a number pages and grab the page
for pageNumber in range(15):
    print("-- Page Number {} ---".format(pageNumber))

    # make the response an existing web page in order to have access later to use it with our paged URLs
    response = requests.get("https://mercadopartners.com")
    if pageNumber == 0:
	       pass
    elif pageNumber == 1:
	       response = requests.get("https://www.zillow.com/homes/San-Francisco,-CA_rb/?searchQueryState=%7B%22usersSearchTerm%22%3A%22San%20Francisco%2C%20CA%22%2C%22mapBounds%22%3A%7B%22west%22%3A-122.83810652685547%2C%22east%22%3A-122.21669234228516%2C%22south%22%3A37.70911569603537%2C%22north%22%3A37.84832142027793%7D%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A20330%2C%22regionType%22%3A6%7D%5D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22pmf%22%3A%7B%22value%22%3Afalse%7D%2C%22pf%22%3A%7B%22value%22%3Afalse%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A12%7D", headers=headers, timeout=5)
    else:
	       response = requests.get("https://www.zillow.com/homes/San-Francisco,-CA_rb/?searchQueryState=%7B%22usersSearchTerm%22%3A%22San%20Francisco%2C%20CA%22%2C%22mapBounds%22%3A%7B%22west%22%3A-122.83810652685547%2C%22east%22%3A-122.21669234228516%2C%22south%22%3A37.70911569603537%2C%22north%22%3A37.84832142027793%7D%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A20330%2C%22regionType%22%3A6%7D%5D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22pmf%22%3A%7B%22value%22%3Afalse%7D%2C%22pf%22%3A%7B%22value%22%3Afalse%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A12%2C%22pagination%22%3A%7B%22currentPage%22%3A{}%7D%7D".format(pageNumber), headers=headers, timeout=5)

    # Grab the full page
    content = BeautifulSoup(response.content, "html.parser")
    print(content)
    # Get the card links and add to the master list
    currentCardLinks = content.find_all("list-card-link")
    print(currentCardLinks)
    cardLinks.extend(currentCardLinks)


print("--- Writing Links to File ---")
with open('card-links.txt', 'w') as f:
    for link in cardLinks:
        f.write("{} \n".format(link))
