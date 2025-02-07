cad = input("Introduzca una cadena: ")
lista = cad.split(" ")
for letra in lista:
    print(letra[0], end="")
print()
for letra in lista:
    print(letra.title(), end="")
print()
for letra in lista:
    if letra.lower().startswith("a"):
        print(letra, sep=", ", end="")