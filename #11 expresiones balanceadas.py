"""Crea un programa que comprueba si los paréntesis, llaves y corchetes
 * de una expresión están equilibrados.
 * - Equilibrado significa que estos delimitadores se abren y cieran
 *   en orden y de forma correcta.
 * - Paréntesis, llaves y corchetes son igual de prioritarios.
 *   No hay uno más importante que otro.
 * - Expresión balanceada: { [ a * ( c + d ) ] - 5 }
 * - Expresión no balanceada: { a * ( c + d ) ] - 5 }

 """
import re

TEXT = input(" expersion: ")

def use_regex(TEXT):
    texto = TEXT.split()
    for i in texto:
        if i == "{" or "[" or "(":
            for x in texto:
                if x == "}" and i == "{":
                    texto.remove(x)
                    texto.remove(i)
                elif x == "]" and i == "[":
                    texto.remove(x)
                    texto.remove(i)
                elif x == ")" and i == "(":
                    texto.remove(x)
                    texto.remove(i)
        else:
            pass

    texto ="".join(texto)
    if "[" or "]" or "{" or "}" or "(" or ")" in texto:
        print(True)
    else:
        print(False)






use_regex(TEXT)