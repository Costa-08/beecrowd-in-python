cartas=list(input().split())
if int(cartas[0])==int(cartas[1]):
    print(int(cartas[0]))
elif int(cartas[0])>int(cartas[1]):
    print(int(cartas[0]))
else:
    print(int(cartas[1]))
