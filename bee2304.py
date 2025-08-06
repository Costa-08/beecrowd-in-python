dados_iniciais=list(input().split())
val_ini=int(dados_iniciais[0])
numop=int(dados_iniciais[1])
d=val_ini
e=val_ini
f=val_ini
i=0
while i!=numop:
    oper=list(input().split())
    if oper[0]=="V":
        if oper[1]=="D":
            d=d+int(oper[2])
        if oper[1]=="E":
            e=e+int(oper[2])
        if oper[1]=="F":
            f=f+int(oper[2])
    if oper[0]=="C":
        if oper[1]=="D":
            d=d-int(oper[2])
        if oper[1]=="E":
            e=e-int(oper[2])
        if oper[1]=="F":
            f=f-int(oper[2])
    if oper[0]=="A":
        if oper[1]=="D":
            d=d+int(oper[3])
            if oper[2]=="E":
                e=e-int(oper[3])
            else:
                f=f-int(oper[3])
        if oper[1]=="E":
            e=e+int(oper[3])
            if oper[2]=="D":
                d=d-int(oper[3])
            else:
                f=f-int(oper[3])
        if oper[1]=="F":
            f=f+int(oper[3])
            if oper[2]=="E":
                e=e-int(oper[3])
            else:
                d=d-int(oper[3])
    i=i+1
print(d, e, f)
