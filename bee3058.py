n=int(input())
i=0
L=[]
while i!=n:
    carne=list(input().split())
    preco=float(carne[0])
    grama=int(carne[1])
    fator=1000/grama
    prkg=preco*fator
    L.append(prkg)
    i=i+1
k=min(L)
print(f"{k:.2f}")
