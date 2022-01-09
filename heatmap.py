import seaborn as sn
import pandas as pd
import matplotlib.pyplot as plt
from pylab import savefig


array = []
file = open("trials.csv", "r")
for line in file:
    separated = line.split(", ")
    list = [float(separated[1]), float(separated[2]), float(separated[3]), float(separated[4]), float(separated[5]), float(separated[6].strip("\n"))]
    array.append(list)
file.close()


df_cm = pd.DataFrame(array)
# yticklabels=["Trump", "Biden"], xticklabels=["Website 1", "Website 2", "Websit


svm = sn.heatmap(df_cm, annot = True, cmap = 'YlGnBu', yticklabels = ["Trump", "Biden", "Obama", "Bush"], xticklabels = ["BBC", "Washington Post", "Website3", "Website4", "Website5"])
svm.title("Favourability of Politicians")

figure = svm.get_figure()
figure.savefig('Favourability of Politicians.png', dpi = 400)
