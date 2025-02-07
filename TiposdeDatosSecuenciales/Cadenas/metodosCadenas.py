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
print(cadena.rfind("la"))#Busca desde la derecha
#Comprueba si la cadena empieza o acaba por una cadena, el segundo paramettro es para buscar a partir de una posicion
print(cadena.startswith("ho"))#TRUE
print(cadena.endswith("j"))#FALSE
#Reemplaza todas los caracteres
print(cadena.replace("a", "i"))
#Quita lo que le indiques al principio y final de la caden, sino se pone nada quita los espacios
#Podemos quitar por izquierda y derecha lstrip y rstrip
print(cadena.strip())
cad2= "000hola00"
print(cad2.strip("0"))
#Separa la cadena por un separador y devuelve un array como en JS
cad3 = "hol/nh/hb"
print(cad3.split("/"))
#Separa por lineas
cad4 = "primera\nsegunda\ntercera"
print(cad4.splitlines())
#Centra una cadena, pone 50 caracteres, se puede elegir cual poner
cad5 = "ALgo"
print(cad5.center(50, "="))
#Alinear derecha
cad6 = "ALgo"
print(cad6.rjust(50, "="))
#Alinear izquierda
cad7 = "ALgo"
print(cad5.ljust(50, "="))
#Rellenar con 0 una cadena
"123".zfill(5)#00123

#FORMATEAR SALIDA
#Mostrará a b
"{} {}".format("a", "b")
#Muestra b a
"{1} {0}".format("a", "b")
'Hoy es {dia} de {mes}'.format(dia = 3, mes = "octubre")
'{0:b} {1:x} {2:.2f}'.format(123, 223, 12.2345) #Primer valor en binario, segundo hexadecimal y tercero con dos decimales
'{:^10}'.format('test') #Centra el texto en 10 caracteres
#END FORMAT
#Join sirve para unir cadenas Ejemplo
formatoFactura = ("Nº 0000-0", "-0000 (ID: ", ")")
#Se añadirá el 275 entre el valor de cada elemento de la tupla
print("275".join(formatoFactura)) #Nº 0000-0275"-0000 (ID: 275)

#Partir cadenas en tuplas
#A diferencia de split solo divide una vez
print("12:45".partition(":")) #Devuelve ("12", ":", "45") Podemos usar rpartition

