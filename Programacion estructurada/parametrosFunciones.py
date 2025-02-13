#Podemos dar valor por defecto a un parámetro
def operar(n1,n2,operador='+',respuesta='El resultado es '):
   if operador=="+":
     return respuesta+str(n1+n2)
   elif operador=="-":
     return respuesta+str(n1-n2)
   else:
     return "Error"
 
#A partir del * nos obliga a indicar los parámetros reales posteriores como keyword
def sumar(n1,n2,*,op="+"):
   if op=="+":
     return n1+n2
   elif op=="-":
     return n1-n2
   else:
     return "error"
 
sumar(2,3,"-")#ERROR
sumar(2,3,op="-")#CORRECTO

#Numero variable de argumentos
def sumar2(n,*args):
   resultado=n
   for i in args:
     resultado+=i
   return resultado
sumar2(2)
sumar2(2,3,4,5,6)
lista=[1,2,3]
#De esta forma le pasamos todos los elementos de la lista
print(sumar2(*lista))


#Para indicar un número indefinido de argumentos keyword usamos **
def saludar(nombre="pepe",**kwargs):
   cadena=nombre
   for valor in kwargs.values():
    cadena=cadena+" "+valor
   return "Hola "+cadena