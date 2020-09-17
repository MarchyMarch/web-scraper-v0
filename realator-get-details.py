from bs4 import BeautifulSoup
import time
from datetime import datetime
from random import uniform, randint
import requests

# Randomization
MIN_RAND = 1.57
MAX_RAND = 2.06

def smallSleep():
	rand = uniform(MIN_RAND, MAX_RAND)
	time.sleep(rand)

def saveData(cardLinks, toGrabURLs):
	print("\n----- Saving Card URLs ----")
	print("----- Saving {} new Detail URLs -----\n".format(len(cardLinks)))
	with open("card-urls.txt", "a") as f:
		for url in cardLinks:
			f.write("{}\n".format(url))

	print("\n----- Saving Remaining URLs -----")
	print("----- {} URLs left to process\n".format(len(toGrabURLs)))
	with open("urls-to-scrape.txt", "w") as f:
		for url in toGrabURLs:
			f.write("{}\n".format(url))

print("----- Begin Algorithm -----")

# Define fake URL headers
headers = {
	"Host": "www.realtor.com",
	"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:80.0) Gecko/20100101 Firefox/80.0",
	"Accept": "*/*",
	"Accept-Language": "en-US,en;q=0.5",
	"Accept-Encoding": "gzip, deflate, br",
	"newrelic": "eyJ2IjpbMCwxXSwiZCI6eyJ0eSI6IkJyb3dzZXIiLCJhYyI6IjM3ODU4NCIsImFwIjoiMTI5NzQxMzUyIiwiaWQiOiI4N2Y3YjMyMTk2OWIwY2Q5IiwidHIiOiJmMGI2Y2U0MmMxZjIyZjY1OTY2OWZmNTAzNjAwYmQyMCIsInRpIjoxNjAwMzE2MzUwMzQyLCJ0ayI6IjEwMjI2ODEifX0=",
	"traceparent": "00-f0b6ce42c1f22f659669ff503600bd20-87f7b321969b0cd9-01",
	"tracestate": "1022681@nr=0-1-378584-129741352-87f7b321969b0cd9----1600316350342",
	"Referer": "https://www.realtor.com/",
	"Connection": "keep-alive",
	"Cookie": "_ga=GA1.2.1921865780.1600316015; _gid=GA1.2.309379420.1600316015; split=n; split_tcv=184; __vst=585aa359-9ee8-49bc-8749-adf07e3fe921; __ssn=f4594f0e-310c-4848-8d1b-0a227306b937; __ssnstarttime=1600316345; __split=53; AMCV_8853394255142B6A0A4C98A4%40AdobeOrg=-432600572%7CMCIDTS%7C18523%7CMCMID%7C38859161362436391571890889863313886485%7CMCAAMLH-1600921145%7C9%7CMCAAMB-1600921145%7C6G1ynYcLPuiQxYZrsz_pkqfLG9yMXBpb2zX5dvJdYQJzPXImdj0y%7CMCOPTOUT-1600323545s%7CNONE%7CMCAID%7CNONE%7CMCSYNCSOP%7C411-18530%7CvVersion%7C4.5.2; ab.storage.userId.7cc9d032-9d6d-44cf-a8f5-d276489af322=%7B%22g%22%3A%22visitor_585aa359-9ee8-49bc-8749-adf07e3fe921%22%2C%22c%22%3A1600316345382%2C%22l%22%3A1600316345382%7D; ab.storage.sessionId.7cc9d032-9d6d-44cf-a8f5-d276489af322=%7B%22g%22%3A%2290af1b81-b235-1b24-e2b5-876ba212229e%22%2C%22e%22%3A1600318145385%2C%22c%22%3A1600316345385%2C%22l%22%3A1600316345385%7D; ab.storage.deviceId.7cc9d032-9d6d-44cf-a8f5-d276489af322=%7B%22g%22%3A%224d54f9c4-fa33-ff78-c27f-671c8561d172%22%2C%22c%22%3A1600316345388%2C%22l%22%3A1600316345388%7D; AMCVS_8853394255142B6A0A4C98A4%40AdobeOrg=1; ajs_anonymous_id=%22a113b375-b2ca-4204-aa77-6d1372aef93f%22; G_ENABLED_IDPS=google; s_ecid=MCMID%7C38859161362436391571890889863313886485; QSI_HistorySession=https%3A%2F%2Fwww.realtor.com%2F~1600316345998; _uetsid=0566c3cf0b529035533834a01e0163a2; _uetvid=d0d36798b2805e987ce55fe1c62a009c; reese84=3:9tzcRHlElewlHlDO5DXONA==:PHeNlv8oX5Fj/d5zhXZb0wZKZ60W8FV6kn3i5BasyN8u4NbiEC6u0C1oSul0C4lnWBSuKPxPL9G4Ax331/MoKCq2+2Tky3kfSv2kb3y1nq6KgB9K2EP8mRsnKSIn4uKQ1fD35otu7DqBJ4A5kk4MjJrQL4wnx6Zzlo/i8Q6CvwYb65Q3wh12uTNtXoUVvzraRQgogCjUY3EUzzaV+4T1nS7oftm4ZC47nLgYutoUZrhovKtd/6f9ORi2jdTgU10EiNqBzTi2EyLgC3bUBgBK9A1pAP4UYbEZmL6eTkOcp0uIWPssiWlPepf7Zf5BiSa7S+d1QweIdPQtLPDblFrDzRjd4cyRTWxADz0TR6rM1/hpkzqESH3k40DdLfySdNPJphcwkRJr2iCsjR2wba3hoEstOvxNIlfXDx9rvX68ww0=:msye8dL4akZZI+90cApgVZSvt1O80gRPS5F4LhvpteI=; _gat=1; adcloud={%22_les_v%22:%22y%2Crealtor.com%2C1600318146%22}; _tac=false~self|not-available; _ta=us~1~89df68bc35032d48c293adce8574aa42; _tas=h861oe8rmi9; _ncg_sp_ses.cc72=*; _ncg_sp_id.cc72=f2b82e8a-fdc1-4495-978f-b3adab5eb3fc.1600316347.1.1600316348.1600316347.b720b6bb-f8e3-4069-8d28-c176f9a74d81; _ncg_id_=f2b82e8a-fdc1-4495-978f-b3adab5eb3fc; __qca=P0-1753274372-1600316347420",
	"If-None-Match": "59a6a-m8F6+EX7QgWekMQRi31BiazcGO8",
	"TE": "Trailers"
}

proxies = []

##########################
###### PROXY LOADING #####
##########################

# Load in proxies from file
print("\n----- Loading HTTP Proxies -----")
with open("proxies.txt", "r") as f:
	for line in f:
		strippedLine = line.strip()
		proxies.append(strippedLine)

# Make sure we have a proxy
if proxies == []:
	print("----- No More Proxies!!! -----")
	quit()

while proxies != []:
	cardLinks = []
	currentURLs = []
	toGrabURLs = []

	# Grab the first proxy to use
	currentProxy = "http://" + proxies[0]


	print("----- Current Proxy is {} -----".format(currentProxy))

	proxyDict = {
		"http" : currentProxy
	}

	# Save the remaining proxies for future use
	with open("proxies.txt", "w") as f:
		for proxyURL in proxies:
			f.write("{}\n".format(proxyURL))

	#####################
	##### LOAD URLS #####
	#####################
	print("\n----- Grabbing URLs ---")

	with open("urls-to-scrape.txt", "r") as f:
		for line in f:
			strippedLine = line.strip()
			currentURLs.append(strippedLine)

	print("----- {} URLs to Scrape ------\n".format(len(currentURLs)))

	#######################
	##### SCRAPE URLS #####
	#######################
	print("----- Requesting URLs -----")
	count = 0
	attempts = 0
	for url in currentURLs:
		smallSleep()
		response = requests.get(url, headers=headers, proxies=proxyDict, timeout=30)

		content = BeautifulSoup(response.content, "html.parser")
		body = content.body

		toProcess = body.find_all(attrs={"data-testid":"property-anchor"}, href=True)

		if toProcess == []:
			toGrabURLs.append(url)
		else:
			for currentCardLinks in toProcess:
				cardLinks.append(currentCardLinks['href'])

		count += 1
		newDetailCount = len(cardLinks)
		if (count % 10) == 0:
			print("----- 10 URLs Requested - {} new Detail URLs".format(newDetailCount))


	#####################
	##### SAVE DATA #####
	#####################
	saveData(cardLinks, toGrabURLs)

	proxies.pop(0)