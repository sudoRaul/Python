def segundos(hora,minutos,segundos):
    return hora * 60*60 + minutos * 60 + segundos

def horas(segundos):
    horas = segundos // 3600
    segundos -= horas * 3600
    minutos = segundos // 60
    segundos -= segundos * 60
    return horas,minutos,segundos

#Con esta función depende del número de parámetros llamaremos a una función u otra
#Si se introducen varios argumentos se harán como una tupla
def calcular(*args):
    if len(args) == 1:
        return horas(args[0])
    elif len(args) == 3:
        segundos(*args)
    else:
        raise TypeError("Se esperan tres parámetros máximo")
                
if __name__ == "__main__":
    print(segundos(4,12,23))
    hora= map(str, horas(12345)) #Como nos devuelve una tupla pues la convertimos a string
    print(":".join(hora))