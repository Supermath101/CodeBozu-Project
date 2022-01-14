import os
from bs4 import BeautifulSoup as bsoup
from urllib.request import urlopen
from sentiment_functions import writing_to_file
import re


links = ["https://www.foxnews.com/category/person/donald-trump", "https://www.foxnews.com/category/person/joe-biden", "https://www.foxnews.com/category/person/barack-obama", "https://www.foxnews.com/category/person/george-w-bush"]
files = ["fox_news_on_trump.csv", "fox_news_on_biden.csv", "fox_news_on_obama.csv", "fox_news_on_bush.csv"]
folder = "Info from Fox News"

def calculate_average(positivity, count):
    average = round(positivity/count,2) #float format
    average_string = str(average) + "%" #string format
    averages.append(average_string)
    return averages


def links_on_page(soup):
    mylist=[]
    f=soup.find('div',class_="content article-list")
    j=f.find_all('article',class_="article")
    for i in j:
        s=i.find('div',class_="m")
        g=s.find('a')
        mylist.append(g)
    mylist1=[]
    for link in mylist:
        mm=str(link)
        if 'href' in link.attrs:
            mj=str(link.attrs['href'])
            mylist1.append(mj)

    for s in mylist1:
        if s[0]!="/":
            mylist1.remove(s)
    mylist2=[]
    for i in mylist1:
        f="https://www.foxnews.com"+i
        mylist2.append(f)
    return mylist2


if not os.path.exists(folder):
    os.makedirs(folder)


averages = []
for link_page in range(0, len(links)):
    html_page = urlopen(links[link_page])
    soup = bsoup(html_page, "lxml")
    link_list = links_on_page(soup)
    
    with open(folder + "/" + files[link_page], 'w', encoding='utf-8') as file:
        positivity = 0
        count = 0
        for i in link_list:
            if re.search(r"(?:video)(.*)", i) == None:
                html_page = urlopen(i)
                soup = bsoup(html_page, "lxml")
                t = soup.find('h1', class_= "headline")
                f = soup.find('div',class_="article-body")
                s = f.find_all('p')
                positivity += writing_to_file(t, s, file)
                count += 1
        # mean used to calculate the average positivity score
        averages = calculate_average(positivity, count)
    file.close()




# Bill Clinton - no overall link
mylist2=["https://www.foxnews.com/politics/clinton-says-he-is-on-the-road-to-recovery-in-a-video-update-following-his-hospital-release","https://www.foxnews.com/politics/bill-clinton-released-hospital-southern-california","https://www.foxnews.com/politics/bill-clinton-to-remain-in-hospital-for-antibiotics-expected-to-be-released-tomorrow","https://www.foxnews.com/politics/bill-clinton-hospitalized-with-an-infection","https://www.foxnews.com/politics/bill-clinton-back-in-new-york-after-brief-hospital-stay-in-california"]


with open(folder + "/" + "fox_news_on_clinton.csv", "w", encoding = "utf-8") as file:
    positivity = 0
    count = 0
    for i in mylist2:
        html_page = urlopen(i)
        soup = bsoup(html_page, "lxml")
        section = soup.find('div',class_="article-body")
        title = soup.find('h1', class_= "headline")
        body_text = section.find_all('p')
        positivity += writing_to_file(title, body_text, file)
        count += 1     
    averages = calculate_average(positivity, count)
file.close()


presidents = ["Donald Trump", "Joe Biden", "Barack Obama", "George W. Bush", "Bill Clinton"]
file = open("Heatmap" + "/" + "averages_fox_news.txt", "w")
for i in range (0, len(averages)):
    file.write(presidents[i] + ", " + averages[i] + "\n")
file.close()