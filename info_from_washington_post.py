from bs4 import BeautifulSoup
import requests
from urllib.request import Request, urlopen
from gazpacho import soup
req = Request("https://www.washingtonpost.com/45th-president/")
html_page = urlopen(req)
soup = BeautifulSoup(html_page, "lxml")
# print(soup)
f=soup.find('div',class_="chain-content no-skin")
m=f.find_all("a")
mylist=[]
for link in m:
    if 'href' in link.attrs:
        mj=str(link.attrs['href'])
        if "https://www.washingtonpost.com/politics/" in mj and "https://www.washingtonpost.com/politics/"!=mj:
            mylist.append(mj)
        if "https://www.washingtonpost.com/immigration/" in mj:
            mylist.append(mj)
        if "https://www.washingtonpost.com/national-security/" in mj:
            mylist.append(mj)
all_the_links = []
for x in mylist:
    if x not in all_the_links:
        all_the_links.append(x)
all_the_links=["https://www.washingtonpost.com/politics/trump-executive-orders/2020/10/29/c2329162-17bd-11eb-aeec-b93bcc29a01b_story.html"]
for i in all_the_links:
    req = Request(i)
    html_page = urlopen(req)
    soup = BeautifulSoup(html_page, "lxml")
    g=soup.find('div',class_="article-body")
    f=g.find_all('div',class_="")
    print [item["data-qa"] for item in bs.find_all() if "data-qa" in item.attrs]