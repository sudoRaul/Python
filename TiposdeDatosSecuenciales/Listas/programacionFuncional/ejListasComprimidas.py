#Es una forma muy completa de crear listas sin usar funciones

#Devuelve una lista con el cubo de cada elemento
[x ** 3 for x in [1, 2, 3, 4, 5, 6]]
#Devuelve una lista con los pares
[x for x in range(10) if x%2==0]
#Devuelve una lista con la suma de cada elemento de la lista 1 con todos los de la lista 2
#Es decir 1+4, 1+5, 1+6, 2+4, 2+5, etc
[x+y for x in [1,2,3] for y in [4,5,6]]