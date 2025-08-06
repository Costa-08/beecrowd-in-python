retanA=list(input().split())
retanB=list(input().split())
x0a, y0a, x1a, y1a = retanA
x0b, y0b, x1b, y1b = retanB
intersecX=not((int(x1b)<int(x0a)) or (int(x1a)<int(x0b)))
intersecy=not((int(y1b)<int(y0a)) or (int(y1a)<int(y0b)))
if intersecX and intersecy:
    print(1)
else:
    print(0)
