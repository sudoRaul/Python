lista = [1, 2, 3, 4, 5, 6]

def par(x): return x%2==0
#Devuelve una lista SOLO con los números pares
list(filter(par, lista))