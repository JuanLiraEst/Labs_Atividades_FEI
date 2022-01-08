def quadrado(lista):
    lista_final = []
    for x in range(len(lista)):
        elevado = (lista[x])**2
        lista_final.append(elevado)
    return lista_final