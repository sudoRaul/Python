num = int(input("Introduzca un número (-1 para salir): "))
listaNums= []
while num != -1:
    listaNums.append(num)
    num = int(input("Introduzca un número (-1 para salir)"))
for num in listaNums:
    if num%2==0:
        print(num, end=" ")
print()  
print(max(listaNums))