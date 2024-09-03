import random
import string

# Generador:
def generar_contraseña(longitud=12, incluir_mayusculas=True, incluir_numeros=True, incluir_simbolos=True):

    caracteres = string.ascii_lowercase
    if incluir_mayusculas:
        caracteres += string.ascii_uppercase
    if incluir_numeros:
        caracteres += string.digits
    if incluir_simbolos:
        caracteres += string.punctuation

    contraseña = ''.join(random.choice(caracteres) for _ in range(longitud))
    
    return contraseña

# Parámetros:
longitud = int(input("Introduce la longitud de la contraseña: "))
usar_mayusculas = input("¿Incluir mayúsculas? (s/n): ").lower() == 's'
usar_numeros = input("¿Incluir números? (s/n): ").lower() == 's'
usar_simbolos = input("¿Incluir símbolos? (s/n): ").lower() == 's'

contraseña_generada = generar_contraseña(longitud, usar_mayusculas, usar_numeros, usar_simbolos)
print(f"Contraseña generada: {contraseña_generada}")

# Para generar la contraseña, escribe en la terminal python index.py