#podemos fazer a condição e deixar o x como a soma dos resultados
#ent vamos usar o percentual assim

ano = int(input("Digite o ano desejado: "))

x = 1.5/100
while ano<2005:
    x = x*2
    
#sa = salariro anterior
sa = 5000
while ano<2005:
    sa = sa*x    

percentual = sa*(1+x)

print("%.2f"%percentual)


