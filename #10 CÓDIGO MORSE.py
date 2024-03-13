"""/*
 * Crea un programa que sea capaz de transformar texto natural a código
 * morse y viceversa.
 * - Debe detectar automáticamente de qué tipo se trata y realizar
 *   la conversión.
 * - En morse se soporta raya "—", punto ".", un espacio " " entre letras
 *   o símbolos y dos espacios entre palabras "  ".
 * - El alfabeto morse soportado será el mostrado en
 *   https://es.wikipedia.org/wiki/Código_morse.
 */
 """

MORSE_TABLE = {"Signo": "Código",
               "A": "·—", "B": "—···", "C": "—·—·", "D": "—··", "E": "·", "F": "··—·", "G": "——·",
               "H": "····", "I": "··", "J": "·———", "K": "—·—", "L": "·—··", "M": "——", "N": "—·",
               "Ñ": "——·——", "O": "———", "P": "·——·", "Q": "——·—", "R": "·—·", "S": "···", "T": "—",
               "U": "··—", "V": "···—", "W": "·——", "X": "—··—", "Y": "—·——", "Z": "——··",
               "0": "—————", "1": "·————", "2": "··———", "3": "···——", "4": "····—",
               "5": "·····", "6": "—····", "7": "——···", "8": "———··", "9": "————·",
               ".": "·—·—·—", ",": "——··——",
               "?": "··——··", " ":" "
               }

TEXTO = input("Texto:")


def morse_table(TEXTO):
    texto = TEXTO.upper()
    texto_traducido = []
    if TEXTO[0:1].isalnum() or TEXTO[1:2].isalnum() or TEXTO[2:3].isalnum():
        for letra in texto:
            if letra == " ":
                texto_traducido.append(" ")
            else:
                texto_traducido.append(MORSE_TABLE[letra] + " ")
        traduccion = "".join(texto_traducido)

    elif (TEXTO[0:1] == "." or "—") or (TEXTO[1:2] == "." or "—"):
        texto = texto.replace("  ", " $ ")
        texto_split = texto.split(" ")
        for item in texto_split:
            if item == "$":
                texto_traducido.extend(" ")
            else:
                value = [i for i in MORSE_TABLE if MORSE_TABLE[i] == item]
                texto_traducido.extend(value)
        traduccion = "".join(texto_traducido)

    print(traduccion)


morse_table(TEXTO)
