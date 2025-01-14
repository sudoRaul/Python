# Escribir un programa que implemente una agenda. En la agenda se podrán guardar nombres y números de teléfono. 
# El programa nos dará el siguiente menú:
# 
# * Añadir/modificar: Nos pide un nombre. Si el nombre se encuentra en la agenda, debe mostrar el teléfono y, 
# opcionalmente, permitir modificarlo si no es correcto. Si el nombre no se encuentra, debe 
# permitir ingresar el teléfono correspondiente. 
# * Buscar: Nos pide una cadena de caracteres, y nos muestras todos los contactos cuyos nombres comiencen por dicha cadena.
# * Borrar: Nos pide un nombre y si existe nos preguntará si queremos borrarlo de la agenda.
# * Listar: Nos muestra todos los contactos de la agenda.
# 
# Implementar el programa con un diccionario.


agenda = {
    "pepe": 673126983,
    "ana": 612345678,
    "juan": 654987321,
    "marta": 698745632,
    "luis": 635987412,
    "laura": 678901234,
    "carlos": 612398745,
    "elena": 645678912,
    "pablo": 689123456,
    "sofia": 659874123,
    "david": 690234567
}

while True:
    opcion = int(input("Introduzca la opción a realizar.\n 1. Añadir contacto.\n 2. Buscar contacto \n 3. Borrar usuario.\n 4.Listar todos los contactos.\n 5. Salir \n"))
    if opcion == 1:
        nombre = input("Introduzca el nombre: ")
        tel = input("Introduzca el número de teléfono: ")
        agenda.update({nombre: tel})
        print("Contacto añadido")
        
    elif opcion == 2:
        cad = input("Introduzca contacto a buscar: ")
        contacto = agenda.get(cad, "USUARIO NO ENCONTRADO")
        print(contacto)
        
    elif opcion == 3:
        cad = input("Introduzca contacto a borrar: ")
        agenda.pop(cad, "USUARIO NO ENCONTRADO")
    elif opcion == 4:
        for clave, valor in agenda.items():
            print(clave, "-", valor)
        
    else: 
        break
            