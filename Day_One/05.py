def mostrar_tareas(tareas):
    if not tareas:
        print("No hay tareas pendientes.")
    else:
        print("Tareas pendientes:")
        for i, tarea in enumerate(tareas, start=1):
            print(f"{i}. {tarea}")

def agregar_tarea(tareas, tarea):
    tareas.append(tarea)
    print(f"Tarea '{tarea}' agregada.")

def eliminar_tarea(tareas, indice):
    if 1 <= indice <= len(tareas):
        tarea_eliminada = tareas.pop(indice - 1)
        print(f"Tarea '{tarea_eliminada}' eliminada.")
    else:
        print("Índice de tarea no válido.")

def main():
    tareas = []

    while True:
        print("\n1. Mostrar tareas")
        print("2. Agregar tarea")
        print("3. Eliminar tarea")
        print("4. Salir")

        opcion = input("Elige una opción: ")

        if opcion == "1":
            mostrar_tareas(tareas)
        elif opcion == "2":
            nueva_tarea = input("Introduce la nueva tarea: ")
            agregar_tarea(tareas, nueva_tarea)
        elif opcion == "3":
            indice = int(input("Introduce el índice de la tarea a eliminar: "))
            eliminar_tarea(tareas, indice)
        elif opcion == "4":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, elige una opción válida.")

if __name__ == "__main__":
    main()
