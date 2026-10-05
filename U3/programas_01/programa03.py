""" "
programa03
Escribe un programa en Python que muestre un menú que permita al
usuario seleccionar qué operación desea realizar. Las operaciones que
puede realizar serán calcular el área de un círculo, un triángulo o un
rectángulo. El menú que se le muestra al usuario será similar al
siguiente:
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
    print("---MENÚ---")
    print("1. Calcular el área de un círculo")
    print("2. Calcular el área de un triángulo")
    print("3. Calcular el área de un rectángulo")
    print("4. Salir")
    opc = int(input("Introduce una opción (1-4): "))

    match opc:
        case 1:
            radio = float(input("Dame el radio del circulo: "))
            resultado = calcular_area_circulo(radio)
            print(f"El área del círculo es: {resultado:.2f}")
        case 2:
            baseTri = float(input("Dame la base del triangulo: "))
            hTri = float(input("Dame la altura del triangulo: "))
            resultado = calcular_area_triangulo(baseTri, hTri)
            print(f"El área del triángulo es: {resultado:.2f}")
        case 3:
            baseRec = float(input("Dame la base del rectangulo: "))
            hRec = float(input("Dame la altura del rectangulo: "))
            resultado = calcular_area_rectangulo(baseRec, hRec)
            print(f"El área del rectángulo es: {resultado:.2f}")
        case 4:
            print("Hasta la proximaaa")
            funcionamiento = False
