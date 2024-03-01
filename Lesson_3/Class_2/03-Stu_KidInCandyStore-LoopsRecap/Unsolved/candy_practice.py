candy_list = ["Snickers", "Kit Kat", "Sour Patch Kids", "Juicy Fruit", "Swedish Fish", "Skittles", "Hershey Bar", "Starbursts", "M&Ms"]

for (i, candy) in enumerate (candy_list,start = 1):
    print(str([i]),candy) 

allowance = 3
candy_cart = []
shopping = "y"

while shopping == "y":
    num = input("Pick the number of candy that you want: ")

    num = int(num) - 1

    candy_cart.append(candy_list[num])

    shopping = input("Do you want to keep shopping, (y)es or (n)o: ")

print("These are the candies you selected: ")
for candy in candy_cart:
        print(candy)


