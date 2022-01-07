import pandas as pd
from csv import writer
import requests
from bs4 import BeautifulSoup as bsoup
from urllib.request import Request, urlopen


link_page ="https://www.bbc.com/news/topics/cp7r8vgl2lgt/donald-trump"
html_page = urlopen(link_page)
soup = bsoup(html_page, "lxml")
links_on_page = soup.findAll("a", class_ = "qa-heading-link lx-stream-post__header-link")
'''
for link in links_on_page:
    getting_link = "https://www.bbc.com/news" + link.get('href')
    req = Request(getting_link)
    html_page = urlopen(req)
    #soup = bsoup(html_page, "lxml")
    #print(soup)'''

getting_link = "https://www.bbc.com/news" + links_on_page[0].get('href')
html_page = requests.get(getting_link)
soup = bsoup(html_page.text, "lxml")
body_text = 

