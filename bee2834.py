def mod(n):
   if n<0:
      n=(-1)*n
   return n

L1=[3, 7, 11]
n, m = map(int, input().split())
xe, ye = map(int, input().split())
xs, ys = map(int, input().split())
nm=n*m
arm=int((n-1)*(m-1)/2)
if ((mod(xe-xs)+mod(ye-ys))//2)%2==0:
   if (n in L1) or (m in L1):
      print(nm-arm-2)
   else:
      print(nm-arm)
else:
   if (n in L1) or (m in L1):
      print(nm-arm)
   else:
      print(nm-arm-2)
