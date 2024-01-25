import json

with open("./info/earthquakes.json", "r") as datafile:
    data = json.load(datafile)

# fetch data
print(f"Total quakes: {data['metadata']['count']}")    

def feltreport(q):
    f = q["properties"]["felt"]
    return (f is not None and f >= 100)

feltreports = list(filter(feltreport, data["features"]))

# filter data
print(f"Total quakes felt by at least 100 people: {len(feltreports)}")

def getfelt(q):
    f = q["properties"]["felt"]
    if f is not None:
        return f
    return 0

mostfeltquake = max(data["features"], key=getfelt)

# max data
print(f"Most felt reports: {mostfeltquake['properties']['title']}, reports: {mostfeltquake['properties']['felt']}")

def getsig(q):
    s = q["properties"]["sig"]
    if s is not None:
        return s
    return 0

sigevents = sorted(data["features"], key=getsig, reverse=True)

# most significant events
print("The five most significant events were: ")
for i in range(0, 5):
    print(f"Event: {sigevents[i]['properties']['title']}, Significance: {sigevents[i]['properties']['sig']}")
