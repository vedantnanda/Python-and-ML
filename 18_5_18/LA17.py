#LA-17 Guess-the-Number Game
#A user get 3 chances to identify a number.
#Once the number is entered, it should print if the input is near range or far range.
#if the number is identified, print winning statement.
#The total range of number is 0 to 10. The near range is +-3 numbers.
import random
r = random.randrange(0, 11,1)
rl = [j for j in range(r-3,r+4)]
print(r,rl)
x = False
for i in range(3):
    n = int(input("Enter guess {0}: ".format(i+1)))
    if n==r:
        print("You Win")
        x = True
    elif n in rl:
        print("Near guess")
    else:
        print("Far guess")
    if x==True:
        break
    if i==2 and x==False:
        print("You lose")