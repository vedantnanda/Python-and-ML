a = float(input("Enter marks of first subject: "))
b = float(input("Enter marks of second subject: "))
c = float(input("Enter marks of third subject: "))
d = float(input("Enter marks of forth subject: "))
e = float(input("Enter marks of fifth subject: "))

avg = (a+b+c+d+e)/5
g=""
if avg>=90:
    g="A"
elif avg>=75:
    g="B"
elif avg>=60:
    g="C"
elif avg>=40:
    g="D"
else:
    g="F"
print("Average percentage = " + str(avg)+" grade = "+g)