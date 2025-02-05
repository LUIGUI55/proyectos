import threading
import time

def tarea(nombre, tiempo):
    for i in range(5):
        print(f"Tarea {nombre} - Iteración {i+1}")
        time.sleep(tiempo)

hilo1 = threading.Thread(target=tarea, args=("A", 1))
hilo2 = threading.Thread(target=tarea, args=("B", 2))

hilo1.start()
hilo2.start()

hilo1.join()
hilo2.join()

print("Ambas tareas han finalizado.")

