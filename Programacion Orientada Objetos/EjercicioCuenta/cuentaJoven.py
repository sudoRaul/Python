from cuenta import Cuenta
# Clase Titular
class Titular:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def esMayorDeEdad(self):
        # Retorna True si la edad es 18 o mayor
        return self.edad >= 18
    
    def mostrar(self):
        # Método para mostrar el nombre del titular
        return self.nombre
    
    
    
class CuentaJoven(Cuenta):
    def __init__(self, titular, cantidad=0, bonificacion=0):
        super().__init__(titular, cantidad)  # Llamamos al constructor de la clase base
        self.__bonificacion = bonificacion  # Atributo privado para la bonificación

    @property
    def bonificacion(self):
        return self.__bonificacion

    @bonificacion.setter
    def bonificacion(self, bonificacion):
        # Verifica que la bonificación esté entre 0 y 100
        if 0 <= bonificacion <= 100:
            self.__bonificacion = bonificacion
        else:
            print("Bonificación incorrecta, debe estar entre 0 y 100.")

    def mostrar(self):
        # Muestra la información de la cuenta joven, incluyendo la bonificación
        return f"Cuenta de {self.titular.mostrar()}, con una cantidad de {self.cantidad} euros, la bonificación es de {self.__bonificacion}%"

    def esTitularValido(self):
        # Verifica si el titular es menor de 25 años y es mayor de edad
        return self.titular.edad < 25 and self.titular.esMayorDeEdad()

    def retirar(self, cantidad):
        # Verifica si el titular es válido antes de permitir el retiro
        if self.esTitularValido():
            super().retirar(cantidad)  # Llamamos al método de la clase base para retirar
        else:
            print("No puedes retirar dinero. El titular no es válido para una cuenta joven.")

# Ejemplo de uso:

# Crear un titular (persona)
titular1 = Titular("Raul", 20)  # Instanciamos un titular con nombre y edad

# Crear una cuenta joven
cuenta_joven = CuentaJoven(titular1, 1000, 5)

# Mostrar la información de la cuenta
print(cuenta_joven.mostrar())  # Muestra los detalles de la cuenta joven

# Verificar si el titular es válido
if cuenta_joven.esTitularValido():
    print("El titular es válido para la cuenta joven.")
else:
    print("El titular no es válido para la cuenta joven.")

# Intentar retirar dinero
cuenta_joven.retirar(200)  # Retira 200 euros de la cuenta

# Mostrar la información de la cuenta después del retiro
print(cuenta_joven.mostrar())