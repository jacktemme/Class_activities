# Print Hello User!
print("Hello User")

number = 6

# Take in User Input
user_name = input("What is your name>")

# Respond Back with User Input
print("Hello " + user_name)

# Take in the User Favorite Number
favorite_number = input("What is your favorite number?")

# Respond Back with a statement based on your favorite number
if number < int(favorite_number):    
    print("Your favoritre number is greater than mine")
elif number > int(favorite_number):
    print("Your favorite number is less than mine")
else:
    print("Your favorite number is the same as mine")