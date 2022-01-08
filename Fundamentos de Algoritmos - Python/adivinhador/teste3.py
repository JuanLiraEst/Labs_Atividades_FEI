lista = [4,14,24,34,44]

q4 = int(input("a soma dos dois dígitos é igual a?"))

numero_final = []

for x in range(len(lista)):
    valor = str(lista[x])

    dig_um = int(valor[0])
    if lista[x]>9:
        dig_dois = int(valor[1])
    
    if lista[x]<10:
        if dig_um== q4:
            numero_final.append(lista[x])

    elif dig_um + dig_dois == q4:
            numero_final.append(lista[x])
print(numero_final)