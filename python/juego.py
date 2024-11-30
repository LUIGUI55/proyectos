import random

def juego_ahorcado():
    palabras = ["python", "programacion", "juego", "codigo"]
    palabra = random.choice(palabras)
    letras_adivinadas = set()
    intentos = 6

    while intentos > 0:
        estado = [letra if letra in letras_adivinadas else "_" for letra in palabra]
        print(" ".join(estado))

        if "_" not in estado:
            print("¡Ganaste!")
            break

        letra = input("Introduce una letra: ").lower()
        if letra in palabra:
            letras_adivinadas.add(letra)
        else:
            intentos -= 1
            print(f"Te quedan {intentos} intentos.")

    if intentos == 0:
        print(f"Perdiste. La palabra era {palabra}.")

juego_ahorcado()
