def mostrar_menu():
    print("\nMenú de Tareas:")
    print("1. Agregar nueva tarea")
    print("2. Eliminar tarea")
    print("3. Mostrar todas las tareas")
    print("4. Salir")

def agregar_nueva_tarea(tareas):
    tarea = input("Introduce la tarea para agregar: ")
    tareas.append(tarea)
    print(f"Tarea '{tarea}' agregada.")

def eliminar_tarea(tareas):
    mostrar_todastareas(tareas)
    try:
        indice = int(input("Introduce el número de la tarea que quieres eliminar: "))
        if 1 <= indice <= len(tareas):
            tarea = tareas.pop(indice - 1)
            print(f"Tarea '{tarea}' eliminada.")
        else:
            print("Número  no válido.")
    except ValueError:
        print(" Por favor, introduce un número.")

def mostrar_todastareas(tareas):
    if tareas:
        print("\nLista de Tareas Pendientes:")
        for i, tarea in enumerate(tareas, 1):
            print(f"{i}. {tarea}")
    else:
        print("No hay tareas pendientes.")

def main():
    tareas = []
    while True:
        mostrar_menu()
        opcion = input("Elige una opción: ")

        if opcion == '1':
            agregar_nueva_tarea(tareas)
        elif opcion == '2':
            eliminar_tarea(tareas)
        elif opcion == '3':
            mostrar_todastareas(tareas)
        elif opcion == '4':
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, elige una opción del 1 al 4.")

if __name__ == "__main__":
    main()