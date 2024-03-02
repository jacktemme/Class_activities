import csv

import csv
with open('/Users/jacktemme/Desktop/Class_activities/Lesson_3/Class_2/09-Stu_ReadComicBooksCSV/comic_books.csv', mode ='r') as file: 
	csvFile = csv.DictReader(file)
	for lines in csvFile:
			print(lines)
