from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import csv

#finding the sentiment scores for a paragraph
def sentiment_scores(paragraph):
    intensity = SentimentIntensityAnalyzer()
    sentiment_dict = intensity.polarity_scores(paragraph)
    percentage_pos = str(round(sentiment_dict['pos']*100,2))+ "%"
    percentage_neg = str(round(sentiment_dict['neg']*100,2))+ "%"
    return percentage_pos, percentage_neg

#writing the percentages to the positive and negative csv files
def write_files(thing, move, impact, upshot):
    #files will be structured: thing, move percentage, impact percentage, upshot percentage
    line = thing + ", "+ str(move[0])+ ", "+ str(impact[0]) + ", "+ str(upshot[0]) +"\n"
    file_pos.write(line)
    line = thing + ", "+ str(move[1])+ ", "+ str(impact[1]) + ", "+ str(upshot[1]) +"\n"
    file_neg.write(line)

file_pos = open("positive_percentage.csv","w")
file_neg = open("negative_percentage.csv","w")

file = open("politico.csv","r")
# looping through the paragraphs in the csv file
for i in file:
    #splitting each line by the commas and allocating the correct sections to two variables
    separated = i.split(", ")
    move = separated[1]
    impact = separated[2]
    upshot = separated[3]
    thing = separated[0]
    # calling the sentiment_scores function
    percentages_move = sentiment_scores(move)
    percentages_impact = sentiment_scores(impact)
    percentages_upshot = sentiment_scores(upshot)
    #calling the write_file procedure
    write_files(thing, percentages_move, percentages_impact, percentages_upshot)
file.close()

file_pos.close()
file_neg.close()

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