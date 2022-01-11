from bs4 import BeautifulSoup
import requests
from urllib.request import Request, urlopen
from gazpacho import Soup
req = Request("https://www.foxnews.com/category/person/donald-trump")
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

print(mylist2)