teste=1 
while True: 
    dbas=list(input().split()) 
    ql=int(dbas[0]) 
    interv=int(dbas[1]) 
    if (ql==0) and (interv==0): 
        break 
    i0=0 
    Lmed=[] 
    while i0!=ql: 
        num=int(input()) 
        Lmed.append(num)
        i0+=1
    soma1=0 
    for i in range(interv): 
        soma1+=Lmed[i] 
    num1=int(soma1/interv) 
    num2=int(soma1/interv) 
    varin=interv 
    for j in range(ql-interv): 
        soma1=soma1-Lmed[varin-interv]+Lmed[varin]
        novamed=(int(soma1/interv)) 
        if novamed>num2: 
            num2=novamed 
        if novamed<num1: 
            num1=novamed 
        varin=varin+1 
    print(f"Teste {teste}") 
    print(num1, num2) 
    print("") 
    teste=teste+1
