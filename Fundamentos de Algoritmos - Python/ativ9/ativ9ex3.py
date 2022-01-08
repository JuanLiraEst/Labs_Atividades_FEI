m = []
loja = []
produto = []

#lojas
for x in range(3):
    loja.append(input("Digite o nome da loja: "))

#nomes dos produtos
for x in range(5):
    produto.append(input("Digite o nome do produto: "))

#matriz
for nlinha in range(3):
    l = []
    for ncoluna in range(5):
        l.append(int(input("Digite o preco do produto %d na loja %d: "%(ncoluna,nlinha))))
    m.append(l)

print("")

#nomes das lojas no print
print("Lojas:")
for x in range(3):
    print(loja[x])

print("")

#produtos no print
print("Produtos: ")
for x in range(5):
    print(produto[x])

print("")

#matrizona
print("Preços:")
for nlinha in range(3):
    for ncoluna in range(5):
        print("%3d"%m[nlinha][ncoluna], end=" ")
    print("")

print("")

print("Preços menores que R$ 50.00:")
x=0

for nlinha in range(3):
    for ncoluna in range(5):
        if int(m[nlinha][ncoluna])<50:
            if nlinha==0:
                print("Loja: %s, produto %s e preço %d"%(loja[0],produto[ncoluna],m[nlinha][ncoluna]))
print("")
    
            
for nlinha in range(3):
    for ncoluna in range(5):
        if int(m[nlinha][ncoluna])<50:            
            if nlinha ==1:
                print("Loja: %s, produto %s e preço %d"%(loja[1],produto[ncoluna],m[nlinha][ncoluna]))
print("")


for nlinha in range(3):
    for ncoluna in range(5):
        if int(m[nlinha][ncoluna])<50:
            if nlinha == 2:
                print("Loja: %s, produto %s e preço %d"%(loja[2],produto[ncoluna],m[nlinha][ncoluna]))
        

