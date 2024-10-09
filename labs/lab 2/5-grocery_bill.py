# prepare grocery bill, enter name of items purchased, qty, price per unit
no_of_items = int(input("enter number of items: "))
items = []
total_price = 0
for i in range(no_of_items):
    item_name = input("Item name: ")
    qty = input("qty: ")
    price = int(input("price: "))
    total_price += price
    items.append([item_name, qty, price])

print("******************************BILL******************************")
print()
print("Item Name                   Item quantity        Item price")
for desc in items:
    print(desc[0], "                        ", desc[1], "                ", desc[2])
print()
print("******************************")
print("Total amount to be paid")
print(total_price)
print("******************************")