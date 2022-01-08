def criptCesar(frase, deslocamento):
    frase = frase.upper()
    resposta = ""
    for letra in frase:
        resposta = resposta + chr((ord(letra)+ deslocamento)%26)    
    print(resposta)

p = "casa"
criptCesar(p, 3)