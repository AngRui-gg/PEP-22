"""
programa05
Escribe un programa que pida dos números y que indique cuál es el menor, cuál el mayor
o que indique que son iguales.
"""

print("Dame el primer numero a comparar")
num1 = int(input())
print("Dame el segundo numero a comparar")
num2 = int(input())

if num1 > num2:
    print(num1 + " es mayor que " + num2)
elif num2 > num1:
    print(num2 + " es mayor que " + num1)
elif num1 == num2:
    print("Ambos números son iguales")
