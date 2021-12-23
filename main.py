from datetime import date
from bs4 import BeautifulSoup
import requests
import re
import Bio_Data

from bs4 import BeautifulSoup
from urllib.request import Request, urlopen

req = Request("https://en.wikipedia.org/wiki/Category:21st-century_vice_presidents_of_the_United_States")
html_page = urlopen(req)

soup = BeautifulSoup(html_page, "lxml")
whole_page=soup.find(class_="mw-content-ltr")
links_f=whole_page.find(class_="mw-content-ltr")

links = []
for link in links_f.findAll('a'):
    getting_link="https://en.wikipedia.org"+link.get('href')
    links.append(getting_link)


for i in links:
    html_file = requests.get(i)
    soup=BeautifulSoup(html_file.text,"lxml")
    Bio_Data.csv_file(soup)
