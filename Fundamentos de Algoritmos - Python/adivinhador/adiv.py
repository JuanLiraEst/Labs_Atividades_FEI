#Uma function ligada a outra, começando pela main
#Digitar 1 pra primeira opção e 2 pra segunda
def main():
    q1 = int(input("Entre 1 e 49 ou entre 50 e 100?"))
    if q1 ==1:
        menor_cinq() #executar a função menor_cinq se a resposta for 1
    if q1 ==2:
        maior_cinq() #executar a maior_cinq se a resposta for 2

#______________________________________________________________________

def maior_cinq(): #gera uma lista com todos os números maiores que 50
    q2 = int(input("Par ou ímpar?")) #e já faz a próxima pergunta tbm

    #Gerando a lista
    um_a_cinq = []
    for x in range(50,100):
        um_a_cinq.append(x)

    #Ifs para as opções de resposta: se for par, cai no primeiro. 
    #Impar, no segundo
    # Os ifs me levam pra próxima função
    if q2 ==1:
        ifpar(um_a_cinq)
    if q2 ==2:
        ifimpar(um_a_cinq)

#______________________________________________________________________

def menor_cinq(): #mesmo esquema da de cima, mas para a opção <50
    q2 = int(input("Par ou ímpar?"))

    #Gerando a lista
    um_a_cinq = []
    for x in range(1,50):
        um_a_cinq.append(x)

    #2 Ifs
    if q2 ==1:
        ifpar(um_a_cinq)
    if q2 ==2:
        ifimpar(um_a_cinq)

#______________________________________________________________________

def ifpar(cinquenta): #analisando a lista de 50nº recebida
    pares = [] #vai gerar uma lista vazia
    for x in range(len(cinquenta)): #enquanto existirem nºs:
        if cinquenta[x]%2==0: #se for divisível por 2
            pares.append(cinquenta[x]) #add na lista vazia

    #assim já temos uma lista menor, com o número escolhido dentro
    #chamando a próxima função
    ultimoDigito(pares)

#______________________________________________________________________

def ifimpar(cinquenta): #mesmo esquema da de cima
    impares = [] #mas para o caso do número ser ímpar
    for x in range(len(cinquenta)):
        if cinquenta[x]%2!=0: #aqui tds os pares são descartados
            impares.append(cinquenta[x])
    ultimoDigito(impares)   

#______________________________________________________________________ 

def ultimoDigito(lista): # recebe uma lista salva anteriormente
    print("qual é o último dígito do seu número? Exemplo, o último dígito de 203 é 3")
    q3 = input("Dígito: ") #vai perguntar o último dígito do número

    newlista = [] #lista onde vamos salvar os numeros

    for x in range(len(lista)): #enquanto existirem números na lista:
        
        #aqui é um loop, que acontece com tds os nºs, um de cada vez, com x+=1

        valor = str(lista[x]) #transformar o número em string

        if lista[x]<10: #se o nº da lista for menor que 10
        #o primeiro dígito é o último (nº de digito unico). Por isso pego o dig da posição 0    
            
            if valor[0]==q3: #se esse dígito for igual ao input:
                newlista.append(lista[x]) #add esse número na lista

        #para números entre 10 e 99, o segundo dígito é o ultimo, então pego o dig da posição 1
        elif valor[1]== q3: #se o segundo(ultimo) dig for igual ao input, add na lista
            newlista.append(lista[x])

    #dps desse loop que verifica o ultimo dig de todos os números, a lista terá 5 valores
    #dependendo de qual número o usuário digitou na q3
    #se ele digitou 4, os valores todos acabarão com 4
    #ex: newlista = [4,14,24,34,44] ou newlista = [54,64,74,84,94]

    somadigito(newlista) #chamando a ultima função

#______________________________________________________________________

def somadigito(lista): #recebe a lista anterior

    #aqui saberemos qual a soma dos 2 dígitos
    q4 = int(input("a soma dos dois dígitos é igual a?"))

    numero_final = [] #lista onde guardo o número escolhido
    #podia ser uma var tb, já q vai guardar 1 só valor

    for x in range(len(lista)): #enquanto existirem números:

        #tudo que ocorrerá em loop, assim como na função acima

        valor = str(lista[x]) #trabalhar com strings dnv

        dig_um = int(valor[0]) #o primeiro dig é o de posição 0
        #para números <10, o primeiro é o último tb (digito unico)
        #então não existe um segundo díg pros nºs <10

        if lista[x]>9: #mas existe dig 2 pros nºs entre 10 e 99
            dig_dois = int(valor[1])
        
        #para os números menores que 10, a soma é igual ao díg 1
        #já q só tem um dig, então n há oq somar
        if lista[x]<10: 
            if dig_um== q4: #se o dig1 == ao input:
                numero_final.append(lista[x]) #temos o número

        #pra todos os números de 2 dígitos
        elif dig_um + dig_dois == q4: #se a soma dos 2 == ao input:
                numero_final.append(lista[x]) #temos o número

    print(numero_final) #e aqui está

#______________________________________________________________________

main()





            

