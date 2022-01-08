''''
print("Linearmente Dependente e Linearmente Independente:")
uv = []

for y in range(2):
  letras = ["u","v"]
  print("Coordenadas do vetor %s:"%letras[y])
  for x in range(1,4):
    coord = int(input("Digite a %da. coordenada: "%x))
    uv.append(coord)

#chamar cada coord por uma letra pra facilitar o if
#coordenadas u
a = uv[0]
b = uv[1]
c = uv[2]
#coordenadas v
d = uv[3]
e = uv[4]
f = uv[5]
# onde uma das coords em cada lado é 0
if ((a==0 and d==0) and(b and c and e and f)!=0 and f/c==e/b) or ((b==0 and e==0) and(a and c and d and f)!=0 and f/c==d/a) or((c==0 and f==0) and(a and b and d and e)!=0 and d/a==e/b):
  print("Conjunto Linearmente Dependente") 
#onde u ou v por completo é 0
elif (a==0 and b==0 and c==0) or (d==0 and e==0 and f==0):
  print("Conjunto Linearmente Dependente") 

#se uma coord do vetor u é diferente de 0
# e a multiplicação der 0, é independente.
#pois a coord v é zero. e um numero
#diferente de 0 n é multiplo de zero
elif((a!=0) or (b!=0) or (c!=0)) and (f*c==0 or e*b==0 or d*a==0):
  print("Conjunto Linearmente Independente")

#nenhum zero e multiplos corretos
elif f/c == e/b and e/b == d/a:
  print("Conjunto Linearmente Dependente")

else:
  print("Conjunto Linearmente Independente")
'''

#___________________________________________________
#EX2
#a primeira linha dessa matriz é apenas i,j e k, então como 
#sei que é nessa ordem, acho desnecessario add na lista
#então a matriz terá 2 linhas e 3 colunas 
#mas o esquema do determinante será o mesmo
from math import sqrt
print("Produto Vetorial - Área:")
vetor = ["u","v"]
m = []
for x in range(2):
  print("Coordenadas do vetor %s:"%vetor[x])
  linha = []
  for y in range(1,4):
    coord = int(input("Digite a %da. coordenada: "%y))
    linha.append(coord)
  m.append(linha)

a = m[0][0]
b = m[0][1]
c = m[0][2]
d = m[1][0]
e = m[1][1]
f = m[1][2]

#Calculo do determinante de cada coord
i = b*f - c*e
j = c*d - a*f
k = a*e - b*d

area = float(sqrt(i*i+j*j+k*k))
print("A área do paralelogramo formada pelos vetores u e v é: %.2f"%area)
    









