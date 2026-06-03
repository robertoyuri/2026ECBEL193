from six import print_

matriz = []
for i in range(3):
    linha = []
    for j in range(3):
        elemento=int(input("digite M["+ str(i) + "][" + str(j) + "]"))
        linha.append(elemento)
    matriz.append(linha)
print(matriz)
for gabriel in range(3):
    print(matriz[gabriel][gabriel])