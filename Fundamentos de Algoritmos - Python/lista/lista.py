import random
import time
#first: usuário monta a lista

list = []

qtde = int(input("Quantos números deseja adicionar na lista? "))

for x in range(1,qtde+1):
    numero = int(input("Digite o %dº número inteiro: "%x))
    x+=1
    list.append(numero)



a = random.randint(0,qtde-1)
b = random.randint(1,10)
list.insert(a,b)
print(list)
#adivinhação
#posicao = int(input("E quanto a posição, em qual você acha que o número está? "))

def chute2():
    
    if num_random2 == b:
        frase = "Você acertou o número"

    elif num_random2 > b:
        frase = "O número que você escolheu é maior que o meu"
    
        

    elif num_random2 < b:
        frase = "O número que você escolheu é menor que o meu"
    print(frase)
        
 


num_random = int(input("De 0 a 10, qual número você acha que eu adicionei? "))
if num_random == b:
    print("Você acertou o número")

elif num_random > b:
    print("O número que você escolheu é maior que o meu")
    num_random2 = int(input("Ok , vamos tentar de novo: qual número você acha que eu digitei? "))
    chute2()

elif num_random < b:
    print("O número que você escolheu é menor que o meu")
    num_random2 = int(input("Ok , vamos tentar de novo: qual número você acha que eu digitei? "))
    chute2()


