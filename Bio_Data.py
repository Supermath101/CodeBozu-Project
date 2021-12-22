import pandas as pd
from csv import writer
import re

def csv_file(full_name, birth_date, birth_place, party):
    df=pd.DataFrame({'birth_name':[full_name], 'date of birth':[birth_date], 'birth location':[birth_place], "political party":[party]})
    df.to_csv('information.csv',mode='a', header=False, index=False)
    mylist=[full_name,birth_date,birth_place,party]

def bio_data(soup, soup_to_infobox_data):

    # Birth details
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
    parties = [] # Just in case we find multiple parties, lets display all of them.

    for maybe_party_container in soup.find_all(string="Political party"):
        for maybe_party in soup_to_infobox_data(maybe_party_container):
            for party in re.findall("[A-Z][a-z]+", maybe_party):
                parties.append(party)

    political_party = ", ".join(parties)

    # Birth Full name
    # Try to get a header than personal info
    # regex for (parenthesis)
    birth_full_name=soup.find(id="firstHeading").text
    for name in re.findall("[A-z \\.]+", birth_full_name):
        full_birth_name=name
    

    birth_location=", ".join(birth_towns)
    date_of_birth=", ".join(birth_dates)
    
    #creating csv file
    csv_file(birth_full_name, date_of_birth, birth_location, political_party)

