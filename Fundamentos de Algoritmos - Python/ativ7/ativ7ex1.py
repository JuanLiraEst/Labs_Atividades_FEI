from math import sqrt
def hipotenusa(l1, l2):
    hip = sqrt(l1**2 + l2**2)
    return hip

def main():
    cat1 = float(input("Digite o primeiro lado do triângulo: "))
    cat2 = float(input("Digite o segundo lado do triângulo: "))
    print("Hipotenusa: %.2f"%hipotenusa(cat1,cat2))

main()