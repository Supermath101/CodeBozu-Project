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
#Obama
# all_the_links=["https://www.washingtonpost.com/news/book-party/wp/2016/12/15/the-self-referential-presidency-of-barack-obama/","https://www.washingtonpost.com/outlook/2021/05/11/leave-barack-obama-alone/","https://www.washingtonpost.com/lifestyle/style/obama-clinton-book-podcast/2021/03/05/beef7224-7b6b-11eb-85cd-9b7fa90c8873_story.html","https://www.washingtonpost.com/politics/obama-struggling-with-immigration-rules-and-cruelties-of-deportation/2016/01/18/5c2d4258-bba7-11e5-b682-4bb4dd403c7d_story.html","https://www.washingtonpost.com/politics/a-crisis-of-confidence-how-the-success-of-obamas-deferred-action-program-for-illegal-immigrants-could-lead-to-its-demise/2017/08/31/94c75ae4-8e3d-11e7-91d5-ab4e4bb76a3a_story.html"]
#Biden
# all_the_links=["https://www.washingtonpost.com/politics/biden-speech-jan6/2022/01/06/20a7c56e-6f1a-11ec-b9fc-b394d592a7a6_story.html","https://www.washingtonpost.com/climate-environment/2022/01/09/energy-efficiency-climate-change-biden/","https://www.washingtonpost.com/national-security/2022/01/03/navy-seals-vaccine-mandate-lawsuit/"]
#George w bush
# all_the_links=["https://www.washingtonpost.com/national-security/2022/01/03/navy-seals-vaccine-mandate-lawsuit/","https://www.washingtonpost.com/news/reliable-source/wp/2017/07/14/presidents-bush-and-clinton-appear-to-offer-trump-some-advice-without-mentioning-his-name/","https://www.washingtonpost.com/news/the-fix/wp/2016/07/19/george-w-bush-is-suddenly-as-popular-as-bill-clinton/"]
# Bill Clinton
# all_the_links=["https://www.washingtonpost.com/politics/2021/10/14/former-president-bill-clinton-hospitalized/","https://www.washingtonpost.com/politics/2022/01/06/americas-living-presidents-save-one-warn-about-danger-our-democracy-faces/"]
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