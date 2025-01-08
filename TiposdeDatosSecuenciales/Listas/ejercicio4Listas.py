tabla = []
#Pedimos al usuario 25 números para completar la tabla
for indice_fila in range(0,5):
    #Limpiamos la fila
    fila = []
    for indice_col in range(0,5):
        #Añadimos los números a la fila
        fila.append(int(input("Introduzca un número: ")))
    #Añadimos la fila
    tabla.append(fila)
    
#Suma de las filas
for fila_tabla in tabla:
    #Suma fila por fila de la tabla
    suma_fila = sum(fila_tabla)
    print("La suma de las filas es", suma_fila)
    
#Suma de las columnas
for col_tabla in tabla:
    #Ponemos de nuevo la suma a 0 para sumar una nueva columna
    sum_columnas = 0
    for fila in tabla:
        sum_columnas += fila[indice_col -1]
    print("La suma de las columnas", sum_columnas)

    