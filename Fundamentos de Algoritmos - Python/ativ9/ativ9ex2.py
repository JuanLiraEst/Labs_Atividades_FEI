m = [] #matriz

for nlinha in range(4): #qtde de linhas
    l=[]
    for ncoluna in range(2): #qtde colunas
        l.append(int(input("Digite o elemento da linha %d e coluna %d: "%(nlinha,ncoluna))))
    m.append(l)

print("Matriz original:")
for nlinha in range(4):
    for ncoluna in range(2):
        print("%3d"%m[nlinha][ncoluna], end = " ")
    print("")

print("")



x=0
for nlinha in range(4):
    for ncoluna in range(2):
        if m[nlinha][ncoluna]>10:
            print(m[nlinha][ncoluna],"é maior que 10!")
            m[nlinha][ncoluna] = 0
            x+=1

print("No total, %d elementos são maiores que 10!"%x)
print("")
print("Matriz sem os números maiores que 10:")
for nlinha in range(4):
    for ncoluna in range(2):
        print("%3d"%m[nlinha][ncoluna], end = " ")
    print("")
