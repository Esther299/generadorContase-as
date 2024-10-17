import random

# Lista de palabras:
palabras = ['perro', 'gato', 'elefante', 'jirafa', 'canguro', 'koala', 'murcielago', 'periquito']

def elegir_palabra():
    return random.choice(palabras)

# Estado:
def mostrar_estado(actual, intentos_restantes, letras_usadas):
    print(f"\nPalabra: {' '.join(actual)}")
    print(f"Intentos restantes: {intentos_restantes}")
    print(f"Letras usadas: {', '.join(letras_usadas)}")

# Juego:
def jugar_ahorcado():
    palabra_secreta = elegir_palabra()
    letras_correctas = ['_'] * len(palabra_secreta)
    intentos_restantes = 6
    letras_usadas = []

    print("¡Bienvenido al juego del ahorcado!")

    while intentos_restantes > 0:
        mostrar_estado(letras_correctas, intentos_restantes, letras_usadas)

        letra = input("Adivina una letra: ").lower()

        if letra in letras_usadas:
            print("Ya has usado esa letra. Intenta con otra.")
            continue

        letras_usadas.append(letra)

        if letra in palabra_secreta:
            for i, char in enumerate(palabra_secreta):
                if char == letra:
                    letras_correctas[i] = letra
        else:
            intentos_restantes -= 1
            print("Letra incorrecta.")

        if '_' not in letras_correctas:
            print(f"\n¡Felicidades! Has adivinado la palabra: {palabra_secreta}")
            break

    if intentos_restantes == 0:
        print(f"\n¡Has perdido! La palabra era: {palabra_secreta}")

jugar_ahorcado()

# Para jugar, escribe en la terminal 'python index.py'