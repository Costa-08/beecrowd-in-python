n=int(input())
while n!=0:
    i=0
    pjog1=0
    pjog2=0
    while i!=n:
        jogs=list(input().split())
        jog1=int(jogs[0])
        jog2=int(jogs[1])
        if jog1>jog2:
            pjog1+=1
        if jog2>jog1:
            pjog2+=1
        i+=1
    print(pjog1, pjog2)
    n=int(input())
