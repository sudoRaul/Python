from notas import Notas
from persona import Persona
from dni import DNI

class Alumno(Persona,Notas):
    def __init__(self,dni, nombre, edad):
        Persona.__init__(self,dni,nombre,edad)
        Notas.__init__(self)
        
    def __str__(self):
        return Persona.__str__(self) + "\n"+Notas.__str__(self)

#RECORDAR en la delegación cuando llamas al constructor de la clase hay que pasarle 
#el constructor de la clase "que se delega"
a1 = Alumno(DNI("12345678"), "raul", 23)
a1.addnotas("mates", 4)
print(a1)