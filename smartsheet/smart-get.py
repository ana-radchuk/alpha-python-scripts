# Smartsheet data as a JSON via Smartsheet API
import json
import csv
import requests

sheet_id = 4030808692051844

# func to access token and the sheet_id stored in the env-var.json file
def getSmartsheet():
    with open("smart-token.json", "r") as datafile:
        creds = json.load(datafile)
    
        token = creds['token']

        # headers for the API
        headers = {
            'Authorization': token,
            'Accept': 'text/csv',
        }

        # API req
        response = requests.get('https://api.smartsheet.com/2.0/sheets/' + str(sheet_id), headers=headers)
        print(response.text)
        return response.text

csvData = getSmartsheet()

# read csv as a Python dict
data = []
reader = csv.DictReader(csvData.split('\n'), delimiter=',')

# Create a new func to append dict data into the new dataset
def processingJson():
     for rows in reader:
        dictData = rows
        data.append(dictData)

        # JSON dumps
        jsonData = json.dumps(data, indent=4)
        print(jsonData)

processingJson()
