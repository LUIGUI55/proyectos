from ARBOL import Nodo

def buscar_solucion_DFS_rec(estado_inicial, solucion, visitados):
    estado_inicial = Nodo(estado_inicial)
    solucion = False
    visitados = []
    visitados.append(estado_inicial)

    if estado_inicial.get_datos() == solucion:
        solucion = True
        return estado_inicial
    else:
        dato_nodo = estado_inicial.get_datos()
        hijo_izquierdo = Nodo([dato_nodo[1], dato_nodo[0], dato_nodo[2], dato_nodo[3]])
        hijo_central = Nodo([dato_nodo[0], dato_nodo[2], dato_nodo[1], dato_nodo[3]])
        hijo_derecho = Nodo([dato_nodo[0], dato_nodo[1], dato_nodo[3], dato_nodo[2]])

        hijo_izquierdo.set_padre(estado_inicial)
        hijo_central.set_padre(estado_inicial)
        hijo_derecho.set_padre(estado_inicial)

        visitados.append(hijo_izquierdo)
        visitados.append(hijo_central)
        visitados.append(hijo_derecho)

        for hijo in [hijo_izquierdo, hijo_central, hijo_derecho]:
            resultado = buscar_solucion_DFS_rec(hijo.get_datos(), solucion, visitados)
            if resultado:
                return resultado
    return None

def imprimir_resultados(estado_inicial, estado_final, max_resultados):
    visitados = []
    resultado = buscar_solucion_DFS_rec(estado_inicial, estado_final, visitados)
    if resultado:
        print(f"Solución encontrada: {resultado.get_datos()}")
    else:
        print("No se encontró solución.")

    print("\nVisitados:")
    for i, nodo in enumerate(visitados[:max_resultados]):
        print(f"{i + 1}: {nodo.get_datos()}")

if __name__ == "__main__":
    estado_inicial = [4, 3, 2, 1]
    estado_final = [1, 2, 3, 4]
    max_resultados = 18
    imprimir_resultados(estado_inicial, estado_final, max_resultados)

