from bs4 import BeautifulSoup
import requests
import re

def soup_to_infobox_data(keyword):
    return keyword.parent.parent.find(class_="infobox-data").stripped_strings

html_file=requests.get('https://en.wikipedia.org/wiki/Donald_Trump')
soup = BeautifulSoup(html_file.text, "lxml")

# Birth Date
birth_dates = [] # Just in case we find multiple birth dates, lets display all of them.

for maybe_birth_date_container in soup.find_all(string="Born"):
    for maybe_birth_date in soup_to_infobox_data(maybe_birth_date_container):
        for birth_date in re.findall("[A-Z][a-z]+ \d{1,2}, \d{4}", maybe_birth_date, re.M):
            birth_dates.append(birth_date)

# Spouses
spouses = []

for maybe_name in soup_to_infobox_data(soup.find(string="Spouse(s)")):
    for name in re.findall("^.+ .+$", maybe_name, re.M):
        spouses.append(name)

print("Spouses: " + ", ".join(spouses))
print("Birth Date: " + ", ".join(birth_dates))

"""
Also I need New York, USA as well.
"""
