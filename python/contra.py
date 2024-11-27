import random
import string

def generar_contrasena(longitud):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    contrasena = ''.join(random.choice(caracteres) for _ in range(longitud))
    return contrasena

longitud = int(input("Introduce la longitud de la contraseña: "))
print(f"Contraseña generada: {generar_contrasena(longitud)}")
