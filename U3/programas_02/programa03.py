""" "
programa03
Utiliza los módulos platform y os para mostrar:
- El procesador del ordenador.
- El sistema operativo y su versión.
- El nombre del host.
- El directorio actual.
"""

import platform
import os

print("INFORMACIÓN DEL SISTEMA")

print("Procesador:", platform.processor())

print("Sistema operativo:", platform.system())

print("Versión del sistema operativo:", platform.release())

print("Nombre del host:", platform.node())

print("Directorio actual:", os.getcwd())
