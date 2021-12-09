from bs4 import BeautifulSoup
import requests

html_file=requests.get('https://en.wikipedia.org/wiki/Donald_Trump')
soup = BeautifulSoup(html_file.text, "lxml")

print("Birthday: " + soup.find(class_="bday").text)