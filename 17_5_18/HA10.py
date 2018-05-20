#list of numbers divisible by 3
#HA10
n = int(input("Enter number of numbers: "))
l = []
for i in range(n):
	t = int(input("Enter number: "))
	if t%3 == 0:
		l.append(t)
print(l)
