from palavras import organizar, contar

def main():
    texto = input("Digite as palavras desejadas separando-as por hífen(-): ")
    organizado = organizar(texto)
    print(organizado)
    contar(texto)

if __name__ == "__main__":
    main()

#_____________________________________________________________________________


def organizar(st= " "):
    palavras = []
    for palavra in st.split("-"):
        palavras.append(palavra)
    palavras.sort()

    frase = ""
    for palavra in palavras:
        frase = frase+ str(palavra)
        if palavra is not palavras[-1]:
            frase = frase + str("-")

    return frase

def contar(st = ""):
    maiusculas = 0
    minusculas = 0
    for l in st:
        if l != "-":
            if 65<= ord(l) <=90:
                maiusculas = maiusculas +1
            elif 97 <= ord(l) <= 122 or 224 <= ord(l) <=255:
                minusculas = minusculas +1

    print("Maiúsculas = "+str(maiusculas))
    print("Minúsculas = "+str(minusculas))