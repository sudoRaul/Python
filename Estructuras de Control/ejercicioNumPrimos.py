num = int(input("Introduzca un número: "))
contador = 0
for i in range(num -1, 1, -1):
    if num % i == 0:
        contador += 1
    
if contador == 0:
    print("Es un número primo")
else:
    print("No es un número primo")