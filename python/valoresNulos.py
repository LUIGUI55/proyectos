data = {
    "Nombre": ["Ana", "Luis", None, "Marta"],
    "Edad": [25, None, 35, 28]
}
df = pd.DataFrame(data)

# Rellenar valores nulos con un valor
df_filled = df.fillna({"Nombre": "Desconocido", "Edad": 0})
print(df_filled)


