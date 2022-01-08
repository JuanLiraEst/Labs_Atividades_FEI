from random import randint

matriz = []

#trabalhar com duas variaveis pra manipular a 
#matriz a.k.a lista alinhada
#um for gera as linhas, e o outro gera os valores
for numero_linha in range(10):
    linha = []
    for numero_coluna in range(15):
        linha.append(randint(0,100))
    matriz.append(linha)

for numero_linha in range(len(matriz)):
    for numero_coluna in range(len(matriz[numero_linha])):
        print("%3d" % matriz[numero_linha][numero_coluna], end = "")

for linha in range(len(matriz)):
    print(matriz[linha][2], end=" ")
    