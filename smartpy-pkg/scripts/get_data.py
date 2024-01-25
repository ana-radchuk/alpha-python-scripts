import csv

def getDataFromCSV(csv_filename):
    
    # open csv file
    with open(csv_filename, "r") as csvfile:

        # read lines in the file
        reader = csv.reader(csvfile)

        # run sniffer to get header titles
        sniffer = csv.Sniffer()
        sample = csvfile.read(1024)
        csvfile.seek(0)

        if(sniffer.has_header(sample)):
            next(reader)

        # get rows from csv file
        result = []
        
        for row in reader:
            result.append(row)

        # remove '*****' lines
        for item in result:
            for i in item:
                if '**' in i:
                    result.remove(item)

        # remove last 'End of Report' line
        result.pop()
    return result
    
def getDataFromExcel(excel_filename):

    # open csv file
    with open(excel_filename, "r") as csvfile:

        # read lines in the file
        reader = csv.reader(csvfile, delimiter=';')

        # run sniffer to get header titles
        sniffer = csv.Sniffer()
        sample = csvfile.read(1024)
        csvfile.seek(0)

        if(sniffer.has_header(sample)):
            next(reader)

        # get rows from csv file
        result = []
        
        for row in reader:
            result.append(row)

    return result