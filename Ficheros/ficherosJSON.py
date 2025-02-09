import json
#Todo Objeto JSON en Python va a ser un diccionario
with open("Ficheros/fichero.json") as fichero:
    datos = json.load(fichero)
    
type(datos) #Diccionario

print(datos)
#Estamos accediendo al nombre del primer elemento
print(datos["users"][0]["name"])

ficherojson = open("Ficheros/fichero2.json", "w")
datosAnadir = {'algo': True, 'nombre': 'Fulano', 'edad':19 }
json.dump(datosAnadir, ficherojson)
ficherojson.close()