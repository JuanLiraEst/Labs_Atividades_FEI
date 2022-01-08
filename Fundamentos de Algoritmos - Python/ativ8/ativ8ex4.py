pares = []
impares = []
todos = []

for x in range(20):
    numeros = int(input(""))
    todos.append(numeros)

    if numeros%2==0:
        pares.append(numeros)
    else:
        impares.append(numeros)

print(*todos)
print(*pares)
print(*impares)

