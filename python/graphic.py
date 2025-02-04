import matplotlib.pyplot as plt
import numpy as np

# Datos
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
x, y = np.meshgrid(x, y)
z = np.sin(np.sqrt(x**2 + y**2))

# Crear el gráfico de contornos
plt.contour(x, y, z, cmap='coolwarm')
plt.title("Gráfico de Contornos")
plt.xlabel("Eje X")
plt.ylabel("Eje Y")
plt.colorbar(label='Valor de z')
plt.show()
