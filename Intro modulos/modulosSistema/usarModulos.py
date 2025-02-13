#Se puede añadir un alias o no
import ejemploModulos as p
from ejemploModulos import cuadrado, cubo #Puedes importar solo las funciones
from ejemploModulos import * #Puedes importar todas las funciones
#Cuando importas dos módulos puede ser que tengan funciones con el mismo nombre por eso
#también se puede dar un alias
#from ejemploModulos import cubo as miCubo
print(p.cuadrado(2))
print(cubo(4))

#Importar paquetes
#import nombrePaquete.modulo
#from nombrePaquete.modulo import miFuncion
#Conforme tengamos más paquetes debemos ir llamandolos con el .

#Devuelve las funciones que podemos usar
print(dir(p))

