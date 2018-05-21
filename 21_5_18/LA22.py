#LA-22. Number of occurances
#Read LotsOfwWrds.txt file and print the number of occurrences of the word "apple"
fo = open("LotsOfWords.txt","r")
l = fo.read().split()
c = 0
for i in l:
    if "apple" in i:
        c+=1
print("Number of 'apple' in file: ",c)
