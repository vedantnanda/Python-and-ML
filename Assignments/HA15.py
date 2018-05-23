# HA15. Addition of elements
#Add elements in 2 list using map and lambda and print the list
l1 = [1,2,3,4,5]
l2 = [5,3,1,-1,-2]
s = lambda x,y: x + y
l3 = list(map(s,l1,l2))
print(l3)