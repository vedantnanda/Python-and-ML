# HA16.Second paragraph reading
#Read a text file and print the second paragraph from the file
fo = open("2ndpara.txt","r")
s = (fo.read())
fo.close()
l = (s.split("\n\n"))
print(l[1])