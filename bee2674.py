def isprime(n):
    if n<2:
        return False
    primo=True
    k=int(n**(1/2))+1
    for i in range(2, k):
        if n%i==0:
            primo=False
            break
    return primo

def isdigitprime(n):
    digprimos=True
    strnum=str(n)
    for i in range(len(strnum)):
        if (strnum[i]=="0") or (strnum[i]=="1") or (strnum[i]=="4") or (strnum[i]=="6") or (strnum[i]=="8") or (strnum[i]=="9"):
            digprimos=False
            break
    return digprimos

try:
    while True:
        n=int(input())
        if isprime(n)==False:
            print("Nada")
        elif isdigitprime(n)==False:
            print("Primo")
        else:
            print("Super")
except EOFError:
    exit()
