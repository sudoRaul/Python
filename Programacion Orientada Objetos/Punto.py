import math

class Punto():
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        
    def mostrar(self):
        return str(self.x) + " : " + str(self.y)
    
    def distancia(self, otro):
        dx = self.x - otro.x
        dy = self.y - otro.y
        return math.sqrt(dx * dx + dy * dy)

# Ejemplo de uso
punto1 = Punto(3, 4)
punto2 = Punto(0, 0)

print("Punto 1:", punto1.mostrar())  # Punto 1: 3 : 4
print("Punto 2:", punto2.mostrar())  # Punto 2: 0 : 0

distancia = punto1.distancia(punto2)
print("Distancia entre puntos:", distancia)  # Distancia entre puntos: 5.0
