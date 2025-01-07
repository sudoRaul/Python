listaNum = [1,2,3,4,5,6,7,8,9,10]
listaLetr= ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
#Recorrer una lista
for i in listaNum:
    print(i)
#Recorrer varias listas a la vez, deben tener la misma longitud, 
#hay que poner tantas varibales como listas tengamos
for num, letra in zip(listaNum, listaLetr):
    print(num, " ", letra)
print("\n================================================")    
#Tambien podemos usar operadores de pertenencia
print(4 in listaNum)#True
print(34 in listaNum)#False
print("f" in listaLetr)#True
print("\n================================================")
#Se pueden concatenar listas
listaNum += [11,12,13]
print(listaNum)
print("\n================================================")
#Al igual que con las cadenas se pueden repetir
listaLetr*=2
print(listaLetr)
print("\n================================================")
#Se puede usar el slice de la misma manera que con las cadenas
#Coge desde la posicion 5 incluido hasta la 8 sin incluir
print(listaNum[5:8])
#El último parametro sirve para en este caso coger de dos en dos coge los valores desde la el 2 hasta el 8 saltando de 2 en 2
print(listaNum[2:8:2])
#Coge del segundo hasta el final
print(listaNum[2:])
#Coge del inicio hasta el quinto sin incluir
print(listaNum[:5])
#Coge la lista del revés
print(listaNum[::-1])
print("\n================================================")
#Para coger el mayor valor
print(max(listaNum))
print("\n================================================")
#Para coger el menor valor
print(min(listaNum))
print("\n================================================")
#Para coger la suma
print(sum(listaNum))
print("\n================================================")
#Para ordenar la lista normal o del revés
listaDesord= [8,5,9,2,4,1,6,3]
print(sorted(listaDesord))
print(sorted(listaDesord, reverse=True))
print("\n================================================")
#Podemos hacer listas bidimensionales
tabla = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
#Para recorrerlo necesitamos dos bucles
for fila in tabla:
    for elem in fila:
        print(elem, end="")
print("\n================================================")
#LAS LISTAS SON MUTABLES
listEjemplos =[1,2,3]
listEjemplos[1]= 4 #La lista ahora sera 1 4 3
del listEjemplos[2] #La lista ahora sera 1 4 
listEjemplos.append(3) #La lista ahora será 1 4 3
#Cuando copiamos una lista
lista2Ej = listEjemplos
#Si se modifica una se modifican las dos, porque están apuntando al mismo trozo de memoria
#Para hacerlo correctamente podemos hacerlo con slice
lista3Ej =listEjemplos[:] #De esta manera si se modifica listEjemplos lista3Ej no lo hará
