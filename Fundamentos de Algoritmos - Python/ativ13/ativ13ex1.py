
def converte(dicionario, texto):
    texto = texto.upper() #transformar o texto pra maiusculas
    lista = []
    
    for letra in texto:
        if letra in dicionario: #conferir se a letra está no dicio
            
            lista.append(dicionario[letra]+" ")
    return "".join(lista) #transforma a lista em texto com o simbolo q passamos

