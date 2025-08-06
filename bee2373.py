num_band=int(input())
i=0
soma=0
while i!=num_band:
    band=list(input().split())
    a=int(band[0])
    b=int(band[1])
    if a>b:
        soma=soma+b
    i=i+1
print(soma)
