from moduloex3 import organizar

def main():
    texto=input("Digite o nome do arquivo com o extensão: ")
    organizar(texto)
    
if __name__ == "__main__":
    main()


#_______________________________________________________________________
def organizar(st=""):
    arq = []
    arquivo = open(st, "r")
    for linha in arquivo.readlines():
        arq.append(linha.strip())
    arquivo.close()

    aux = []
    for i in arq[0].split(","):
        aux.append(i)

    for i in range(len(arq)):
        if i != 0:
            for p in arq[i].split(","):
                if p == "ball":
                    frase = arq[i].split(",")
                    frase_final = ""
                    for p in frase:
                        if p == "640" or p == "360":
                            pass
                        else:
                            frase_final+=p
                            frase_final+=","
                    frase_final2 = ""
                    for i in range(len(frase_final)-1):
                        frase_final2+=frase_final[i]
                    frase_final2+='\n'
                    print(frase_final2)