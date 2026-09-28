"""
programa03
Escribe un programa que pida dos numero y muestre su división. Se deben tener en
cuenta que no se puede dividir por 0 mostrando en ese caso un aviso.
"""

try:
    print("Dame el número que queires dividir: ")
    div = int(input())

    print("Dame el numero por el que lo quieres dividir: ")
    divis = int(input())

    division = div / divis
    print(division)

except ZeroDivisionError:
    print("No se puede dividir entre 0")
