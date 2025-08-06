msg=str(input())
crib=str(input())
tammsg=len(msg)
tamcrib=len(crib)
numtestes=tammsg-tamcrib+1
i1=0
i3=0
soma=0
while i1!=numtestes:
    i2=0
    while i2!=tamcrib:
        if crib[i2]==msg[i3]:
            break
        i2=i2+1
        i3=i3+1
    if i2==tamcrib:
        soma=soma+1
    i3=i1+1
    i1=i3
print(soma)
