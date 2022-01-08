sorteados = [5, 31, 33, 46 ,55
,16 ,28, 36, 65 ,74,
28, 33, 44, 60, 61,
3, 18, 31, 37, 65,
1, 10, 20, 24, 46,
18, 19, 38, 49, 74,
14, 25, 49, 73, 77,
12, 47, 60, 69, 77,
20, 32, 38, 56, 65,
3, 21, 42, 64, 73,
28, 43, 61, 63, 67 ]
print(sorteados)
repeticoes = {}

for x in range(len(sorteados)):
    chave = str(sorteados[x])
    if chave not in repeticoes:
        repeticoes[chave]= 1
    else:
        repeticoes[chave]+=1

for chave, valor in repeticoes.items():
    print(chave,valor)
