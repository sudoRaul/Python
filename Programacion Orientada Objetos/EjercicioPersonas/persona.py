class Persona:
    def __init__(self, nombre="", edad=0, dni=""):
        self._nombre = nombre  # Usamos nombres internos para evitar conflictos con getters/setters
        self._edad = edad
        self._dni = dni
        self.validarDNI()  # Validamos el DNI al inicializar

    # Propiedad nombre
    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    # Propiedad edad
    @property
    def edad(self):
        return self._edad

    @edad.setter
    def edad(self, edad):
        if edad < 0:
            print("Edad incorrecta")
            self._edad = 0
        else:
            self._edad = edad

    # Propiedad DNI
    @property
    def dni(self):
        return self._dni

    @dni.setter
    def dni(self, dni):
        self._dni = dni
        self.validarDNI()  # Validamos el DNI al asignarlo

    # Validar DNI
    def validarDNI(self):
        letras = "TRWAGMYFPDXBNJZSQVHLCKE"
        if len(self._dni) != 9:
            print("DNI incorrecto: longitud inválida")
            self._dni = ""
        else:
            letra = self._dni[-1]
            try:
                num = int(self._dni[:-1])  # Convertimos los primeros 8 caracteres a número
                if letra.upper() != letras[num % 23]:
                    print("DNI incorrecto: letra inválida")
                    self._dni = ""
            except ValueError:
                print("DNI incorrecto: los primeros 8 caracteres deben ser números")
                self._dni = ""

    # Mostrar información de la persona
    def mostrar(self):
        return f"{self.nombre} tiene {self.edad} años y su DNI es {self._dni}"

    # Verificar si es mayor de edad
    def mayorEdad(self):
        return "Eres mayor de edad" if self.edad >= 18 else "Eres menor de edad"


# Ejemplo de uso
persona1 = Persona("Raul", 19, "21038262R")
#print(persona1.dni)
#print(persona1.mostrar())
persona1.dni = "21038262R"
