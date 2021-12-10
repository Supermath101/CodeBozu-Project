from bs4 import BeautifulSoup
import requests
import re

html_file=requests.get('https://en.wikipedia.org/wiki/Donald_Trump')
soup = BeautifulSoup(html_file.text, "lxml")

# Birthday
print("Birthday: " + soup.find(class_="bday").text)

# Spouse
spouses = []

container=soup.find(string="Spouse(s)")
for maybe_name in container.parent.parent.find(class_="infobox-data").stripped_strings:
    for name in re.findall("^.+ .+$", maybe_name, re.M):
        spouses.append(name)

print("Spouses: " + ", ".join(spouses))
# Political Party
political_party=soup.find('div',class_='plainlist')
print(political_party.text)
