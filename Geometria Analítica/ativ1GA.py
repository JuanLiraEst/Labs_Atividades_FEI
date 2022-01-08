''''
ordem = int(input("DETERMINANTE: \n\nDigite a ordem da matriz (até ordem 3): "))

m = []

for nlinha in range(ordem):
    linha = [] #gera uma linha
    for ncoluna in range(ordem):
        linha.append(float(input("Digite o elemento %d %d da matriz: "%(nlinha+1,ncoluna+1)))) #add os numeros na linha
    m.append(linha)
    
det = 0

if ordem ==1:
    print("Determinante:  %.1f"%(m[0][0]))
    
if ordem ==2:
    det = (m[0][0]*m[1][1])-(m[0][1]*m[1][0])
    print("Determinante: %.1f"%det)
    
if ordem ==3:
    a = m[0][0]
    b = m[0][1]
    c = m[0][2]
    d = m[1][0]
    e = m[1][1]
    f = m[1][2]
    g = m[2][0]
    h = m[2][1]
    i = m[2][2]
    det = (a*e*i + b*f*g + c*d*h) - (b*d*i + a*f*h + c*e*g)
    print("Determinante: %.1f"%det)
  '''


''''
print("PRODUTO DE MATRIZES:")
m1 = []

linha1 = int(input("Digite o número de linhas  da matriz M: "))
coluna1 = int(input("Digite o número de colunas da matriz M: "))

for nlinha in range(linha1):
    linha = [] 
    for ncoluna in range(coluna1):
        linha.append(float(input("Digite o elemento %d %d da matriz: "%(nlinha+1,ncoluna+1)))) 
    m1.append(linha)
    
m2 = []

linha2 = int(input("\nDigite o número de linhas  da matriz N: "))
coluna2 = int(input("Digite o número de colunas da matriz N: "))

for nlinha2 in range(linha2):
    l2 = [] 
    for ncoluna2 in range(coluna2):
        l2.append(float(input("Digite o elemento %d %d da matriz: "%(nlinha2+1,ncoluna2+1)))) 
    m2.append(l2)

m3 = []
if coluna1 == linha2:

  for l in range(linha1):
    m3.append([])
    for c in range(coluna2):
      m3[l].append(0)
      for x in range(coluna1):
        m3[l][c] += m1[l][x] * m2[x][c]
  for l in range(linha1):
    for c in range(coluna2):
      print("%.1f" %m3[l][c], end=' ')
    print("")
else:
  print("Matrizes Incompatíveis.")
'''

m = []
l = int(input("Digite o número de linhas  da matriz M: "))
c = int(input("Digite o número de colunas da matriz M: "))

for nlinha in range(l):
    linha = [] 
    for ncoluna in range(c):
        linha.append(float(input("Digite o elemento %d %d da matriz: "%(nlinha+1,ncoluna+1)))) 
    m.append(linha)

transp = []
#o n de coluna vira o de linhas, por isso o range de c será usado nas linhas
for x in range(c):
  linha = [] 
  for y in range(l):
    linha.append(m[y][x]) #y x ao invés de x y pra fz a transp
  transp.append(linha)


print("MATRIZ")
for x in range(l):
    for y in range(c):
        print(m[x][y], end=' ')
    print(" ")

print(" ")
 
print("MATRIZ TRANSPOSTA:") 
for x in range(c): #coluna e dps linha pq os parâmetros invertem (transp)
    for y in range(l):
        print("%.1f" %transp[x][y], end=' ')
    print(" ")


