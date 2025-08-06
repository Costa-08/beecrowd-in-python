div, ndiv, mult, nmult = map(int, input().split())
i=div
resp=-1
if (div==ndiv) or (mult==nmult) or (mult%div!=0):
    print(resp)
else:   
    while i<=mult:
        if mult%i==0:
            if i%ndiv!=0:
                if nmult%i!=0:
                    resp=i
                    break
        i=i+div
    print(resp)
