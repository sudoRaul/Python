import json
import os

file_path = "ProyectoFinal/listaTareas.json"

print("Bienvenido a la aplicación de gestión de tareas")

def cargar_tareas():
    if os.path.exists(file_path):
        try:
            with open(file_path, "r") as json_file:
                return json.load(json_file)
        except json.JSONDecodeError:
            return []
    return []

def guardar_tareas(listaTareas):
    with open(file_path, "w") as json_file:
        json.dump(listaTareas, json_file, indent=4)

def validar_opcion(mensaje, opciones_validas):
    while True:
        opcion = input(mensaje).strip()
        if opcion in opciones_validas:
            return opcion
        print("❌ Opción no válida, intenta de nuevo.")

def obtener_indice(mensaje, lista):
    while True:
        try:
            indice = int(input(mensaje)) - 1
            if 0 <= indice < len(lista):
                return indice
            print("❌ Índice fuera de rango.")
        except ValueError:
            print("❌ Debes introducir un número válido.")

def crear_tarea():
    titulo = input("Introduce el título de la tarea: ").strip()
    while not titulo:
        print("❌ El título no puede estar vacío.")
        titulo = input("Introduce el título de la tarea: ").strip()
    
    descripcion = input("Introduce la descripción de la tarea: ").strip()
    while not descripcion:
        print("❌ La descripción no puede estar vacía.")
        descripcion = input("Introduce la descripción de la tarea: ").strip()
    
    estado = validar_opcion("Introduce el estado de la tarea (1: Completo, 2: Incompleto): ", ["1", "2"])
    estado = "completo" if estado == "1" else "incompleto"
    
    listaTareas = cargar_tareas()
    listaTareas.append({"titulo": titulo, "descripcion": descripcion, "estado": estado})
    guardar_tareas(listaTareas)
    print("✅ Tarea añadida correctamente.")

def mostrar_tareas():
    listaTareas = cargar_tareas()
    if listaTareas:
        for i, tarea in enumerate(listaTareas, start=1):
            print(f"\nTarea Nº {i}")
            for clave, valor in tarea.items():
                print(f"{clave.capitalize()}: {valor}")
            print("-" * 20)
    else:
        print("📭 No hay tareas actualmente.")

def actualizar_tarea():
    listaTareas = cargar_tareas()
    if not listaTareas:
        print("📭 No hay tareas actualmente.")
        return
    
    indice = obtener_indice("Introduce el índice de la tarea a editar: ", listaTareas)
    campo = validar_opcion(" 1. Editar título\n 2. Editar descripción\n 3. Cambiar estado\n", ["1", "2", "3"])
    
    if campo == "1":
        nuevo_titulo = input("Introduce el nuevo título: ").strip()
        while not nuevo_titulo:
            print("❌ El título no puede estar vacío.")
            nuevo_titulo = input("Introduce el nuevo título: ").strip()
        listaTareas[indice]["titulo"] = nuevo_titulo
    elif campo == "2":
        nueva_descripcion = input("Introduce la nueva descripción: ").strip()
        while not nueva_descripcion:
            print("❌ La descripción no puede estar vacía.")
            nueva_descripcion = input("Introduce la nueva descripción: ").strip()
        listaTareas[indice]["descripcion"] = nueva_descripcion
    else:
        listaTareas[indice]["estado"] = "completo" if listaTareas[indice]["estado"] == "incompleto" else "incompleto"
    
    guardar_tareas(listaTareas)
    print("✅ Tarea actualizada correctamente.")

def eliminar_tarea():
    listaTareas = cargar_tareas()
    if not listaTareas:
        print("📭 No hay tareas actualmente.")
        return
    
    indice = obtener_indice("Introduce el índice de la tarea a eliminar: ", listaTareas)
    del listaTareas[indice]
    guardar_tareas(listaTareas)
    print("✅ Tarea eliminada correctamente.")

def comprobar_opcion():
    while True:
        opcion = validar_opcion("\n¿Qué desea hacer?\n1. Crear una tarea\n2. Mostrar las tareas\n3. Actualizar una tarea\n4. Eliminar una tarea\n-1. Salir\n", ["1", "2", "3", "4", "-1"])
        
        if opcion == "-1":
            print("👋 Hasta pronto!")
            break
        elif opcion == "1":
            crear_tarea()
        elif opcion == "2":
            mostrar_tareas()
        elif opcion == "3":
            actualizar_tarea()
        elif opcion == "4":
            eliminar_tarea()

if __name__ == "__main__":
    comprobar_opcion()
