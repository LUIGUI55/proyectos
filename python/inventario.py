class Producto:
    def __init__(self, nombre, precio, cantidad):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

    def valor_total(self):
        return self.precio * self.cantidad

    def __str__(self):
        return f"{self.nombre} - Precio: ${self.precio:.2f}, Cantidad: {self.cantidad}, Total: ${self.valor_total():.2f}"

class Inventario:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def mostrar_inventario(self):
        print("Inventario:")
        for producto in self.productos:
            print(producto)
        print(f"Valor total del inventario: ${self.valor_total_inventario():.2f}")

    def valor_total_inventario(self):
        return sum(producto.valor_total() for producto in self.productos)

# Ejemplo de uso
inventario = Inventario()
inventario.agregar_producto(Producto("Laptop", 1200.00, 5))
inventario.agregar_producto(Producto("Teléfono", 800.00, 10))
inventario.mostrar_inventario()