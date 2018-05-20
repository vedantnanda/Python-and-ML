#LA-13
#Factorial Calculation Accept a number from user and calculate the factorial of the number using function
def fact(n):
    if n>=1:
        return(n*fact(n-1))
    else:
        return 1
n = str(input("Enter number: "))
l = n.split(".")
if len(l)>1:
    print("Number not Integer")
elif len(l)>2:
    print("Not a number")
elif int(n)<0:
    print("Negative not allowed")
else:
    print(fact(int(n)))