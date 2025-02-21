class punto():
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        
    @property
    def x(self):
        return self._x
    
    @x.setter
    def x(self, x):
        self._x = x
    
    @property
    def y(self):
        return self._y
    
    @y.setter
    def y(self, value):
        self._y=value
        
    def __str__(self):
          return "{0}:{1}".format(self.x, self.y)
      
    def distancia(self, otro):
        dx = self.x - otro.x
        dy = self.y - otro.y
        return(dx * dx + dy * dy)**0.5

#La delegación consiste en que un atributo de una clase es del tipo
#de otra clase definida por nosotros, en este caso el centro es un punto
#Para usar la delegación cuando se cree un objeto de la clase circulo en
#el constructor de la clase circulo hay que pasarle un punto
#Ej: c1 = circulo(Punto(2,3), 5)
class circulo():	

	def __init__(self,centro,radio):
		self.centro=centro
		self.radio=radio	

	def __str__(self):
		return "Centro:{0}-Radio:{1}".format(self.centro.__str__(),self.radio)	