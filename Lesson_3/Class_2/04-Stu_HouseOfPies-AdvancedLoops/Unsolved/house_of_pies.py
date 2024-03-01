pie_list = [
    "Pecan", "Blueberry", "Apple","Pumpkin", "Shepards", "Banana Cream"
]

shopping = "y"
shopping_cart = []
print("Welcome to the House of Pies! Here are our pies:")

while shopping == "y":
    for pie in pie_list:
        print(f'[{str(pie_list.index(pie))}]) {pie}')



    selected_pie = input("Which number of pie do you want? ")

    shopping_cart.append(selected_pie)

    print("We'll have that " + pie_list[int(selected_pie)] + " pie, Right out for you" )

    shopping = input("Would you like to make another purchase: (y)es or (n)o ")


print("You purchased a total of " + str(len(shopping_cart)) + " pies")