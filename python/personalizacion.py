# Definir una función para categorizar edades
def categorizar_edad(edad):
    if edad < 30:
        return "Joven"
    else:
        return "Adulto"

df["Categoría"] = df["Edad"].apply(categorizar_edad)
print(df)


