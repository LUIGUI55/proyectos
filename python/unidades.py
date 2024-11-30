def convertir_km_millas(km):
    return km * 0.621371

kilometros = float(input("Introduce los kilómetros: "))
print(f"{kilometros} km son {convertir_km_millas(kilometros)} millas.")

