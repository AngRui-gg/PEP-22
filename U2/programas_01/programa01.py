"""
programa01
Escribe un programa que pida primero un número par y luego un número impar (positivos
o negativos). En caso de que uno o los dos valores no sea correcto (es decir no sea par o
impar respectivamente), se mostrará un aviso.
"""

print("Dame un numero par")
par = int(input())

print("Dame un numero impar")
impar = int(input())

if par % 2 != 0:
    print("El valor no es correcto")

if impar % 2 == 0:
    print("El valor no es correcto")
