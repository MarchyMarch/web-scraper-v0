from bs4 import BeautifulSoup
import time
from datetime import datetime
from random import uniform, randint
import requests

# Randomization
MIN_RAND = 0.67
MAX_RAND = 1.26

def smallSleep():
	rand = uniform(MIN_RAND, MAX_RAND)
	time.sleep(rand)

print("----- Begin Algorithm -----")

# Define fake URL headers
headers = {
	"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36" ,'referer':'https://www.google.com/','Accept-Encoding': 'identity'
}

cardLinks = []
currentURLs = []
toGrabURLs = []

print("----- Grabbing URLs ---")

with open("urls-to-scrape.txt", "r") as f:
	for line in f:
		strippedLine = line.strip()
		currentURLs.append(strippedLine)


print("----- Requesting URLs -----")
for url in currentURLs:

	response = requests.get(url, headers=headers, timeout=5)

	content = BeautifulSoup(response.content, "html.parser")
	body = content.body

	toProcess = body.find_all(attrs={"data-testid":"property-anchor"}, href=True)

	if toProcess == []:
		toGrabURLs.append(url)
	else:
		for currentCardLinks in toProcess:
			cardLinks.append(currentCardLinks['href'])

	smallSleep()


print("----- Saving Card URLs ----")
with open("card-urls.txt", "a") as f:
	for url in cardLinks:
		f.write("{}\n".format(url))

print("----- Saving Remaining URLs -----")
with open("urls-to-scrape.txt", "w") as f:
	for url in toGrabURLs:
		f.write("{}\n".format(url))