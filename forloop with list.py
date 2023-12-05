#wap in which after entering a name if the name contains(u,v,m,e) those items will be deleted and will be displayed;also display the final list
n=list(input("enter items for the list:"))
delete=input("enter ur choice item to be deleted:")
for i in n:
    if i==delete:
        r=[]
        n.remove(i)
        r.append(i)
        print("the popped element is:",r)
print("the final list is:",n)
