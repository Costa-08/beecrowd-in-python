ntrilhas=int(input()) 
i1=0 
L=[] 
while i1!=ntrilhas: 
    trilha=list(input().split()) 
    npontos=int(trilha[0]) 
    i2=1 
    somac=0 
    somad=0 
    while i2!=npontos: 
        dif=int(trilha[i2+1])-int(trilha[i2]) 
        if dif>0: 
            somac=somac+dif 
        else: 
            somad=somad-dif 
        i2=i2+1 
    if somac<somad: 
        L.append(somac) 
    else: 
        L.append(somad) 
    i1=i1+1 
i3=1 
num=int(L[0]) 
tam=len(L) 
while i3!=tam: 
    if int(L[i3])<num: 
        num=int(L[i3]) 
    i3=i3+1 
melhortrilha=L.index(num)+1 
print(melhortrilha)
