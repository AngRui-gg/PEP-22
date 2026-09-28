"""
programa08
Escribe un programa para jugar a adivinar un número. En primer lugar la aplicación
solicita genera un número aleatorio entre 1 y 20. A continuación va pidiendo números y va
respondiendo si el número a adivinar es mayor o menor que el introducido. El programa
termina cuando se acierta el número.
"""

import random

secreto = random.randrange(1, 21)
intentos = 3
acertado = False

while intentos > 0 and not acertado:
    num = int(input("Adivina el número (entre 1 y 20): "))
    intentos -= 1

    if num == secreto:
        acertado = True
    elif secreto > num:
        print("El número a adivinar es mayor")
    else:
        print("El número a adivinar es menor")

    if not acertado and intentos > 0:
        print("Te quedan", intentos, "intentos")

if acertado:
    print("¡Has acertado!")
else:
    print("Has agotado los intentos. El número era: ", secreto)
