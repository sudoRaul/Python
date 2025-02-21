from metodosCirculo import CalculadoraGeometrica

# Python va a saber que calculadora es de tipo CalculadoraGeometrica porque buscará los métodos
# de área y perímetro, no es como en Java que estableces exactamente de qué tipo es el campo
class Circulo:
    def __init__(self, radio, calculadora):
        # Inicializamos el valor del radio
        self.radio = radio  # Estamos llamando al setter
        self.calculadora = calculadora

    @property  # Realmente es un getter
    def radio(self):
        # Este es el getter que devuelve el valor del radio, es necesario poner el @property
        # El __ significa que el atributo es privado y no se debe acceder de forma directa
        print("Accediendo al radio")
        return self.__radio

    @radio.setter
    def radio(self, radio):
        # Este es el setter que valida que el radio sea positivo antes de asignarlo, es necesario poner el @radio.setter
        # El __ significa que el atributo es privado y no se debe acceder de forma directa
        if radio >= 0:
            self.__radio = radio
        else:
            print("El radio debe ser positivo")
            self.__radio = 0

    # Elimina el atributo
    @radio.deleter
    def radio(self):
        del self.__radio

    # Dentro de ambos métodos estamos haciendo una llamada al getter de radio para obtener su valor y calcular ambas operaciones
    def area(self):
        return self.calculadora.calcular_area_circulo(self.radio)

    def perimetro(self):
        return self.calculadora.perimetro_circulo(self.radio)

    #Representacion informal del objeto, es decir podemos usar print
    def __str__(self):
        clase = type(self).__name__
        msg = "{0} de radio {1}"
        return msg.format(clase, self.radio)

    #Representacion formal del objeto
    def __repr__(self):
        clase = type(self).__name__
        msg = "{0}({1})"
        return msg.format(clase, self.radio)

    #Permite comparar objetos con el ==
    def __eq__(self, otro):
        return self.radio == otro.radio

    #Permite sumar un circulo con otro, es decir un radio mas otro
    def __add__(self, otro):
        self.radio += otro.radio

    #Permite restar un circulo con otro, restando dos radios aunque no puede ser negativo
    def __sub__(self, otro):
        if self.radio - otro.radio >= 0:
            self.radio -= otro.radio
        else:
            raise ValueError("No se pueden restar")

# Ejemplo de uso, Python sabe qué método usar dependiendo de si estás asignando un valor o estás cogiendo el valor de radio
calculadora = CalculadoraGeometrica()
circulo = Circulo(5, calculadora)  # Usamos el constructor para asignar el valor
print(circulo.radio)  # Usamos el getter para acceder al valor del radio

circulo.radio = 3  # Intentamos asignar un valor negativo
print(circulo.radio)  # El valor del radio sigue siendo 0 debido a la validación

print(circulo.area())
