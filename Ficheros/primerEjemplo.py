#En este caso será solo modo lectura
file = open("Ficheros/texto.txt", "r")
#Atributos
file.closed
file.mode
file.name
#Metodos
#IMPORTANTE Conforme se va leyendo va avanzando el puntero
file.read()
file.tell()#Posicion del puntero
file.seek(0)#Pone el putero en la posición 0
file.read(4)#Lee 4 caracteres
file.readline()#Lee toda una linea
file.readlines()#Lee todas las lineas y las guarda en una lista

file.close()


#De esta manera se lee el fichero se almacena en contenido y se cierra
with open("Ficheros/texto.txt", "r") as ejemplo:
    contenido = ejemplo.read()


fileEscritura = open("Ficheros/texto.txt", "w")
fileEscritura.write("Texto añadido")
fileEscritura.writelines(["cosa 1", "cosa 2"])

with open("Ficheros/texto.txt", "r") as fichero:
    for linea in fichero:
        print(linea)