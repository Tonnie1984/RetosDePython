""" Escribe una función que calcule si un número dado es un número de Armstrong
  (o también llamado narcisista).
  Si no conoces qué es un número de Armstrong, debes buscar información
  al respecto.
 """


def numero_armstrong(numero):
    """ es aquel que es igual a la suma de sus dígitos elevados a la potencia de su número de cifras.
        Su nombre alude a lo mucho que parecen "quererse a sí mismos".
    Args:
        numero = número dado

    Returns:
         True or False si es igual a la suma de sus dígitos elevados a la potencia de su número de cifras.
    """
    #  Primera idea de solución:
    potencia = len(str(numero))
    narmstrong = 0
    for digit in str(numero):
        narmstrong = int(digit) ** potencia + narmstrong
    if narmstrong == numero:
        print(True)
    else:
        print(False)


numero_armstrong(153)
