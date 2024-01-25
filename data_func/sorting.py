import json

# MIN-MAX SECTION ##########################################

# values = [3.0, 7.0, 1.6, 8.9, 15.9]
# strings = ["one", "three", "ten", "five", "zero", "eighteen"]

# print(f"The minimal value is: {min(values)}")
# print(f"The minimal value is: {min(strings)}")

# print(f"The minimal value is: {min(strings, key=len)}")
# print(f"The maximal value is: {max(strings, key=len)}")

# ANY-ALL-SUM SECTION #######################################

# values = [0, 1, 2, 3, 4, 5]
# print(any(values))
# print(all(values))
# print(sum(values))

# SORTING SECTION ###########################################

# numbers = [42, 54, 19, 17, 23, 31, 16, 4]
# names = ["Jeff", "Bill", "Kristy", "Daniel", "Dean", "Adam"]

# result = sorted(numbers)
# print(result)

# names.sort(reverse=True)
# print(names)

with open("./info/earthquakes.json", "r") as datafile:
    data = json.load(datafile)

def getmag(dataitem):
    magnitude = dataitem["properties"]["mag"]
    if (magnitude is None):
        magnitude = 0
    return float(magnitude)

# SORTING SECTION #########################################

data["features"].sort(key=getmag, reverse=True)
for i in range(0, 10):
    print(data["features"][i]["properties"]["place"])


# MIN-MAX SECTION #########################################

# print(data["metadata"]["title"])
# print(len(data["features"]))

# print(min(data["features"], key=getmag))
# print(max(data["features"], key=getmag))

# ANY-ALL-SUM SECTION ####################################

# print(any(quake["properties"]["felt"] is not None and quake["properties"]["felt"] > 900
#           for quake in data["features"]))

# print(sum(quake["properties"]["felt"] is not None and quake["properties"]["felt"] > 900
#           for quake in data["features"]))

# print(sum(quake["properties"]["mag"] is not None and quake["properties"]["mag"] > 2
#           for quake in data["features"]))





