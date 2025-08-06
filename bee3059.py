dadosin=list(input().split())
quant=int(dadosin[0])
smin=int(dadosin[1])
smax=int(dadosin[2])
vet=list(map(int, input().split()))
i1=0
soma=0
while i1!=len(vet):
    i2=i1+1
    while i2!=len(vet):
        if ((vet[i1]+vet[i2])>=smin) and ((vet[i1]+vet[i2])<=smax):
            soma=soma+1
        i2=i2+1
    i1=i1+1
print(soma)
