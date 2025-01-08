#Ejemplo para validar que se introduzca un número
while True:
    try:
        num = int(input("Introduzca un número: "))
        break
    except ValueError:
        print("Debes introducir un número")