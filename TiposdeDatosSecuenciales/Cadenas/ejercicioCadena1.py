cad1 = input("Introduzca una cadena: ")
cad2 = input("Introduzca otra cadena: ")
if cad1.startswith(cad2):
    print("La cadena %s sí comienza por la cadena %s" % (cad1, cad2))
else:
    print("La cadena %s no comienza por la cadena %s" % (cad1, cad2))