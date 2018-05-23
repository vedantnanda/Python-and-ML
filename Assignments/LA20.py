#LA 20-
#Create the grocery list in dictionary of name quantity and price.
#keep updating the list till user stops.
#if the name matches with previous  name, only update quantity with price.
#Print the list. Check if the items are within budget. Ask amount initially.
#if not keep updating the quantity, and use negative numbers to reduce quantity
#finally print qrocery amount and balance amount left
from typing import Dict
n = int(input("Enter number of vegetable you want to enter: "))
print("Enter vegetable and price per each with space in between: potato 5")
d = {}
for _ in range(n):
  l = input("Enter the vegetable and price of it: ").split()
  d[l[0]] = int(l[1])
print(d)
a = int(input("Enter your budget: "))
rm = a
gr = {}
bag = {}
while(True):
    print("Enter what you want to buy/replace and how much quantity")
    l = input("Enter the vegetable and quantity of it: ").split()
    if l[0] in d:
        if int(l[1])>0 and rm>0:
            if l[0] in gr:
                gr[l[0]]+=int(l[1])*d[l[0]]
                bag[l[0]] += int(l[1])
            else:
                gr[l[0]] = int(l[1]) * d[l[0]]
                bag[l[0]] = int(l[1])
        else:
            if int(l[1])>0 and rm<0:
                print("Out of Budget, cannot Buy")
            else:
                if l[0] not in bag:
                    print("Item not in bag")
                else:
                    if bag[l[0]]>=abs(int(l[1])):
                        bag[l[0]] += int(l[1])
                        gr[l[0]] += int(l[1])*d[l[0]]
                    else:
                        print("You do not have the quantity of {0} in your bag".format(l[0]))
    else:
        print("Item not in shop, cannot buy!!")
    rm = a -  sum([gr[x] for x in gr])
    print("Remaining balance: ",rm)
    print(gr,bag)
    b = input("Enter ~ to stop shopping else enter anything else to continue")
    if b=="~" and rm>=0:
        break
    elif b=="~" and rm<0:
        print("Balance out of budget can't exit")
print("Grocery list: ",gr,"\n Thanks for shopping!!")
