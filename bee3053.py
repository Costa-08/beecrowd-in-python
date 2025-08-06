n=int(input())
pos=str(input())
for i in range(n):
    t=int(input())
    if t==1:
        if pos=="A":
            pos="B"
        elif pos=="B":
            pos="A"
    elif t==2:
        if pos=="B":
            pos="C"
        elif pos=="C":
            pos="B"
    else:
        if pos=="A":
            pos="C"
        elif pos=="C":
            pos="A"
print(pos)
