from gerador import gerar

#o x será o limite
def main():
    x = int(input("Digite um limite para os números primos: "))
    gerar(x)


if __name__ == "__main__":
    main()


#_______________________________________________________________________________-





def gerar(x):
    numeros = []
    for i in range(x + 1):
        if i == 1:
            numeros.append(0)
        else:
            numeros.append(i)

    a = 2

    ant = [0, 1]

    while a < x:
        for x in range(len(numeros)):
            if numeros[x] % a == 0 and numeros[x] != a:
                numeros[x] = 0

        for y in range(x + 1):
            if y != 0 and y != a and y not in ant:
                a = y
                ant.append(y)
                break

    palavras = ""
    for j in numeros:
        palavras += str(j)
        palavras += " "

    print(palavras)