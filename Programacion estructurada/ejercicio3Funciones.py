#Funcion para sacar la fecha introducida por el usuario
def leerFecha():
    try:
        dia = int(input("Introduzca el día: "))
        mes = int(input("Introduzca el mes: "))
        anio = int(input("Introduzca el año: "))
        return dia, mes, anio
    except ValueError:
        print("Los valores deben ser numéricos")
     
#Funcion para comprobar si el año es bisiesto   
def anioBisiesto(ano):
    return (ano % 4 == 0 and not (ano % 100 == 0)) or ano % 400 == 0

#Calculamos los dias del mes dependiendo que dia es y si es bisiesto
def calcularDiasMes(mes, anio):
    if mes in [1,3,5,7,8,10,12]:
        return 31
    elif mes in [4,6,9,11]:
        return 30
    elif mes ==2:
        if anioBisiesto(anio):
            return 29
        else:
            return 28
#Calculamos el dia Juliano        
def calcularDiaJuliano(dia, mes, ano):
    diaJuliano = 0
    #Recorremos desde el 1 hasta el mes indicado sin incluirlo debido a que al final de la funcion sumamos los dias de ese mes
    for month in range(1, mes):
        diaJuliano = diaJuliano + calcularDiasMes(month, ano)
    diaJuliano =diaJuliano + dia
    return diaJuliano

#Leemos la fecha de la funcion que devuelve una tupla
d,m,a = leerFecha()
print("El día Juliano es", calcularDiaJuliano(d,m,a))
        