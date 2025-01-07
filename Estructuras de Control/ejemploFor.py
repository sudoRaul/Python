#FORMA 1
#Hace un rango de números que serán el valor de la variable, llega hasta 10 -1, end="" sirve para ponerlos en línea
for var in range(0,10):
    print(var, " ", end="",)
print("\n")    
#FORMA 2
#De esta manera con el -1 hace que var empiece con 10 y vaya restando 1 hasta 0 +1
for var in range(10,0, -1):
    print(var, " ", end="")
print("\n")    
   
#FORMA 3
#De esta manera el contador hace que avance de dos en dos, en un for de otro lenguaje seria correspondiente a:
#for(i = 0; i < 10; i+=2)
for var in range(0,10, 2):
    print(var, " ", end="")
    
print("\n")
#Recorrer cadenas caracter por caracter
cadena = "holaMundo"
for var in cadena:
    print(var)