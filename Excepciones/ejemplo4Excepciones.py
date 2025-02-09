def dividir(x,y):
    try:
        return x/y
    except ZeroDivisionError:
        return "no se puede dividir"
    
def dividir2(x,y):
    try:
        return x/y
    except ZeroDivisionError:
        #Sirve para indicarle al programa principal que se ha producido una excepción
        raise
    
print(dividir(2,0))
try:
    print(dividir2(2,0))
except:
    "No se puede dividir"