import csv
import numpy as np

data = []
seen = set()
for row in csv.reader(open("googleplaystore.csv"), delimiter=','):
    if row[0] in seen: continue

    seen.add(row[0])
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
    else (1.0 if row[11] == "NaN" else (row[11][:3] if row[11][:2] in '"0.""1.""2.""3.""4.""5.""6.""7.""8.""9."' else 1.0))
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

np.savetxt('test.csv', data, fmt='%s', delimiter=',', newline='\n', encoding='utf8')
with open('test.csv', mode='w') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(
        ["App", "Category", "Rating", "Reviews", "Size", "Installs", "Type", "Price", "Content Rating", "Genres",
         "Last Updated", "Current Ver", "Android Ver"])
    for row in data:
        writer.writerow(row)
