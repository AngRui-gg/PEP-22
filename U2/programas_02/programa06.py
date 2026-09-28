"""
programa06
Escribe un programa que realice las siguientes operaciones:
- Leer x teclado num entre 1 y 10...
- Tabla de multiplicar de num
- ¿Otro num o no?
"""

continuar = 1

while continuar == 1:
    # 1. Pedir el número hasta que sea válido
    num = int(input("Introduce un número entre 1 y 10: "))
    while num < 1 or num > 10:
        print("El número introducido no es válido")
        num = int(input("Introduce un número entre 1 y 10: "))

    # 2. Mostrar la tabla de multiplicar
    print("Tabla del", num)
    for i in range(1, 11):
        print(num, "x", i, "=", num * i)

    # 3. Preguntar si quiere continuar
    continuar = int(input("¿Quieres introducir otro número? (1 = sí, 0 = no): "))
    while continuar != 1 and continuar != 0:
        print("Opción no válida")
        continuar = int(input("¿Quieres introducir otro número? (1 = sí, 0 = no): "))

print("Adios!")
