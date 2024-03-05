import os
import csv

census_csv = "12-Stu_CensusZip/Resources/census_starter.csv"

with open (census_csv, newline = "") as file:
    csvreader = csv.reader(file, delimiter = ",")

    Place = []
    Population = []
    Income = []
    Poverty_Count = []
    Poverty_Rate = []
    County = []
    State = []

    for row in csvreader:
        
        Place.append(row[0])
        Population.append(row[1])
        Income.append(row[4])
        Poverty_Count.append(row[8])
        Poverty_Rate.append((int(row[8])/int(row[1]))*100)
        
        split_place = row[0].split(", ")

        County.append(split_place[0])
        State.append(split_place[1])

cleaned_csv = list(zip (County, State, Population, Income, Poverty_Count,Poverty_Rate))

output_file = os.path.join("census_final1.csv")

with open(output_file, "w", newline = "") as datafile:
    csvwriter = csv.writer(datafile)


    csvwriter.writerow(["County", "State", "Population", "Per Capita Income", "Poverty Count", "Poverty Rate"])

    for row in cleaned_csv:
        csvwriter.writerow(row)