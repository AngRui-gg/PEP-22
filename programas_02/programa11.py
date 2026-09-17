"""
Programa 11
Un ciclista parte de una ciudad A a las HH horas, MM minutos y SS segundos.
El tiempo de viaje hasta llegar a otra ciudad B es de N segundos.
Escribie un programa que determine la hora de llegada a la ciudad B.
"""

# 1. Solicitar los datos de entrada al usuario
print("--- Datos de salida del ciclista ---")
hh = int(input("Introduce la hora de salida (0-23):  "))
mm = int(input("Introduce los minutos de salida (0-59):  "))
ss = int(input("Introduce los segundos de salida (0-59):  "))
n = int(input("¿Cuántos segundos tarda en llegar a la otra ciudad?  "))

segundos_totales_salida = (hh * 3600) + (mm * 60) + ss
segundos_totales_llegada = segundos_totales_salida + n
segundos_totales_llegada = (
    segundos_totales_llegada % 86400
)  # 86400s equivalen a 24 horas

hh_llegada = segundos_totales_llegada // 3600
segundos_sobra = segundos_totales_llegada % 3600

mm_llegada = segundos_sobra // 60
ss_llegada = segundos_sobra % 60

print("\n--- RESUMEN ---")
# el format hace que solo se selecciones 2 dígitos (2d)
print(
    "Hora de salida→ ",
    format(hh, "02d"),
    ":",
    format(mm, "02d"),
    ":",
    format(ss, "02d"),
)

print(
    "Hora de llegada→ ",
    format(hh_llegada, "02d"),
    ":",
    format(mm_llegada, "02d"),
    ":",
    format(ss_llegada, "02d"),
)
