tareas = []

def mostrar_tareas():
    if not tareas:
        print("No hay tareas.")
    else:
        for i, tarea in enumerate(tareas, 1):
            print(f"{i}. {tarea}")

def agregar_tarea():
    tarea = input("Escribe la nueva tarea: ")
    tareas.append(tarea)

def eliminar_tarea():
    mostrar_tareas()
    indice = int(input("Introduce el número de la tarea a eliminar: "))
    if 0 < indice <= len(tareas):
        tareas.pop(indice - 1)
    else:
        print("Número inválido.")

while True:
    print("\n1. Mostrar tareas\n2. Agregar tarea\n3. Eliminar tarea\n4. Salir")
    opcion = input("Elige una opción: ")

    if opcion == "1":
        mostrar_tareas()
    elif opcion == "2":
        agregar_tarea()
    elif opcion == "3":
        eliminar_tarea()
    elif opcion == "4":
        break
    else:
        print("Opción inválida.")
        
        