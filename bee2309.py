ordem=[4, 5, 6, 7, 12, 11, 13, 1, 2, 3]
vitA=0
vitB=0
nump=int(input())
i0=0
while i0!=nump:
    part=list(map(int, input().split()))
    i1=0
    somaA=0
    while i1!=3:
        if ordem.index(part[i1])>=ordem.index(part[i1+3]):
            somaA=somaA+1
        i1=i1+1
    if somaA>=2:
        vitA=vitA+1
    else:
        vitB=vitB+1
    i0=i0+1
print(vitA, vitB)
