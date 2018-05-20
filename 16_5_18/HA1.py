#unique ID generator
name = str(input("Enter Name: "))
phn = int(input("Enter 10 digit phn number: "))
if len(str(phn)) != 10:
    print("Phone number size not 10")
else:
    pin = str(input("Enter pin code: "))
    if len(pin) != 6:
        print("Pincode number size not 6")
    else:
        acc = str(input("Enter account type: "))
        if len(acc) != 1:
            print("Account type number size not 1")
        else:
            if len(str(phn))==10 and len(pin)==6 and len(acc)==1:
                id = ""
                id += pin[:6]
                l = []
                l = name.split()
                if len(l)>1:
                    id+=l[0][0]+l[1][0]
                elif len(l)==1:
                    id+=l[0][0]+l[0][0]
                ll = [')','!','@','#','$','%','^','&','*','(']
                phn = str(phn)
                sum = int(phn[0])+int(phn[1])+int(phn[2])+int(phn[3])+int(phn[4])+int(phn[5])+int(phn[6])+int(phn[7])+int(phn[8])+int(phn[9])
                if len(str(sum))==1:
                    id+=ll[sum]
                else:
                    sum = str(sum)
                    sum = int(sum[0])+int(sum[1])
                    if len(str(sum))==1:
                        id+=ll[sum]
                    else:
                        sum = str(sum)
                        sum = int(sum[0]) + int(sum[1])
                        if len(str(sum)) == 1:
                            id += ll[sum]
                id+=acc
                print(id)


