import matplotlib.pyplot as plt
import numpy as np

# Datos
x = np.linspace(-10, 10, 100)
y = x**2

# Crear la figura y los ejes
plt.figure(figsize=(8, 6))

# Graficar
plt.plot(x, y, label=r'$y = x^2$', color='b', linewidth=2)

# Personalizar el gráfico
plt.title('Gráfica de $y = x^2$', fontsize=14)
plt.xlabel('x', fontsize=12)
plt.ylabel('y', fontsize=12)
plt.grid(True)
plt.axhline(0, color='black',linewidth=1)
plt.axvline(0, color='black',linewidth=1)

# Agregar una leyenda
plt.legend()

# Mostrar el gráfico
plt.show()


