def mostrar_primeros_colaboradores(num_colaboradores=5):
    with open("colaboradores.txt", "r") as file:
        colaboradores = file.readlines()

    print("Los primeros {} colaboradores son:".format(num_colaboradores))
    for i in range(min(num_colaboradores, len(colaboradores))):
        print(colaboradores[i].strip())


def agregar_colaborador(nombre):
    with open("colaboradores.txt", "r") as file:
        colaboradores = file.readlines()

    if len(colaboradores) >= 15:
        print("No se pueden agregar más colaboradores. Se alcanzó el límite máximo.")
        return

    with open("colaboradores.txt", "w") as file:
        file.write(nombre + "\n")
        print("Colaborador {} agregado correctamente.".format(nombre))


mostrar_primeros_colaboradores()

nuevo_colaborador = input("Ingrese el nombre del nuevo colaborador: ")

if nuevo_colaborador:
    agregar_colaborador(nuevo_colaborador)
