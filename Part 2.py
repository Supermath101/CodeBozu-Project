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

body_text_info = soup.find_all('p', class_="story-text__paragraph")

#Extracting the things done
def things(soup):
    things_done = []
    for thing in soup.find_all('h3', class_="story-text__heading-medium label"):
        #adding each string to the array
        things_done.append(thing.text)
    return things_done #returns an ARRAY

#Extracting the moves made
def move(info):
    move_done = [] 
    for bit in info:
        result = re.search(r"(?:The move:)(.*)", bit.text)
        if result != None:
            #adding each string to the array
            move_done.append(result.group().replace("The move: ", ''))
    return move_done #returns an ARRAY
 
#problem - one bit contains a couple of 'The move:' s and it is placed separately into the array, not grouped together.


#Extracting the impacts made
def impact(info):
    impact_done = [] 
    for bit in info:
        result = re.search(r"(?:The impact:)(.*)", bit.text)
        if result != None:
            #adding each string to the array.
            impact_done.append(result.group().replace("The impact: ", ''))
    return impact_done #returns an ARRAY

#Extracting the upshots made
def upshot(info):
    upshot_done = [] 
    for bit in info:
        result = re.search(r"(?:The upshot:)(.*)", bit.text)
        if result != None:
            #Finding the writers name in the data
            writer = bit.find('i').text
            #cleaning each string up and adding it to the array.
            upshot_done.append(result.group().replace("The upshot: ", '').strip(writer))
    return upshot_done #returns ARRAY
        
#printing the upshots_done array (testing the program)
print(upshot(body_text_info))
#csv_file(soup)