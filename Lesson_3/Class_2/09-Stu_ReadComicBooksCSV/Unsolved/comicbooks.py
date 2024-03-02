# Modules
import os
import csv

# Prompt user for title lookup

# Set path for file
csvpath = os.path.join("09-Stu_ReadComicBooksCSV/Resources/comic_books.csv")

# Set variable to check if we found the video
found = False
# Open the CSV using the UTF-8 encoding
with open(csvpath, encoding='UTF-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")


    # Loop through looking for the video
    title = []
    for row in csvfile:
        title.append(row[0])
        user_title = "Xenozoic"
        for row in title:
            if title == user_title:
                print(row)
                found = True

            # Set variable to confirm we have found the video

    # If the book is never found, alert the user
if not found:
    print("Book was not found")