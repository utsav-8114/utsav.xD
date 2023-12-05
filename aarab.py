a=input("enter list of numbers: ")
l1=a.split(",")
b=[]
for i in a:
    for j in a:
        for k in a:
            if (i!=j) and (j!=k) and (i!=k):
                if i+j+k==0:
                    b.append(i)
                    b.append(j)
                    b.append(k)
print(b)