from bs4 import BeautifulSoup
import requests
import time

from random import uniform

from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from fake_useragent import UserAgent


# url = 'http://ethans_fake_twitter_site.surge.sh/'
# response = requests.get(url, timeout=5)
# content = BeautifulSoup(response.content, "html.parser")
# print("\n\n------------- content --------------------\n\n")
# print(content)

# url2 = 'https://www.zillow.com/homes/for_rent/San-Francisco,-CA_rb/'
# response2 = requests.get(url2, timeout=5)
# content2 = BeautifulSoup(response2.content, "html.parser")
# print("\n\n------------- content2 --------------------\n\n")
# print(content2)

#Randimization
MIN_RAND = 0.69
MAX_RAND = 1.34
LONG_MIN_RAND = 4.20
LONG_MAX_RAND = 11.13

def smallSleep():
	rand = uniform(MIN_RAND, MAX_RAND)
	time.sleep(rand)

# pageNumber = 2
# print("https://www.zillow.com/homes/San-Francisco,-CA_rb/?searchQueryState=%7B%22usersSearchTerm%22%3A%22San%20Francisco%2C%20CA%22%2C%22mapBounds%22%3A%7B%22west%22%3A-122.83810652685547%2C%22east%22%3A-122.21669234228516%2C%22south%22%3A37.70911569603537%2C%22north%22%3A37.84832142027793%7D%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A20330%2C%22regionType%22%3A6%7D%5D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22pmf%22%3A%7B%22value%22%3Afalse%7D%2C%22pf%22%3A%7B%22value%22%3Afalse%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A12%2C%22pagination%22%3A%7B%22currentPage%22%3A{}%7D%7D".format(2))

print("----- Start Scraping -----")
# options = Options()
# ua = UserAgent()
# userAgent = ua.random

# print(userAgent)

# options.add_argument(f'user-agent={userAgent}')
# browser = webdriver.Chrome(ChromeDriverManager().install(), options=options)

headers = {
	'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36',
}

for pageNumber in range(15):
	print("-- Page Number {} ---".format(pageNumber))
	response = requests.get("https://mercadopartners.com")
	if pageNumber == 0:
		pass
	elif pageNumber == 1:
		response = requests.get("https://www.zillow.com/homes/San-Francisco,-CA_rb/?searchQueryState=%7B%22usersSearchTerm%22%3A%22San%20Francisco%2C%20CA%22%2C%22mapBounds%22%3A%7B%22west%22%3A-122.83810652685547%2C%22east%22%3A-122.21669234228516%2C%22south%22%3A37.70911569603537%2C%22north%22%3A37.84832142027793%7D%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A20330%2C%22regionType%22%3A6%7D%5D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22pmf%22%3A%7B%22value%22%3Afalse%7D%2C%22pf%22%3A%7B%22value%22%3Afalse%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A12%7D", headers=headers, timeout=5)
	else:
		response = requests.get("https://www.zillow.com/homes/San-Francisco,-CA_rb/?searchQueryState=%7B%22usersSearchTerm%22%3A%22San%20Francisco%2C%20CA%22%2C%22mapBounds%22%3A%7B%22west%22%3A-122.83810652685547%2C%22east%22%3A-122.21669234228516%2C%22south%22%3A37.70911569603537%2C%22north%22%3A37.84832142027793%7D%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A20330%2C%22regionType%22%3A6%7D%5D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22pmf%22%3A%7B%22value%22%3Afalse%7D%2C%22pf%22%3A%7B%22value%22%3Afalse%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A12%2C%22pagination%22%3A%7B%22currentPage%22%3A{}%7D%7D".format(pageNumber), headers=headers, timeout=5)
#	smallSleep()

#	print("----- Grabbing Listings ----")

	content = BeautifulSoup(response.content, "html.parser")
#	listingObjs = browser.find_elements_by_class_name("list-card-info")

	with open('listingObjs-0{}.txt'.format(pageNumber), 'w') as f:
		f.write(str(content))

# listingHREFs = [listing.get_attribute("href") for listing in listingObjs]

# print("----- Finished HREF Listings Writing to File ----")

# with open('listingHREFs.txt', 'w') as f:
# 	for listing in listingHREFs:
# 		f.write("%s\n" % listing)

# print("----- Finished Scraping -----")

# browser.quit()