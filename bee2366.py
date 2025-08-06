lista1=list(input().split())
pontos=list(input().split())
nump=int(lista1[0])
dim=int(lista1[1])
i1=0
while i1!=nump-1:
    dist=int(pontos[i1+1])-int(pontos[i1])
    if dist>dim:
        break
    i1+=1
if dist>dim:
    print("N")
elif int(pontos[nump-1])+dim<42195:
    print("N")
else:
    print("S")
