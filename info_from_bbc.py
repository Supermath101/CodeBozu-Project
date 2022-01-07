import pandas as pd
from csv import writer
import requests
from bs4 import BeautifulSoup as bsoup
from urllib.request import urlopen


link_page ="https://www.bbc.com/news/topics/cp7r8vgl2lgt/donald-trump"
html_page = urlopen(link_page)
soup = bsoup(html_page, "lxml")
links_on_page = soup.findAll("a", class_ = "qa-heading-link lx-stream-post__header-link")
<<<<<<< HEAD:info_from_bbc.py
<<<<<<< HEAD:info_from_bbc.py
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
=======

>>>>>>> f3637c01d080c5421e088cc894fe15a7f84a44d9:BBC.py
=======

>>>>>>> f3637c01d080c5421e088cc894fe15a7f84a44d9:BBC.py
file = open("BBC.csv", "w")
for link in links_on_page:
    getting_link = "https://www.bbc.com" + link.get('href')
    html_page = requests.get(getting_link)
    soup = bsoup(html_page.text, "lxml")
    title = soup.find("h1", class_="ssrcss-gcq6xq-StyledHeading e1fj1fc10").text
    body_text = soup.findAll("div",class_="ssrcss-uf6wea-RichTextComponentWrapper e1xue1i85").text
    statement = title + ", " + body_text + "\n"
    file.write(statement)
file.close()