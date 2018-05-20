#print number of days in the input month number
n = int(input("Enter month number: "))
if n == 1 or n ==3 or n == 5 or n == 7 or n == 8 or n == 10 or n == 12:
	print("Number of days in the month is 31")
elif n==2:
	print("Number of days in the month is 28/29")
else:
	print("Number of days in the month is 30")