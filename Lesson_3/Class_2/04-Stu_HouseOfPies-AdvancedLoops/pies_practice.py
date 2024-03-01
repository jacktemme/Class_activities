Pie_list = ["Pecan",  "Apple Crisp", "Bean", "Banoffee", "Black Bun", " Blueberry", "Buko",  "Burek", "Tamale", "Steak"]

print("Welcome to the House of Pies! Here are our pies: ")
for (i,pie) in enumerate(Pie_list, start = 1):
    print(str([i]),pie)

shopping = "y"
pie_cart = []
pie_amount = [0,0,0,0,0,0,0,0,0,0]

while shopping == "y":
    pie_num = input("Select which number of pie that you want: ")

    pie_num = int(pie_num) - 1
    pie_cart.append(Pie_list[pie_num])

    pie_amount[pie_num] = pie_amount[pie_num] + 1

    shopping = input("Do you want to continue shopping: (y)es or (n)o \n")
    
print("You selected these pies: ")

final = list(zip(pie_amount,Pie_list))
for x in final:
    print(x)