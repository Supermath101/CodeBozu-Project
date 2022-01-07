import pandas as pd
from csv import writer
import requests
from bs4 import BeautifulSoup as bsoup
from urllib.request import Request, urlopen


link_page ="https://www.bbc.com/news/topics/cp7r8vgl2lgt/donald-trump"
html_page = urlopen(link_page)
soup = bsoup(html_page, "lxml")
links_on_page = soup.find_all("a", class_ = "qa-heading-link lx-stream-post__header-link")

for link in links_on_page:
    getting_link = "https://www.bbc.com/news/topics" + link.get('href')
    html_file = requests.get(getting_link)
    soup = bsoup(html_file, "lxml")

