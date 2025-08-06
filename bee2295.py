lista=list(input().split())
rendal=float(lista[2])/float(lista[0])
rendgas=float(lista[3])/float(lista[1])
if rendal>rendgas:
    print("A")
else:
    print("G")
