while True:
    k=str(input())
    if k=="0 0":
        break
    numq, valor = k.split()
    newvalor=""
    k=len(valor)
    for i in range(k):
        if valor[i]!=numq:
            newvalor+=valor[i]
    if newvalor=="":
        print(0)
    else:
        print(int(newvalor))
