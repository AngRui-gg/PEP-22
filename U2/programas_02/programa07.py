"""
programa07
Escribe un programa que pida números hasta que se introduzca un
cero. Debe imprimir la suma y la media de todos los números
introducidos. Realiza dos versiones: una que utiliza la
instrucción break y otra no.
"""

suma = 0
cantidad = 0

while True:
    num = int(input("Introduce un número (0 para terminar): "))
    if num == 0:
        break
    suma += num
    cantidad += 1

if cantidad > 0:
    print("Suma:", suma)
    print("Media:", suma / cantidad)
else:
    print("No se ha introducido ningún número")
