from bs4 import BeautifulSoup
import pandas as pd
from urllib.request import HTTPDefaultErrorHandler, Request, urlopen
import re

req = Request("https://www.politico.com/news/magazine/2021/01/18/trump-presidency-administration-biggest-impact-policy-analysis-451479")
html_page = urlopen(req)
soup = BeautifulSoup(html_page, "lxml")

body_text_info = soup.find_all(class_=re.compile("story-text__"))

# there was an error on the politico website which meant it had three 'the moves' - they were supposed to be labelled 'the move', 'the impact' and 'the upshot'
# the code below - classes were created to categorize the text and place it in the correct subcategory. 
# this fixed the three 'the moves' issue because although these were all classed as a 'move' belonging to the 'Religion in Schools' heading,
# when added to a csv this did not matter, as all the sections were simply inserted into a string in the csv file.

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


composite_list = []
for section in sections:
    lists = [[section.name]]
    bit = section.subsections
    length = len(bit)

    for subsection in range (0,length):
        lists.append(bit[subsection].text)

    construction = []
    for i in lists:
        statement_section = i[0]
        if len(i)>1:
            for j in range(1, len(i)):
                # // used to represent new paragraph.
                # this section adds paragraphs under one subheading (e.g. the move) together
                statement_section += "//" + i[j]
        construction.append('"%s"' % statement_section)

    statement = construction[0]
    for item in range(1,len(construction)):
        statement += ", " + construction[item]
    statement += "\n"
    composite_list.append(statement)

file = open('politico.csv', 'w')
for item in composite_list:
    file.write(item)
    # file.write('\n')
file.close()