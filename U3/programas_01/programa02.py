""" "
programa02
Escribe un programa en Python que haga uso de una función llamada
saludar que cumpla los siguientes requisitos:
"""

alumno = {
    "nombre": "Angela",
    "apellido": "Ruiz",
    "apellido2": "Alcalde",
    "curso": "2DAW",
}


def saludar(datos):
    print(
        f"Hola {datos['nombre']} {datos['apellido']} {datos['apellido2']} {datos['curso']}"
    )


saludar(alumno)
