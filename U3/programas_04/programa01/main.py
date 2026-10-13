# programa01: crear un paquete matematicas con operaciones, figuras y
# conversiones; mostrar un menú de operaciones y áreas geométricas.

# Imports de la librería estándar
# Imports de librerías de terceros
# Imports de módulos propios
from matematicas import operaciones, figuras


def main():
    """Función principal del programa."""
    print("1. Operaciones matemáticas")
    print("2. Cálculo de áreas geométricas")
    opcion = input("Elige una opción: ")

    try:
        if opcion == "1":
            a = float(input("Primer número: "))
            b = float(input("Segundo número: "))
            print("Suma:", operaciones.suma(a, b))
            print("Resta:", operaciones.resta(a, b))
            print("Multiplicación:", operaciones.multiplicacion(a, b))
            print("División:", operaciones.division(a, b))
        elif opcion == "2":
            print("1. Rectángulo")
            print("2. Triángulo")
            print("3. Círculo")
            figura = input("Elige una figura: ")
            if figura in ("1", "2"):
                base = float(input("Base: "))
                altura = float(input("Altura: "))
                if base < 0 or altura < 0:
                    print("Las medidas no pueden ser negativas")
                elif figura == "1":
                    print("Área:", figuras.area_rectangulo(base, altura))
                else:
                    print("Área:", figuras.area_triangulo(base, altura))
            elif figura == "3":
                radio = float(input("Radio: "))
                if radio < 0:
                    print("El radio no puede ser negativo")
                else:
                    print("Área:", figuras.area_circulo(radio))
            else:
                print("Figura no válida")
        else:
            print("Opción no válida")
    except ValueError:
        print("Introduce números válidos")


if __name__ == "__main__":
    main()
