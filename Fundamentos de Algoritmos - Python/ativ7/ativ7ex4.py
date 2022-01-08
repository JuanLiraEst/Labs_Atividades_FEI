def tarifa(quilometros):
    tarifafinal = 10+((quilometros*1000)/125)*0.5
    return tarifafinal
    
def main():
    km = float(input("Digite a quantidade de quilômetros: "))
    print("Tarifa %.2f"%tarifa(km))
    
main()
