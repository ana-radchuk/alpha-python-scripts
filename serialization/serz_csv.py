import csv
import json
import datetime

with open("./info/earthquakes.json", "r") as datafile:
    data = json.load(datafile)

def isbig(x):
    mag = x["properties"]["mag"]
    return mag is not None and mag > 5

largerquakes = list(filter(isbig, data["features"]))

# create header and row structures for the data
header = ["Place", "Magnitude", "Link", "Date"]
rows = []

# populate the rows with the resulting quake data
for q in largerquakes:
    thedate = datetime.date.fromtimestamp(
        int(q["properties"]["time"]/1000))
    rows.append([q["properties"]["place"],
                q["properties"]["mag"],
                q["properties"]["url"],
                thedate])   

# write the results to the CSV file
with open("largequakes.csv", "w") as csvfile:
    writer = csv.writer(csvfile, delimiter=",")
    writer.writerow(header)
    writer.writerows(rows)
