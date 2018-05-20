#create a lambda function to create sum of square of digits for 3 digit number
p1 = lambda x : int(x[0])**2+int(x[1])**2+int(x[2])**2
p2 = str(input("Enter 3 digit number: "))
print(p1(p2))