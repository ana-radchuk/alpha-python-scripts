import json

nums = (1, 8, 4, 49, 32, 89, 7)
chars = "abcDgjksrJKIrsdfmnO"

def filterEvens(x):
    # filters out even numbers and keeps odds
    if x % 2 == 0:
        return False
    return True

def filterUppers(x):
    # filters out upper case letters and keeps lower case letters
    if x.isupper():
        return False
    return True

# odds = list(filter(filterEvens, nums))
# print(odds)

# lowers = list(filter(filterUppers, chars))
# print(lowers)

with open("./info/earthquakes.json", "r") as datafile:
    data = json.load(datafile)

def notAQuake(q):
    if q["properties"]["type"] == "earthquake": 
        return False
    return True

events = list(filter(notAQuake, data["features"]))
print(f"Total non quake events: {len(events)}")

for i in range(0, 1):
    print(events[i]["properties"]["type"])

    