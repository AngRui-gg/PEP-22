"""
Programa 14
Escribe un programa que reciba un número de bytes y muestre por
pantalla cuantos GBytes, MBytes, KBytes y Bytes son. Tanto para el
sistema decimal como el binario.
"""

# 1. Solicitar el número de bytes al usuario
num_bytes = int(input("Introduce el número de bytes: "))

# SISTEMA DECIMAL (SI)
bytes_dec = num_bytes

gb = bytes_dec // (1000**3)
bytes_dec %= 1000**3

mb = bytes_dec // (1000**2)
bytes_dec %= 1000**2

kb = bytes_dec // 1000
b_dec = bytes_dec % 1000

# SISTEMA BINARIO (IEC)
bytes_bin = num_bytes

gib = bytes_bin // (1024**3)
bytes_bin %= 1024**3

mib = bytes_bin // (1024**2)
bytes_bin %= 1024**2

kib = bytes_bin // 1024
b_bin = bytes_bin % 1024


print(
    "\n",
    num_bytes,
    "bytes en sistema decimal (SI): ",
    gb,
    "GB, ",
    mb,
    "MB, ",
    kb,
    "KB, ",
    b_dec,
    "bytes",
    sep="",
)
print(
    num_bytes,
    "bytes en sistema binario (IEC): ",
    gib,
    "GiB, ",
    mib,
    "MiB, ",
    kib,
    "KiB, ",
    b_bin,
    "bytes",
    sep="",
)
