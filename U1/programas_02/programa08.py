"""
programa08
Una tienda ofrece un descuento del 15% sobre el total de la compra y un cliente
desea saber cuanto deberá pagar finalmente por su compra
"""

compra = float(input("Introduce el total de la compra= "))

descuento = compra * 0.15
precio_final = compra - descuento

print("El descuento es =", descuento)
print("El precio final es =", precio_final)