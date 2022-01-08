numero = [83,85,87,88,89]
valor = str(numero)
print(valor[0])
for x in range(len(numero)):
    valor = str(numero[x])
    if valor[1]=="5":
        print(numero[x]," acaba com 5")
    else:
        print("Não acaba com 5")