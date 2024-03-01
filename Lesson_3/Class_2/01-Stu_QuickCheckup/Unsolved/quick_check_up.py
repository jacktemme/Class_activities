# Print Hello User!

print("Hello User!")
# Take in User Input

name = input("What is your name: ")
# Respond Back with User Input

print("Hello " + name)
# Take in the User Favorite Number
number = input("What is your favorite number: ")


# Respond Back with a statement based on your favorite number
if int(number) > 10:
    print("Your favorite number is greater than mine")
elif int(number) < 10:
    print("Your favorite number is less than mine")
else:
    print("Our favorite numbers are the same")
       