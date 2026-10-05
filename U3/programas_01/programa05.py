""" "
programa05
Escribe un programa donde crees varias funciones y
pruebes el ámbito de las variables en Python
(globales, no locales y locales).
"""

variable_global = "Soy GLOBAL (accesible en todo el archivo)"


def probar_ambito_local():
    variable_local = "Soy LOCAL (solo existo dentro de probar_ambito_local)"
    print(variable_local)
    print(variable_global)


def intentar_modificar_global():
    global variable_global
    variable_global = "Soy GLOBAL (¡y acabo de ser modificada!)"
    print("Variable global modificada con éxito.")


def funcion_externa():
    variable_envolvente = "Soy de la función externa"

    def funcion_interna():
        nonlocal variable_envolvente
        variable_envolvente = (
            "Soy de la función externa (¡pero cambiada por la interna!)"
        )

    print(f"Antes de llamar a la interna: {variable_envolvente}")
    funcion_interna()
    print(f"Después de llamar a la interna: {variable_envolvente}")


probar_ambito_local()
# print(variable_local) Comentado para que funcione correctamenete el programa entero
intentar_modificar_global()
print(f"Comprobación fuera de la función: {variable_global}")
funcion_externa()
