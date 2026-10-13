""" "
programa04
Utiliza el módulo turtle para:
- Dibujar un cuadrado rojo sin rellenar.
- Dibujar un círculo verde relleno.
"""

import turtle

pantalla = turtle.Screen()
pantalla.title("Cuadrado y círculo")

lapiz = turtle.Turtle()
lapiz.speed(3)

# Dibujar un cuadrado rojo sin rellenar
lapiz.color("red")
lapiz.pensize(3)

for i in range(4):
    lapiz.forward(100)
    lapiz.right(90)

# Mover el lápiz para dibujar el círculo
lapiz.penup()
lapiz.goto(150, -100)
lapiz.pendown()

# Dibujar un círculo verde relleno
lapiz.color("green")
lapiz.begin_fill()
lapiz.circle(50)
lapiz.end_fill()

# Ocultar la tortuga
lapiz.hideturtle()

# Mantener la ventana abierta
turtle.done()
