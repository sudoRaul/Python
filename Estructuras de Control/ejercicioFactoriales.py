#FORMA 1
num = int(input("Introduzca un número: "))
for var in range(num -1, 0, -1):
    num *= int(var)
print(num)
print("\n================================")


#FORMA 2
resultado = 1
num2 = int(input("Introduzca un número: "))
contador = 2
while contador <= num2:
    resultado = resultado *  contador
    contador= contador + 1
print("El factorial es: ", resultado)
        