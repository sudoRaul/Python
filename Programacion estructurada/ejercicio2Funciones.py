import random
listaNum = []
for i in range(0, 9):
    listaNum.append(random.randint(0,15))
    
def maximo(list):
    return max(list)
def minimo(list):
    return min(list)

print(listaNum)
print(maximo(listaNum))
print(minimo(listaNum))

listaUsuario = []
for i in range(0, 9):
    numUser = int(input("Introduzca un número: "))
    listaUsuario.append(numUser)
    
print(listaUsuario)
print(maximo(listaUsuario))
print(minimo(listaUsuario))


def calcularMaxMin(lista):
    return (max(lista),min(lista))
#Se declaran las dos variables ya que la función devuelve una tupla de dos numeros
vmax, vmin = calcularMaxMin(listaNum)
