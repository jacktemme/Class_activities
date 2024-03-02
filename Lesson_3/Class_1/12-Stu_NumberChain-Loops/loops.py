proceed = "y"

while proceed == "y":
    num = input("How many numbers do you want to print out? ")
    
    num = int(num) + 1
    for x in range(num):
        print(x)
    proceed = input("Do you want to continue: (y)es or (n)o ")
    