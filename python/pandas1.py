# Importamos pandas
import pandas as pd

# Creamos un DataFrame con los datos del ejercicio
data = {
    'Producto': ['Camiseta', 'Pantalón', 'Laptop', 'Auriculares', 'Zapatillas', 'Smartphone'],
    'Categoría': ['Ropa', 'Ropa', 'Electrónica', 'Electrónica', 'Ropa', 'Electrónica'],
    'Precio': [15.50, 35.00, 700.00, 80.00, 50.00, 600.00],
    'Unidades Vendidas': [100, 50, 30, 120, 70, 40],
    'Fecha': ['2024-11-01', '2024-11-01', '2024-11-02', '2024-11-02', '2024-11-03', '2024-11-03']
}

# Convertimos el diccionario a un DataFrame
df = pd.DataFrame(data)

# 1. Calcular la venta total por producto (Precio * Unidades Vendidas)
df['Venta Total'] = df['Precio'] * df['Unidades Vendidas']

# Mostramos el DataFrame con la columna de ventas totales
print("Venta total por producto:")
print(df[['Producto', 'Venta Total']])

# 2. Calcular las ventas totales por categoría
ventas_por_categoria = df.groupby('Categoría')['Venta Total'].sum()

# Mostramos las ventas por categoría
print("\nVentas totales por categoría:")
print(ventas_por_categoria)

# 3. Encontrar los productos más vendidos (mayor cantidad de unidades)
producto_mas_vendido = df.loc[df['Unidades Vendidas'].idxmax()]

# Mostramos el producto más vendido
print("\nProducto más vendido:")
print(f"Producto: {producto_mas_vendido['Producto']}, Unidades Vendidas: {producto_mas_vendido['Unidades Vendidas']}")

# 4. Filtrar las ventas de un día específico (por ejemplo, 2024-11-02)
ventas_dia_especifico = df[df['Fecha'] == '2024-11-02']

# Mostramos las ventas del 2024-11-02
print("\nVentas del 2024-11-02:")
print(ventas_dia_especifico[['Producto', 'Venta Total']])

