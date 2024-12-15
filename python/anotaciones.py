import matplotlib.pyplot as plt
import numpy as np

# Datos
x = np.linspace(0, 10, 100)
y = np.sin(x)

# Crear el gráfico
plt.plot(x, y, label="y = sin(x)")

# Anotaciones
plt.annotate('Máximo', xy=(1.57, 1), xytext=(3, 0.8),
             arrowprops=dict(facecolor='red', arrowstyle='->'))
plt.annotate('Mínimo', xy=(4.71, -1), xytext=(6, -0.8),
             arrowprops=dict(facecolor='blue', arrowstyle='->'))

# Títulos y etiquetas
plt.title("Gráfico de Líneas con Anotaciones")
plt.xlabel("Eje X")
plt.ylabel("Eje Y")
plt.legend()
plt.grid(True)
plt.show()

