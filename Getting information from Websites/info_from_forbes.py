import os
from csv import writer
import requests
from bs4 import BeautifulSoup as bsoup
from urllib.request import urlopen
from sentiment_functions import writing_to_file
import re

links = ["https://www.forbes.com/search/?q=trump&sh=5b7d3f4c279f", "https://www.forbes.com/search/?q=biden&sh=64e1c236279f",
"https://www.forbes.com/search/?q=obama&sh=64e1c236279f", "https://www.forbes.com/search/?q=bush&sh=64e1c236279f",
"https://www.forbes.com/search/?q=bill%20clinton&sh=64e1c236279f"]
files = ["forbes_trump.csv", "forbes_biden.csv", "forbes_obama.csv", "forbes_w_bush.csv", "forbes_clinton.csv"]
folder = "Info from Forbes"

def calculate_average(positivity, count):
    average = round(positivity/count,2) #float format
    average_string = str(average) + "%" #string format
    averages.append(average_string)
    return averages

if not os.path.exists(folder):
    os.makedirs(folder)

averages = []

for link_page in range(0, len(links)):
    positivity = 0
    count = 0
    html_page = urlopen(links[link_page])
    soup = bsoup(html_page, "lxml")
    links_edit = soup.findAll("a", class_= "stream-item__title")
    with open(folder + "/" + files[link_page], 'w', encoding='utf-8') as file:
        for link in links_edit:
            getting_link = link.get('href')
            if re.search(r"(?:https://www.forbes.com/video)(.*)", getting_link) == None:
                html_page = requests.get(getting_link)
                soup = bsoup(html_page.text, "lxml")
                title = soup.find("h1", class_="fs-headline speakable-headline font-base font-size")        
                body_text = soup.findAll("p")
                if title != None and body_text != None:
                    positivity += writing_to_file(title, body_text, file)
                    count += 1
        # mean used to calculate the average positivity score for the current link page
        if count != 0:
            averages = calculate_average(positivity, count)
        else:
            print(positivity, file) #check
    file.close()

presidents = ["Donald Trump", "Joe Biden", "Barack Obama", "George W. Bush", "Bill Clinton"]
file = open("Heatmap" + "/" + "averages_forbes.txt", "w")
for i in range (0, len(averages)):
    file.write(presidents[i] + ", " + averages[i] + "\n")
file.close()
    

#cleaning ending "forbes" check if files are clean