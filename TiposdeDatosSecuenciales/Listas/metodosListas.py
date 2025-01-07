listEjemplos =[1,2,3]
listEjemplos2 =[5,6]
listEjemplos.append(4) #La lista ahora será 1 2 3 4
listEjemplos.extend(listEjemplos2) #Para unir las dos listas
listEjemplos.insert(2, 34) #Añade en la posición 2 el 34
listEjemplos.pop()#Elimina el último elemento de la lista y lo devuelve
listEjemplos.pop(1)#Elimina la posición indicada
listEjemplos.remove(3)#Elimina todos los 3 que haya en la lista
listEjemplos.reverse()#Ordena la lista a la inversa
listEjemplos.sort(reverse=True)#Ordena la lista a la inversa
listEjemplos.sort()#Ordena la lista 
#Todas estos métodos también sirven con listas de cadenas
listEjemplos.count(1)#Cuenta las veces que aparece ese elemento
listEjemplos.index(3)#Muestra el indice donde se encuentra por primera vez ese elemento, sino lo encuentra devuelve -1
listEjemplos.index(3,2)#Muestra el indice donde se encuentra el elemento a partir de la posicion indicada en el segundo parametro, sino lo encuentra devuelve -1
