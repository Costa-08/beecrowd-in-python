grid=list(input().split())
nlinhas=int(grid[0])
ncolunas=int(grid[1])
i1=0
L1=[]
while i1!=nlinhas:
    linhan=list(input().split())
    L1.append(linhan)
    i1=i1+1
L2=[]
i2=0
while i2!=nlinhas:
    i3=0
    soma1=0
    while i3!=ncolunas:
        num1=int((L1[i2])[i3])
        soma1=soma1+num1
        i3=i3+1
    L2.append(soma1)
    i2=i2+1
i4=0
while i4!=ncolunas:
    i5=0
    soma2=0
    while i5!=nlinhas:
        num2=int((L1[i5])[i4])
        soma2=soma2+num2
        i5=i5+1
    L2.append(soma2)
    i4=i4+1
k=int(L2[0])
i6=1
q=len(L2)
while i6!=q:
    if int(L2[i6])>k:
        k=int(L2[i6])
    i6=i6+1
print(k)
