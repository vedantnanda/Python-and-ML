#celcius to farenheit using lambda and map
#23 45.5 87.3 34.3 -56.5
l=[]
#l = list(map(faren,list(map(float,input().split()))))
l = list(map(lambda c : c * 1.8 +32,list(map(float,input().split()))))
print(l)