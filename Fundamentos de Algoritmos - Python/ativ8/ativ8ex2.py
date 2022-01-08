neg = []
pos = []

while True:
    x = int(input())
    if x ==0:
        break
    if x <0:
        neg.append(x)
    else:
        pos.append(x)

neg.extend(pos)
print(neg)
# ou concatenar (completo = neg+pos)
# print(completo)