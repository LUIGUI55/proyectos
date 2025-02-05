import matplotlib.pyplot as plt
import numpy as np

# Datos
x = np.linspace(-10, 10, 100)
y = x ** 2

# Crear el gráfico
plt.plot(x, y, label="y = x²", color="blue", linewidth=2)
plt.title("Gráfico de Línea")
plt.xlabel("Eje X")
plt.ylabel("Eje Y")
plt.legend()
plt.grid()
plt.show()

