def generar_tabla(num):
    for i in range(1, 11):
        print(f"{num} x {i} = {num * i}")

numero = int(input("Introduce un número: "))
generar_tabla(numero)

