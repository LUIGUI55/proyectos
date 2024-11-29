def analizar_texto(texto):
    palabras = texto.split()
    num_palabras = len(palabras)
    num_caracteres = len(texto)
    num_oraciones = texto.count('.') + texto.count('!') + texto.count('?')
    return num_palabras, num_caracteres, num_oraciones

texto = input("Introduce un texto: ")
palabras, caracteres, oraciones = analizar_texto(texto)
print(f"Palabras: {palabras}, Caracteres: {caracteres}, Oraciones: {oraciones}")

