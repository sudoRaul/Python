notas =[]
for i in range(0,5):
    while True:
        nota = int(input("Introduzca su nota: "))
        if nota >=0 and nota <=10:
            break
    notas.append(nota)
    
sumaNotas = sum(notas) / len(notas)
maximo = max(notas)
minimo = min(notas)
print("La media de sus notas es %.2f, su nota máxima es %d y su nota mínima es %d" % (sumaNotas, maximo, minimo))