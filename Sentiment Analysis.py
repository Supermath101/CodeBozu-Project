from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

#testing th eprogram for one impact only 
impact1 = "The health exchanges didn't collapse, as Trump had hoped. Instead, health plans and states quickly figured out a way to claw back the federal dollars they lost: They built the costs of the subsidies into premiums for Obamacare s benchmark  silver  policies. This meant that premiums for these  silver  plans spiked and as a result, the premium subsidies the government had to pay for low-income enrollees vastly increased. The concept, known as  silver-loading,  grew government subsidizing of the exchanges by upwards of $20 billion per year."

def sentiment_scores(impact):
    intensity = SentimentIntensityAnalyzer()
    sentiment_dict = intensity.polarity_scores(impact)
    percentage_pos = sentiment_dict['pos']*100, "%"
    percentage_neg = sentiment_dict['neg']*100, "%"
    return percentage_pos, percentage_neg

percentages = sentiment_scores(impact1) #this will be looped through for each of the impacts of each thing done

#creating positive percentage file
file_pos = open("positive_percentage.csv","w")
thing = "1" #this will be updated to include the name of the thing done
line = thing + ","+ str(percentages[0]) +"\n"
file_pos.write(line)
file_pos.close()

#creating negative percentage file
file_neg = open("negative_percentage.csv","w")
thing = "1"
line = thing + ","+ str(percentages[1]) +"\n"
file_neg.write(line)
file_neg.close()