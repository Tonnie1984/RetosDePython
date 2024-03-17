"""
 * Escribe una función que reciba un texto y retorne verdadero o
 * falso (Boolean) según sean o no palíndromos.
 * Un Palíndromo es una palabra o expresión que es igual si se lee
  * de izquierda a derecha que de derecha a izquierda.
 * NO se tienen en cuenta los espacios, signos de puntuación y tildes.
 * Ejemplo: Ana lleva al oso la avellana.
"""

TEXTO = input("Texto:")


def es_palindromo(TEXTO):
    """

    Args:
        texto (): = palindromo

    Returns:
        True
        False

    """
    texto = TEXTO.casefold().replace(" ", "")
    texto1 = texto[::-1]

    if texto == texto1:
        print(True)
    else:
        print(False)


es_palindromo(TEXTO)
