dict1={}
cad = input("Introduzca una cadena: ")
for car in cad:
    #Si ese caracter ya ha aparecido previamente pasamos al siguiente caracter
    if car in dict1:
        dict1[car] +=1
    else:
        dict1[car]= car.count(car)
        
print(dict1)