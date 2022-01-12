import pandas as pd
from csv import writer
import requests
from bs4 import BeautifulSoup as bsoup
from urllib.request import urlopen
from sentiment_functions import writing_to_file


links = ["https://www.bbc.com/news/topics/cp7r8vgl2lgt/donald-trump", "https://www.bbc.com/news/topics/czyymgqmn6dt/joe-biden",
 "https://www.bbc.com/news/topics/cvenzmgywl4t/barack-obama", "https://www.bbc.com/news/topics/cv0y3dkx5eet/george-w-bush",
 "https://www.bbc.com/news/topics/c4n0j9r0n8wt/bill-clinton"]
files = ["bbc_trump.csv","bbc_biden.csv","bbc_obama.csv", "bbc_w_bush.csv", "bbc_clinton.csv"]

def calculate_average(positivity, count):
    average = round(positivity/count,2) #float format
    average_string = str(average) + "%" #string format
    averages.append(average_string)
    return averages

averages = []
for link_page in range(0, len(links)):
    html_page = urlopen(links[link_page])
    soup = bsoup(html_page, "lxml")
    links_in_page = soup.findAll("a", class_="qa-heading-link lx-stream-post__header-link")
    
    with open(files[link_page], 'w', encoding='utf-8') as file:
        positivity = 0
        count = 0
        for link in links_in_page:
            getting_link = "https://www.bbc.com" + link.get('href')
            html_page = requests.get(getting_link)
            soup = bsoup(html_page.text, "lxml")

            title_vid = soup.find("h1", class_="ssrcss-1qr3f1s-StyledHeading e1fj1fc10")
            body_text_vid = soup.findAll("div", class_="ssrcss-1up5zkp-StyledSummary elwf6ac3")
            title_reg = soup.find("h1", class_="ssrcss-gcq6xq-StyledHeading e1fj1fc10")
            body_text_reg = soup.findAll("div",class_="ssrcss-uf6wea-RichTextComponentWrapper e1xue1i85")
            title_pictures_story = soup.find("h1", class_="ssrcss-gcq6xq-StyledHeading e1fj1fc10")
            body_text_pictures_story = soup.findAll("p", class_="ssrcss-1q0x1qg-Paragraph eq5iqo00")

            if title_reg != None and body_text_reg != None and body_text_reg != []:
                positivity += writing_to_file(title_reg, body_text_reg, file)
                count += 1
            elif title_vid != None and body_text_vid != None and body_text_vid != []:
                positivity += writing_to_file(title_vid, body_text_vid, file)
                count += 1

            #clean "The bbc is not responsible..."
            #check the pictures file for Bush
            elif title_pictures_story != None and body_text_pictures_story != None and body_text_pictures_story != []:
                positivity += writing_to_file(title_pictures_story, body_text_pictures_story, file)
                count += 1

        # mean used to calculate the average positivity score for the current link page
        print(positivity,count)
        averages = calculate_average(positivity, count)

    file.close()


presidents = ["Donald Trump", "Joe Biden", "Barack Obama", "George W. Bush", "Bill Clinton"]
file = open("averages_bbc.txt", "w")
for i in range (0, len(averages)):
    file.write(presidents[i] + ", " + averages[i] + "\n")
file.close()
    