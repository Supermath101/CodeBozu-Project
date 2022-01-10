import pandas as pd
from csv import writer
import requests
from bs4 import BeautifulSoup as bsoup
from urllib.request import urlopen
from sentiment_functions import writing_to_file

links = ["https://www.huffpost.com/news/topic/donald-trump", "https://www.huffpost.com/news/topic/joe-biden", 
"https://www.huffpost.com/news/topic/barack-obama", "https://www.huffpost.com/news/topic/george-w-bush", 
"https://www.huffpost.com/news/topic/bill-clinton"]

files = ["huff_post_trump.csv","huff_post_biden.csv","huff_post_obama.csv", "huff_post_w_bush.csv", "huff_post_clinton.csv"]


def calculate_average(positivity, count):
    average = round(positivity/count,2) #float format
    average_string = str(average) + "%" #string format
    averages.append(average_string)
    return averages

averages = []
for link_page in range(0, len(links)):
    html_page = urlopen(links[link_page])
    soup = bsoup(html_page, "lxml")
    links_in_page = soup.findAll("a", class_="card__headline card__headline--long")
    
    with open(files[link_page], 'w', encoding='utf-8') as file:
        positivity = 0
        count = 0
        for link in links_in_page:
            getting_link = link.get('href')
            html_page = requests.get(getting_link)
            soup = bsoup(html_page.text, "lxml")

            title = soup.find("h1", class_="headline")
            body_text = soup.findAll(("p"))
            
            if title != None and body_text != None and body_text != []:
                positivity += writing_to_file(title, body_text, file)
                count += 1

        # mean used to calculate the average positivity score for the current link page
        averages = calculate_average(positivity, count)


    file.close()


presidents = ["Donald Trump", "Joe Biden", "Barack Obama", "George W. Bush", "Bill Clinton"]
file = open("averages_huff_post.txt", "w")
for i in range (0, len(averages)):
    file.write(presidents[i] + ", " + averages[i] + "\n")
file.close()



#clean data and csv files
