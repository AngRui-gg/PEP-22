"""
programa07
Escribe un programa que reciba una cantidad de minutos y muestre por pantalla a
cuantas horas y minutos corresponde.
"""

minutos = int(input("Cuántos minutos quieres pasar a horas y minutos= "))

horas = minutos // 60
minutos_restantes = minutos % 60
print("Horas:Minutos =", horas, ":", minutos_restantes)