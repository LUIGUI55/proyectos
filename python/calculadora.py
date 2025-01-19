import tkinter as tk

# Función para actualizar la pantalla con el número o resultado
def button_click(number):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + str(number))

# Función para realizar operaciones
def button_clear():
    entry.delete(0, tk.END)

def button_equal():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# Crear la ventana principal
window = tk.Tk()
window.title("Calculadora")

# Crear un campo de entrada para mostrar los números
entry = tk.Entry(window, width=35, borderwidth=5)
entry.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

# Crear los botones
button_1 = tk.Button(window, text="1", padx=20, pady=20, command=lambda: button_click(1))
button_2 = tk.Button(window, text="2", padx=20, pady=20, command=lambda: button_click(2))
# ... (Crear los demás botones de la misma manera)

button_clear = tk.Button(window, text="Clear", padx=20, pady=20, command=button_clear)
button_equal = tk.Button(window, text="=", padx=20, pady=20, command=button_equal)

# Organizar los botones en la ventana
button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
# ... (Posicionar los demás botones)

button_clear.grid(row=4, column=1)
button_equal.grid(row=4, column=2)

# Iniciar la aplicación
window.mainloop()

