import pandas as pd
from csv import writer
import requests
from bs4 import BeautifulSoup as bsoup
from urllib.request import urlopen
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

#finding the sentiment scores for a paragraph
def sentiment_scores(paragraph):
    intensity = SentimentIntensityAnalyzer()
    sentiment_dict = intensity.polarity_scores(paragraph)
    percentage_pos = str(round(sentiment_dict['pos']*100,2))+ "%"
    return percentage_pos


def writing_to_file(title, body_text):
    total_positivity = 0
    count = 0
    if body_text != []:
        if len(body_text) > 1:
            body = body_text[0].text
            for i in range(0, len(body_text)):
                text = body_text[i].text
                body += "//" + text
        else:
            body = body_text[0].text
        title_article = '"%s"'% title.text
        text_article = '"%s"'% body
        positivity_score = sentiment_scores(text_article)
        statement = title_article + ", " + text_article  + ", " + positivity_score + "\n"
        file.write(statement)
        total_positivity += float(positivity_score.strip("%")) 
        count += 1
    return(total_positivity, count)


links = ["https://www.bbc.com/news/topics/cp7r8vgl2lgt/donald-trump", "https://www.bbc.com/news/topics/czyymgqmn6dt/joe-biden",
 "https://www.bbc.com/news/topics/cvenzmgywl4t/barack-obama", "https://www.bbc.com/news/topics/cv0y3dkx5eet/george-w-bush"]
files = ["bbc_trump.csv", "bbc_obama.csv", "bbc_biden.csv", "bbc_bush.csv"]


for link_page in range(0, len(links)):
    html_page = urlopen(links[link_page])
    soup = bsoup(html_page, "lxml")
    links_in_page = soup.findAll("a", class_="qa-heading-link lx-stream-post__header-link")
    
    with open(files[link_page], 'w', encoding='utf-8') as file:
        for link in links_in_page:
            getting_link = "https://www.bbc.com" + link.get('href')
            html_page = requests.get(getting_link)
            soup = bsoup(html_page.text, "lxml")
            title_vid = soup.find("h1", class_="ssrcss-1qr3f1s-StyledHeading e1fj1fc10")
            body_text_vid = soup.findAll("div", class_="ssrcss-1up5zkp-StyledSummary elwf6ac3")
            title_reg = soup.find("h1", class_="ssrcss-gcq6xq-StyledHeading e1fj1fc10")
            body_text_reg = soup.findAll("div",class_="ssrcss-uf6wea-RichTextComponentWrapper e1xue1i85")    
            if title_reg != None and body_text_reg != None:
                regular_details = writing_to_file(title_reg, body_text_reg)
            elif title_vid != None and body_text_vid != None:
                video_details = writing_to_file(title_vid, body_text_vid)        
    file.close()

    # mean used to calculate the average positivity score for the current link page
    total_positivity = float(regular_details[0]) + float(video_details[0])
    count = int(regular_details[1]) + int(video_details[1])

    average = round(total_positivity/count,2) #float format
    average_string = str(average) + "%" #string format
    
