a=int(input("enter in hours"))
if a<=12:
    print("ok you may continue")
else:
    print("error")
b=int(input("enter in mins"))
if b<=60:
    print("ok you may continue")
else:
    print("error")
c=int(input("enter in seconds"))
if c<=60:
    print("ok you may continue")
else:
    print("error")
s1=a*3600
s2=b*60
print(s1+s2+c)
