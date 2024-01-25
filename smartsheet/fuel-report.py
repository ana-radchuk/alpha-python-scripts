import json
import requests
import csv

# method to create headers for API requests
def getHeaders():

    # open file that holds authentication token
    with open("smart-token.json", "r") as datafile:
        creds = json.load(datafile)
        token = creds['token']

        # create headers object
        headers = {
            'Authorization': token,
            'Content-Type': 'application/json'
        }

    return headers

# method to get data from file
def getDataFromCSV():

    # open csv file
    with open("report.csv", "r") as csvfile:
        reader = csv.reader(csvfile)
        sniffer = csv.Sniffer()
        sample = csvfile.read(1024)
        csvfile.seek(0)

        if(sniffer.has_header(sample)):
            next(reader)

        # get output from csv file
        result = []
        
        for row in reader:
            result.append(row)

        # filter data
        data = []

        for item in result:
            for i in item:
                if '*' not in i:
                    data.append(item)
    
        return data


# method to create smartsheet
def createSmartsheet(): 
    result = []

    # create columns payload object 
    data = {
        "name": "My Smartsheet",
        "columns": [{
            "title": "A",
            "type": "TEXT_NUMBER",
            "primary": True
        }, {
            "title": "B",
            "type": "TEXT_NUMBER",
            "primary": False
        }, {
            "title": "C",
            "type": "TEXT_NUMBER",
            "primary": False
        }, {
            "title": "D",
            "type": "TEXT_NUMBER",
            "primary": False
        }, {
            "title": "E",
            "type": "TEXT_NUMBER",
            "primary": False
        }, {
            "title": "F",
            "type": "TEXT_NUMBER",
            "primary": False
        }, {
            "title": "G",
            "type": "TEXT_NUMBER",
            "primary": False
        }]
    }

    # API request to create smartsheet
    response = requests.post('https://api.smartsheet.com/2.0/sheets', headers=getHeaders(), json=data)

    # save created sheet_id into variable
    sheet_id = response.json()['result']['id']

    # save created column ids into variable
    cols = []
    for c in response.json()['result']['columns']:
        cols.append(c['id'])
        
    result.append(sheet_id)
    result.append(cols)

    return result  

# method to create rows
def processRows(rows, cols): 

    # create cell objects
    items = []
    for r in rows:
        for idx, c in enumerate(cols):
            items.append({
                "columnId": int (c),
                "value": r[idx]
            })  

    # group cells into row object
    data = [items[n:n+len(cols)] for n in range(0, len(items), len(cols))]
    payload = []

    # create row payload
    for d in data:
        payload.append({
            "toTop": True,
            "cells": d
        })

    return payload

def populateSmartsheetFromCSV():
    rows = []

    # create new smartsheet
    smartsheet = createSmartsheet()
    sheet_id = smartsheet[0]
    cols = smartsheet[1]

    print("sheet_id: " + str(sheet_id))
    print("column ids: " + str(cols))

    # get data from csv file
    rows = getDataFromCSV()   
    data = processRows(rows, cols)

    # API request to add rows
    response = requests.post("https://api.smartsheet.com/2.0/sheets/" + str(sheet_id) + "/rows", json=data, headers=getHeaders())
        
    return response.text

# method to attach more rows to already existing smartsheet
def addRows():
    # read csv file to be uploaded into smartsheet
    rows = getDataFromCSV()

    # indicate sheet_id
    sheet_id = 3424687858077572

    # indicate columns
    cols = [570538405613444, 5074138032983940, 2822338219298692, 7325937846669188, 1696438312456068, 6200037939826564, 3948238126141316]

    # process rows as payload
    data = processRows(rows, cols)

    # API request to add rows
    response = requests.post("https://api.smartsheet.com/2.0/sheets/" + str(sheet_id) + "/rows", json=data, headers=getHeaders())
        
    return response.text

# populateSmartsheetFromCSV()
addRows()