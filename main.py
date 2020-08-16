import csv

data = []

for row in csv.reader(open("googleplaystore.csv"), delimiter=','):
    data.append(row)

# print(data)
data = data[1:]
remove_underline = lambda row: row[1].replace("_", " ")
remove_sizeM = lambda row: row[4].replace("M", "000000")
remove_nan_rating = lambda row: row[2].replace("NaN", "0")
remove_plus = lambda row: row[5].replace("+", "")
remove_various_device4 = lambda row: row.replace("Varies with device", "0")
print(data[1])
# remove_various_device11 = lambda row:
row4v = list(map(remove_various_device4, data))
# row11v = list(map(remove_various_device11, data))
# Clear underline in Category
row1 = list(map(remove_underline, data))
row4 = list(map(remove_sizeM, data))
row2 = list(map(remove_nan_rating, data))
i = 0
for row in data:
    row[1] = row1[i]
    row[4] = row4v[i]
    row[2] = float(row2[i])
    # row[11] = row11v[i]
    i = i + 1

x = 0
for row in data:
    row[4] = float(row4[x])
print(data[37])
