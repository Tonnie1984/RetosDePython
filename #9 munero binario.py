""" * Crea un programa se encargue de transformar un número
 * decimal a binario sin utilizar funciones propias del lenguaje que lo hagan directamente.
 """
DECIMAL = input( "numero : ")


def decimal_binario(DECIMAL):

    resultado = int(DECIMAL)
    decimal= []
    while resultado / 2 >= 1:
           resto = resultado % 2
           resultado = int(resultado / 2)
           if resultado >= 2:
               decimal.append(str(resto))
           else:
               decimal.extend([str(resto),str(resultado)])

           print(resultado, resto, decimal)
    decimal.reverse()
    cadena_invertida = "".join(decimal)
    print(cadena_invertida)


decimal_binario(DECIMAL)