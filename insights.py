from datetime import date
from bs4 import BeautifulSoup
import requests
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
req = Request('https://en.wikipedia.org/wiki/East_Coast_of_the_United_States')
html_page = urlopen(req)
def soup_to_infobox_data(keyword):
    return keyword.parent.parent.find(class_="infobox-data")

soup = BeautifulSoup(html_page, "lxml")
cities=[]
east_coast_cities=[]
for i in soup.find_all(string="Principal cities"):
    for maybe_birth in soup_to_infobox_data(i):
        cities.append(maybe_birth)
while ' ' in cities:
    cities.remove(' ')
for i in cities:
    east_coast_cities.append(i.text)
while '' in east_coast_cities:
    east_coast_cities.remove('')
print(east_coast_cities)