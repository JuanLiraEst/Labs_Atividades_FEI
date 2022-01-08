import random
sorteados = [28,18,3,46,33]
resultado=[]
x=0
while x<5:
    escolhido = random.choice(sorteados)
    if escolhido not in resultado:
        resultado.append(escolhido)
        x+=1
    if escolhido in resultado:
        x = x
resultado.sort()
print(resultado)
