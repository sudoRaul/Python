contrasena = "raul"
#De esta forma siempre entrará en el bucle al menos una vez
while True:
    contrUser = input("Introduzca la contraseña: ")
    if contrUser != contrasena:
        continue
    print("CONTRASEÑA CORRECTA")
    break