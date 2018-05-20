# LA18 Password Assignment
# WAP to check the validity of password and assign it to the user.
# Following are the criteria for checking the password:
# -At least 1 small character
# -At least 1 number
# -At least 1 special character
# -Min Length: 6
# -Max Length: 12
# Your program should accept a username from user and check if it is present in the predeclared list.
# If it is present, ask user for a password, assign it after checking validity and store it as a dictionary of username
def passetter():
    for i in range(3):
        cc = 0
        x = False
        sm = False
        cap = False
        num = False
        le = False
        p = str(input("Enter password: "))
        if (len(p) < 6 or len(p) > 12):
            print("length not in range(6-12)")
        else:
            for j in p:
                cc += 1
                if len(p) > 6 or len(p) < 12:
                    le = True
                t2 = ord(j)
                if (t2 >= 97 and t2 <= 122):
                    sm = True
                elif (t2 >= 65 and t2 <= 90):
                    cap = True
                elif (t2 >= 48 and t2 <= 57):
                    num = True
                elif (t2>0 and t2<127):
                    x = True
                if (cc == len(p)):
                    if (sm == False):
                        print("No small Letter present")
                    if (cap == False):
                        print("No capital letter present")
                    if (num == False):
                        print("No number present")
                    if (x == False):
                        print("No special character present")
                if (x and sm and cap and num and le):
                    return p
        if i != 2:
            print("Try again, Attempt -> {0}: ".format(i+2))
        if i == 2:
            return False
names = ["alpha", "beta", "charlie", "delta", "echo", "foxtrot"]
d2 = {}
nam = str(input("Enter name for which you want to set password: "))
if nam in names:
    pp = passetter()
    if type(pp) == bool:
        print("Password not set")
    else:
        d2[nam] = pp
        print("password set")
        print(d2)
else:
    print("Name not found")
