from bs4 import BeautifulSoup
import requests
from urllib.request import Request, urlopen
from gazpacho import Soup
req = Request("https://www.foxnews.com/category/person/george-w-bush")
html_page = urlopen(req)
soup = BeautifulSoup(html_page, "lxml")
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

# Bill Clinton
mylist2=["https://www.foxnews.com/politics/clinton-says-he-is-on-the-road-to-recovery-in-a-video-update-following-his-hospital-release","https://www.foxnews.com/politics/bill-clinton-released-hospital-southern-california","https://www.foxnews.com/politics/bill-clinton-to-remain-in-hospital-for-antibiotics-expected-to-be-released-tomorrow","https://www.foxnews.com/politics/bill-clinton-hospitalized-with-an-infection","https://www.foxnews.com/politics/bill-clinton-back-in-new-york-after-brief-hospital-stay-in-california"]

with open('fox_news_on_clinton.csv', 'w', encoding='utf-8') as file:
    for i in mylist2:
        req = Request(i)
        html_page = urlopen(req)
        soup = BeautifulSoup(html_page, "lxml")
        f=soup.find('div',class_="article-body")
        s=f.find_all('p')
        for i in s:
            l=i.text
            file.write(str(l))
        print('----------------------')