import random
listaNumeros = []
for i in range(0, 10):
    listaNumeros.append(random.randint(0, 10))
    
    
for i in listaNumeros:
    print("El cuadrado y el cubo de %d es: %d y %d" % (i, pow(i, 2), pow(i, 3)))