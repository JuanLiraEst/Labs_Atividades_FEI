from random import randint
m = []    
vetor = []
mfinal = []
somatoria = 0
for nlinha in range(20):
    l = []
    for ncoluna in range(10):
        l.append(randint(0,10))
        somatoria = somatoria + l[ncoluna]
    vetor.append(somatoria)
    m.append(l)




print("Matriz original:")
for nlinha in range(20):
    for ncoluna in range(10):
        print("%3d"%m[nlinha][ncoluna],end =" ")
    print("")

print("")

print("Vetor com a somatória de cada linha:")
print(vetor)

print("")
    
print("matriz depois da multiplicação:")
for nlinha in range(20):
    for ncoluna in range(10):
        print("%5d"%(m[nlinha][ncoluna]*vetor[nlinha]), end=" ") 
    print("")


