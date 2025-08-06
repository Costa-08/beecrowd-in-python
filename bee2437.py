dists=list(input().split())
dx=int(dists[2])-int(dists[0])
if dx>=0:
    dx=dx
else:
   dx=-dx
dy=int(dists[3])-int(dists[1])
if dy>=0:
    dy=dy
else:
   dy=-dy
dtotal=dx+dy
print(dtotal)
