cad = input("Dame un número: ")
try:
    i = int(cad)
#De esta manera obtenemos información del error
except ValueError as error:
    print(type(error))
    print(error.args)
    print(error)