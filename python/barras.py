import matplotlib.pyplot as plt

# Datos
meses = ["Enero", "Febrero", "Marzo", "Abril"]
ventas = [2500, 3200, 2800, 3500]

# Crear el gráfico
plt.bar(meses, ventas, color="green")
plt.title("Ventas por Mes")
plt.xlabel("Meses")
plt.ylabel("Ventas (USD)")
plt.show()

