import csv
from bs4 import BeautifulSoup
import requests
html_file = requests.get('https://en.wikipedia.org/wiki/East_Coast_of_the_United_States')
soup=BeautifulSoup(html_file.text,"lxml")
# print(soup)
with open('information.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    republican=0
    democratic=0
    independent=0
    others=0
    for i in csv_reader:
        if i[3]=="Independent":
            independent+=1
        elif i[3]=="Democratic":
            democratic+=1
        elif i[3]=="Republican":
            republican+=1
        else:
            parties_list=i[3].split(',')
            if parties_list[-1]==" Independent":
                independent+=1
            elif parties_list[-1]==" Democratic":
                democratic+=1
            elif parties_list[-1]==" Republican":
                republican+=1
            else:
                others+=1
print(independent)
print(democratic)
print(republican)
# because i do not want to include the first line.
print(others-1)