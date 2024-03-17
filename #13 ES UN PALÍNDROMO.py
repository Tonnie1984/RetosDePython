"""
 * Escribe una función que reciba un texto y retorne verdadero o
 * falso (Boolean) según sean o no palíndromos.
 * Un Palíndromo es una palabra o expresión que es igual si se lee
  * de izquierda a derecha que de derecha a izquierda.
 * NO se tienen en cuenta los espacios, signos de puntuación y tildes.
 * Ejemplo: Ana lleva al oso la avellana.
"""
import re
from unicodedata import normalize

TEXTO = input("Texto:")


def es_palindromo(TEXTO):
    """

    Args:
        texto (): = palindromo

    Returns:
        True
        False

    """

    texto = re.sub(r"([^n\u0300-\u036f]|n(?!\u0303(?![\u0300-\u036f])))[\u0300-\u036f]+", r"\1",
                   normalize("NFD", TEXTO), 0, re.I
                   )
    texto = normalize("NFC", texto)

    texto1 = texto[::-1]

    if texto == texto1:
        print(True)
    else:
        print(False)


es_palindromo(TEXTO)
