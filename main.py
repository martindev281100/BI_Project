import csv
import numpy as np

data = []
seen = set()
for row in csv.reader(open("googleplaystore.csv"), delimiter=','):
    if row[0] in seen: continue
    seen.add(row[0])
    data.append(row)

# Remove header in dataset
data = data[1:]

# Remove dash in second column
remove_dash = list(map(lambda row: row[1].replace("_", " "), data))

# Remove Various with device value, 'M' at size and convert it to bytes
remove_sizeMk = lambda row: float(row[4].replace("M", "")) * 1000000 if row[4].find("M") != -1 \
    else float(row[4].replace("k", "")) * 1000
remove_vdevice4 = list(map(lambda row: 0 if row[4] == "Varies with device" else (remove_sizeMk)(row), data))


# Remove NaN value in review column
remove_nan_rating = list(map(lambda row: row[2].replace("NaN", "0"), data))

# Remove plus character in install column
remove_plus = list(map(lambda row: row[5].replace("+", ""), data))

# Remove Varies with device and *trash value in column then change to 1.0
convert_num11 = list(map(lambda row: 1.0 if row[11] == "Varies with device" \
    else (
    1.0 if row[11] == "NaN" else (row[11][:3] if row[11][:2] in '"0.""1.""2.""3.""4.""5.""6.""7.""8.""9."' else 1.0)),
                         data))

# Remove Varies with device and Nan then change to 1.0
convert_num12 = list(map(lambda row: 1.0 if row[12] == "Varies with device" \
    else (1.0 if row[12] == "NaN" else row[12][:3]), data))

# Apply function into individual row in data list
i = 0
for row in data:
    row[1] = remove_dash[i]
    row[4] = float(remove_vdevice4[i])
    row[2] = float(remove_nan_rating[i])
    row[5] = float(remove_plus[i].replace(",", ""))
    row[11] = convert_num11[i]
    row[12] = convert_num12[i]
    i = i + 1
print(data)

# Write data in a new csv file
np.savetxt('test.csv', data, fmt='%s', delimiter=',', newline='\n', encoding='utf8')
with open('test.csv', mode='w') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(
        ["App", "Category", "Rating", "Reviews", "Size", "Installs", "Type", "Price", "Content Rating", "Genres",
         "Last Updated", "Current Ver", "Android Ver"])
    for row in data:
        writer.writerow(row)
