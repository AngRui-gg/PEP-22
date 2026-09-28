"""
programa03
Escribe un programa que muestre los números pares que hay
entre 0 y 10. Resuelve el ejercicio de 4 formas diferentes.
Usando los bucles for y while sin y con la sentencia continue.
"""

# FOR SIN CONTINUE
for i in range(11):
    if i % 2 == 0:
        print(i)

# FOR CON CONTINUE
for i in range(11):
    if i % 2 != 0:
        continue
    print(i)

# WHILE SIN CONTINUE
i = 0
while i <= 10:
    if i % 2 == 0:
        print(i)
    i += 1

# WHILE CON CONTINUE
i = 0
while i <= 10:
    if i % 2 != 0:
        i += 1
        continue
    print(i)
    i += 1
