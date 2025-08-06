prod1=list(input().split())
prod2=list(input().split())
cust1=int(prod1[1])*float(prod1[2])
cust2=int(prod2[1])*float(prod2[2])
custototal=cust1+cust2
print("VALOR A PAGAR: R$", "{:.2f}".format(custototal))
