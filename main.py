from bs4 import BeautifulSoup
import requests
import re

html_file=requests.get('https://en.wikipedia.org/wiki/Donald_Trump')
soup = BeautifulSoup(html_file.text, "lxml")

print("Birthday: " + soup.find(class_="bday").text)

# print(soup.find(string="Spouse(s)").parent.parent.prettify())

container=soup.find(string="Spouse(s)")
for thing in container.parent.parent.find(class_="infobox-data").stripped_strings:
    if (re.findall("[a-zA-Z]"))