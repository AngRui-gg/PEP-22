# Módulo conversiones: representaciones numéricas y conversión de texto.

def a_binario(n):
    return bin(n)

def a_hexadecimal(n):
    return hex(n)

def a_entero(texto):
    try:
        return int(texto)
    except (ValueError, TypeError):
        return None
