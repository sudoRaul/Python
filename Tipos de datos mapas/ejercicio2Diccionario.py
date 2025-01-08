dicFrutas = {"manzanas": 1.5, "peras": 1.2, "platano": 0.96, "melocoton": 1.75}
while True:
    fruta_user = input("Introduzca la fruta a buscar: ")
    cantidad_user = int(input("Introduzca la cantidad: "))
    fruta_seleccionada = dicFrutas.get(fruta_user, " ")
    if fruta_seleccionada != " ":
        print("La cantidad de %d %s cuesta %.2f" % (cantidad_user, fruta_user, cantidad_user*fruta_seleccionada))
    else:
        print("ERROR")
    decision = input("Quiere seguir buscando (Y/N): ").lower()
    if decision == "n":
        break