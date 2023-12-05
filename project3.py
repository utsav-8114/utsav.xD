#Code to remove special characters from string
a="c#od#ta@nt__ra"
l1=list(a)
l2=[]
for i in l1:
    if i.isalpha==True:
        l2.append(i)
print(l2)
