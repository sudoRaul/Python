cad1 = input("Introduzca una frase: ")
contador = 0
posicion = 0
#Para eliminar los posibles espacios al principio y al final
cad1 = cad1.strip()
#Guardamos la posición donde encuentra el primer espacio, sino encuentra es -1
posicion = cad1.find(" ", posicion)
while posicion != -1:
    contador +=1
    #Controlamos que no se cuenten los espacios repetidos, es decir si la siguiente posicion es un espacio aumentamos la posicion
    #para buscar en la siguiente
    while cad1[posicion +1] ==" ":
        posicion +=1
    #Seguimos buscando los espacios
    posicion = cad1.find(" ", posicion +1)
print("La frase %s tiene %d palabras "% (cad1, contador + 1))