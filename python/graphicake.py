import matplotlib.pyplot as plt

# Datos
categorias = ["Aprobado", "Reprobado", "Pendiente"]
porcentajes = [60, 30, 10]

# Crear el gráfico
plt.pie(porcentajes, labels=categorias, autopct="%1.1f%%", startangle=90, colors=["blue", "red", "yellow"])
plt.title("Resultados de la Encuesta")
plt.show()