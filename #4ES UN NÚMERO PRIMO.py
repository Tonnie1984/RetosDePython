"""/*
 * Escribe un programa que se encargue de comprobar si un número es o no primo.
 * Hecho esto, imprime los números primos entre 1 y 100.
 */
"""

"""Un número primo es un número natural mayor que 1 que solo tiene dos divisores distintos: 1 y él mismo.
En otras palabras, un número primo es un número que no puede ser dividido exactamente por ningún otro número
que no sea 1 y el propio número primo.
"""


def es_primo(n1):
    primos = []
    for n in range(2, n1):
        if n1 % n == 0:
            primos.append(n)

    if len(primos) == 0:
        return True
    else:
        return False


def primos_rango(n1):
    for n in range(2, n1):
        if es_primo(n):
            print(n)


primos_rango(470)
