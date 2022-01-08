import random
numeros = []
for x in range(1,21):
    numeros.append(x)

sorteados = []
for x in range(5):
    sorteado = random.choice(numeros)
    sorteados.append(sorteado)
print(sorteados)
repeticoes = {}

for x in range(len(sorteados)):
    chave = str(sorteados[x])
    if chave not in repeticoes:
        repeticoes[chave]= 1
    else:
        repeticoes[chave]+=1


print(repeticoes)


