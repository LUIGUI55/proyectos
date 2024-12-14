import matplotlib.pyplot as plt
import numpy as np

# Datos
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)
y3 = np.tan(x)

# Crear subgráficos
fig, axs = plt.subplots(3, 1, figsize=(6, 10))

# Primer gráfico
axs[0].plot(x, y1, color='blue')
axs[0].set_title("Seno")
axs[0].grid(True)

# Segundo gráfico
axs[1].plot(x, y2, color='green')
axs[1].set_title("Coseno")
axs[1].grid(True)

# Tercer gráfico
axs[2].plot(x, y3, color='red')
axs[2].set_title("Tangente")
axs[2].grid(True)
axs[2].set_ylim(-10, 10)  # Limitar los valores para evitar saltos en la tangente

# Mostrar todos los subgráficos
plt.tight_layout()
plt.show()
