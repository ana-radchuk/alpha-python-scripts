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

# method to create columns
def processColumns(columns):
    cols = columns[0]
    result = []

    # enumeration through column that defines the first column as primary
    for idx, c in enumerate(cols):
        if (idx == 0):
            result.append({
                "title": c,
                "type": "TEXT_NUMBER",
                "primary": True
            })
        else:
            result.append({
                "title": c,
                "type": "TEXT_NUMBER",
                "primary": False
            })

    return result         

# method to create smartsheet
def createSmartsheet(columns): 
    result = [] 

    # create payload object 
    data = {
        "name": "My Smartsheet",
        "columns": processColumns(columns)
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
    column_headers = []

    # read csv file to be uploaded into smartsheet
    with open("sample.csv", "r") as csvfile:
        reader = csv.reader(csvfile)
        sniffer = csv.Sniffer()
        sample = csvfile.read(1024)
        csvfile.seek(0)

        # separate headers from rows with Sniffer
        if(sniffer.has_header(sample)):
            for row in reader:
                rows.append(row) 

        column_headers.append(rows[0])
        rows.pop(0)

        # create smartsheet
        smartsheet = createSmartsheet(column_headers)

        sheet_id = smartsheet[0]
        cols = smartsheet[1]

        print("sheet_id: " + str(sheet_id))
        print("cols: " + str(cols))

        # process rows as payload
        data = processRows(rows, cols)

        # API request to add rows
        response = requests.post("https://api.smartsheet.com/2.0/sheets/" + str(sheet_id) + "/rows", json=data, headers=getHeaders())
        
        return response.text
    
#populateSmartsheetFromCSV()

def addRows():
    rows = []
    column_headers = []

    # read csv file to be uploaded into smartsheet
    with open("sample.csv", "r") as csvfile:
        reader = csv.reader(csvfile)
        sniffer = csv.Sniffer()
        sample = csvfile.read(1024)
        csvfile.seek(0)

        # separate headers from rows with Sniffer
        if(sniffer.has_header(sample)):
            for row in reader:
                rows.append(row) 

        column_headers.append(rows[0])
        rows.pop(0)

        # indicate sheet_id
        sheet_id = 4017281675775876

        # indicate columns
        cols = [3742703808368516, 8246303435739012, 927954041261956, 5431553668632452]

        # process rows as payload
        data = processRows(rows, cols)

        # API request to add rows
        response = requests.post("https://api.smartsheet.com/2.0/sheets/" + str(sheet_id) + "/rows", json=data, headers=getHeaders())
        
        return response.text
    
# populateSmartsheetFromCSV()    
addRows()