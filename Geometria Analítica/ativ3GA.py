#A matriz vai guardar os pontos A B e C 
#E eu vou encontrar os vetores AB e AC pra fazer o produto vetorial

print("Plano:")
vetor = ["A","B","C"]
m = []
for x in range(3):
  print("Coordenadas do ponto %s:"%vetor[x])
  linha = []
  for y in range(1,4):
    coord = int(input("Digite a %da. coordenada: "%y))
    linha.append(coord)
  m.append(linha)

ab = { #Vetor ab = b-a (de cada ponto)
  1 : m[1][0]- m[0][0],
  2 : m[1][1]- m[0][1],
  3 : m[1][2]- m[0][2],
  #vetor ab = (1,2,3)
}

ac = { #Vetor ac = c-a (de cada ponto)
  1 : m[2][0]- m[0][0],
  2 : m[2][1]- m[0][1],
  3 : m[2][2]- m[0][2],
  #vetor ac = (1,2,3)
}

#Produto vetorial dos dois vetores (determinante)
#A matriz será assim, com os valores dos dicionários acima

#  | i  j  k | 
#  | a  b  c |  
#  | d  e  f |  

# linha 2 = vetor ab = (a,b,c)
# linha 3 = vetor ac = (d,e,f) 

a = ab[1]
b = ab[2]
c = ab[3]
d = ac[1]
e = ac[2]
f = ac[3]

#Calculo do determinante

#  | i  j  k |  i  j
#  | a  b  c |  a  b
#  | d  e  f |  d  e


i = b*f - (c*e)
j = c*d - (a*f)
k = a*e - (b*d)

#encontramos o prod vetorial ab*ac = (i,j,k)
#i,j e k são o a, b e c da equação do plano respectiv.
# ax + by + cz + d = 0 
# pra encontrar o d, usar o produto vetorial e um dos pontos (A,B ou C, que foram inseridos na matriz)
# os valores do ponto escolhido vão substituir o x,y e z da eq do plano
# assim isolamos o d e encontramos seu valor
#eu vou usar o ponto A, da primeira linha da matriz
d_eq = -(i*m[0][0]) -(j*m[0][1]) -(k*m[0][2])

#se os valores da equação forem todos nulos, são inválidos
if i==0 and j==0 and k==0 and d_eq==0:
  print("Dados Incorretos") 

else: 
  print("Equação Geral do plano:")
  print("ax + by + cz + d = 0")
  print("onde:")
  #O valor a(no meu caso é a var i ) precisa ser >=0. Se n for, multiplicar a eq por -1
  if i<0:
    print("a = %.2f, b = %.2f, c = %.2f e d = %.2f"%(-i,-j,-k,-d_eq))  

  else:
    print("a = %.2f, b = %.2f, c = %.2f e d = %.2f"%(i,j,k,d_eq))  
