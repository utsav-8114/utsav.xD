#wap in which after entering a name if the name contains(u,v,m,e) those items will be deleted and will be displayed;also display the final list
n=list(input("enter items for the list:"))
for i in n:
    if i=="u":
        r=[]
        n.remove(i)
        r.append(i)
        print(r)
print(n)
