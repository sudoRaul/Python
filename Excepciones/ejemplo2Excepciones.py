#Un programa puede provocar varias excepciones, es necesario controlarlas todas
num = input("Introduzca un número: ")
try:
    result = (10 / int(num))
except ValueError:
    print("Debes introducir un número")
except ZeroDivisionError:
    print("No se puede introducir un 0")
#De esta manera controlamos cualquier error que suceda que no se haya controlado
else:
    print("Se ha producido otro error")
#Se ejecuta siempre pase lo que pase
finally:
    print("Programa terminado")