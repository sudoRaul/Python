dia = int(input("Introduzca un día válido: "))
mes = int(input("Introduzca un mes válido: "))
anio = int(input("Introduzca un año válido: "))

if mes % 2 == 1 or mes == 8: 
    if dia > 31 or mes > 13 or anio > 2025:
        print("ERROR EN LA FECHA")
    else:
        print("Fecha introducida: ", dia , "/" , mes, "/" , anio)
elif mes % 2 == 0 and mes != 2:
    if dia > 30 or mes > 13 or anio > 2025:
        print("ERROR EN LA FECHA")
    else:
        print("Fecha introducida: ", dia , "/" , mes, "/" , anio)
elif mes == 2 and anio % 4 == 0:
    if dia > 29 or anio > 2026:
        print("ERROR EN LA FECHA")
    else:
        print("Fecha introducida: ", dia , "/" , mes, "/" , anio)       
elif mes == 2 and anio % 4 != 0:
    if dia > 28 or anio > 2026:
        print("ERROR EN LA FECHA")
    else:
        print("Fecha introducida: ", dia , "/" , mes, "/" , anio)  