from datetime import date
from bs4 import BeautifulSoup
import requests
import csv
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen

east_coast_states=["Maine", "New Hampshire", "Massachusetts", "Rhode Island", "Connecticut", "New York", "New Jersey", "Delaware", "Maryland", "Virginia", "North Carolina", "South Carolina", "Georgia", "Florida"]

file = open('unique_information.csv')
csvreader = csv.reader(file)
birth_area=[]
all_the_people = []
birth_states=[]
people_from_east_coast=0
for row in csvreader:
    all_the_people.append(row)
for birth in all_the_people:
    for cities in east_coast_states:
        if cities in birth[2]:
            # print(cities,birth[0])
            birth_states.append(cities)
            people_from_east_coast+=1
            continue
    # birth_area.append(births[2])
print(people_from_east_coast)
print('----------------')
print(set(birth_states))