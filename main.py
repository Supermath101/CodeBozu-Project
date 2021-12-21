from datetime import date
from bs4 import BeautifulSoup
import requests
import re
import pandas as pd
from csv import writer

def soup_to_infobox_data(keyword):
    return keyword.parent.parent.find(class_="infobox-data").get_text().splitlines()


from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import re

req = Request("https://en.wikipedia.org/wiki/Category:20th-century_vice_presidents_of_the_United_States")
html_page = urlopen(req)

soup = BeautifulSoup(html_page, "lxml")
whole_page=soup.find(class_="mw-content-ltr")
links_f=whole_page.find(class_="mw-content-ltr")

links = []
for link in links_f.findAll('a'):
    getting_link="https://en.wikipedia.org"+link.get('href')
    links.append(getting_link)


# Birth details
for i in links:
    html_file = requests.get(i)
    soup=BeautifulSoup(html_file.text,"lxml")
    birth_towns = []

    birth_dates = [] # Just in case we find multiple birth dates, lets display all of them.

    for maybe_birth_container in soup.find_all(string="Born"):
        for maybe_birth in soup_to_infobox_data(maybe_birth_container):
            for birth_date in re.findall("[A-Z][a-z]+ \d{1,2}, \d{4}", maybe_birth):
                birth_dates.append(birth_date)
            for birth_town in re.findall("[A-z., ]+U\\.S\\.", maybe_birth):
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
    # Try to get a header than personal info
    # regex for (parenthsis)
    birth_full_name=soup.find(id="firstHeading").text
    for name in re.findall("[A-z \\.]+", birth_full_name):
        full_birth_name=name
    # Birth Location
    """
    This is probably a bug as I think this does not work with everything. Also I need New York, USA as well.
    """

    birth_location=", ".join(birth_towns)
    date_of_birth=", ".join(birth_dates)

    df=pd.DataFrame({'birth_name':[birth_full_name], 'date of birth':[date_of_birth], 'birth location':[birth_location], "political party":[political_party]})
    # print(df)
    df.to_csv('information.csv',mode='a', header=False, index=False)
    mylist=[birth_full_name,date_of_birth,birth_location,political_party]


# feature a
# feature b               but  buugs 