"""
 * Escribe una función que reciba dos palabras (String) y retorne
 * verdadero o falso (Bool) según sean o no anagramas.
 * - Un Anagrama consiste en formar una palabra reordenando TODAS
 *   las letras de otra palabra inicial.
 * - NO hace falta comprobar que ambas palabras existan.
 * - Dos palabras exactamente iguales no son anagrama.

 """


def anagrama(n1, n2):
    n1 = n1.lower()
    n2 = n2.lower()

    if sorted(n1) == sorted(n2):
        return True
    else:
        return False


""" # solucion mia, muy larga
def anagrama(n1, n2):
    letras_n1 = []
    letras_n2 = []

    n1 = n1.lower()

    for letra in n1:
        letra.lower()
        letras_n1.append(letra)
        letras_n1.sort()

        print(letras_n1)

    for letra in n2:
        letra.lower()
        letras_n2.append(letra)
        letras_n2.sort()

    if letras_n1 == letras_n2:
        print(True)
    else:
        print(False)
"""

print(anagrama("Casas", "saca"))
