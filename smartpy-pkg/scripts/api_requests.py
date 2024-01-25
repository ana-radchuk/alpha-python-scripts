from scripts.get_data import *
from scripts.process_data import * 

import requests
import json

# main method to update smartsheet by extracting data from excel
def updateSmartsheetFromExcel(excel_filename, sheet_id):
    
   # get raw  data
    data = getDataFromExcel(excel_filename)

    # filter and clean data
    rows = processDataFromExcel(data)

    # indicate columns ids
    cols = getColumnIds(sheet_id)

    # process rows as payload
    payload = createPayload(rows, cols)

    # API request to add rows
    response = requests.post("https://api.smartsheet.com/2.0/sheets/" + str(sheet_id) + "/rows", json=payload, headers=getHeaders())
        
    print('Smartsheet #' + str(sheet_id) + ' was successfully updated')    
    return response.text

# main method to update smartsheet by extracting data from csv
def updateSmartsheetFromCSV(csv_filename, sheet_id):

    # get raw csv data
    data = getDataFromCSV(csv_filename)

    # filter and clean data
    rows = processDataFromCSV(data)

    # indicate columns ids
    cols = getColumnIds(sheet_id)

    # process rows as payload
    payload = createPayload(rows, cols)

    # API request to add rows
    response = requests.post("https://api.smartsheet.com/2.0/sheets/" + str(sheet_id) + "/rows", json=payload, headers=getHeaders())
        
    print('Smartsheet #' + str(sheet_id) + ' was successfully updated')    
    return response.text

# delete all rows in smartsheet
def deleteAllRows(sheet_id):

    # get all row ids
    rows = getRowIds(sheet_id)

    for row in rows:
        response = requests.delete("https://api.smartsheet.com/2.0/sheets/" + str(sheet_id) + "/rows?ids=" + str(row) + "&ignoreRowsNotFound=true", headers=getHeaders())

    print("All rows were successfully deleted")
    return response.text

# get column ids from smartsheet
def getColumnIds(sheet_id):

    # API call to get column information
    response = requests.get("https://api.smartsheet.com/2.0/sheets/" + str(sheet_id) + '/columns', headers=getHeaders())
    arr = response.json()['data']

    # get columns to be updated
    cols = []
    cols.append(arr[1]['id']) # get Acronyme ou CLLI 
    cols.append(arr[2]['id']) # get Tank
    cols.append(arr[3]['id']) # get Fuel
    cols.append(arr[4]['id']) # get Ullage

    return cols

# get row ids from smartsheet
def getRowIds(sheet_id):

    response = requests.get("https://api.smartsheet.com/2.0/sheets/" + str(sheet_id), headers=getHeaders())
    data = response.json()['rows']

    rows = []
    for i in data:
        rows.append(i['id'])

    return rows

# utility method to create headers to pass API request
def getHeaders():

    # open file that holds authentication token
    with open("./files/smart-token.json", "r") as datafile:
        creds = json.load(datafile)
        token = creds['token']

        # create headers object
        headers = {
            'Authorization': token,
            'Content-Type': 'application/json'
        }

    return headers

# utility method to produce payload
def createPayload(rows, cols):

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