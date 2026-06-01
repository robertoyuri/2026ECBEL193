from xml.etree.ElementInclude import include

from six import print_

f=1
#e=int(input("escreva um numero:"))
#while(e>0):
#    f=f*e
#    e=e-1
print(f)

n=int(input("digite um numero inteiro:"))
primo = False
if n<2:
    primo = False
else:
    for i in range(2,n):
        if n % i == 0:
            primo=False
            break
        else:
            primo=True
if primo:
    print("Número é primo")
else:
    print("Número não é primo")

n=int(input("digite um numero entre 1 e 10:"))
i=1
while i<10:
    print(str(i) + "x" + str(n) + "="+ str(n*i))
    i+=1





