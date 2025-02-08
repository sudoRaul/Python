#Los bytes son inmutables
byte1 = b"hola"
byte2 = bytes(10) #Crea 10 bytes
byte3 = bytes(range(10)) #Crea 10 bytes
byte4 = bytes.fromhex("2EF0 F1F2") #En hexadecimal
byte5 = bytes("piña", "utf-8")
byte6= "piña".encode("utf-8")
#Util para cuando no sabemos con que tipo de caracteres estamos tratando
cadenaConÑ= byte6.decode("utf-8")

#Los byteArray son mutable y se pueden usar todos los métodos de las secuencias
#Ordenar sum max min in, etc
#Los métodos son similares a los de los arrays y cadenas
byteArray = bytearray(b"hola")

