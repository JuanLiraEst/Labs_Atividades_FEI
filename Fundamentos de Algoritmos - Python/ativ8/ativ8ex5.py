lista1 = []
lista2 = []

tamanho = int(input("Digite a dimensão dos vetores: "))

print("Digite o vetor 1:")
for x in range(tamanho):
    x1 = int(input(""))
    lista1.append(x1)    

print("Digite o vetor 2:")
for x in range(tamanho):
    x2 = int(input(""))
    lista2.append(x2)   

resultado = 0
for x in range(tamanho):
    multipl = lista1[x]*lista2[x]
    resultado = resultado + multipl

print(resultado)