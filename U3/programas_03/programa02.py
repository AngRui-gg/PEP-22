""" "
programa02
Modificar el programa anterior para utilizar:
- Imports organizados por categorías.
- Una función principal main().
- Un bloque de ejecución principal.

Imports de la librería estándar
Imports de librerías de terceros
Imports de módulos propios
"""

import operaciones


def main():
    """Función principal del programa"""

    a = float(input("Introduce el primer número: "))
    b = float(input("Introduce el segundo número: "))

    print("Suma:", operaciones.suma(a, b))
    print("Resta:", operaciones.resta(a, b))
    print("Multiplicación:", operaciones.multiplicacion(a, b))
    print("División:", operaciones.division(a, b))


if __name__ == "__main__":
    main()
