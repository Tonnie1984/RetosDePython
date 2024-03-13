"""* Crea un programa que cuente cuantas veces se repite cada palabra
 * y que muestre el recuento final de todas ellas.
 * - Los signos de puntuación no forman parte de la palabra.
 * - Una palabra es la misma aunque aparezca en mayúsculas y minúsculas.
 * - No se pueden utilizar funciones propias del lenguaje que
 *   lo resuelvan automáticamente.
 """
import re

FRASE = input("Texto: ")


def contar_palabras(FRASE):
    frase = FRASE.lower()
    texto_frase = re.sub(r'[^\w\s]', '', frase)
    palabras = texto_frase.split()
    dic_palabras = {}
    for p in palabras:
        if p in dic_palabras.keys():
            cantidad = dic_palabras[p]
        else:
            cantidad = 0
        if p == p:
            cantidad += 1
        dic_palabras.update({p: cantidad})

    print(dic_palabras)


contar_palabras(FRASE)
