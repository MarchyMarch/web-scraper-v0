from bs4 import BeautifulSoup
import time
from datetime import datetime
from random import uniform, randint
import requests

# Randomization
MIN_RAND = 1.5
MAX_RAND = 2

headers = {
	"Host": "www.realtor.com",
	"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:80.0) Gecko/20100101 Firefox/80.0",
	"Accept": "*/*",
	"Accept-Language": "en-US,en;q=0.5",
	"Accept-Encoding": "gzip, deflate, br"
}

url = "https://www.realtor.com/realestateandhomes-detail/1170-Sacramento-St-Apt-4A_San-Francisco_CA_94108_M16435-50122"

response = requests.get(url, headers=headers, timeout=5)

content = BeautifulSoup(response.content, "html.parser")
body = content.body

with open("body.txt", "w") as f:
	for line in body:
		f.write("{}\n".format(line))