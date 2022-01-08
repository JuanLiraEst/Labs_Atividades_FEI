def contaPalavras(frase):
    
    l = []

    frase = frase.lower()

    frase = frase.replace("!","")
    frase = frase.replace("?","")
    frase = frase.replace(",","")
    frase = frase.strip()
    n_palavras = int(frase.count(" "))+1
    #Acho que da pra usar o numero de palavras pra mostrar quantas linhas o dicionario vai ter
    frase = frase.split(" ")
    l.append(frase)
    for x in frase:
        dicionario = {
            x : frase.split(" ")
    }


    print("temos %d"%n_palavras)
    l.append(frase)
    print(dicionario)
    print(frase)
    return frase

def main():
    texto = str(input("Digite uma frase: "))
    contaPalavras(texto)

main()
