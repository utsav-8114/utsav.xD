def valley(l):
    increasing=True
    decreasing=False
    if len(l)<=3:
        return False
    i=0
    while(l[i]>l[i+1]):
        i+=1
        decreasing=True
    while(i<len(l)-1):
        if l[i]<l[i+1]:
            i=i+1
            increasing=True
    if (increasing and decreasing)==True:
        return True
    else:
        return False
lst=[int(x) for x in input("enter the numbers").split(" ")]
print(valley(lst))