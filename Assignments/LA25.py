#LA-25. Identity matrix Generation
#Take a number representing orderof a matrix from the user and
#create an identity matrix of that ordser using list comprehension
n = int(input("Enter size of matrix:  "))
for i in range(n):
    for j in range(n):
        if i==j:
            print("1 ",end="")
        else:
            print("0 ",end="")
    print("\n")