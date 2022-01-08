carros = []
carros.append(input(""))
carros.append(input(""))
carros.append(input(""))
carros.append(input(""))
carros.append(input(""))

consumo = []
consumo.append(float(input("")))
consumo.append(float(input("")))
consumo.append(float(input("")))
consumo.append(float(input("")))
consumo.append(float(input("")))

i = 0
for x in range(5): #de 0 a 4
    #usar variaveis no indice p descobrir a posicao
    if consumo[x] > consumo[i]:
        i = x #o x passará por todos os índices, salvando o maior smp
        #maior valor salvo em i. Agora, conectar com a outra lista
print(carros[i])

#em 1km:
for x in range(5):
    print(round(1000/consumo[x]))