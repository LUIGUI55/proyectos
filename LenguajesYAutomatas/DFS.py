from ARBOL import Nodo
def buscar_solucion_DFS(conexiones,estado_inicial,solucion):
    solucionado = False
    nodos_visitados = []
    nodos_frontera = []
    nodoInicial = Nodo(estado_inicial)
    nodos_frontera.append(nodoInicial) 

    if nodoInicial.get_datos() == solucion:
        solucionado = True
        return nodoInicial 
    else:
        # Expandir los nodos sucesores(hijos)
        nodoInicial.get_datos()
    
    