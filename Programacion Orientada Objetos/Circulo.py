from metodosCirculo import CalculadoraGeometrica
#Python va a saber que calculadora es de tipo CalculadoraGeometrica porque buscara los metodos  
#de area y perimetro, no es como en Java que estableces exactamente de que tipo es el campo
class Circulo:
    def __init__(self, radio, calculadora):
        # Inicializamos el valor del radio
        self.radio = radio
        self.calculadora = calculadora

    @property
    def radio(self):
        # Este es el getter que devuelve el valor del radio, es necesario poner el @property
        #El __ significa que el atributo es privado y no se debe acceder de forma directa
        print("Accediendo al radio")
        return self.__radio

    @radio.setter
    def radio(self, radio):
        # Este es el setter que valida que el radio sea positivo antes de asignarlo, es necesario poner el @radio.setter
        #El __ significa que el atributo es privado y no se debe acceder de forma directa
        if radio >= 0:
            self.__radio = radio
        else:
            print("El radio debe ser positivo")
            self.__radio = 0
            
    #Dentro de ambos métodos estamos hacienodo una llamada al getter de radio para obtener su valor y calcular ambas operaciones
    def area(self):
        return self.calculadora.calcular_area_circulo(self.radio)
    
    def perimetro(self):
        return self.calculadora.perimetro_circulo(self.radio)

# Ejemplo de uso, Python sabe que metodo usar dependiendo si estas asignando un valor o estas cogiendo el valor de radio

calculadora = CalculadoraGeometrica()
circulo = Circulo(5, calculadora)  # Usamos el constructor para asignar el valor
print(circulo.radio)   # Usamos el getter para acceder al valor del radio

circulo.radio = 3     # Intentamos asignar un valor negativo
print(circulo.radio)   # El valor del radio sigue siendo 0 debido a la validación

print(circulo.area()) 
