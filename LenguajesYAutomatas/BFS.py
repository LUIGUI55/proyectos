from ARBOL import Nodo

def buscar_solucion_BFS(conexiones, estado_inicial, solucion):
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
            return nodo
        
        dato_nodo = nodo.get_datos()
        lista_hijos = []
        for un_hijo in conexiones[dato_nodo]:
            hijo = Nodo(un_hijo)
            lista_hijos.append(hijo)
            if not hijo.en_lista(nodos_visitados) and not hijo.en_lista(nodos_frontera):
                hijo.padre = nodo  # se asigna el nodo actual como padre 
                nodos_frontera.append(hijo)
                
        nodo.set_hijos(lista_hijos)
        
    return None  # en caso de que no se encuentre resultado se retornara un nulo

if __name__ == "__main__":
    conexiones = {
        'CDMX': {'SLP','MEXICALI', 'CHIHUAHUA'},
        'SAPOPAN': {'ZACATECAS', 'MEXICALI'},
        'GUADALAJARA':{'CHIAPAS'},
        'VHIAPAS':{'CHIHUAHUA'},
        'MEXICALI':{'SLP', 'SAPOPAN', 'CDMX', 'CHIHUAHUA', 'SONORA'},
        'SLP':{'CDMX', 'MEXICALI'},
        'ZACATECAS':{'SAPOPAN', 'SONORA', 'CHIHUAHUA'},
        'SONORA':{'ZACATECAS', 'MEXICALI'},
        'MICHOACAN':{'CHIHUAHUA'},
        'CHIHUAHUA':{'MICHOACAN', 'ZACATECAS', 'MEXICALI', 'CDMX','CHIAPAS' }
    }

    estado_inicial = 'CDMX'
    solucion = 'ZACATECAS'
    nodo_solucion = buscar_solucion_BFS(conexiones, estado_inicial, solucion)
    
    # Mostrar Resultado
    if nodo_solucion:
        resultado = []
        nodo = nodo_solucion
        while nodo.get_padre() is not None:
            resultado.append(nodo.get_datos())
            nodo = nodo.get_padre()
        resultado.append(estado_inicial)
        resultado.reverse()
        
        
        ciudades_interes = {'CDMX', 'CHIHUAHUA', 'ZACATECAS'}
        resultado_filtrado = [ciudad for ciudad in resultado if ciudad in ciudades_interes]
        
        print("Camino encontrado (filtrado):")
        print(resultado_filtrado)
    else:
        print("No se encontró solución.")
