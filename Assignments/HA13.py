#HA13.List to dictionary mapping
#map 2 list, one with student name and other with roll number and save it as a dictionary.
#the output on should be:
#{"Name1":'12a1234',"Name2":'3456'}
di = {}
def todict(n,a):
    for i in range(len(n)):
        di[n[i]]=a[i]
    return di
n = ["Name1","Name2","Name3"]
r = ["1234","9asd0","asd12"]
print(todict(n,r))