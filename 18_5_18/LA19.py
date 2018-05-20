#LA19 Matrix Multiplication
#Write a program to take input for two matrices and perform multiplication on them
#print the resultant matrix
x1 = input("Enter size of matrix1: ").split()
x2 = input("Enter size of matrix2: ").split()
if x1[1] != x2[0]:
    print("Matrix multiplication not possible")
else:
    m1,m2,m3 =[],[],[]
    for i in range(int(x1[0])):
        m1.append(("0 "*int(x1[1])).split())
    for i in range(int(x2[0])):
        m2.append(("0 "*int(x2[1])).split())
    for i in range(int(x1[0])):
        m3.append(("0 "*int(x2[1])).split())
    for i in range(int(x1[0])):
       for j in range(int(x1[1])):
           m1[i][j]=int(input("for 1st matrix enter value at poisition{0}{1} ".format(i,j)))
    for i in range(int(x2[0])):
       for j in range(int(x2[1])):
           m2[i][j]=int(input("for 2nd matrix enter value at poisition{0}{1} ".format(i,j)))
    print(m2)
    sum = 0
    for i in range(int(x1[0])):
        for j in range(int(x2[1])):
            for k in range(int(x2[0])):
                sum = sum + m1[i][k]*m2[k][j]
            m3[i][j] = sum
            sum = 0
    print(m3)
