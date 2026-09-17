"""
Programa 09
Escribe un programa que calcule la calificación de estudiante en un
módulo. La calificación se obtiene de la calificación parcial en cada
RA (RA1 20%, RA2, 60% y RA3 20%).
"""

print("Ve escribiéndome las notas de cada RA del módulo")
ra1 = int(input("Nota de tu RA1 (20%)  "))
ra2 = int(input("Nota de tu RA2 (60%)  "))
ra3 = int(input("Nota de tu RA3 (20%)  "))

ra1 = ra1 * 20 / 100
ra2 = ra2 * 60 / 100
ra3 = ra3 * 20 / 100

media = ra1 + ra2 + ra3

print("Tu nota media es: ", media)
