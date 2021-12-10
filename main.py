from bs4 import BeautifulSoup
import requests
import re

html_file=requests.get('https://en.wikipedia.org/wiki/Donald_Trump')
soup = BeautifulSoup(html_file.text, "lxml")

# Birthday
date_of_birth=soup.find(class_="bday").text
# print("Birthday: " + soup.find(class_="bday").text)
"""
We need it in this type of format 
July 15,1975
"""
# Spouse
spouses = []

container=soup.find(string="Spouse(s)")
for maybe_name in container.parent.parent.find(class_="infobox-data").stripped_strings:
    for name in re.findall("^.+ .+$", maybe_name, re.M):
        spouses.append(name)

# print("Spouses: " + ", ".join(spouses))


# Political Party
political_party=soup.find('div',class_='plainlist').text

# Politicians
politician=soup.find('div',class_='fn').text

# Birth Full name
birth_full_name=soup.find('div',class_="nickname").text

# Birth Location
"""
This is probably a bug as I think this does not work with everything. Also I need New York, USA as well.
"""

birth_location=soup.find('a',title="Queens").text

print(politician, birth_full_name,date_of_birth,birth_location,political_party)