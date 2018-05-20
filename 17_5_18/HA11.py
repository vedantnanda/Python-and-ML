#Calculator using function
#HA11
def addit(a,b):
	return(a+b)
def subit(a,b):
	return(a-b)
def mulit(a,b):
	return(a*b)
def divit(a,b):
	return(a/b)

print("Calculator using function")
n1 = float(input("Enter first number: "))
n2 = float(input("Enter second number: "))
ch = str(input("Enter choice(A:Addition,S:Substraction,M:Multiplication,D:Division):  "))

if n2 == 0:
	print("Division by zero not possible")
else:
	if ch == 'A' or ch == 'a':
		print("The Addition of {0} and {1} is {2}".format(n1,n2,addit(n1,n2)))
	elif ch == 'S' or ch == 's':
		print("The Substraction of {0} and {1} is {2}".format(n1,n2,subit(n1,n2)))
	elif ch == 'M' or ch == 'm':
		print("The Multiplication of {0} and {1} is {2}".format(n1,n2,mulit(n1,n2)))
	elif ch == 'D' or ch == 'd':
		print("The Division of {0} and {1} is {2}".format(n1,n2,divit(n1,n2)))

