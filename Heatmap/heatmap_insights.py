files = ["averages_bbc.txt", "averages_forbes.txt",  "averages_fox_news.txt", "averages_huff_post.txt"]
names = ["BBC", "Forbes", "Fox News", "Huffington Post"]
presidents = ["Donald Trump", "Joe Biden", "Barack Obama", "George W. Bush", "Bill Clinton"]
party = ["Republican", "Democratic", "Democratic", "Republican", "Democratic"]
folder = "Heatmap/"


def largest(array, max):
    for item in array:
        if item > max:
            max = item
    return max

def smallest(array, min):
    for item in array:
        if item < min:
            min = item
    return min

def max_and_min(folder, file):
    file = open(folder + file, "r")
    max = -1
    min = 1000
    array = []
    item_largest = []
    item_smallest = []

    for line in file:
        value = float(line.split(", ")[1].strip("\n").strip("%"))
        array.append(value)
    file.close()

    found_largest = largest(array, max)
    found_smallest = smallest(array, min)


    for j in range(0, len(array)):
        if array[j] == found_largest:
            item_largest.append(j)

    for j in range(0, len(array)):
        if array[j] == found_smallest:
            item_smallest.append(j)          

    return item_largest, item_smallest

# Finding the most favoured and the most disfavoured politican for each website
max_and_mins = []
for i in range(0, len(files)):
    max_and_mins.append(max_and_min(folder, files[i]))

largest_items = []
smallest_items = []
for i in range(0, len(max_and_mins)):
    largest_items.append(max_and_mins[i][0])
    smallest_items.append(max_and_mins[i][1])
    
        

# finding the most favoured politican
percentage = []
max = -1
file = open(folder + "heatmap_data.csv", "r")
for line in file:
    percentages = 0
    for i in range (1, len(files)+1):
        split_line = line.split(", ")[i].strip("\n")
        percentages += float(split_line.strip("%"))
    percentage.append(percentages)
file.close()


largest_percentage = largest(percentage, max)
for i in range(0, len(percentage)):
    if percentage[i] == largest_percentage:
        most_favoured = i



# Favouring of political party
democratic = 0
republican = 0
array = []
party_fav = []
party_favoured = []

file = open(folder + "heatmap_data.csv", "r")
for line in file:
    separated = line.split(", ")
    array.append(separated)
file.close()

numr = 0
numd = 0
for j in range(1, 5):
    for item in range(0, len(array)):
        if party[item] ==  "Democratic":
            democratic += float(array[item][j].strip("\n").strip("%"))
            numd += 1
        if party[item] == "Republican":
            republican += float(array[item][j].strip("\n").strip("%"))
            numr += 1
    party_fav.append([democratic/numd, republican/numr])

dem_faved = 0
rep_faved = 0
for item in party_fav:
    if item[0] > item[1]:
        party_favoured.append("Democratic")
        dem_faved += 1 
    elif item[0] < item[1]:
        party_favoured.append("Republican")
        rep_faved += 1 
    else:
        party_favoured.append("No party preferance")



# overall party favoured:
if dem_faved > rep_faved:
    overall_party_fav = "Democratic"
elif rep_faved > dem_faved:
    overall_party_fav = "Republican"
else:
    overall_party_fav = "No overall party favoured"


for i in range (0, len(files)):
    most_fav = "Most favoured politican(s): "
    least_fav = "Least favoured politican(s): "
    print(names[i])
    large = largest_items[i]
    small = smallest_items[i]
    count_large = 0
    count_small = 0
    for item in large:
        length = len(large)
        count_large += 1
        most_fav += presidents[item]
        if count_large != length:
            most_fav += ", "
    for item in small:
        length = len(small)
        count_small += 1
        least_fav += presidents[item]
        if count_small != length:
            least_fav += ", "
    print(most_fav)
    print(least_fav)
    print(f'Political Party Favoured: {party_favoured[i]}')
    print("\n")

print(f'Most favoured president overall: {presidents[most_favoured]}')
print(f'The overall political party favoured: {overall_party_fav}')
