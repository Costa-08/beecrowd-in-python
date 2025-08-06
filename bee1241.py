n=int(input())
i1=0
while i1!=n:
    nums=list(input().split())
    a=nums[0]
    b=nums[1]
    tam_a=len(a)
    tam_b=len(b)
    i2=0
    soma=0
    while i2!=tam_b:
        if a[tam_a-1-i2]==b[tam_b-1-i2]:
            soma=soma+1
        i2=i2+1
    if soma==tam_b:
        print("encaixa")
    else:
        print("nao encaixa")
    i1=i1+1
