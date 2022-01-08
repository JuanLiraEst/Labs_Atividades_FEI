def contaPalavras(word):
    lista = word.split(" ")
    palavras = len(lista)
    return palavras

def main():
    print(contaPalavras("A FEI eh fantástica"))

