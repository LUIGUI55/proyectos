- se puede imaginar visiblemente el resultado es peor que el obtenido con la busqued en amplitud. Esto indica que la entrada de esta busqueda no es obtim, mcomo n el casi de la busqueda en amplitud se dice que es sub-optima. Otro problema que presenta el algoritmo es que el arbol de busqueda no esyta acotado en profundidad es decir, es definitivamente profundo nunca saldra de la primera rama. En cuantro al complejidad temporal un arbol con profundidad no esta acotado en profundidad **P** tiene una complejidad **O(b^p)**, recordemos que la cmplejidad de busued aen amplitud es **O(b^b)**, donde d es la prfundidad en la que se encuentra la solucion como en la mayoria de los casos **p** es mayor que d se puede afirmar que la complejidad de la busqueda en profundida sera para la mayoria de los casos, mayor que la busqueda en amplitud (o en el mayor de los casos igual).
porque presentar entonces la busqueda en profundidad, parece no tener ninguna ventaja sobre la busqueda en amplitud?
Deliveradamente no se ha habladon aun de la complejidad espacial.

- En los pseudocodigos de ambas busqueda, se ha usado una lista para almacenar lis nodoos visitados.
se ha echo asi para no perder la generalidad y que el algoritmo fuera usable tanto en arboles como en grafos, se puede prescendir de una lista de nodos visitados. en la busqueda en profundidad, si el espacio de busquedes representado por un arbol la complejidad espacial se reduce ah O(Bm) lo que supone un costo de almacenamiento muy inferior al usarlo en la busqueda  en amplitud. Esto es debudo a que cuando se explora en una rama, sus nodos quedan eliminados de la busqueda de amplitud es necesario manterner almacenados

investigar como medir los ciclos de reloj de un lenguaje en Python. 
para hacernos una idea se tomara como ejemplo el puzzle linea. si se supone que un nodo necesita un kilobyte de almacenamiento incluyendo las estructuras propias de python la exploracion de un arbol (es decir sin lista de nodos visitados) hastsa el nivel 10 se necesita unos 60Mb de memoria RAM oara la busqueda en aplictud mientras que la misma busaueda usando el algoritmo en amplitud necesita unos 90KB la diferencia es mas que apreciable. Si la busqueda se realiza usando la losta de visitados, la busqueda es tambien completa en cadso de presciindir de almacenar los nodos bvisitados enb aras de preservar el uso de memoria, el algoritmo no es completo, ya que podria entrsar en bucles durante la busqueda.

Por las caracteristicas propias de la busqueda en profundidad, es posible una implementacion alternativa usando la recursividad. El siguinete pseudocodigo muestra la implementacion de forma general



**funcion_DFS_rec(nodo,solucion,visitados):**
    **anadir nodo a visitados**
    **si nodo == solucion**
        salir con la solucion
    Sino:

        por cada operador:
            nodo_hijo == operador(nodo)
        Si nodo_hijo no esta en visitados:
            S = DFS_rec(nodo_hijo, nodosolucion,nodovisitados)
        Salir con s

    Nodo_inicial 
    visitados == lista
    solucion == solucion
    S == DFS_rec(nodo, solucion,visitados)


    el esquema expresado en el pseudocodigo se puede llevar ala implementacion correcta para resolver el puzzle lineal