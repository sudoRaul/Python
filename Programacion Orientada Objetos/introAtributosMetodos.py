class Alumno():
    #Esto es un atributo de clase, se puede llamar con el nombre de la clase .atributo
    contador = 0
    def __init__(self, nombre):
        #Esto es un atributo de objeto, se llama con el propio self
        self.nombre = nombre
        #Este atributo es privado, se indican con el guion bajo previamente
        #Es más una convencion debido a que realmente si se puede acceder directamente a este atributo
        self._secreto = "asdasd"
        #Usando dos guiones bajo es como un nivel mas de ocultamiento
        #Es mas complicado acceder a el ya que no sería únicamente con el nombre del objeto
        #Sino que seria: alumno1._Alumno.__massecreto
        self.__massecreto = "secretisimo"
        #Cada vez que inicialicemos un alumno se aumentará el atributo de clase
        Alumno.contador += 1
        
    #Los métodos estáticos pertenecen a la clase no al objeto
    #Por ello no hay que pasarle la referencia al objeto self
    #Se llama mediante la clase Alumno.sumar(1,2)
    @staticmethod
    def sumarAlgo(x,y):
        return x + y

a1 = Alumno("fulano")
#Obtenemos el atributo
getattr(a1, "nombre")
#Cambiamos el valor del atributo
setattr(a1, "nombre", "mengano")
#Preguntamos si tiene el atributo
hasattr(a1, "nombre")

        
        