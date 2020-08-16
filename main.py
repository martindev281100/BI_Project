import csv

data = []

for row in csv.reader(open("googleplaystore.csv"), delimiter=','):
    data.append(row)

# print(data)
data = data[1:]
remove_underline = lambda row: row[1].replace("_", " ")

remove_sizeMk = lambda row: float(row[4].replace("M", "")) * 1000000 if row[4].find("M") != -1 \
    else float(row[4].replace("k", "")) * 1000

remove_nan_rating = lambda row: row[2].replace("NaN", "0")
remove_plus = lambda row: row[5].replace("+", "")
remove_vdevice4 = lambda row: 0 if row[4] == "Varies with device" else (remove_sizeMk)(row)
convert_num11 = lambda row: 1.0 if row[11] == "Varies with device" \
    else (1.0 if row[11] == "NaN" else row[11][:3])
convert_num12 = lambda row: 1.0 if row[12] == "Varies with device" \
    else (1.0 if row[12] == "NaN" else row[12][:3])

# Clear underline in Category
row1 = list(map(remove_underline, data))
row4 = list(map(remove_vdevice4, data))
row2 = list(map(remove_nan_rating, data))
row5 = list(map(remove_plus, data))
row11 = list(map(convert_num11, data))
row12 = list(map(convert_num12, data))
i = 0
for row in data:
    row[1] = row1[i]
    row[4] = float(row4[i])
    row[2] = float(row2[i])
    row[5] = float(row5[i].replace(",", ""))
    row[11] = row11[i]
    row[12] = row12[i]
    i = i + 1

print(data)
