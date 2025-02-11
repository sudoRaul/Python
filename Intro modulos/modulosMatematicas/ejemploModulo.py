import math
#from math import sqrt En caso que solo necesite esa funcion
from fractions import Fraction #Para trabajar con fracciones
import statistics #Para estadística
import random #Para numeros aleatorios
math.factorial(5)
math.pow(2,4)
math.sqrt(4)
math.cos(1)
math.pi
math.log(10)

#Las fracciones se pueden sumar, restar multiplicar, dividir, etc
a=Fraction(4,7) 
b=Fraction(2,8)

statistics.mean([2,3,4,5,6,7,7,8])#Calcula la media de una lista
statistics.median([2,3,4,5,6])#Calcula la mediana de una lista

random.randint(10,100)#Genera un numero aleatorio entre 10 y 100
random.choice([1,2,3,4,5,6]) #Elegir entre los valores de esa lista, también con cadenas
lista = [2,5,1,3,7,9,4,6,8]
random.shuffle(lista) #Reordena la lista aleatoriamente
random.sample(lista, 2) #Devuelve dos elementos aleatorios de la lista