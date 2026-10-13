""" "
programa02
Modifica el programa anterior para importar
únicamente las funciones del módulo math que se
utilizan.
"""

from math import sin, cos, radians, sqrt, pow

print("OPERACIONES MATEMÁTICAS")
print("1. Seno de un ángulo")
print("2. Coseno de un ángulo")
print("3. Raíz cuadrada de un número")
print("4. Potencia de dos números")

opcion = input("Elige una opción (1-4): ")

if opcion == "1":
    angulo = float(input("Introduce el ángulo en grados: "))
    resultado = sin(radians(angulo))
    print("El seno es:", resultado)

elif opcion == "2":
    angulo = float(input("Introduce el ángulo en grados: "))
    resultado = cos(radians(angulo))
    print("El coseno es:", resultado)

elif opcion == "3":
    numero = float(input("Introduce un número: "))

    if numero >= 0:
        resultado = sqrt(numero)
        print("La raíz cuadrada es:", resultado)
    else:
        print("No se puede calcular la raíz real de un número negativo.")

elif opcion == "4":
    base = float(input("Introduce la base: "))
    exponente = float(input("Introduce el exponente: "))
    resultado = pow(base, exponente)
    print("El resultado de la potencia es:", resultado)

else:
    print("Opción no válida.")
