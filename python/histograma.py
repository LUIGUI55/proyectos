import matplotlib.pyplot as plt
import numpy as np

# Datos
datos = np.random.normal(50, 10, 1000)  # Distribución normal con media=50 y desviación estándar=10

# Crear el gráfico
plt.hist(datos, bins=20, color="orange", edgecolor="black", alpha=0.7)
plt.title("Histograma de Frecuencia")
plt.xlabel("Valores")
plt.ylabel("Frecuencia")
plt.show()