import matplotlib.pyplot as plt
import numpy as np

# Datos
x = np.random.rand(50) * 10  # Valores aleatorios en el rango [0, 10]
y = 2 * x + np.random.randn(50)  # Relación lineal con ruido

# Crear el gráfico
plt.scatter(x, y, color="purple", alpha=0.7)
plt.title("Gráfico de Dispersión")
plt.xlabel("Variable X")
plt.ylabel("Variable Y")
plt.grid()
plt.show()
