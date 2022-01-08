from placas import numeros, letras, montarPlaca

def main():
    numero = numeros()
    letra = letras()
    placa = montarPlaca(letra, numero)
    print("Placa =", end=" ")
    for digito in placa:
        print(digito, end="")

#Quando um módulo é diretamente executado, __name__ é
#definido como “__main__”

if __name__ == "__main__":
    main()

    #___________________________________________________________
from random import choice, randrange
def letras():
    alfabeto = ["A","B","C","D","E","F","G","H",
                "I","J","K","L","M","N","O","P","Q","R","S",
                "T","U","V","W","X","Y","Z"]
    letras_placa = []
    for i in range(4):
        letras_placa.append(choice(alfabeto))

    return letras_placa

def numeros():
    numeros_placa = []
    for i in range(3):
        numeros_placa.append(randrange(0,9))
    return numeros_placa

def montarPlaca(letra, numero):
    placa = []
    placa.append(letra[0])
    placa.append(letra[1])
    placa.append(letra[2])
    placa.append(numero[0])
    placa.append(letra[3])
    placa.append(numero[1])
    placa.append(numero[2])
    return placa
    
    
    
    
    
        
