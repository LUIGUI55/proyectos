import time

def medir_tiempo_ejecucion():
    inicio = time.process_time_ns()

    for i in range(1000000):
        pass

    fin = time.process_time_ns()
    tiempo_ejecucion = fin - inicio

    print(f"Tiempo de ejecución (ciclos de reloj): {tiempo_ejecucion} segundos")

if __name__ == "__main__":
    medir_tiempo_ejecucion()
