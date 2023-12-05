def frequency(l):
    s=l
    s=sorted(s)
    c=0
    lt1=[]
    lt2=[]
    lt3=[]
    ck=[]
    for i in s:
        for j in s:
            if i==j:
                c=c+1
        ck.append(c)
        c=0
    mx=max(ck)
    mn=min(ck)
    for i in s:
        for j in s:
            if i==j:
                c=c+1
        if ((i not in lt1) and (c==mn)):
            lt1.append(i)  
        if ((i not in lt2) and (c==mx)):
            lt2.append(i)
        c=0
    lt3=[]
    lt3.append(lt1)
    lt3.append(lt2)
    
    lt3.append(mn)
    lt3.append(mx)
    freq=tuple(lt3)
    return(freq)
l1=[int(x) for x in input("Please Enter sep by spaces").split(" ")]
print(frequency(l1))

        
        