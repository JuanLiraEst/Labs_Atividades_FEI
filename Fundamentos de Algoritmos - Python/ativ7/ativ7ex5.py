def conversao(planeta,peso):
    if planeta == "Mercúrio":
        pesofinal = (peso)*0.37
    elif planeta == "Vênus":
        pesofinal = (peso)*0.88
    elif planeta == "Marte":
        pesofinal = (peso)*0.38    
    elif planeta == "Júpiter":
        pesofinal = (peso)*2.64
    elif planeta == "Saturno":
        pesofinal = (peso)*1.15
    elif planeta == "Urano":
        pesofinal = (peso)*1.17
    elif planeta == "Netuno":
        pesofinal = (peso)*1.18
    return(pesofinal)


def main():
    planeta_desejado = input("Digite o nome do planeta desejado: ")
    peso_terra= float(input("Digite o peso da pessoa na Terra em kg: "))
    print("Peso em %s: %.2f" %(planeta_desejado,conversao(planeta_desejado,peso_terra)))
main()