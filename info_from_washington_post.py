from bs4 import BeautifulSoup
import requests
from urllib.request import Request, urlopen
from gazpacho import Soup
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
        if "https://www.washingtonpost.com/politics/" in mj and "https://www.washingtonpost.com/politics/"!=mj and "https://www.washingtonpost.com/politics/courts-law/"!=mj:
            mylist.append(mj)
        if "https://www.washingtonpost.com/immigration/" in mj and "https://www.washingtonpost.com/immigration/"!=mj:
            mylist.append(mj)
        if "https://www.washingtonpost.com/national-security/" in mj and "https://www.washingtonpost.com/national-security/":
            mylist.append(mj)
all_the_links = []
for x in mylist:
    if x not in all_the_links:
        all_the_links.append(x)
print(all_the_links)
print(len(all_the_links))
with open('washington_post_on_trump.csv', 'w', encoding='utf-8') as file:
    for i in all_the_links:
        req = Request(i)
        html_page = urlopen(req)
        soup = BeautifulSoup(html_page, "lxml")
        g=soup.find('div',class_="article-body")
        j=g.find_all('div', attrs={'class': None})
        for i in j:
            l=i.text
            print(l)
            file.write(str(l))
            file.write('\n')
file.close()

"""
with open('washington_post_on_trump', 'w', encoding='utf-8') as file:
    for i in all_the_links:
        req = Request(i)
        html_page = urlopen(req)
        soup = BeautifulSoup(html_page, "lxml")
        g=soup.find('div',class_="article-body")
        j=g.find_all('div', attrs={'class': None})
        """