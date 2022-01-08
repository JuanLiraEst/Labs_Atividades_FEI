quantidade = int(input("Quantos números deseja digitar?"))
base=0
soma=0

while(base<quantidade):
    base= base+1
    numeros = int(input("Digite o ",base,"º número:"))
    soma = soma+numeros


print(numeros)