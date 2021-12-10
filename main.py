from bs4 import BeautifulSoup
import requests
import re

html_file=requests.get('https://en.wikipedia.org/wiki/Donald_Trump')
soup = BeautifulSoup(html_file.text, "lxml")

print("Birthday: " + soup.find(class_="bday").text)

# print(soup.find(string="Spouse(s)").parent.parent.prettify())

mylist=[]
container=soup.find(string="Spouse(s)")
print(container)

print(container.parent.parent.find(class_="infobox-data").text)