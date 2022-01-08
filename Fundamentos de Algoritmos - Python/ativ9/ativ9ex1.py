matriz = []

for numero_linha in range(2):
    linha = []
    for numero_coluna in range(2):
        linha.append(int(input("Digite o elemento da linha %d e coluna %d: "%(numero_linha,numero_coluna))))
    matriz.append(linha)

maior = matriz[0][0]
for numero_linha in range(2):
    for numero_coluna in range(2):
        while matriz[numero_coluna][numero_linha]>maior:
            maior = matriz[numero_coluna][numero_linha]

print("Matriz resultante:")
for numero_linha in range(2):
    for numero_coluna in range(2):
        print("%3d"%(matriz[numero_linha][numero_coluna]*maior), end = " ")
    print("")
