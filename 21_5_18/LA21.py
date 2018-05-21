#LA-21. Prime numbers using list comprehension
#Print the prime numbers between 1 to 100 using list comprehension
l = [z for z in range(2,101) if z not in [x for x in range(1,101) for y in range(1,x//2+1) if(x%y==0 and y!=1 and y!=x)]]
print(l)
