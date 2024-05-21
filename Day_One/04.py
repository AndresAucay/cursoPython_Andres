import random

def adivinar_numero():
    numero_secreto = random.randint(1, 100)  
    intentos = 2

    print("Intenta adivinar un numero al azar entre el 1 y el 100")

    while True:
        intento = int(input("Introduce el numero que crees correcto: "))
        intentos += 1

        if intento < numero_secreto:
            print("Demasiado bajo.")
        elif intento > numero_secreto:
            print("Demasiado alto.")
        else:
            print(f"¡Felicidades! ¡Adivinaste el número en {intentos} intentos!")
            break


adivinar_numero()
