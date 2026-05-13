for i in range(0,5):
    print(i)
print("While")
i=0
while i < 5:
    print(i)
    i+=1

n=0
for j in range(10):
    n+=int(input('Digite o número '+str(j+1)+": "))
print("A média é "+str(n/10))


c=int(input("Digite um número: "))
while c >= 0:
    print(c)
    c=c-1
print("BOOM!")