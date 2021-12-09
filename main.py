from bs4 import BeautifulSoup
import requests
html_file=requests.get('https://en.wikipedia.org/wiki/Donald_Trump')

soup = BeautifulSoup(html_file.text, "lxml")
html_tag=soup.find('div',class_='plainlist')
html_tag1=soup.find('div',style='display:inline;white-space:nowrap;')
html_tag2=soup.find('div',style='display:inline-block;line-height:normal;margin-top:1px;white-space:normal;')
print(html_tag2.text)