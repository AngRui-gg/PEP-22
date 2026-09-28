"""
Programa04
Escribe un programa que pregunte la base y altura de una rectángulo y calcule su área y
perímetro
"""

base = float(input("Dame la base de tu rectángulo "))
altura = float(input("Dame la altura de tu rectángulo "))

area = base * altura / 2
perimetro = base * 2 + altura * 2

print("El area es= ", area)
print("El perimetro es= ", perimetro)
