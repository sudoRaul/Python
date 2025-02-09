import csv
fichero = open("Ficheros/ejemplo.csv", "r")
#Opcionalmente se puede poner un segundo parámetro para separar los datos
#contenido = csv.reader(fichero, quotechar='"')
contenido = csv.reader(fichero)
#print(list(contenido))
#Si volvemos a leer no mostraría nada debido a que el puntero estaría al final
fichero.seek(0)
#Esto nos sirve para tener los datos en la lista y así poder acceder a ellos
#datos = list(contenido)
for row in contenido:
    print("Fila " + str(contenido.line_num)+" "+ str(row))
    
    
fichero.close()

fichero2= open("Ficheros/nuevo.csv", "w")
contenido = csv.writer(fichero2)
contenido.writerow(['4/5/2015 13:34', 'Apples', '73'])
fichero2.close()