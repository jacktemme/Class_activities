import os
import csv

cereal_csv = "01-Evr_CerealCleaner/Resources/cereal.csv"

with open (cereal_csv, newline = '') as file:
    csvreader = csv.reader(file, delimiter = ",")
    next(csvreader, None)

    for row in csvreader:
        if float(row[7]) >=5:
            print(row[0])

