import matplotlib.pyplot as plt

# Datos
categorias = ["A", "B", "C", "D"]
valores = [10, 15, 7, 20]

# Crear el gráfico
plt.bar(categorias, valores, color="skyblue")
plt.title("Gráfico de Barras")
plt.xlabel("Categorías")
plt.ylabel("Valores")
plt.show()
