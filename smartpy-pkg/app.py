from scripts.api_requests import *

################# VARIABLES #################
csv_filename = "./files/report.csv"
excel_filename = "./files/report-excel.csv"

# add Smartsheet
sheet_id = "" 

################ REQUESTS ##################

# update smartsheet from CSV file
updateSmartsheetFromCSV(csv_filename, sheet_id)
updateSmartsheetFromExcel(excel_filename, sheet_id)

# delete all rows in smarthseet
deleteAllRows(sheet_id)