lista1=list(input().split())
alturas=list(input().split())
numalts=int(lista1[0])
altpad=int(lista1[1])
i=0
soma=0
while i!=numalts:
    num=int(alturas[i])
    if num<altpad:
        dif=altpad-num
        alturas[i]=altpad
        alturas[i+1]=int(alturas[i+1])+dif
        soma=soma+dif
    if num>altpad:
        dif=num-altpad
        alturas[i]=altpad
        alturas[i+1]=int(alturas[i+1])-dif
        soma=soma+dif
    i=i+1
print(soma)
