from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

file=open("politico.csv","r")
print(file)
for i in file:
    print(i[0])
file.close()
impact1=""

def sentiment_scores(impact):
    intensity = SentimentIntensityAnalyzer()
    sentiment_dict = intensity.polarity_scores(impact)
    percentage_pos = str(sentiment_dict['pos']*100)+ "%"
    percentage_neg = str(sentiment_dict['neg']*100)+ "%"
    return percentage_pos, percentage_neg

percentages = sentiment_scores(impact1) #this will be looped through for each of the impacts of each thing done

#creating positive percentage file
file_pos = open("positive_percentage.csv","w")
thing = "1" #this will be updated to include the name of the thing done
line = thing + ", "+ str(percentages[0]) +"\n"
file_pos.write(line)
file_pos.close()

#creating negative percentage file
file_neg = open("negative_percentage.csv","w")
thing = "1"
line = thing + ", "+ str(percentages[1]) +"\n"
file_neg.write(line)
file_neg.close()