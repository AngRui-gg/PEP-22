""" "
programa01
Crear un módulo llamado operaciones con cuatro funciones:
suma, resta, multiplicacion y division.
La división debe controlar la división entre cero.
"""


def suma(a, b):
    return a + b


def resta(a, b):
    return a - b


def multiplicacion(a, b):
    return a * b


def division(a, b):
    if b == 0:
        return "No se puede dividir entre cero"
    return a / b
