"""
programa02
Escribe un programa que pida primero un número par (positivo o negativo) y si el valor no
es correcto, muestre un aviso. Si el valor es correcto, pedirá un número impar (positivo o
negativo) y si el valor no es correcto, mostrará un aviso.
"""

print("Dame un numero par")
par = int(input())

if par % 2 != 0:
    print("El valor no es correcto")
else:
    print("Dame un numero impar")
    impar = int(input())

    if impar % 2 == 0:
        print("El valor no es correcto")
