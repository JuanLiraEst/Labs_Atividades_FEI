# o mínimo são 3, então há 100% de ctz que
# a,b,c serão digitados. Podemos deixar d,e,f
#como 1, pois não alteram a multiplicação
#aí, caso sejam digitados, eles se alteram

def produtorio(a,b,c, d=1, e=1, f=1):
    return a*b*c*d*e*f

#EXTRA (SOMATÓRIA)
#msm esquema na somatória, mas dxo 0 pra não
#alterar as somas
def somatoria(a , b , c , d=0, e=0, f=0):
    return a+b+c+d+e+f