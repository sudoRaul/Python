cadena = "HolaMundo"
#Imprimirá True
print("a" in cadena)
#Imprimirá False
print("b" in cadena)
#Imprimirá True
print("e" not in cadena)
#Imprimirá False
print("M" not in cadena)
#Para coger subcadenas podemos hacerlo de varias maneras
#Coge desde el caracter 5 incluido hasta el 8 sin incluir
print(cadena[5:8])
#El último parametro sirve para en este caso coger de dos en dos coge los caracteres 0 2 4 a partir del indicado en el parametro 1
print(cadena[2:8:2])
#Coge del segundo hasta el final
print(cadena[2:])
#Coge del inicio hasta el quinto sin incluir
print(cadena[:5])
#Coge la cadena del revés
print(cadena[::-1])
