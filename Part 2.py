from bs4 import BeautifulSoup
import pandas as pd
from urllib.request import Request, urlopen
import re

req = Request("https://www.politico.com/news/magazine/2021/01/18/trump-presidency-administration-biggest-impact-policy-analysis-451479")
html_page = urlopen(req)
soup = BeautifulSoup(html_page, "lxml")

body_text_info = soup.find_all(class_=re.compile("story-text__"))

class section: 
    def __init__(self, name):
        self.name = name
        self.subsections = []

class subsection:
    def __init__(self, name, text):
        self.name = name
        self.text = [text]

current_subsection = ''
current_section = ''
sections = []

for paragraph in body_text_info:
    item = paragraph.text
    if paragraph.name == "h3":
        if current_subsection != '' and current_section != '':
            current_section.subsections.append(current_subsection)
            current_subsection = ''
            sections.append(current_section)
        current_section = section(item)

    elif re.search(r"(?:The move:)(.*)", item):
        if current_subsection != '':
            current_section.subsections.append(current_subsection)
        current_subsection = subsection("Move",item.replace("The move: ", ""))

    elif re.search(r"(?:The impact:)(.*)", item):
        if current_subsection != '':
            current_section.subsections.append(current_subsection)
        current_subsection = subsection("Impact",item.replace("The impact: ", ""))

    elif re.search(r"(?:The upshot:)(.*)", item):
        if current_subsection != '':
            current_section.subsections.append(current_subsection)
        writer = paragraph.find('i')
        current_subsection = subsection("Upshot",item.replace("The upshot: ", "").replace(writer.text,""))

    else:
        #stopping text after heading but before 'The move:' from being added
        if current_subsection != '':
            current_subsection.text.append(item)
if current_subsection != '' and current_section != '':
    current_section.subsections.append(current_subsection)
    sections.append(current_section)
for section in sections:
    thing = section.name
    statement = thing
    for subsection in section.subsections:
        statement += ", " + ''.join(subsection.text)
        #problem, commas in the text will mess up the csv file. 
        #Need to add quotation marks around the large pieces of text 
        #Also need use pandas to make the csv file instead 
    df=pd.DataFrame({'everything':[statement]})
    df.to_csv('politico.csv',mode='a', header=False, index=False)