cad1 = ""
cad2 = ""
while True:
    cad1 = input("Introduzca una cadena: ")
    cad2 = input("Introduzca un caracter: ")
    if len(cad1) and len(cad2) == 1 and not cad2.isdigit():
        break
    print("ERROR: Repita el proceso")
print("La cadena %s aparece %d veces en la cadena %s" % (cad2, cad1.count(cad2), cad1))
