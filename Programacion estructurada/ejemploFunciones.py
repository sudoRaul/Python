#EL TIPO DE UNA FUNCION DEPENDERA DEL VALOR QUE DEVUELVA
#FORMA NORMAL
def factorial(n):
    """Calcula el factorial de un número""" #Descripción de la función
    result= 1
    for i in range(1, n+1):
        result *= i
    return result
print(factorial(4))

#FORMA RECURSIVA
def factorial2(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)
    
print(factorial2(4))