from csv import reader
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer


files = ["fox_news_on_trump.csv", "fox_news_on_biden.csv", "fox_news_on_obama.csv", "fox_news_on_bush.csv", "fox_news_on_clinton.csv"]
names = ["Donald Trump", "Joe Biden", "Barack Obama", "George W. Bush", "Bill Clinton"]

statements = []
num = -1
for i in files:
    average = 0
    with open(i,'r') as read_obj:
        csv_reader = reader(read_obj)
        for row in csv_reader:
            for i in row:
                sid_obj = SentimentIntensityAnalyzer()
                sentiment_dict = sid_obj.polarity_scores(i)
                average += (sentiment_dict['pos']*10)
        f = round(average/10,2)
        num += 1
        statements.append(names[num] + ", " + str(f) +'%') 


with open("averages_fox_news.txt", "w") as file:
    for j in statements:
        file.write(j)
        file.write('\n')
file.close()        
