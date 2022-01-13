import seaborn as sn
import pandas as pd
import matplotlib.pyplot as plt
from pylab import savefig


array = []
file = open("heatmap_data.csv", "r")
for line in file:
    separated = line.split(", ")
    bbc = separated[1].strip("%")
    forbes = separated[2].strip("\n")
    fox_news=separated[3].strip('%')
    huff_post=separated[4]
    list = [float(bbc), float(forbes.strip("%")),float(fox_news.strip('%')),float(huff_post)]
    array.append(list)
print(array)
file.close()


df_cm = pd.DataFrame(array)

sn.set(font_scale = 1.5)
svm = sn.heatmap(df_cm, annot = True, cmap = 'YlGnBu', yticklabels = ["Donald Trump", "Joe Biden", "Barack Obama", "George W. Bush", "Bill Clinton"], xticklabels = ["BBC", "Forbes","Fox News","Huffington Post"])
plt.rcParams["figure.autolayout"] = True
plt.tight_layout()
plt.title("Favourability of Politicians")

figure = svm.get_figure()
figure.savefig('Favourability of Politicians.png', dpi = 600)
