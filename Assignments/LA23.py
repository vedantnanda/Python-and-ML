# LA-23 Inverse of numbers to take numbers from user and store them to a list.
#Then add the inverse of all numbers and print sum
li = []
sum = 0.0
m = int(input("Rnter number of numbers you want to enter: "))
for i in range(m):   
    n = (input("Enter number(q to stop and show sum):"))
    if n=="q":
        break
    else:
        n=float(n)
    try:
        li.append(1/n)
        sum += 1/n
    except ZeroDivisionError:
        print("Zero not allowed!")
print(li,"\nSum of all inverse: ",sum)