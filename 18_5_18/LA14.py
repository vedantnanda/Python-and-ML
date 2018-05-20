#LA14 Number format change
#Accept a decimal number from user and print equivalent binary,octal,hexadecimal number using functions
def tobinary(dec):
    bb = ""
    while(dec>0):
        bb += str(dec%2)
        dec = dec//2
    return bb[::-1]
def tooct(dec):
    bb = ""
    while(dec>0):
        bb += str(dec%8)
        dec = dec//8
    return bb[::-1]
def tohex(dec):
    bb=""
    li = ["A","B","C","D","E","F"]
    while(dec>0):
        t = dec%16
        if t>9:
            bb += li[t-10]
        else:
            bb += str(t)
        dec = dec//16
    return bb[::-1]

dec = int(input("Enter decimal Integer: "))
sign = ""
if dec<0:
    sign="-"
bi = tobinary(abs(dec))
oc = tooct(abs(dec))
he = tohex(abs(dec))
if sign=="-":
    bi="-"+bi
    oc="-"+oc
    he="-"+he
print("Binary Equivalent of {0} is {1}".format(dec,bi))
print("Octal Equivalent of {0} is {1}".format(dec,oc))
print("Hexadecimal Equivalent of {0} is {1}".format(dec,he))