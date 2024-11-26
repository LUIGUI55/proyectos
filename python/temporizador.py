import time

def temporizador(segundos):
    while segundos > 0:
        mins, secs = divmod(segundos, 60)
        print(f"{mins:02}:{secs:02}")
        time.sleep(1)
        segundos -= 1
    print("¡Tiempo terminado!")

segundos = int(input("Introduce el tiempo en segundos: "))
temporizador(segundos)
