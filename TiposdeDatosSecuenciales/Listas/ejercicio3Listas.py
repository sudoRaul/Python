listaNombres = []
listaEdades = []
while True: 
    nombre = input("Introduzca su nombre: ")
    edad = int(input("Introduzca su edad: "))
    if nombre != "*":
        listaNombres.append(nombre)
        listaEdades.append(edad)
    else:
        break
edad_max = max(listaEdades)
for nombre, edad in zip(listaNombres, listaEdades):
    if edad >= 18:
        print("El usuario %s es mayor de edad y tiene %d" %(nombre, edad))
    print("================================")
    #Escribimos el nombre de la persona con más edad
    if edad_max == edad:
        print("El usuario más mayor es", nombre)
    
