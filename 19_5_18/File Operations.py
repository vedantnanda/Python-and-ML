fo = open("file1.txt","r")
print(fo.name)
print(fo.read())
#fo.write("new data") error
fo.close()



fo = open("file2.txt","w")
print(fo.name)
fo.write("data written on file")
#print(fo.read()) Error
fo.close()



#writing to a file
fo = open("file3.txt","w")
print(fo.name)
fo.write("First Name: {0}\nRoll No:{1}\nCollege:{2}\nThanks!".format(input("First Name:"),input("Enter Roll no:"),input("Enter College:")))
#print(fo.read())
fo.close()


#reading from a file
fo = open("file3.txt","r")
print(fo.name)
print(fo.read(15)) #number of bytes to be read from file
fo.close()

#appending to a file
fo = open("file2.txt","a")
print(fo.name)
print(fo.write("\nthis is the appended sentence"))
fo.close()