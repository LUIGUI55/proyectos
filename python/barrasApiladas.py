import matplotlib.pyplot as plt
import numpy as np

# Datos
categorias = ['A', 'B', 'C', 'D']
grupo1 = [10, 15, 25, 30]
grupo2 = [5, 10, 15, 10]
grupo3 = [2, 3, 4, 5]

# Crear el gráfico
plt.bar(categorias, grupo1, label="Grupo 1", color='orange')
plt.bar(categorias, grupo2, bottom=grupo1, label="Grupo 2", color='blue')
plt.bar(categorias, grupo3, bottom=np.array(grupo1)+np.array(grupo2), label="Grupo 3", color='green')

# Títulos y etiquetas
plt.title("Gráfico de Barras Apiladas")
plt.xlabel("Categorías")
plt.ylabel("Valores")
plt.legend()
plt.show()
