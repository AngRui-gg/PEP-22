"""
programa05
Escribe un programa que pregunte al usuario dos números y calcule su suma, resta,
multiplicación, división, módulo y potencia
"""
numero1 = float(input("Dame el primer número: "))
numero2 = float(input("Dame el segundo número: "))

suma = numero1 + numero2
resta = numero1 - numero2
multiplicacion = numero1 * numero2
division = numero1 / numero2
modulo = numero1 % numero2
potencia = numero1 ** numero2

print("La suma es =", suma)
print("La resta es =", resta)
print("La multiplicación es =", multiplicacion)
print("La división es =", division)
print("El resto es =", modulo)
print("La potencia es =", potencia)

