from Punto import Punto
class Punto3d(Punto):
    def __init__(self, x=0,y=0, z=0):
        #Llamamos al constructo de la clase padre
        super().__init__(x,y)
        self.z = z
        
    @property
    def z(self):
        print("Esto es z")
        return self.z
    
    
    @z.setter
    def z(self, z):
        print("Cambio z")
        self.__z = z
        
    def mostrar(self):
        #Devolvemos el metodo mostrar de la clase padre y le añadimos el del nuevo punto
        return super().mostrar() + " : " +str(self.z)