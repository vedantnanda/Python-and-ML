#replace
oldstring = "I like python programming"
newstring = oldstring.replace("like","love")
print(newstring)

#what happens if no match
oldstring = "I like python programming"
newstring = oldstring.replace("khela","love")
print(newstring) #no change

#join
print("-".join(["34","55","46","75"]))

mySeq = ["Aditya","Rahul","Allen","Akanshya"]
print(" & ".join(mySeq))

#split
str1 = "cat,ball,apple,mango"
print(str1.split(","))
print(type(str1.split(",")))


str1 = "cat,ball,apple,mango"
ll = str1.split("p")
print("After splitting with p as separator: ",ll," lenth of list:",len(ll)) #the character that we split on that character is lost

