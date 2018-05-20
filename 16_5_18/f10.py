units = float(input("Enter units consumed: "))
a = 0.0;
if units<=50:
    a=units*0.5
elif units<=100:
    a = ((units-50)*0.75) + (50*0.5)
elif units<=200:
    a = (50*0.75) + (50*0.5) + (units-100)*1
else:
    a = (50*0.75) + (50*0.5) + (100 * 1)+ ((units-200)*1.8)
print("Amount to be paid: "+str(a))

