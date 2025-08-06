cartas=list(input().split())
i=0
Lc=[]
Ld=[]
vaz=[]
while i!=4:
   if int(cartas[i])<int(cartas [i+1]):
      Lc.append(1)
   elif int(cartas[i])>int(cartas[i+1]):
      Ld.append(1)
   i=i+1
if (Lc==vaz) and (Ld!=vaz):
   print("D")
elif (Lc!=vaz) and (Ld==vaz):
   print("C")
else:
   print("N")
