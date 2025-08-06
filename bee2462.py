Lista1=list(input().split())
i1=0
Lista2=[]
while i1!=4:
    num1=(int(Lista1[i1][0])*10+int(Lista1[i1][1]))*60 +int(Lista1[i1][3])*10+int(Lista1[i1][4])
    Lista2.append(num1)
    i1=i1+1
num2=Lista2[1]-Lista2[0]
num3=Lista2[3]-Lista2[2]
teste1=num2+num3
if teste1>0:
    tempo=int((num2+num3)/2)
    teste3=int((num2-tempo)/60)
    if (teste3<=12) and (teste3>-12):
        dif=teste3
    elif teste3<=-12:
        dif=teste3+24
    else:
        dif=teste3-24
else:
    teste5=int((num2+num3+1440)/2)
    if teste5<0:
        tempo=teste5+720
    else:
        tempo=teste5
    teste2=int((num2-tempo)/60)
    if (teste2<=12) and (teste2>-12):
        dif=teste2
    elif teste2<=-12:
        dif=teste2+24
    else:
        dif=teste2-24
print(tempo, dif)
