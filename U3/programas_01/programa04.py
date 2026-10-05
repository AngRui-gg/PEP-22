""" "
programa04
Mejora el programa anterior de forma que compruebe si el usuario está
introduciendo valores correctos (por ejemplo, el radio no puede ser un
número negativo) y si no es así que pida muestre un aviso y vuelva a
pedir el valor.
"""

import math

funcionamiento = True


def calcular_area_circulo(radio):
    area = math.pi * (radio**2)
    return area


def calcular_area_triangulo(base, altura):
    area = (base * altura) / 2
    return area


def calcular_area_rectangulo(base, altura):
    area = base * altura
    return area


while funcionamiento == True:
    print("\n---MENÚ---")
    print("1. Calcular el área de un círculo")
    print("2. Calcular el área de un triángulo")
    print("3. Calcular el área de un rectángulo")
    print("4. Salir")

    # Try-except para la opción del menú
    try:
        opc = int(input("Introduce una opción (1-4): "))
    except ValueError:
        print("Error: Debes introducir un número entero del 1 al 4.")
        continue

    match opc:
        case 1:
            while True:
                try:
                    radio = float(input("Dame el radio del círculo: "))
                    if radio <= 0:
                        print("El radio debe ser un número positivo mayor que cero.")
                        continue
                    break
                except ValueError:
                    print("Error: No puedes introducir letras. Pon un número.")

            resultado = calcular_area_circulo(radio)
            print(f"El área del círculo es: {resultado:.2f}")

        case 2:
            while True:
                try:
                    baseTri = float(input("Dame la base del triángulo: "))
                    if baseTri <= 0:
                        print("La base debe ser un número positivo mayor que cero.")
                        continue
                    break
                except ValueError:
                    print("Error: Introduce un número válido.")

            while True:
                try:
                    hTri = float(input("Dame la altura del triángulo: "))
                    if hTri <= 0:
                        print("La altura debe ser un número positivo mayor que cero.")
                        continue
                    break
                except ValueError:
                    print("Error: Introduce un número válido.")

            resultado = calcular_area_triangulo(baseTri, hTri)
            print(f"El área del triángulo es: {resultado:.2f}")

        case 3:
            while True:
                try:
                    baseRec = float(input("Dame la base del rectángulo: "))
                    if baseRec <= 0:
                        print("La base debe ser un número positivo mayor que cero.")
                        continue
                    break
                except ValueError:
                    print("Error: Introduce un número válido.")

            while True:
                try:
                    hRec = float(input("Dame la altura del rectángulo: "))
                    if hRec <= 0:
                        print("La altura debe ser un número positivo mayor que cero.")
                        continue
                    break
                except ValueError:
                    print("Error: Introduce un número válido.")

            resultado = calcular_area_rectangulo(baseRec, hRec)
            print(f"El área del rectángulo es: {resultado:.2f}")

        case 4:
            print("Hasta la proximaaa")
            funcionamiento = False

        case _:
            print("Opción no válida. Por favor, elige un número del 1 al 4.")
