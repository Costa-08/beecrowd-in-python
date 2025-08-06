nterrits=int(input())
territs=list(input().split())
i1=0
soma1=0
while i1!=nterrits:
    soma1=soma1+int(territs[i1])
    i1=i1+1
metade=soma1/2
soma2=0
i2=0
while soma2!=metade:
    soma2=soma2+int(territs[i2])
    i2=i2+1
print(i2)
