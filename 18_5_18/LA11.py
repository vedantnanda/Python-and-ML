
#LA-11 Chess board checker
#Find the colour at a particular position of the chess board a1,a3,b2 are black but a2,a4,b1 are white User enter "e7" it should print "Black Position"
u = str(input("Enter position: "))
row = u[0]
if((ord(u[1])<48 or ord(u[1])>57) or len(u)>2):
    print("Error input")
else:    
    col = int(u[1])
    if col>0 and col<9:    
        if row in ['a','b','c','d','e','f','g','h']:
            l1 = ['a','c','e','g']
            if row in l1:
                if col in [1,3,5,7]:
                    print("Black position")
                else:
                    print("white position")
            else:
                print("white position")
        else:
            print("Wrong input")
    else:
        print("Wrong input")