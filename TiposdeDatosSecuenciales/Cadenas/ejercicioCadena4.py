cad1 = input("Introduzca una cadena: ")
cad2 = input("Introduzca otra cadena: ")
#FORMA 1
#Ponemos != -1 debido a que esto significa que ha encontrado esa cadena
if cad1.find(cad2) != -1:
    print("La cadena %s sí incluye a la cadena %s" % (cad1, cad2))
else:
    print("La cadena %s no incluye a la cadena %s" % (cad1, cad2))
    
#FORMA 2
if cad2 in cad1:
    print("La cadena %s sí incluye a la cadena %s" % (cad1, cad2))
else:
    print("La cadena %s no incluye a la cadena %s" % (cad1, cad2))