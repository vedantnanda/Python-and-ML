#LA16 Phonebook Number Check
#Create a Phonebook by taking 10 names and phone number from user and store as a dictionary of (name,number).<br>
#Ask user to enter a number and print the name of the person after searching for the number.

phn = {}
n = int(input("Enter number of names: "))
if n<=0:
    print("Phone book size invalid")
else:
    for i in range(n):
        n1 = str(input("Enter name: "))
        n2 = int(input("Enter number: "))
        phn[n1]=n2
    ch = int(input("Enter number you want to search: "))
    f = False
    for i in phn:
        if phn[i]==ch:
            print("The person with number {0} is {1}".format(ch,i))
            f = True
    if f==False:
        print("Number {0} not present in phonebook".format(ch))