# Incorporate the random library
import random

# Print Title
print("Let's Play Rock Paper Scissors!")

# Specify the three options
options = ["r", "p", "s"]

# Computer Selection
computer_choice = random.choice(options)
# User Selection
user_choice = input("Make your Choice: (r)ock, (p)aper, (s)cissors? ")

# Run Conditionals
if computer_choice == user_choice:
    print("Its a tie")
elif computer_choice == "r" and user_choice == "s":
    print("Computer chose rock, you lost!")
elif computer_choice == "p" and user_choice == "r":
    print("Computer chose paper, you lost!")
elif computer_choice == "s" and user_choice == "p":
    print("Computer chose scissors, you lost!")
elif computer_choice == "r" and user_choice == "p":
    print("Computer chose rock, you win!")
elif computer_choice == "s" and user_choice == "r":
    print("Computer chose scissors, you won!")
elif computer_choice == "p" and user_choice == "s":
    print("Computer chose rock, you lost!")
else:
    print("Entered the wrong input")





