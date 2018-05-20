#LA12 Palindrome Check
#Accept a string and check if string is palindrome or not
s1 = str(input("Enter String: "))
if len(s1)==0:
    print("Empty String")
else:
    s2 = s1[::-1]
    if s1==s2:
        print("Palindrome")
    else:
        print("Not Palindrome")