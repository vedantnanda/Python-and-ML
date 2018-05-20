#LA15 Dictionary of Cubes
#Accept a number from the user and create a dictionary of all numbers starting from 1 and store the number and its cube in a dictionary. Print all the cubes in dictionary.
n = int(input("Enter number: "))
dic = {}
ll = []
for i in range(1,n+1):
    dic[i]=i*i*i
    ll.append(dic[i])
print(dic)
print(ll)