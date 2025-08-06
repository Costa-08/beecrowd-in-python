Lnump=[]
Lpen=[]
while True:
    nump=int(input())
    if nump==0:

        break
    pessoas=list(input().split())
    Lnump.append(nump)
    Lpen.append(pessoas)
numtestes=len(Lnump)
i1=0
teste=1
while i1!=numtestes:
    print(f"Teste {teste}")
    i2=0
    while True:
        if (Lpen[i1])[i2]==str(i2+1):
            venc=(Lpen [i1])[i2]
            break
        i2=i2+1
    print(venc)
    print("")
    i1=i1+1
    teste=teste+1
