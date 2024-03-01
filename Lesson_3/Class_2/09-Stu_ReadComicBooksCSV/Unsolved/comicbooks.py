# Modules
import os
import csv

# Prompt user for title lookup

# Set path for file
csvpath = os.path.join(Users/jacktemme/Desktop/comic_books.csv)







# Set variable to check if we found the video

# Open the CSV using the UTF-8 encoding
with open(csvpath, encoding='UTF-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Loop through looking for the video
for row in csvreader:
        if row[0] == "comic":
                print("comic")
        else:
               print("not here")



            # Set variable to confirm we have found the video

    # If the book is never found, alert the user
