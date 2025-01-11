from persona import Persona
class Alumno(Persona):
    def __init__(self,nombre, edad, dni, curso, nota):
        super().__init__(nombre, edad, dni)
        self._curso = curso #Usamos atributos internos
        self.nota = nota #Para que al inicializar los parámetro se use el setter no hay que hacer los atributos internos
        
    @property
    def curso(self):
        return self._curso
    
    @curso.setter
    def curso(self,curso):
        self._curso = curso
        
    @property
    def nota(self):
        return self._nota
    
    @nota.setter
    def nota(self,nota):
        if 0 <= nota <= 10:
            self._nota = nota
        else:
            self._nota = 0
            print("Nota incorrecta")
        
    def isAprobado(self):
        return "Usted está aprobado" if self._nota >= 5 else "Usted está suspenso"
        
    def mostrar(self):
        return f"{super().mostrar()} está matriculado en {self._curso} y ha sacado un {self._nota}, es decir, {self.isAprobado()}"
            
            
alum1 = Alumno("Raul", 20, "21038262R", "2ºDAW", -7)
print(alum1.mostrar())
