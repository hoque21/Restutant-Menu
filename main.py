print("Hello")

menu = {
    "pizza": 30,
    "Pasta": 20,
    "Burgur": 40,
    "Salad": 10,
    "Coffee": 303,
}
print("Welcome to my sweet caffee")

for item , price in menu.items():
    print(f"{item} : Bdt {price}")

order = 0
item1 = input("Enter the item name: ")
if item1 in menu:
    order += menu[item1]
    print(f"Your item {item1} has been added to the order")
else:
    print("Order isnot available at this moment")





item2 = input("Do you want to add another item?  (Yes/No)")

if item2  == "Yes" :
    item2 = input("Enter the second item name: ")
    if item2 in menu:
        order += menu[item2] 
        print(f"Your item {item2} has been added to the order")
    else:
        print("Order isnot available at this moment")


print(f"Total order is {order}")

