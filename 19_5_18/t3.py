#lambda function to calculate simple interest
si = lambda p,r,t : (p*r*t)/100
p = float(input("Enter principal: "))
r = float(input("Enter rate: "))
t = float(input("Enter time: "))
print(si(p,r,t))