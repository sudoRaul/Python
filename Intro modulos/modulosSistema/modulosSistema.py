import os #Funcionalidad del sistema operativo
import os.path #Permite obtener información de ficheros o directorios
import subprocess #Para guardar la salida de un comando en una variable
import shutil #Permite copiar ficheros, obtener información del espacio total, etc
import sys #Nos sirve para pedir información del intérprete de Python
os.getcwd() #Directorio en el que estamos trabajando
os.chdir("..") #Cambiamos el directorio actual


os.system("ls") #Muestra la salida de esa instruccion
salida = subprocess.check_output("ls")

salida2 = subprocess.check_output(["df", "-h"]) #Tratar comandos con parámetros

sys.exit() #Para salir del programa, cortar la ejecución
sys.version #Version de Python
sys.platform #SO que estamos usando Linuz, Windows


#EJEMPLO 1
#Devuelve el directorio actual más el separador para separar archivos
ruta = os.getcwd() + os.sep
origen= ruta + "fichero.txt"
destino = ruta + "destino.txt"

try:
    #Copia un fichero con otro
    shutil.copyfile(origen, destino)
    print("Archivo copiado")
except:
    print("Se ha producido un error")
    
#EJEMPLO 2
#Lee todos los argumentos que se le pasen al ejecutar el programa, y los suma

print("Has introducido",len(sys.argv),"argumento")
suma=0
for i in range(1,len(sys.argv)):
	suma=suma+int(sys.argv[i])
print("La suma es ",suma)