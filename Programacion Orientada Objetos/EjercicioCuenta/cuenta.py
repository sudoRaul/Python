class Cuenta:
    def __init__(self, titular, cantidad =0):
        self.__titular = titular
        self.__cantidad = cantidad
        
    @property
    def titular(self):
        return self.__titular
    
    @property
    def cantidad(self):
        return self.__cantidad
    
    @titular.setter
    def titular(self, titular):
        self.__titular = titular
        
        
    def mostrar(self):
        return f"El titular es {self.__titular} y tiene una cantidad de {self.__cantidad} de euros."
    
    def ingresar(self, cantidad):
        if cantidad > 0:
            self.__cantidad += cantidad
        else:
            print("Cantidad introducida incorrecta")
            
    def retirar(self, cantidad):
        if cantidad > 0:
            self.__cantidad -= cantidad
        else:
            print("Cantidad introducida incorrecta")
            
cuenta = Cuenta("alguien", 30)
print(cuenta.titular)
            
            