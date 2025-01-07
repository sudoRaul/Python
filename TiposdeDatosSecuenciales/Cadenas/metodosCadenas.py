cadena = "hola mundo"
#Pone la primera letra en mayus
print(cadena.capitalize())
#Convierte las mayusculas a minusculas y viceversa
print(cadena.swapcase())
#Como capitalize pero si hay varias palabras pone tambien las primeras mayus
print(cadena.title())
#Cuenta cuantas veces aparece a en la cadena, los dos ultimos parametros sirven para buscar dentro de un rango
print(cadena.count("a", 3, 7))
#Devuelve la posicion de la primera aparicion de esa cadena, si no la encuentra -1
print(cadena.find("la"))
#Comprueba si la cadena empieza o acaba por una cadena, el segundo paramettro es para buscar a partir de una posicion
print(cadena.startswith("ho"))#TRUE
print(cadena.endswith("j"))#FALSE
#Reemplaza todas los caracteres
print(cadena.replace("a", "i"))
#Quita lo que le indiques al principio y final de la caden, sino se pone nada quita los espacios
print(cadena.strip())
cad2= "000hola00"
print(cad2.strip("0"))
#Separa la cadena por un separador y devuelve un array como en JS
cad3 = "hol/nh/hb"
print(cad3.split("/"))
#Separa por lineas
cad4 = "primera\nsegunda\ntercera"
print(cad4.splitlines())
