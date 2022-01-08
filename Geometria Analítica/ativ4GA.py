from math import sqrt
print("Digite as coordenadas do centro da superfície esférica: C=(a, b, c)")
ca = int(input("a: "))
cb = int(input("b: "))
cc = int(input("c: "))

print("Digite o raio da superfície esférica")
r = float(input("raio: "))

print("Digite a equação geral do plano: Ax+By+Cz+D=0")
a = int(input("A: "))
b = int(input("B: "))
c = int(input("C: "))
d = int(input("D: "))

dist = float(abs(a*ca + b*cb + c*cc + d)/sqrt(a*a + b*b + c*c))

if dist==r:
  print("Plano Tangente à Superfície Esférica")
  print("Distância do centro da superfície esférica ao plano: %.2f"%dist)   
  pa = ca+a
  pb = cb+b
  pc = cc+c
  print("Ponto de Tangência: (%.2f, %.2f, %.2f)"%(pa,pb,pc))

elif dist>r:
  print("Plano Externo à Superfície Esférica")
  print("Distância do centro da superfície esférica ao plano: %.2f"%dist)   

elif dist<r:
  #valor de t = equação do plano
  #isolando um t
  t = float(-(ca*a + cb*b + cc*c + d)/ (a*a + b*b + c*c))
  centro1 = ca + a*t
  centro2 = cb + b*t
  centro3 = cc + c*t

  #pitagoras
  r_circ = sqrt( r**2 - (abs(t)*sqrt(a*a + b*b + c*c))**2 )

  print("Plano Secante à Superfície Esférica")
  print("Distância do centro da superfície esférica ao plano: %.2f"%dist)   
  print("Raio da circunferência: %.2f"%r_circ)
  print("Centro da circunferência: (%.2f, %.2f, %.2f)"%(centro1,centro2,centro3))
  