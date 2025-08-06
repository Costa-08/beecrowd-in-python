n1=int(input())
i1=0
while i1!=n1:
    n2=int(input())
    i2=0
    pos=0
    L1=[]
    while i2!=n2:
        num=str(input())
        L1.append(num)
        i2=i2+1
    i3=0
    while i3!=n2:
        var=L1[i3]
        if var=="LEFT":
            pos=pos-1
        elif var=="RIGHT":
            pos=pos+1
        else: 
            while (var!="RIGHT") and (var!="LEFT"):
                var=L1[int((var.split())[2])-1]
            if var=="LEFT":
                pos=pos-1
            elif var=="RIGHT":
                pos=pos+1
        i3=i3+1
    print(pos)
    i1=i1+1
