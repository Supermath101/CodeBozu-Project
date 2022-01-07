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
    percentage_neg = str(round(sentiment_dict['neg']*100,2))+ "%"
    return percentage_pos, percentage_neg


link_page ="https://www.bbc.com/news/topics/cp7r8vgl2lgt/donald-trump"
html_page = urlopen(link_page)
soup = bsoup(html_page, "lxml")
links_on_page = soup.findAll("a", class_ = "qa-heading-link lx-stream-post__header-link")

with open("bbc.csv", 'w', encoding='utf-8') as file:
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
            paragraph_sentiment = sentiment_scores(text_article)
            statement = title_article + ", " + text_article + paragraph_sentiment[0]+"%" +", " + "\n"
            file.write(statement)
            
    file.close()





'''
#finding the average from the percentage files
def average(file):
    added_move = 0
    added_upshot = 0
    added_impact = 0
    count = 0
    for bit in file:
        separate = bit.split(", ")
        cleaned_move = separate[1].strip("\n").strip("%")
        cleaned_impact = separate[2].strip("\n").strip("%")
        cleaned_upshot = separate[3].strip("\n").strip("%")
        added_move += float(cleaned_move)
        added_impact += float(cleaned_impact)
        added_upshot += float(cleaned_upshot)
        count += 1
    averages = [round(added_move/count,2), round(added_impact/count,2), round(added_upshot/count,2)]
    return averages

file_pos = open("positive_percentage.csv", "r")
averages = average(file_pos)
# used the mean to find the average because there were no extreme pieces of data to skew the results
# and the mean is more inclusive than the median
final_av = (float(averages[0]) + float(averages[1]) + float(averages[2]))/3
final_average = round(final_av,2) #float version of the favourability with respect to Politico
final_average_string = str(final_average) + "%" #string version of the favourability
file_pos.close()

print(final_average_string)

'''
