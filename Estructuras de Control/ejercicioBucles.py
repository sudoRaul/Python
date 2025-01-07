contador = 0
acumulador = 0
while True:
    num = int(input("Introduzca un número: "))
    if num !=0:
        acumulador += num
        contador +=1
    else:
        break
media = acumulador / contador
print("La suma de los números introducidos es de %d, \nLa media es %.2f" % (acumulador, media))