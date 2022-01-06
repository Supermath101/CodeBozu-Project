from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import csv

#finding the sentiment scores for an impact
def sentiment_scores(impact):
    intensity = SentimentIntensityAnalyzer()
    sentiment_dict = intensity.polarity_scores(impact)
    percentage_pos = str(round(sentiment_dict['pos']*100,3))+ "%"
    percentage_neg = str(round(sentiment_dict['neg']*100,3))+ "%"
    return percentage_pos, percentage_neg

#writing the percentages to the positive and negative csv files
def write_files(thing, percentages):
    line = thing + ", "+ str(percentages[0]) +"\n"
    file_pos.write(line)
    line = thing + ", "+ str(percentages[1]) +"\n"
    file_neg.write(line)

file_pos = open("positive_percentage.csv","w")
file_neg = open("negative_percentage.csv","w")

file = open("politico.csv","r")
# looping through the impacts in the csv file
for i in file:
    #splitting each line by the commas and allocating the correct sections to two variables
    separated = i.split(", ")
    impact = separated[2]
    thing = separated[0]
    # calling the sentiment_scores function
    percentages = sentiment_scores(impact)
    #calling the write_file procedure
    write_files(thing, percentages)
file.close()

file_pos.close()
file_neg.close()