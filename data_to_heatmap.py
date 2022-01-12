from csv import reader
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
average=0
num=0
with open("washington_post_on_trump.csv",'r')as read_obj:
    csv_reader=reader(read_obj)
    print(csv_reader)
    for row in csv_reader:
        num+=1
        for i in row:
            sid_obj = SentimentIntensityAnalyzer()
            sentiment_dict = sid_obj.polarity_scores(i)
            average+=(sentiment_dict['pos']*10)
    f=round(average/10,2)
    with open("washington_post.txt", "a") as file:
        file.write('\n')
        file.write('Donald Trump'+str(f)+'%')
    file.close()




# files = ["averages_bbc.txt", "averages_forbes.txt", "averages_huff_post.txt","average_fox_news.txt"]
# array_name = []
# array_data = []

# for text_file in range (0, len(files)):
#     file = open(files[text_file], "r")
#     array_data_website = []
#     for line in file:
#         if text_file == 0:
#             array_name.append(line.split(", ")[0])
#         array_data_website.append(line.split(", ")[1].strip("\n"))
#     array_data.append(array_data_website)
#     file.close()

# file = open("heatmap_data.csv", "w")
# for i in range(0,5):
#     statement = array_name[i]
#     for j in range(0,len(files)):
#         statement += ", " + array_data[j][i]
#     statement += "\n"
#     file.write(statement)
# file.close()