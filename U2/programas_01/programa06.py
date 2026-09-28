"""
programa06
Escribe un programa que pida una fecha (día, mes y año) y diga si es correcta
"""

try:
    print("Dame un día: ")
    d = int(input())
    print("Dame un mes (de forma numérica): ")
    m = int(input())
    print("Dame un año: ")
    a = int(input())

    if d <= 31:
        if m <= 12:
            print(d, m, a, sep="/")
        else:
            print("El mes introducido no es válido")
    else:
        print("El día introducido no es válido")
except Exception as ex:
    print(ex)
