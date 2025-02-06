lista = ["1", "2", "3", "4", "5", "6"]
#Convierte a entero los elementos y devuelve un tipo mapa por eso hay que convertir a lista
list(map(int, lista))

def cuadrado(x): return x**2
#Convierte a cuadrado cada elemento
list(map(cuadrado, lista))