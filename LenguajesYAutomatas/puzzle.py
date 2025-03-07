from puzzle4 import Nodo

def buscar_solucion_BFS(estado_inicial, solucion):
    solucionado = False
    nodos_visitados = []
    nodos_frontera = []
    nodoInicial = Nodo(estado_inicial)
    nodos_frontera.append(nodoInicial)
    while not solucionado and len(nodos_frontera) != 0:
        nodo = nodos_frontera.pop(0)  # FIFO (cola) first in first out
        nodos_visitados.append(nodo)

        if nodo.get_datos() == solucion:
            solucionado = True
            return obtener_camino(nodo)  # regresa el camino del nodo
        
        dato_nodo = nodo.get_datos()
        hijos = [
            Nodo([dato_nodo[1], dato_nodo[0], dato_nodo[2], dato_nodo[3]]),  # Hijo izquierdo
            Nodo([dato_nodo[0], dato_nodo[2], dato_nodo[1], dato_nodo[3]]),  # Hijo derecho
            Nodo([dato_nodo[0], dato_nodo[1], dato_nodo[3], dato_nodo[2]])  # Hijo central
        ]
        for hijo in hijos:
            if not hijo.en_lista(nodos_visitados) and not hijo.en_lista(nodos_frontera):
                hijo.padre = nodo  # se asigna el nodo actual como padre 
                nodos_frontera.append(hijo)

    return None  # en caso de que no se encuentre resultado se retornara un nulo
def obtener_camino(nodo):
    camino = []
    while nodo:
        camino.append(nodo.get_datos())
        nodo = nodo.padre
    return camino[::-1]  # se invierte el camino de los nodos

# Estado inicial del problema y la solucion 
estado_inicial = [1, 2, 3, 4]
solucion = [4, 3, 2, 1]

# se ejecuta la solucion de BFS
resultado = buscar_solucion_BFS(estado_inicial, solucion)

# aqui se mostrara el resultado dado
if resultado:
    print("Camino encontrado:")
    for paso in resultado:
        print(paso)
else:
    print("No se encontró solución.")

