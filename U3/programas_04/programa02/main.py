# programa02: investigar usos de __init__.py y probar uno.
# Aquí se usa para exportar funciones y simplificar las importaciones.

# Imports de la librería estándar
# Imports de librerías de terceros
# Imports de módulos propios
from matematicas import suma, division, area_circulo, a_binario, a_entero


def main():
    """Prueba de funciones importadas directamente desde el paquete."""
    print("Suma de 5 y 3:", suma(5, 3))
    print("División de 8 entre 0:", division(8, 0))
    print("Área del círculo de radio 2:", area_circulo(2))
    print("10 en binario:", a_binario(10))
    print("Texto '123' convertido a entero:", a_entero("123"))
    print("Texto no válido convertido a entero:", a_entero("hola"))


if __name__ == "__main__":
    main()
