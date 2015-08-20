import urllib2
from bs4 import BeautifulSoup

url = "http://dolarhoje.com"
capture = urllib2.urlopen(url)
reading = capture.read()
soup = BeautifulSoup(reading)
todasTags = soup.findAll("input", {"id": "nacional"})
valorDolar = todasTags[0]['value']

print valorDolar

