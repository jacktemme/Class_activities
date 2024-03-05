import os
import csv

# Path to collect data from the Resources folder
graduation_csv = "08-Evr_GraduatingFunctions/Resources/graduation_data.csv"
# Define the function and have it accept the 'state_data' as its sole parameter
def print_percentages(state_data):
    
    state_array = str(state_data[0])
    public_students = int(state_data [1])
    public_completed = int(state_data[2])
    non_prof_students = int(state_data[3])
    non_prof_completed = int(state_data[4])
    prof_students = int(state_data[5])
    prof_completed = int(state_data[6])



# Find the total students
    tot_students = public_students + non_prof_students + prof_students

# Find the total graduates
    tot_grads = public_completed + non_prof_completed + prof_completed
# Find the public school graduation rate
    pub_grad_rate = (public_completed / public_students) * 100
# Remember that some states do not have nonprofit or forprofit private schools
# Find the non-profit school graduation rate
    if non_prof_students != 0:
        non_prof_grad_rate = (non_prof_completed / non_prof_students) * 100
    else:
        non_prof_grate_rate = 0
# Find the for-profit school graduation rate
    if prof_students != 0:
        prof_grad_rate = (public_completed / public_students) * 100
    
    else:
        prof_grad_rate = 0

# Calculate the overall graduation ratetit
        tot_grad_rate = (tot_grads / tot_students) * 100
# Print out the state's name and its graduation rates

    print(f"Stats for {state_array}")
    print(f"Public School Graduation Rate: {pub_grad_rate}")
    print(f"Profit School Graduation Rate: {prof_grad_rate}")
    print(f"Non_Profit School Graduation Rate: {non_prof_grad_rate}")

# Read in the CSV file
with open(graduation_csv, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')

    header = next(csvreader)

    # Prompt the user for what state they would like to search for
    state_to_check = input("What state do you want to look for? ")

    # Loop through the data
    for row in csvreader:

        # If the state's name in a row is equal to that which the user input, run the 'print_percentages()' function
        if state_to_check == row[0]:
            print_percentages(row)
