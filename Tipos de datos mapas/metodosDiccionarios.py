#Los diccionarios son mutables
#El orden en ellos no importa
#Se accede por la clave
#Se pueden copiar correctamente con el metodo copy()
#Se pueden usar los operadores de pertenencia con la clave
dic1 = {"name": "raul", "edad": 20}
#Limpia el diccionario
dic1.clear()
dic1 = {"name": "raul", "edad": 20, "alto":True, "bajo":False}
dict2 ={"genero": "m"}
#Añade el diccionario 2 al 1
dic1.update(dict2)
#Formas de acceder al diccionario
dic1["name"] #Sino existe devuelve un error
dic1.get("name", "no existe")#Sino existe devuelve la cadena pasada en el segundo parametro
#Eliminar elementos, se puede usar un segundo parametro para que en caso de que no exista no de un error y devuelva esa cadena
dic1.pop("name", "no existe")
#FORMAS DE RECORRER LOS DICCIONARIOS
#FORMA 1: CLAVES
for clave in dic1.keys():
    print(clave)
    
#FORMA 2: VALORES
for valor in dic1.values():
    print(valor)
    
#FORMA 3: CLAVES Y VALORES
for clave, valor in dic1.items():
    print(clave, valor)