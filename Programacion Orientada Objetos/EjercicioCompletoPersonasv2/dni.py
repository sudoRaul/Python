class DNI():
    def __init__(self, numero):
        self.numero=numero
        
    def __calcularLetra(self):
        letras = "TRWAGMYFPDXBNJZSQVHLCKE"
        return letras[int(self.numero)%23]
    
    @property
    def numero(self):
        return self._numero
    
    @numero.setter
    def numero(self, num):
        if(len(num )==8 and num.isdigit()):
            self._numero = num
            self._letra = self.__calcularLetra()
        else:
            raise ValueError("Invalid numero")
        
    @property
    def letra(self): 
        return self._letra
    
    def __str__(self):
        return "{0}-{1}".format(self._numero, self._letra)