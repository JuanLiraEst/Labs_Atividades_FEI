print("qual é o último dígito do seu número? Exemplo, o último dígito de 203 é 3")
q3 = input("Dígito: ")

lista = []
for x in range(1,101):
    lista.append(x)

newlista = []
for x in range(len(lista)):
    valor = str(lista[x])
    if x<10:
        if valor[0]==q3:
            newlista.append(lista[x])
    elif valor[1]== q3:
        newlista.append(lista[x])

print(newlista)