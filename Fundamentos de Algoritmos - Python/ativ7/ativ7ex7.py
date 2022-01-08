import math

def distancia(laa,loa,lab,lob):
    delta_s = 6371.01*math.acos(math.sin(math.radians(laa)) * math.sin(math.radians(lab)) + math.cos(math.radians(laa)) * math.cos(math.radians(lab)) * math.cos(math.radians(loa) - math.radians(lob)))
    return delta_s

def main():
    lat_a = float(input("Digite a latitude A: "))
    lon_a = float(input("Digite a longitude A: "))
    lat_b = float(input("Digite a latitude B: "))
    lon_b = float(input("Digite a longitude B: "))
    print("A distância é %.2fkm."%distancia(lat_a,lon_a,lat_b,lon_b))

main()