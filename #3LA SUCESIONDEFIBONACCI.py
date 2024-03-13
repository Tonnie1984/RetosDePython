"""/*
 * Escribe un programa que imprima los 50 primeros números de la sucesión
 * de Fibonacci empezando en 0.
 * - La serie Fibonacci se compone por una sucesión de números en
 *   la que el siguiente siempre es la suma de los dos anteriores.
 *   0, 1, 1, 2, 3, 5, 8, 13...
 */
"""

def fibonacci():
    fibo1 = []
    inicio = (0, 1)
    fibo1.extend(inicio)
    while len(fibo1) <= 50:
        fibo1.append(fibo1[-2] + fibo1[-1])
    return fibo1






print(fibonacci())