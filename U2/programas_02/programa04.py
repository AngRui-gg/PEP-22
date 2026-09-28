"""
programa04
Escribe un programa que use un bucle while y le pida continuamente
al usuario que introduzca un número hasta que ingrese 45 como la
número de salida secreto, en cuyo caso el mensaje "¡Has dejado el
bucle con éxito" debe imprimirse en la pantalla y el bucle debe
 terminar.
"""

# VERSION1
while True:
    num = int(input("Introduce un número: "))
    if num == 45:
        print("¡Has dejado el bucle con éxito!")
        break

# VERSION2
num = int(input("Introduce un número: "))

while num != 45:
    num = int(input("Introduce un número: "))

print("¡Has dejado el bucle con éxito!")
