import pandas as pd
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import re

#def csv_file(soup):
#    df=pd.DataFrame({'Things':[things(soup)], 'Move':[move(soup)], 'Impact':[impact(soup)], "Upshot":[upshot(soup)]})
#    df.to_csv('politico.csv',mode='a', header=False, index=False)


req = Request("https://www.politico.com/news/magazine/2021/01/18/trump-presidency-administration-biggest-impact-policy-analysis-451479")
html_page = urlopen(req)
soup = BeautifulSoup(html_page, "lxml")
#csv_file(soup)

body_text_info = soup.find_all('p', class_="story-text__paragraph")

#things done works
def things(soup):
    things_done = []
    for thing in soup.find_all('h3', class_="story-text__heading-medium label"):
        things_done.append(thing.text)
    return things_done #returns an ARRAY

#move doesnt work
#def move(info):
#    move_done = [] 
#    for bit in info:
#        if bit.find(string="The move:") != None:
#            print(bit) #still prints the non-containing "The move:" bits; do not know why
#            move_done.append(bit.text.strip("The move:"))

#once move is corrected format can be copied for these as 'info' variable contains these bits as well

#def impact(soup):
#    impact_done = []
#    for impact in soup.find_all('h3', class_="story-text__heading-medium label"):
#        impact_done.append(impact.text)

#def upshot(soup):
#    upshot_done = []
#    for upshot in soup.find_all('h3', class_="story-text__heading-medium label"):
#        upshot_done.append(upshot.text)

#print(move(body_text_info))
