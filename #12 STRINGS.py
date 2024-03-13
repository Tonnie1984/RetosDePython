"""* Crea una función que reciba dos cadenas como parámetro (str1, str2)
 * e imprima otras dos cadenas como salida (out1, out2).
 * - out1 contendrá todos los caracteres presentes en la str1 pero NO
 *   estén presentes en str2.
 * - out2 contendrá todos los caracteres presentes en la str2 pero NO
 *   estén presentes en str1.
"""
import re

STR1 = "contendrá todos los caracteres presentes en la str1 pero NO estén presentes en str2.2"  # input(" introduzca primera cadena: ")
STR2 = "reciba dos cadenas como parámetro (str1, str2) imprima otras dos cadenas como salida"  # input(" introduzca segunda cadena: ")


def strings_check(SRT1, SRT2):
    """ Crea una función que reciba dos cadenas como parámetro (str1, str2
    e imprima otras dos cadenas como salida (out1, out2).

    Args:
        SRT1 ():
        SRT2 ():

    Returns:
        out1 =  contendrá todos los caracteres presentes en la str1 pero NO estén presentes en str2.
        out2 =contendrá todos los caracteres presentes en la str2 pero NO estén presentes en str1.

    """
    out1 = []
    out2 = []
    for letra in SRT1.casefold():
        if letra not in SRT2.casefold() and letra  not in out1:
            out1.append(letra)

    for letra in SRT2.casefold():
        if letra not in SRT1.casefold() and letra not in out2:
            out2.append(letra)

    print(out1,out2)







strings_check(STR1, STR2)
