import re

# method to extract only the necessary data from raw data
def processDataFromCSV(data):

    # loop to extract acronyme, tank and fuel
    rows = []
    for i in data[::2]:
        row = []
        splitted = i[0].split('.')

        row.append(splitted[0]) # acronyme
        row.append(splitted[1]) # tank
        row.append(i[4]) # fuel

        rows.append(row)

    # loop to extract ullage
    rows_ullage = []
    for i in data[1::2]:
        ullage = []
        splitted = i[0].split('.')

        ullage.append(i[4]) # ullage

        rows_ullage.append(ullage)

    # loop to merge the two above-mentioned loops
    for idx, i in enumerate(rows):
        i.append(rows_ullage[idx][0])

    return rows

def processDataFromExcel(data):
    rows = []

    # loop through each first element in pair
    for d in data[::2]:
        item = []

        # extract acronyms
        acronym = d[1].split('_')[0]
        item.append(acronym)

        # extract tank
        tank = re.findall(r'\d+', str(d[1].split('_')[1]))
        item.append('' if len(tank) == 0 else tank[0])

        # extract fuel and ullage
        fuelOrUllage = re.findall("[a-zA-Z]+", d[1].split('_')[1])   
        fuel = []
        ullage = [] 

        if (fuelOrUllage[0] == 'VL' or fuelOrUllage[0] == 'VLM' or fuelOrUllage[0] == 'VOLCAR'):
            fuel.append(d[2])
        if (fuelOrUllage[0] == 'VLMB' or fuelOrUllage[0] == 'ULLAGE' or fuelOrUllage[0] == 'Ullage'):
            ullage.append(d[2])
        
        item.append('' if len(fuel) == 0 else fuel[0])
        item.append('' if len(ullage) == 0 else ullage[0])
    
        rows.append(item)

    # loop through each second element in pair
    values = []
    for d in data[1::2]:
        values.append(d[2])

    #complete the items list
    for idx, row in enumerate(rows):
        if (len(row[2]) == 0):
            row[2] = values[idx]
        else:
            row[3] = values[idx]

    return rows