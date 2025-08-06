njog, nrod = map(int, input().split())
Rodadas=list(map(int, input().split()))
Lpontos=[]
for i1 in range(njog):
    soma=0
    for i2 in range(nrod):
        soma+=Rodadas[i1+njog*i2]
    Lpontos.append(soma)

ijog=0
pontjog=Lpontos[0]
for i in range(1, njog):
    if Lpontos[i]>=pontjog:
        ijog=i
        pontjog=Lpontos[i]

print(ijog+1)
