def esMultiplo(num1, num2):
    if num1 % num2 == 0:
        return True
    return False


num11 = int(input("Introduzca un número: "))
num22 = int(input("Introduzca un número: "))
print(esMultiplo(num11, num22))
