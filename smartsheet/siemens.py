import json
import requests
import csv

url = 'https://api.smartsheet.com/2.0/sheets/'
fileName = "report.csv"
sheet_id = 6450965704036228

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

# method to get column information
def getColumnInfo(sheet_id):

    # API call to get column information
    response = requests.get(url + str(sheet_id) + '/columns', headers=getHeaders())
    arr = response.json()['data']

    # get columns to be updated
    cols = []
    cols.append(arr[1]['id']) # get Acronyme ou CLLI 
    cols.append(arr[2]['id']) # get Tank
    cols.append(arr[3]['id']) # get Fuel
    cols.append(arr[4]['id']) # get Ullage

    return cols

def getDataFromCSV():
    
    # open csv file
    with open(fileName, "r") as csvfile:
        reader = csv.reader(csvfile)
        sniffer = csv.Sniffer()
        sample = csvfile.read(1024)
        csvfile.seek(0)

        if(sniffer.has_header(sample)):
            next(reader)

        # get rows from csv file
        result = []
        
        for row in reader:
            result.append(row)

        for item in result:
            for i in item:
                if '**' in i:
                    result.remove(item)

        result.pop()
        return result

# filter and clean data from csv    
def processDataFromCSV(data):
    rows = []
    for i in data[::2]:
        row = []
        splitted = i[0].split('.')

        row.append(splitted[0])
        row.append(splitted[1])
        row.append(i[4])

        rows.append(row)

    rows_ullage = []
    for i in data[1::2]:
        ullage = []
        splitted = i[0].split('.')

        ullage.append(i[4])

        rows_ullage.append(ullage)

    for idx, i in enumerate(rows):
        i.append(rows_ullage[idx][0])

    return rows

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

    # create payload
    for d in data:
        payload.append({
            "toBottom": True,
            "cells": d
        })

    return payload

def updateSmartsheet(sheet_id):

    # get raw csv data
    data = getDataFromCSV()

    # filter and clean data
    rows = processDataFromCSV(data)

    # indicate columns ids
    cols = getColumnInfo(sheet_id)

    # process rows as payload
    payload = processRows(rows, cols)

    # API request to add rows
    response = requests.post(url + str(sheet_id) + "/rows", json=payload, headers=getHeaders())
        
    print('Smartsheet #' + str(sheet_id) + ' was successfully updated')    
    return response.text

# get row ids from smartsheet
def getRows(sheet_id):

    response = requests.get(url + str(sheet_id), headers=getHeaders())
    data = response.json()['rows']

    rows = []
    for i in data:
        rows.append(i['id'])

    return rows

def deleteRows(sheet_id):

    # get all row ids
    rows = getRows(sheet_id)

    for row in rows:
        response = requests.delete(url + str(sheet_id) + "/rows?ids=" + str(row) + "&ignoreRowsNotFound=true", headers=getHeaders())

    print("All rows were successfully deleted")
    return response.text

updateSmartsheet(sheet_id)
# deleteRows(sheet_id)

