# recebimento dos dados iniciais
dadosiniciais=list(input().split())
qpostos=int(dadosiniciais[0])
qcars=int(dadosiniciais[1])
qleits=int(dadosiniciais[2])
# Recebimento dos sinais e transformar em lista (Lsinais)
i1=0
Lsinais=[]
while i1!=qleits:
    pos=list(input().split())
    Lsinais.append(pos)
    i1=i1+1
# Leitura de Lsinais por cada carrinho e criação da lista de posições (Lpos)
Lpos=[]
i2=1
while i2!=qcars+1:
    i3=0
    pos=[0, 0, 0]
    while i3!=qleits:
        if int(Lsinais[i3][0])==i2:
            posatual=int(pos[1])
            if posatual<qpostos:
                possnovpos=posatual+1
            else:
                possnovpos=1
            if int(Lsinais[i3][1])==possnovpos:
                if posatual==qpostos:
                    pos[0]=int(pos[0])+1
                pos[1]=possnovpos
                pos[2]=i3+1
        i3=i3+1
    Lpos.append(pos)
    i2=i2+1
# Leitura de Lpos e transformação em lista na ordem correta (Lresult)
Lresult=[]
i4=0
while i4!=qcars:
    num1=int(Lpos[0][0])*qpostos+int(Lpos[0][1])
    num2=int(Lpos[0][2])
    num3=1
    k=len(Lpos)
    i5=1
    while i5!=k:
        x=int(Lpos[i5][0])*qpostos+int(Lpos[i5][1])
        y=int(Lpos[i5][2])
        z=i5+1
        if (x>num1) or ((x==num1) and (y<num2)):
            num1=x
            num2=y
            num3=z
        i5=i5+1
    Lresult.append(num3)
    Lpos[num3-1]=[0, 0, 0]
    i4=i4+1
# Transformação da lista correta em string como pedido
resp=str(Lresult[0])
i6=1
while i6!=qcars:
    resp=resp+" "+str(Lresult[i6])
    i6=i6+1
print(resp)
