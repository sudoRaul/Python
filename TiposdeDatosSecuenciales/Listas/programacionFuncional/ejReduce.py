from functools import reduce
lista = [1, 2, 3, 4, 5, 6]

def add(x,y): return x + y
#Suma todos los elementos de la lista
reduce(add, lista)