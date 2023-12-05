import math
n=int(input("enter the number of values: "))
pi=22/7
for i in range(1,n+1):
    print("{:.{}f}".format(pi,i))    