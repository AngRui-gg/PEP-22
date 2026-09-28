"""
programa09
Escribe un programa en Python que simule el juego de piedra, papel o tijera. En primer
lugar el programa tendrá que mostrar un mensaje por pantalla al usuario para preguntarle
qué opción desea elegir.
"""

import random

print("JUEGO DE PIEDRA, PAPEL O TIJERA")
print("Seleccione una opción (1, 2 o 3): ")
print("1. Piedra")
print("2. Papel")
print("3. Tijera")
esc = int(input())

esc_aleatorio = random.randrange(1, 4)

if (
    (esc == 1 and esc_aleatorio == 3)
    or (esc == 2 and esc_aleatorio == 1)
    or (esc == 3 and esc_aleatorio == 2)
):
    print("Has ganado")
else:
    print("¡Has perdido!")
