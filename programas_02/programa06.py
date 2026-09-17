"""
programa06
Escribe un programa que convierta un valor dado en grados 
Fahrenheit a grados Celsius.
"""

grados = float(input("Dame los grados Fahrenheit que quieras transformar= "))

celsius = (grados - 32) * 5 / 9

print("Los grados Celsius son =", celsius)