import csv
import os

graduation_csv = "08-Evr_GraduatingFunctions/Resources/graduation_data.csv"

def print_percentages(state_data):

    state = str(state_data[0])
    pub_students = int(state_data[1])
    pub_grads = int(state_data[2])
    non_prof_students = int(state_data[3])
    non_prof_grads = int(state_data[4])
    prof_students = int(state_data[5])
    prof_grads = int(state_data[6])


    pub_rate = (pub_grads/pub_students)* 100

    if non_prof_grads != 0: 
        non_prof_rate = (non_prof_grads/non_prof_students)* 100
    else:
        non_prof_rate = 0

    if prof_grads != 0:
        prof_rate = (prof_grads/prof_students)* 100

    else:
        prof_rate = 0

    tot_students = pub_students + non_prof_students + prof_students
    tot_grads = pub_grads + non_prof_grads + prof_grads
    overall_grad_rate = (tot_grads / tot_students) * 100

    if overall_grad_rate > 50:
        message = "graduation success"
    else:
        message = "state needs improement"

    print(f"For {state}: ")
    print(f"Public school graduation rate was {pub_rate}")
    print(f"Non-Profit school graduation rate was {non_prof_rate}")
    print(f"Profit school graduation rate was {prof_rate}")
    print(f"Overall graduation rate was {overall_grad_rate} meaning {message}")


with open(graduation_csv, newline = '') as file:
    csvreader = csv.reader(file, delimiter = ",")
    next(csvreader, None)

    state_choice = input("Enter state that you want to look at: ")
    for row in csvreader:
        if row [0] == state_choice:
            print_percentages(row)


