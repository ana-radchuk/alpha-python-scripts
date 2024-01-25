import json
import pprint
import datetime

def squareFunc(x):
    return x**2

def toGrade(x):
    if (x >= 90):
        return "A"
    elif (x >= 80 and x < 90):
        return "B"
    elif (x >= 70 and x < 80):
        return "C"
    elif (x >= 65 and x < 70):
        return "D"
    return "F"

nums = (1, 8, 4, 345, 23, 3252, 324)
grades = (81, 95, 74, 61, 55, 99)

# squares = list(map(squareFunc, nums))
# print(squares)

# grades = sorted(grades)
# letters = list(map(toGrade, grades))
# print(letters) 

with open("./info/earthquakes.json", "r") as datafile:
    data = json.load(datafile)

def bigmag(q):
    return q["properties"]["mag"] is not None and q["properties"]["mag"] >= 6

results = list(filter(bigmag, data["features"]))

def simplify(q):
    return {
        "place": q["properties"]["place"],
        "magnitude": q["properties"]["mag"],
        "date": str(datetime.date.fromtimestamp(q["properties"]["time"]/1000))
    }

results = list(map(simplify, results))
pprint.pp(results)

    