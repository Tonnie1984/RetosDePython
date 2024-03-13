"""/*
 * Crea un programa que invierta el orden de una cadena de texto
 * sin usar funciones propias del lenguaje que lo hagan de forma automática.
 * - Si le pasamos "Hola mundo" nos retornaría "odnum aloH"""

CADENA = input(" Ingrese texto: ")


def invertir_cadena(CADENA):
    cadena_inversa = []
    for _ in CADENA[-1::-1]:
        cadena_inversa.append(_)

    cadena = "".join(cadena_inversa)


    print(cadena_inversa, str(cadena))


invertir_cadena(CADENA)
