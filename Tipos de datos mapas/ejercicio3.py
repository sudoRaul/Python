gustos={}
nombre = input("Nombre: ")
while nombre != "*":
    gusto = input("Gustos: ")
    #Busca en el diccionario si lo encuentra no hace nada y sino lo añade
    listaGustos = gustos.setdefault(nombre, [gustos])
    if listaGustos != [gusto]:
        gustos[nombre].append(gusto)
    nombre = input("Nombre: ")
print(gustos)