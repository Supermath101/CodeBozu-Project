files = ["averages_bbc.txt", "averages_forbes.txt"]
array_name = []
array_data = []

for text_file in range (0, len(files)):
    file = open(files[text_file], "r")
    array_data_website = []
    for line in file:
        if text_file == 0:
            array_name.append(line.split(", ")[0])
        array_data_website.append(line.split(", ")[1].strip("\n"))
    array_data.append(array_data_website)
    file.close()

file = open("heatmap_data.csv", "w")
for i in range(0,5):
    file.write(array_name[i] + ", " + array_data[0][i] + ", " + array_data[1][i]+ "\n")
file.close()