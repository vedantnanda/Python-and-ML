#Addition of marks in dictionary
#HA7
dictionary2 = {"Unix": 50,"Economics": 60,"Science": 70,"Chem":80,"Computer": 90,}
sum = 0
for i in dictionary2:
	sum+=dictionary2[i]
print("The total score is {0}.".format(sum))