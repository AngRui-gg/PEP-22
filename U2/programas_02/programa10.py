"""
programa10
Modifica el programa anterior par que pida en primer lugar el número de jugadores que
van a jugar. Cada jugador irá jugando y el programa mostrará si ha ganado o no a la
banca.
"""

import random

banca = random.randrange(17, 22)

jugadores = int(input("¿Cuántos jugadores van a jugar?: "))
while jugadores < 1:
    print("Tiene que haber al menos 1 jugador")
    jugadores = int(input("¿Cuántos jugadores van a jugar?: "))

for jugador in range(1, jugadores + 1):
    print("\n--- TURNO DE JUGADOR ", jugador, "---")
    puntos = 0
    seguir = 1

    while seguir == 1 and puntos <= 21:
        carta = random.randrange(1, 6)
        puntos += carta
        print("Has sacado un", carta, "→ Tu puntuación: ", puntos)

        if puntos <= 21:
            seguir = int(input("¿Quieres otra carta? (1 = sí, 0 = no): "))
            while seguir != 1 and seguir != 0:
                print("Opción no válida")
                seguir = int(input("¿Quieres otra carta? (1 = sí, 0 = no): "))

    if puntos > 21:
        print("Jugador ", jugador, " se ha pasado de 21. Perdedor!!")
    elif puntos > banca:
        print("Jugador ", jugador, " ¡Has ganado!")
    else:
        print("Jugador ", jugador, " pierde (igual o menor que la banca)")

print("\nPuntuación de la banca: ", banca)
