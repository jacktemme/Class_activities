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
    print("Computer wins")
elif computer_choice == "p" and user_choice == "r":
    print("Computer wins")
elif computer_choice == "s" and user_choice == "p":
    print("Computer wins ")
elif computer_choice == "r" and user_choice == "s":
    print("Computer wins")
elif computer_choice == "p" and user_choice == "s":
    print("You win")
elif computer_choice == "s" and user_choice == "r":
    print("You win")
else:
    print("You win")



