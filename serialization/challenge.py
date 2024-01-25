import json
import csv
import datetime

with open("./info/earthquakes.json", "r") as datafile:
    data = json.load(datafile)

# return sig value from the table or 0 if None
def getsig(x):
    sig = x["properties"]["sig"]
    return 0 if sig is None else sig

sig_events = sorted(data["features"], key=getsig, reverse=True)
sig_events = sig_events[:40]
sig_events.sort(key=lambda e: e["properties"]["time"], reverse=True)

header = ["Magnitude", "Place", "Felt Reports", "Date", "Link"]
rows = []

for e in sig_events:
    thedate = datetime.datetime.fromtimestamp(
        int(e["properties"]["time"]) / 1000)
    lat = e["geometry"]["coordinates"][1]
    long = e["geometry"]["coordinates"][0]
    gmaplink = f"https://maps.google.com/maps/search/?api=1&query={lat}%2C{long}"

    rows.append([e["properties"]["mag"],
                 e["properties"]["place"],
                 0 if e["properties"]["felt"] is None else e["properties"]["felt"],
                 thedate,
                 gmaplink
                 ])
    
with open("significantevents.csv", "w") as csvfile:
    writer = csv.writer(csvfile, delimiter=',')
    writer.writerow(header)
    writer.writerows(rows)
    