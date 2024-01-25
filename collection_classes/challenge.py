import json
from collections import defaultdict

with open("./info/earthquakes.json", "r") as datafile:
    data = json.load(datafile)

# use defaultdict to categorize each event and count each one
totals = defaultdict(int)
for e in data['features']:
    totals[e['properties']['type']] += 1

for k, v in totals.items():
    print(f"{k:15}: {v}")