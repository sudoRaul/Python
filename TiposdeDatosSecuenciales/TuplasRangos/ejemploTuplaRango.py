#LAS TUPLAS SON INMUTABLES, ES DECIR, NO SE PUEDEN MODIFICAR
tuppla1 = (1,2,3,1)
tupla2 = tuple([1,2,3]) 
tupla3 = tuple(range(5))
#a=1, b=2, c=3
a,b,c = tupla2

2 in tuppla1 #True

tuppla1+=(4,5,6, 1)
#Cuenta las apariciones del 1
print(tuppla1.count(1))
#Devuelve la posición en que encuentra por primera vez
print(tuppla1.index(3))

#RANGOS
rango = range(10,20, 2)#Del 10 al 19 de 2 en 2
list(range(10))#Lista del 0 al 9
list(range(0,30,5))#Lista del 0 al 29 de 5 en 5
list(range(0,-10,-1))#Lista del 0 al -10
#Se pueden usar operadores de pertenencia, indexar o slice
10 in rango
rango[1]
rango[1:4]
#Atributo
rango.start #Valor inicial
rango.stop #Valor final
rango.step #Intervalo indicado (último parámetro)