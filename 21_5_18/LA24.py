#LA-24. Certificate
#One file contains details of student line Name, Roll number, Class and percentage.
#Another text file contains the sdample certificate printing data.
#Replace the sample copy with student details and keep a separate copy
#for all students who are in class 10 and have scored above 40%

try:
    fo = open("stulist.txt","r")
    l = fo.read()
    fo.close()
    ll = list(map(str,l.split("\n")))
    f1 = open("samplecertificate.txt","r")
    s = str(f1.read())
    f1.close()
    k = 1
    li = []
    lj = []
    for j in range(len(ll)):
        li.append(ll[j].split())
    for i in li:
        if i!=[] and int(i[2]) == 10 and float(i[3]) >=40 and k<len(li):
            c = "certificate{0}.txt".format(k)
            f2 = open(c,"w")
            f2.write(s.format(i[0],i[2],i[1],i[3]))
            f2.close()
            k +=1
except Exception as e:
    print("Eception Occured: ",e)