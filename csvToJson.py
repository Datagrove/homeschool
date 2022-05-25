#!/usr/bin/python
import csv, json

# print("hello")

csvFilePath = 'staterequirements.csv'
jsonFilePath = 'stateRequirementsJSON.json'

data = {}
with open(csvFilePath) as csvFile:
    csvReader = csv.DictReader(csvFile)
    for rows in csvReader:
        id = rows["State"]
        data[id] = rows

with open(jsonFilePath, 'w') as jsonFile:
    jsonFile.write(json.dumps(data, indent=4))