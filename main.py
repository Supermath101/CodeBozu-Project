from bs4 import BeautifulSoup
import requests
import re

def soup_to_infobox_data(keyword):
    return keyword.parent.parent.find(class_="infobox-data").get_text().splitlines()

html_file=requests.get('https://en.wikipedia.org/wiki/Donald_Trump')
soup = BeautifulSoup(html_file.text, "lxml")

# Birth details

"""
We need the birthday in this type of format 
July 15,1975
"""

birth_towns = []

birth_dates = [] # Just in case we find multiple birth dates, lets display all of them.

for maybe_birth_container in soup.find_all(string="Born"):
    for maybe_birth in soup_to_infobox_data(maybe_birth_container):
        for birth_date in re.findall("[A-Z][a-z]+ \d{1,2}, \d{4}", maybe_birth):
            birth_dates.append(birth_date)
        for birth_town in re.findall("[A-z. ]+, [A-z. ]+, [A-z. ]+", maybe_birth):
            birth_towns.append(birth_town)

# Spouse
spouses = []

for maybe_name_container in soup.find_all(string="Spouse(s)"):
    for maybe_name in soup_to_infobox_data(maybe_name_container):
       for name in re.findall("^[A-z]+ [A-z]+", maybe_name):
            spouses.append(name)


# Political Party
parties = [] # Just in case we find multiple birth dates, lets display all of them.

for maybe_party_container in soup.find_all(string="Political party"):
    for maybe_party in soup_to_infobox_data(maybe_party_container):
        for party in re.findall("[A-Z][a-z]+", maybe_party):
            parties.append(party)

political_party = ", ".join(parties)

# Birth Full name
birth_full_name=soup.find(class_="nickname").text

# Birth Location
"""
This is probably a bug as I think this does not work with everything. Also I need New York, USA as well.
"""

birth_location=", ".join(birth_towns)
date_of_birth=", ".join(birth_dates)

print(birth_full_name,date_of_birth,birth_location,political_party, ", ".join(spouses))