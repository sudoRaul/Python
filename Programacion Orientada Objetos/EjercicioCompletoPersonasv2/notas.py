class Notas():

	def __init__(self):
		self._notas={}

	
	@property
	def notas(self):
		resultado=""
		for key,value in self._notas.items():
			resultado+=key+":"+str(value)+"\n"
		return resultado

	def addnotas(self,asig,nota):
        #Coge la clave que es el nombre del alumno y añade su nota
		self._notas[asig]=nota

	def modnota(self,asig,nota):
		if asig in self._notas.keys():
            #Recorre el diccionario de notas y la actualiza
			self._notas[asig]=nota
		else:
			raise ValueError("Asignatura incorrecta")

	def delnota(self,asig):
		if asig in self._notas.keys():
			del self._notas[asig]
		else:
			raise ValueError("Asignatura incorrecta")

	def media(self):
		return sum(self._notas.values())/len(self._notas.values())

	def __str__(self):
		resultado=""
		for key,value in self._notas.items():
			resultado+=key+":"+str(value)+"\n"
		return resultado
			