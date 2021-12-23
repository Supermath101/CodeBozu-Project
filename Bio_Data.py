import pandas as pd
from csv import writer
# import csv
import re

def soup_to_infobox_data(keyword):
    return keyword.parent.parent.find(class_="infobox-data").get_text().splitlines()

def csv_file(soup):
    df=pd.DataFrame({'birth_name':[birth_full_name(soup)], 'date of birth':[date_of_birth(soup)], 'birth location':[birth_location(soup)], "political party":[political_party(soup)]})
    df.to_csv('information.csv',mode='a', header=False, index=False)

def date_of_birth(soup):
    birth_dates = []
    for maybe_birth_container in soup.find_all(string="Born"):
        for maybe_birth in soup_to_infobox_data(maybe_birth_container):
            for birth_date in re.findall("[A-Z][a-z]+ \d{1,2}, \d{4}", maybe_birth):
                birth_dates.append(birth_date)
    date_of_birth=", ".join(birth_dates)
    return date_of_birth

def birth_location(soup):
    birth_towns = [] 
    for maybe_birth_container in soup.find_all(string="Born"):
        for maybe_birth in soup_to_infobox_data(maybe_birth_container):
            first=re.sub('(.*?)(\d)', '', maybe_birth)
            if first[0]==")":
                birth_towns.append(first[1::])
            else:
                birth_towns.append(first)
    birth_location=", ".join(birth_towns)
    return birth_location

def spouses(soup):
    spouses = []
    for maybe_name_container in soup.find_all(string="Spouse(s)"):
        for maybe_name in soup_to_infobox_data(maybe_name_container):
            for name in re.findall("^[A-z]+ [A-z]+", maybe_name):
                    spouses.append(name)
    return spouses

def political_party(soup):
    # Political Party
    parties = [] # Just in case we find multiple parties, lets display all of them.
    for maybe_party_container in soup.find_all(string="Political party"):
        for maybe_party in soup_to_infobox_data(maybe_party_container):
            for party in re.findall("[A-Z][a-z]+", maybe_party):
                parties.append(party)
    political_party = ", ".join(parties)
    return political_party

def birth_full_name(soup):
    birth_name=soup.find(id="firstHeading").text
    return birth_name