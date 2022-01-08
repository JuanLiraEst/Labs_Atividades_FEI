print("_______________________________________")
print(" Projeto: Números Complexos em Python")
print(" Gabriel Lopez Vendramini RA 22121015-6")
print(" Juan Lira Estevão RA 22121033-9    ")
print("_______________________________________")


w = complex(input("Digite o valor de w: "))
M = int(input("Digite a quantidade de números da sequência: "))
eps = float(input("Digite o valor de épsilon: "))

z = [0]
for x in range(M):
    z.append(z[x]**2 + w)
z.pop(0)

conferes = []
maior_dist = []

for x in range(M-1):
    maior_dist.append(abs(z[x] - z[M-1]))
    if maior_dist[x] > eps:
        frase = "não"
        conferes.append(frase)
    else:
        frase = "sim"
        conferes.append(frase)

print("Nossa sequência possui os valores:\n", z , "\n")
print("As distâncias entre os índices e o último índice da lista:\n", maior_dist, "\n")
print("Esses valores são menores que o valor de epsolon?\n",conferes,"\n")


if conferes[0] == "sim":
    print("O menor índice (menor que o valor de épsolon) é o 1 \n")


if conferes[0] == "não":
    x=0
    while conferes[x] == "não":
        x+=1
        if conferes[x] == "sim":
                indice = x+1
                print("O menor índice (menor que o valor de épsolon) é o ",indice, "\n")
                break
        else:
            x = x





        #indice = x +1
        #print("OBS: Estamos considerando o primeiro valor como índice 1:")
        #print("O menor índice (menor que o valor de épsolon) é o ",indice, "\n")
        #break
    #else:
     #   print("Não há nenhum índice que satisfaça (dist < epsolon)\n")
      #  break 




