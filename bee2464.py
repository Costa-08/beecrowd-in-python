pal="abcdefghijklmnopqrstuvwxyz"
tampal=len(pal)
i1=0
Alf=[]
while i1!=tampal:
    car1=pal[i1]
    Alf.append(car1)
    i1=i1+1
permut=str(input())
AlfPermut=[]
i2=0
while i2!=tampal:
    car2=permut[i2]
    AlfPermut.append(car2)
    i2=i2+1
crip=str(input())
tamcrip=len(crip)
i3=0
dcrip=""
while i3!=tamcrip:
    dcrip=dcrip+Alf[AlfPermut.index(crip[i3])]
    i3=i3+1
print(dcrip)
