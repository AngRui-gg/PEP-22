"""
programa02
Escribe un que lea por teclado un número comprendido entre 1 y 10.
No se dejara de pedir el número hasta que no se introduzca
correctamente.
"""

funcionamiento = True

while funcionamiento == True:
    num = int(input("Dame un número entre el 1 y 10: "))
    if num < 1 or num > 10:
        print("El numero introducido no es válido")
    else:
        funcionamiento = False
