import pandas as pd

data = {
    "Nombre": ["Ana", "Luis", "Juan", "Marta"],
    "Edad": [25, 30, 35, 28],
    "Ciudad": ["Madrid", "Barcelona", "Valencia", "Sevilla"]
}
df = pd.DataFrame(data)
print(df)
