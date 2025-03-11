import json
import os

listaTareas = []

file_path = "ProyectoFinal/listaTareas.json"

print("Bienvenido a la aplicación de gestión de tareas")

from gestion_tareas import crearTarea, mostrarTareas, actualizarTarea, eliminarTarea

#Esta función se itera mientras que el valor indicado no sea -1
def comprobarOpcion():
    while True:
        try:
            opcion = int(input("¿Qué desea hacer? \n1. Crear una tarea \n2. Mostrar las tareas \n3. Actualizar una tarea \n4. Eliminar una tarea \n-1. Salir \n"))
            #Si elige -1 finaliza el programa
            if opcion == -1:
                print("Esperemos verle pronto")
                break  # Salimos del bucle y terminamos el programa
            #Si introduce un valor válido ejecutamos la función que corresponda, hasta que elija -1
            elif 1 <= opcion <= 4:
                if opcion == 1: 
                    crearTarea()
                elif opcion == 2:
                    mostrarTareas()
                elif opcion == 3:
                    actualizarTarea()
                elif opcion == 4:
                    eliminarTarea()
            else:
                print("❌ Opción no válida, intenta de nuevo.")
        except ValueError:
            print("❌ Debes introducir un número válido.")


if __name__ == "__main__":
    try: 
        comprobarOpcion()
    except ValueError:
        print("Debes introducir un número")
        comprobarOpcion()

