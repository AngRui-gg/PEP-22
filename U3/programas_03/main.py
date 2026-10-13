""" "
programa01
Importar el módulo operaciones, pedir dos números
y mostrar los resultados de las cuatro operaciones.

"""

import operaciones

a = float(input("Introduce el primer número: "))
b = float(input("Introduce el segundo número: "))

print("Suma:", operaciones.suma(a, b))
print("Resta:", operaciones.resta(a, b))
print("Multiplicación:", operaciones.multiplicacion(a, b))
print("División:", operaciones.division(a, b))
