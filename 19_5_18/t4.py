#lambda function for celcius to farenheit
faren = lambda c : c * 1.8 +32
c = float(input("Enter temperature in celcius: "))
print("farenheit value of celius degree {0} is {1}".format(c,faren(c)))