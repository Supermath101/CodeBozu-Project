import seaborn as sn
import pandas as pd
import matplotlib.pyplot as plt
from pylab import savefig
import os 

# Data to heatmap
files = ["averages_bbc.txt", "averages_forbes.txt", "averages_huff_post.txt", "averages_fox_news.txt"]
array_name = []
array_data = []
folder = "Heatmap"

if not os.path.exists(folder):
    os.makedirs(folder)

for text_file in range (0, len(files)):
    file = open(folder + "/" + files[text_file], "r")
    array_data_website = []
    for line in file:
        if text_file == 0:
            array_name.append(line.split(", ")[0])
        array_data_website.append(line.split(", ")[1].strip("\n"))
    array_data.append(array_data_website)
    file.close()


file = open(folder + "/" + "heatmap_data.csv", "w")
for i in range(0,5):
    statement = array_name[i]
    for j in range(0,len(array_data)):
        statement += ", " + array_data[j][i]
    statement += "\n"
    file.write(statement)
file.close()



# Creating the heatmap
array = []
file = open(folder + "/" + "heatmap_data.csv", "r")
for line in file:
    separated = line.split(", ")
    bbc = separated[1].strip("%")
    forbes = separated[2].strip("%")
    huff_post=separated[3].strip("%")
    fox_news=separated[4].strip("\n")
    list = [float(bbc), float(forbes),float(huff_post),float(fox_news.strip('%'))]
    array.append(list)
file.close()


df_cm = pd.DataFrame(array)

sn.set(font_scale = 1.5)
svm = sn.heatmap(df_cm, annot = True, cmap = 'YlGnBu', yticklabels = ["Donald Trump", "Joe Biden", "Barack Obama", "George W. Bush", "Bill Clinton"], xticklabels = ["BBC", "Forbes", "Huffington Post", "Fox News"])
plt.rcParams["figure.autolayout"] = True
plt.tight_layout()
plt.title("Politican Favourability by News Media")

figure = svm.get_figure()
figure.savefig(folder + "/" + 'Politican Favourability by News Media.png', dpi = 600)
