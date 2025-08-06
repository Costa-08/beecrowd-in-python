risada=str(input())
quantl=len(risada)
i1=0
i2=quantl-1
Lc=[]
Ld=[]
while i1!=quantl:
    if risada[i1]=="a":
        Lc.append("a")
    if risada[i1]=="e":
        Lc.append("e")
    if risada[i1]=="i":
        Lc.append("i")
    if risada[i1]=="o":
        Lc.append("o")
    if risada[i1]=="u":
        Lc.append("u")
    i1=i1+1
while i2!=(-1):
    if risada[i2]=="a":
        Ld.append("a")
    if risada[i2]=="e":
        Ld.append("e")
    if risada[i2]=="i":
        Ld.append("i")
    if risada[i2]=="o":
        Ld.append("o")
    if risada[i2]=="u":
        Ld.append("u")
    i2=i2-1
if Lc==Ld:
    print("S")
else:
    print("N")
