from datetime import date
from bs4 import BeautifulSoup
import csv
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen

east_coast_states=["Maine", "New Hampshire", "Massachusetts", "Rhode Island", "Connecticut", "New York", "New Jersey", "Delaware", "Maryland", "Virginia", "North Carolina", "South Carolina", "Georgia", "Florida"]
west_coast_states=["California","Oregon","Washington","Alaska","Hawaii"]
folder = "Bio data"

file = open(folder + "/" + 'unique_information.csv')
csvreader = csv.reader(file)
birth_area=[]
all_the_people = []
people_from_east_coast=0
people_from_west_coast=0
for row in csvreader:
    all_the_people.append(row)
for birth in all_the_people:
    for cities in east_coast_states:
        if cities in birth[2]:
            people_from_east_coast+=1

for birth in all_the_people:
    for cities in west_coast_states:
        if cities in birth[2]:
            people_from_west_coast+=1
print(people_from_east_coast)
print(people_from_west_coast)