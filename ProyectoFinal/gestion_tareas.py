import json
import os

listaTareas = []

file_path = "ProyectoFinal/listaTareas.json"

def cargarTareas():
    if os.path.exists(file_path):
        with open(file_path, "r") as json_file:
            listaTareas = json.load(json_file)
    else:
        listaTareas = []
        
def guardarTareas():
    with open(file_path, 'w') as json_file:
        json.dump(listaTareas, json_file)

def crearTarea():
    tituloTarea = input("Introduce el título de la tarea: ").strip()
    descripcionTarea = input("Introduce la descripción de la tarea: ").strip()
    estadoTarea = input("Introduce el estado de la tarea: (Completo/Incompleto): ").lower().strip()
    while estadoTarea != "completo" and estadoTarea != "incompleto" and tituloTarea == "" and descripcionTarea == "":
        print("Por favor, introduzca Completo o Incompleto")
        estadoTarea = input("Introduce el estado de la tarea: (Completo/Incompleto): ")
    tarea= {
        "titulo": tituloTarea,
        "descripcion": descripcionTarea,
        "estado": estadoTarea
    }
    #listaTareas.append(tarea)
    cargarTareas()
        
    listaTareas.append(tarea)
    guardarTareas()
        
        
def mostrarTareas():
    cargarTareas()
    
    if len(listaTareas) > 0:
        print("Tareas: ")
        for i, tarea in enumerate(listaTareas, start=1):
            print("Tarea Nº " + str(i))
            for clave, valor in tarea.items():
                print(clave + ": " + str(valor))
            print("-" * 20)
    else:
        print("No hay tareas actualmente, añada alguna para visualizarlas")
    
def actualizarTarea():
    cargarTareas()    
    
    if len(listaTareas) > 0:
        tarea = int(input("Introduzca el índice de la tarea a editar: "))
        tarea -= 1
        try:
            
            campo_editar = int(input(" 1. Editar título \n 2. Editar descripción \n 3. Editar estado \n"))
            while campo_editar < 0 or campo_editar > 3:
                print("Por favor introduzca un número válido")
                campo_editar = int(input("1. Editar título \n 2. Editar descripción \n 3. Editar estado \n"))

            if campo_editar == 1:
                nuevoTitulo = input("Introduzca el nuevo nombre de la tarea: ")
                listaTareas[tarea]["titulo"] = nuevoTitulo
                print("Título de la tarea actualizado. Título actual: " + listaTareas[tarea]["titulo"])
                guardarTareas()
                    
                    
            if campo_editar == 2:
                nuevaDescripcion = input("Introduzca la nueva descripción de la tarea: ")
                listaTareas[tarea]["descripcion"] = nuevaDescripcion
                print("Descripción de la tarea actualizado. Descripción actual: " + listaTareas[tarea]["descripcion"])
                guardarTareas()
                    
                
            if campo_editar == 3:
                if listaTareas[tarea]["estado"] == "completo":
                    listaTareas[tarea]["estado"] = "incompleto"
                else:
                    listaTareas[tarea]["estado"] = "completo"
                print("Estado de la tarea actualizado. Estado actual: " + listaTareas[tarea]["estado"])
                guardarTareas()
                
        except IndexError:
            print("Índice no encontrado, introduzca un índice correcto por favor")
    else:
        print("No hay tareas actualmente, añada alguna para visualizarlas")
    
def eliminarTarea():
    cargarTareas()
        
    if len(listaTareas) > 0:   
        indice_tarea = int(input("Introduzca el índice de la tarea a eliminar: "))
        indice_tarea -= 1
        try:
            del listaTareas[indice_tarea]
            guardarTareas()
        except IndexError:
            print("Índice no encontrado, introduzca un índice correcto por favor")
            
    else:
        print("No hay tareas actualmente, añada alguna para visualizarlas")