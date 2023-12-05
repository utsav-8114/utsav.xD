a=int(input("a: "))
b=int(input("b: "))
if (a<b):
    a,b=b,a
while(b!=0):
    s,b=b,a%b
print("gcd is",a)