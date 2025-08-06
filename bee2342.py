numax=int(input())
oper=list(input().split())
a=int(oper[0])
b=int(oper[2])
if oper[1]=="+":
    result=a+b
else:
    result=a*b
if result>numax:
    print("OVERFLOW")   
else:
    print("OK")
