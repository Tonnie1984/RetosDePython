"""
 Escribe una función que calcule y retorne el factorial de un número dado
 de forma recursiva.
 """


#  Solución sin usar el método interno de Python:
def factorial_numero(numero):
    factorial = numero
    while numero > 1:
        factorial = factorial * (numero - 1)
        numero = numero - 1
    return factorial


print(factorial_numero(20))

#  Solución usando  el método interno de Python:
from math import factorial


def factorial_metodo_interno(numero):  # https://www.w3schools.com/python/ref_math_factorial.asp
    return factorial(numero)


print(factorial_metodo_interno(20))
