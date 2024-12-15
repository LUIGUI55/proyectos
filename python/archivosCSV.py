import pandas as pd

# Crear un DataFrame
data = {
    "Nombre": ["Ana", "Luis", "Carlos", "María"],
    "Edad": [25, 30, 22, 29],
    "Ciudad": ["Madrid", "Barcelona", "Valencia", "Sevilla"]
}

df = pd.DataFrame(data)
df.to_csv("personas.csv", index=False)

# Leer el archivo CSV
df_leido = pd.read_csv("personas.csv")
print("Datos del archivo CSV:")
print(df_leido)

# Filtrar personas mayores de 25 años
mayores = df_leido[df_leido["Edad"] > 25]
print("\nPersonas mayores de 25 años:")
print(mayores)

