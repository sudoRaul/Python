#FUNCIONES LAMBDA O ANONIMAS
cuadrado = lambda x: x**2

#Coge la lista y la oredena por el valor en vez de por la clave
pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
pairs.sort(key=lambda pair: pair[1])

#DECORADORES
#En este ejemplo la función envoltura solo pinta el encabezado, pone tabla del x, y recorre los numeros del 1 al 10

def tablas(funcion):
    def envoltura(tabla=1):
        print('Tabla del %i:' %tabla)
        print('-' * 15)
        for numero in range(0, 11):            
            funcion(numero, tabla)
        print('-' * 15)
    return envoltura
 
@tablas
def suma(numero, tabla=1):
    print('%2i + %2i = %3i' %(tabla, numero, tabla+numero))
 
@tablas
def multiplicar(numero, tabla=1):
    print('%2i X %2i = %3i' %(tabla, numero, tabla*numero))

# Muestra la tabla de sumar del 1
print(suma())
# Muestra la tabla de sumar del 4 
suma(4)	
# Muestra la tabla de multiplicar del 1
multiplicar()	
# Muestra la tabla de multiplicar del 10
multiplicar(10)  



#GENERADORES
#Generan un iterador
def par(inicio,fin):
   for i in range(inicio,fin):
     if i % 2==0:
       yield i

#Podemos ir viendo los números como en los iteradores
datos = par(1,5)
next(datos)

next(datos)


for i in par(20,30):
   print(i,end=" ")


lista_pares = list(par(1,10)) #Lista de números pares
