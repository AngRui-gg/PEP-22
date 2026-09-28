"""
programa04
Escribe un programa que lea por teclado un número real entre 1 y 10, simulando una
nota numérica, y muestre un mensaje indicando la calificación obtenida teniendo en
cuenta los siguientes rangos:
"""

print("Dame tu nota")
nota = float(input())

match nota:
    case n if nota < 5:
        print("Inuficiente")
    case n if nota >= 5 and nota < 6:
        print("Suficiente")
    case n if nota >= 6:
        print("Bien")
    case n if nota >= 7 and nota < 9:
        print("Notable")
    case n if nota >= 9 and nota <= 10:
        print("Sobresaliente")
    case _:
        print("La nota introducida no es válida")
