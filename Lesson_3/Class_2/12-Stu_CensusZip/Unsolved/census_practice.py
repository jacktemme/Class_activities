import os
import csv

census_csv = os.path.join("12-Stu_CensusZip/Resources/census_starter.csv")

place = []
population = []
income = []
poverty_count = []
poverty_percent = []
county = []
state = []

with open(census_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
    for row in csvreader:
        place.append(row[0])
        population.append(row[1])
        income.append(row[4])
        poverty_count.append(row[8])
        percent = round((int(row[8])/int(row[1])) *100, 2)
        poverty_percent.append(str(percent) + "%")

        split_place = row[0].split(", ")

        county.append(split_place[0])
        state.append(split_place[1])


zipped_csv = list(zip(county,state,population,income,poverty_count,poverty_percent))

out_file = os.path.join("final_census.csv")

with open(out_file, "w", newline='') as datafile:
    writer = csv.writer(datafile)

    writer.writerow(["County", "State", "Population", "Income", "Poverty Count","Poverty Percent"])
    
    for row in zipped_csv:
        writer.writerow(row)

