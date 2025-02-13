def multiplicar_lista(list):
    if len(list) == 1:
        return list[0]
    else:
        #Sacamos el elemento de la lista y multiplicamos
        return list.pop()* multiplicar_lista(list)

print(multiplicar_lista([1,2,3,4]))