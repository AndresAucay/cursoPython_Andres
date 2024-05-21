def contar_palabras(texto):
    palabras = texto.split()
    numero_palabras = len(palabras)
    return numero_palabras

texto = "este sabado estare ocupado, no me molesten por favor"

numero_palabras = contar_palabras(texto)


print("El número de palabras en el texto es:", numero_palabras)
