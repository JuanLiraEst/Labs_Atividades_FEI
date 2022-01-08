from math import sqrt
lista = []

tamanho = int(input("Qual o tamanho da lista: "))

print("Digite os valores:")

somatoria = 0
somatoria_desvio = 0
for x in range(tamanho):
    valores = int(input(""))
    lista.append(valores)
    somatoria = somatoria + lista[x]
    media = somatoria/tamanho
    
for x in range(tamanho):    
    somatoria_desvio = somatoria_desvio + ((lista[x]- media)**2)
    desvio = sqrt(somatoria_desvio/tamanho)

print("Média = %.2f e Desvio = %.4f"%(media,desvio))

