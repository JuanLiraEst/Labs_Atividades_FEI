import random
jogos = []

numeros = []
for x in range(1,81):
    numeros.append(x)

def sortear():
    sorteados = []

    x=0
    while x<5:
        escolhido = random.choice(numeros)
        if escolhido not in sorteados:
            sorteados.append(escolhido)
            x+=1
        if escolhido in sorteados:
            x = x
    sorteados.sort()
    jogos.append(sorteados)

for x in range(20):
    sortear() #repetindo isso 20x, temos 20 listas dentro de uma

#_____________________________________
#outro método de sortear sem repetir:
#from random import sample
#sorteados = sample(range(1,81),5)
#sorteados.sort()
#_____________________________________
            


for x in range(len(jogos)):
    print("Jogo ",x+1,": ",jogos[x])


tds_numeros = []
qtde = 0
num = 0

for qtde in range(20):
    for num in range(5):
        tds_numeros.append(jogos[qtde][num])


repeticoes = {}

for x in range(len(tds_numeros)):
    chave = str(tds_numeros[x])
    if chave not in repeticoes:
        repeticoes[chave]= 1
    else:
        repeticoes[chave]+=1
        
print(repeticoes)