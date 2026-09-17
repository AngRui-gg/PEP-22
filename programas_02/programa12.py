"""
Programa 12
Sabiendo que 1 milla equivale a 1,61 Km escribe un programa que pida un
número de millas y un número de Km, muestre respectivamente el número de
millas y kilómetros. Los resultados deben estar redondeados a 2 decimales.
"""

print("---TRANSFORMADOR DE MILLAS A KILOMETROS Y VICE VERSA---")
millas_user = float(input("Introduce un número de millas:  "))
km_user = float(input("Introduce un número de km:  "))

millas_a_km = millas_user * 1.61
km_a_millas = km_user / 1.61

print("\n --RESULTADOS--")
# La función format(valor, ".2f"), convierte el número en un texto con exactamente dos dígitos después de la coma.
print(millas_user, " millas equivalen a ", format(millas_a_km, ".2f"), "km")
print(km_user, " km equivalen a ", format(km_a_millas, ".2f"), " millas")
