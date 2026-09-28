"""
programa08
Escribe un programa que simule un juego en el que dos jugadores tiran dos dados. El que
saque mayor puntuación total, gana. Si la puntuación total coincide, gana quien haya
sacado el dado con el valor más alto. Si el valor más alto también coincide, empatan.
"""

import random

dado1_j1 = random.randrange(1, 7)
dado2_j1 = random.randrange(1, 7)
total_j1 = dado1_j1 + dado2_j1

if dado1_j1 > dado2_j1:
    alto_j1 = dado1_j1
else:
    alto_j1 = dado2_j1

dado1_j2 = random.randrange(1, 7)
dado2_j2 = random.randrange(1, 7)
total_j2 = dado1_j2 + dado2_j2

if dado1_j2 > dado2_j2:
    alto_j2 = dado1_j2
else:
    alto_j2 = dado2_j2

print(
    "Jugador 1 sacó: ",
    dado1_j1,
    " y ",
    dado2_j1,
    "(Total:",
    total_j1,
    "- Dado más alto:",
    alto_j1,
    ")",
)
print(
    "Jugador 2 sacó:",
    dado1_j2,
    "y",
    dado2_j2,
    "(Total:",
    total_j2,
    "- Dado más alto:",
    alto_j2,
    ")",
)
print()


if total_j1 > total_j2:
    print("Gana el Jugador 1 (por mayor puntuación total)")
elif total_j2 > total_j1:
    print("Gana el Jugador 2 (por mayor puntuación total)")
else:
    if alto_j1 > alto_j2:
        print("Gana el Jugador 1 (por tener el dado más alto)")
    elif alto_j2 > alto_j1:
        print("Gana el Jugador 2 (por tener el dado más alto)")
    else:
        print("Empatan")
