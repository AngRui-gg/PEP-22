"""
Programa06
Escribe un programa que use varias veces la funcion printf() para
- Mostrar las operaciones del los operadores aritmeticos de Python entre dos
numeros.
- Mostrar las operaciones de los operadores logicos de Python con valores
booleanos.
- Mostrar las operaciones de los operadores de comparacion de Python con valores
booleanos y/o numeros.
"""

a=3
b=2

#ARITMETICOS
print("ARITMETICOS")
print("Suma → ", a+b,  
      "\nResta → ", a-b,
      "\nMultiplicacion → ", a*b,
      "\nDivision (float) → ", a/b,
      "\nDivision (entera) → ", a//b,
      "\nModulo → ", a%b, #Resto de una división
      "\nPotencia → ", a**b,
      "\nIdentidad (num positivo) → ", +b,
      "\nIdentidad (num negativo) → ", -b,)

#LOGICOS
print("\nLOGICOS")
print(True and False, 
      "\n",True or False, 
      "\n",not False)

#COMPARACION
print("\nCOMPARACION")
print(a==a,
      "\n", a!=True,
      "\n", a>b,
      "\n", a<b,
      "\n", a>=b,
      "\n", a<=b,
)