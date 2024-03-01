# The list of candies to print to the screen
candy_list = ["Snickers", "Kit Kat", "Sour Patch Kids", "Juicy Fruit", "Swedish Fish", "Skittles", "Hershey Bar", "Starbursts", "M&Ms"]

for (i, candy) in enumerate (candy_list,start = 1):
      print(i,candy)

                                 
# The amount of candy the user will be allowed to choose
allowance = 5

# The list used to store all of the candies selected inside of
candy_cart = []

# Print out options
print("which candy would you like to bring home?")
for x in range(allowance):
        selected = input("Which candy number do you want:")

        selected = int(selected) - 1

        candy_cart.append(candy_list[(selected )])


print("I brought home with me")
for candy in candy_cart:
    print(candy)

