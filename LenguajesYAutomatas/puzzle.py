# puzzle lineal con busqueda en amplitud 
from puzzle4 import puzzle4

def buscar_solucion_BFS (estado_inicial,solucion):
    solucionado = False 
    nodos_visitados = []
    nodos_frontera = []
    nodoInicial = nodo(estado_inicial)
    nodos_frontera.append(nodoInicial)

    while(not solucionado) and len(nodos_frontera)!=0:
        nodo = nodos_frontera.pop(0)
        #Extraer el nodo y agregarlo a visitados
        nodos_visitados.append(nodo)
        if nodo.get_datos() == solucion:
            #solucion Encontrada
            solucion = True
            return nodo
        else: 
            #expandir los nodos hijos.
            dato_nodo = nodo.get_datos()


            #Operador izq
            hijo = [dato_nodo[1],dato_nodo[0],dato_nodo[2],dato_nodo[3]]
            hijo_izq = nodo(hijo)
            if not hijo_izq.en_lista(nodos_visitados) and not hijo_izq.en_lista(nodos_frontera)
            nodos_frontera.append(hijo_izq)


#programar el hijo central y el hijo derecho