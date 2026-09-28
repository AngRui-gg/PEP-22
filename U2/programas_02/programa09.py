"""
programa09
Escribe un programa para jugar a una versión muy simplificada del black jack. En primer
lugar el ordenador obtendrá un número aleatorio entre 17 y 21 (está será su jugada). A
continuación el jugador ira sacando cartas (con valores entre 1 y 5), que se irán sumando
para obtener su puntuación, hasta que el quiera. Si se pasa de 21 pierde, si obtiene una
puntuación igual o menor que la banca pierde, y si obtiene una puntuación superior a la
banca gana.
"""

import random

banca = random.randrange(17, 22)
puntos = 0
seguir = 1

while seguir == 1 and puntos <= 21:
    carta = random.randrange(1, 6)
    puntos += carta
    print("Has sacado un", carta, "→ Tu puntuación:", puntos)

    if puntos <= 21:
        seguir = int(input("¿Quieres otra carta? (1 = sí, 0 = no): "))
        while seguir != 1 and seguir != 0:
            print("Opción no válida")
            seguir = int(input("¿Quieres otra carta? (1 = sí, 0 = no): "))

print("Puntuación de la banca:", banca)

if puntos > 21:
    print("Te has pasado de 21. Perdedor!!")
elif puntos > banca:
    print("¡Ganas!")
else:
    print("Pierdes (igual o menor que la banca)")
