rh=str(input())
gh=str(input())
bh=str(input())
rd=int(rh, 16)
gd=int(gh, 16)
bd=int(bh, 16)
soma=1
if gd<=rd:
    qgreen=(rd//gd)**2
    soma=soma+qgreen
    if bd<=gd:
        qblue=(gd//bd)**2
        soma=soma+qgreen*qblue
result=hex(soma)
prefix="0x"
resultf = result.removeprefix(prefix)
print(resultf)
