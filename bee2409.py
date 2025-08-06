while True: 
    dadin=list(map(int, input().split())) 
    if dadin==[0, 0, 0]: 
        break 
    ar=dadin[0] 
    l1=dadin[1]+1 
    l2=dadin[2]+1 
    dadtri=list(map(int, input().split())) 
    if dadtri[2]>dadtri[1]: 
        propar=dadtri[0]*(dadtri [2]-dadtri[1]) 
    else: 
        propar=dadtri[0]*(dadtri[1]-dadtri[2]) 
    novaar=round(ar*(propar/(l1*l2))) 
    print(novaar)
