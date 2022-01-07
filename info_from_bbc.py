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


link_page ="https://www.bbc.com/news/topics/cp7r8vgl2lgt/donald-trump"
html_page = urlopen(link_page)
soup = bsoup(html_page, "lxml")
links_on_page = soup.findAll("a", class_ = "qa-heading-link lx-stream-post__header-link")

with open("bbc.csv", 'w', encoding='utf-8') as file:
    total_positivity = 0
    count = 0
    for link in links_on_page:
        getting_link = "https://www.bbc.com" + link.get('href')
        html_page = requests.get(getting_link)
        soup = bsoup(html_page.text, "lxml")
        title = soup.find("h1", class_="ssrcss-gcq6xq-StyledHeading e1fj1fc10")
        body_text = soup.findAll("div",class_="ssrcss-uf6wea-RichTextComponentWrapper e1xue1i85")
        if body_text != []:
            body = body_text[0].text
            for i in range(0, len(body_text)):
                text = body_text[i].text
                body += "//" + text
            title_article = '"%s"'% title.text
            text_article = '"%s"'% body
            positivity_score = sentiment_scores(text_article)
            statement = title_article + ", " + text_article  + ", " + positivity_score + "\n"
            file.write(statement)
            total_positivity += float(positivity_score.strip("%"))
            count += 1
    file.close()


# mean used to calculate the average positivity score 
average = round(total_positivity/count,2) #float format
average_string = str(average) + "%" #string format



#check that all links are being scraped